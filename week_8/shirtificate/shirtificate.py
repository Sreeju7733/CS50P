from fpdf import FPDF

class PDF():
    def __init__(self, name):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font("helvetica", "B", 30)
        pdf.set_text_color(255, 255, 255)
        text_width = pdf.get_string_width(name)
        centered_x = (pdf.w - text_width) / 2
        pdf.text(centered_x, 140, name)
        pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    shirtificate = PDF(name)

if __name__ == "__main__":
    main()
