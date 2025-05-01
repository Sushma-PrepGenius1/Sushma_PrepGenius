from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(input_text, output_filename):
    try:
        c = canvas.Canvas(output_filename, pagesize=letter)
        x = 40
        y = 750
        
        for line in input_text.splitlines():
            c.drawString(x, y, line)
            y -= 12
            
            if y < 40:
                c.showPage()
                y = 750

        c.save()
        print(f"PDF saved as {output_filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage:
text_to_pdf("This is a sample text.", "output.pdf")
