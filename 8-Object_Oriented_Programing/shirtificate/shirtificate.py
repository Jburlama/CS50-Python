from fpdf import FPDF
import fpdf.enums


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(text="CS50 Shirtificate", center=True)
    pdf.image("shirtificate.png", x="C", y=50)
    pdf.set_text_color(255,255,255)
    pdf.set_font("helvetica", style="B", size=30)
    pdf.cell(w=0, h=225, text=f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")
    return 0


if __name__ == "__main__":
    main()
