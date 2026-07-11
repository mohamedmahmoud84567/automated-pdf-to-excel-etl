import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf():
    output_dir = os.path.join("data", "raw")
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "sample.pdf")
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    
    c.drawString(100, 750, "Sample Invoice Data - Raw File")
    c.setFont("Helvetica", 10)
    c.drawString(100, 730, "ID, Name, Product, Price")
    c.drawString(100, 720, "--------------------------------------------------")
    
    data = [
        "101, John Doe, Laptop, 1200",
        "102, Jane Smith, Phone, 800",
        "102, Jane Smith, Phone, 800",  
        "103, Alex Jones, Monitor, 300",
        "101, John Doe, Laptop, 1200",  
        "104, Sam Wilson, Keyboard, 50"
    ]
    
    y = 700
    for line in data:
        c.drawString(100, y, line)
        y -= 20
        
    c.save()
    print(f"✅ [Done] Created dummy PDF at: {pdf_path}")

if __name__ == "__main__":
    create_sample_pdf()
