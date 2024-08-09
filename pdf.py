from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.pdfgen.canvas import Canvas


def generate_pdf_from_images(file_name, images):
    canvas = Canvas(file_name, pagesize=A4)
    i = 0
    while i < len(images):
        canvas.drawImage(images[i], 0, 0, A4[0], A4[1])
        canvas.showPage()
        i += 1

    canvas.save()
