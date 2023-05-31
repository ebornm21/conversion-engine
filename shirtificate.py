#A program that can take the name given by the user and creates a "shirtificate", a certificate depicting a shirt with the user's name on it.

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.image("shirtificate.png", 40, 20)
name = input("Name: ")
pdf.cell(40, 30, name, align="C")
pdf.output("shirtificate.pdf")