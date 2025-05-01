import os
import cv2
import mediapipe as mp
import json
from typing import Dict, List

# Suppress MediaPipe warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def captureExpressionSamples(expressionName: str, sampleCount: int = 10) -> List[Dict[str, float]]:
    """
    Opens webcam, shows live preview, and captures face mesh landmarks for a given expression.

    Args:
        expressionName: The name of the expression (smile, neutral, angry)
        sampleCount: Number of samples to capture

    Returns:
        List of dicts of landmark coordinates (x, y, z)
    """
    print(f"\n[INFO] Get ready to record: {expressionName.upper()}")
    print("[INFO] Press ENTER to capture when ready...")

    mpFaceMesh = mp.solutions.face_mesh
    faceMesh = mpFaceMesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
    drawingUtils = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    capturedSamples = []
    currentSample = 0

    while currentSample < sampleCount:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read frame from webcam.")
            break

        frameFlipped = cv2.flip(frame, 1)
        rgbFrame = cv2.cvtColor(frameFlipped, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(rgbFrame)

        if results.multi_face_landmarks:
            faceLandmarks = results.multi_face_landmarks[0]
            drawingUtils.draw_landmarks(
                image=frameFlipped,
                landmark_list=faceLandmarks,
                connections=mpFaceMesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawingUtils.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
            )
            status = f"{expressionName.upper()} - Sample {currentSample+1}/{sampleCount}"
        else:
            status = "No face detected!"

        # Show status text
        cv2.putText(frameFlipped, status, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        cv2.imshow("Capture Expression", frameFlipped)

        key = cv2.waitKey(1)
        if key == 13 and results.multi_face_landmarks:  # ENTER key
            landmarkList = [{"x": lm.x, "y": lm.y, "z": lm.z} for lm in faceLandmarks.landmark]
            capturedSamples.append(landmarkList)
            print(f"[INFO] Captured sample {currentSample+1}")
            currentSample += 1
        elif key == 27:
            print("[INFO] Capture cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return capturedSamples


def saveSamplesToJson(data: Dict[str, List[List[Dict[str, float]]]], fileName: str = "expressionSamples.json") -> None:
    """
    Saves collected expression data to a JSON file.

    Args:
        data: Dict with expression name as keys and list of landmarks as values
        fileName: File name to save

    Returns:
        None
    """
    with open(fileName, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[INFO] Saved data to {fileName}")


if __name__ == "__main__":
    expressions = ["smile", "neutral", "angry"]
    allSamples = {}

    for exp in expressions:
        samples = captureExpressionSamples(expressionName=exp, sampleCount=10)
        allSamples[exp] = samples

    saveSamplesToJson(allSamples)
