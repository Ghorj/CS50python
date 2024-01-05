from fpdf import FPDF
from fpdf import Align

def main():

    #prompts the user for their name
    #outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf
    create_shirt(input("Name: "))

def create_shirt(name):
    #The orientation of the PDF should be Portrait.
    #The format of the PDF should be A4, which is 210mm wide by 297mm tall.

    #create pdf file
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    #add page (pdf initially empty)
    pdf.add_page()

    #The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    pdf.set_font("Times", size=36)
    pdf.cell(text="CS50 SHIRTIFICATE", center=True, new_y="NEXT")

    #empty line
    pdf.ln()

    #The shirt’s image should be centered horizontally
    pdf.image("shirtificate.png", x=Align.C, w=pdf.epw)


    #The user’s name should be on top of the shirt, in white text.
    pdf.set_y(100)

    pdf.set_text_color(r=255)
    pdf.cell(text=f"{name.upper()} TOOK CS50", center=True)

    #create pdf
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
