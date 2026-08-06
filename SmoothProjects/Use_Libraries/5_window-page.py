from reportlab.pdfgen import canvas
from reportlab.lib.colors import black

# Create PDF
c = canvas.Canvas("fillable_form.pdf")

# Add text
c.drawString(100, 750, "Enter your name:")

# Create text field
c.acroForm.textfield(
    name='username',
    x=100,
    y=720,
    width=200,
    height=20,
    borderColor=black
)

# Finalize page
c.showPage()

# Save PDF
c.save()

print("PDF Created Successfully")