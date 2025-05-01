import mediapipe as mp
import cv2



# imgPath = "media/frames/interview_3/frame_0.jpg"
# imgPath = "media/frames/interview_3/frame_1.jpg"
imgPath = "simileFace.jpg"
# imgPath = "angry.jpg"
# imgPath = "angry2.jpg"
# imgPath = "media/frames/interview_/frame_0.jpg"

# imgPath = "media/frames/interview_/frame_19.jpg"


mp_face_mesh = mp.solutions.face_mesh
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    image = cv2.imread(imgPath)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if results.multi_face_landmarks:
        print("Face detected with landmarks")
    else:
        print("No face detected")



















Act as an Interview Report Generator

🎯 Objective:
Generate a structured evaluation report based only on the candidate’s spoken responses from the Audio Detection section.

📤 Input:
Use only the candidate’s spoken answers from the Audio Detection section. Ignore all other metadata or inputs.

🧾 Output Format:
Return only HTML body content. Wrap everything inside a single <div>.

🎨 TailwindCSS Styles Guide:

Main Container: p-6 rounded-lg shadow-md bg-white min-h-screen flex overflow-y-auto

Background: bg-gray-100

Headings: text-2xl text-3xl font-semibold italic text-center

Text: text-lg test-gray-400

Spacing: mt-4 space-y-6 pl-6

UI Hover: hover:bg-red-100

🧱 Structure:

📄 Final Interview Report

Title styled: text-3xl text-center font-semibold

👤 Candidate Info

Include:

Candidate Name

Role Interviewed For

Interview Type

❓ Question-wise Evaluation
For each question:

Question: Show the exact question

Rating: Score out of 10

Evaluation Summary: Bullet points summarizing how well the answer aligns with the question.

Justification Required: Every score must be clearly explained, whether high or low.

🌟 Overall Highlights

Title: Overall Highlights

Style: text-2xl font-semibold mt-4

4–6 bullet points highlighting candidate strengths

🔧 Areas for Improvement

Title: Areas for Improvement

Style: text-2xl font-semibold mt-4

4–8 bullet points for suggested improvements

🧾 Final Summary

Title: Final Summary

Style: text-2xl font-semibold mt-4

Include:

Star Rating (e.g., ★★★★☆ (4.5/5))

Final remarks on overall performance

📌 Important:
Base all evaluations strictly on spoken content. Justify all ratings with clear, bullet-pointed evaluation summaries.





# Input Data:
    Interview Title : Interview - atharva
Username        : atharva


Consder this for interview question evaluation : 
 User Input : 
User Camera Detection (detect the face in frame and then the face emotion): Detection: Face detected - 1 times
Detection: Face detected, Emotion Detected as angry - 13 times
Detection: Face detected, Emotion Detected as neutral - 1 times
Detection: No Face detected - 3 times
User Interview Audio Text Response : Audio Detection: hello this is the robot boy from projects with word.in 1 2 3
Job Description : Job Title: AI/ML Engineer
Location: Bangalore, India
Company: Google
Department: Artificial Intelligence & Machine Learning

About Google:
Google is a global leader in technology, with a mission to organize the worldâ€™s information and make it universally accessible and useful. We empower individuals and businesses around the world with tools and technologies that help them achieve more. Google is at the forefront of innovation in AI and machine learning, using advanced technologies to solve complex problems and improve the world.

Position Overview:
Google is seeking an AI/ML Engineer to join our dynamic and fast-paced team in Bangalore. In this role, you will design, develop, and deploy cutting-edge machine learning models and algorithms to solve real-world problems. You will work with large datasets, innovate using the latest AI/ML technologies, and collaborate with cross-functional teams to push the boundaries of artificial intelligence.

Responsibilities:
Design & Develop AI/ML Models: Build and deploy scalable machine learning models and algorithms to tackle complex problems in various domains, such as natural language processing (NLP), computer vision, and predictive analytics.

Data Analysis & Preprocessing: Work with large datasets, clean, preprocess, and analyze data to extract valuable insights and features for model training.

Collaboration: Work closely with product managers, software engineers, and other stakeholders to define AI solutions, improve model performance, and integrate machine learning into production systems.

Research & Innovation: Stay up-to-date with the latest advancements in AI/ML and propose new algorithms, techniques, and frameworks that can be applied to existing problems.

Model Optimization & Testing: Continuously monitor, optimize, and test AI/ML models to ensure high accuracy, performance, and scalability.

Documentation & Reporting: Maintain clear documentation for models, experiments, and results. Communicate findings effectively to both technical and non-technical stakeholders.

Required Qualifications:
Education: Bachelor's or Masterâ€™s degree in Computer Science, Electrical Engineering, Mathematics, or related field. PhD is a plus.

Experience: 2+ years of hands-on experience in AI/ML engineering, with a strong understanding of machine learning algorithms and techniques.

Technical Skills:

Proficiency in Python, C++, or Java.

Strong knowledge of AI/ML frameworks such as TensorFlow, PyTorch, Keras, or scikit-learn.

Experience with cloud-based machine learning platforms (Google Cloud AI, AWS, or similar).

Knowledge of deep learning, reinforcement learning, NLP, or computer vision.

Solid understanding of data structures, algorithms, and software engineering principles.

Familiarity with data manipulation and analysis tools like Pandas, NumPy, and SQL.

Problem-Solving Skills: Strong analytical skills with the ability to break down complex problems into manageable components.

Communication: Excellent written and verbal communication skills. Ability to convey complex technical concepts to non-technical stakeholders.

Collaboration: Ability to work in a collaborative, fast-paced environment and contribute to the success of the team.

Preferred Qualifications:
Experience with deploying AI/ML models into production.

Familiarity with distributed computing systems and cloud platforms.

Experience in model interpretability and explainability techniques.

Publications or contributions to AI/ML research or open-source projects.

Why Google?
Innovative Environment: Work in a cutting-edge technological environment with access to the latest tools and resources.

Career Growth: Google offers numerous opportunities for professional development, mentoring, and career advancement.

Inclusive Culture: Google fosters an inclusive and diverse workplace, encouraging innovation from individuals of all backgrounds.

Competitive Compensation: Google offers a competitive salary, comprehensive benefits, and performance-based bonuses.

How to Apply:
Interested candidates can apply through the Google Careers page with a resume and a cover letter outlining their qualifications and experience.
Interview Questions       : 
 This job description emphasizes designing, developing, and deploying machine learning models. Can you walk me through a project where you tackled a complex problem using these skills, highlighting the specific technologies and your contributions?
Google values collaboration and cross-functional teamwork. Describe a situation where you had to work with a diverse team, including non-technical stakeholders, to deliver an AI/ML solution. How did you ensure effective communication and alignment?
The role requires expertise in various AI/ML frameworks and cloud platforms. How familiar are you with Google Cloud AI Platform, and how have you utilized it in past projects to train, deploy, and manage machine learning models?
Google emphasizes continuous learning and staying updated with the latest advancements in AI/ML.  What are some recent advancements in the field that excite you, and how do you see them potentially impacting Google's products and services?
This role requires strong problem-solving skills and the ability to break down complex problems into manageable components. Can you describe a challenging technical problem you faced and how you approached solving it, outlining your thought process and the steps you took?