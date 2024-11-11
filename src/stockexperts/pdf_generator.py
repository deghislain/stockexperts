from datetime import date
from fpdf import FPDF
import os


OUTCOME_MSG = "PDF successfully exported. You can find it here doc/pdf within this project"


PATH_TO_GENERATED_CONTENT = 'reports/md/'
PATH_TO_PDF = 'reports/pdf/'


def generate_pdf():
    print("generate_pdf Start")
    pdf = FPDF()
    pdf.add_page()
    pdf_name = ""

    pdf.set_font("Arial", size=12)
    today = str(date.today())
    #title = today + topic
    file_path = PATH_TO_GENERATED_CONTENT + today + "_search_stock_report.md"
    pdf_name = "_search_stock_report"
    if not os.path.exists(file_path):
        file_path = PATH_TO_GENERATED_CONTENT + today + "_compare_stock_report.md"
        pdf_name = "_compare_stock_report"


    try:
        with open(file_path, "r") as file:
            for line in file:
                # Split line into words
                words = line.split()
                chunk = ""
                for word in words:
                    # Check if adding word exceeds max line length
                    if len(chunk) + len(word) + 1 > 95:
                        pdf.cell(200, 10, txt=chunk.strip(), ln=True, align='L')
                        chunk = word + " "
                    else:
                        chunk += word + " "

                # Add remaining chunk to PDF
                if chunk:
                    pdf.cell(200, 10, txt=chunk.strip(), ln=True, align='L')

        # Save the PDF with filename
        pdf.output(PATH_TO_PDF + today + pdf_name + ".pdf")
    except Exception as ex:
        OUTCOME_MSG = "Error while generating the pdf file. Please, try again"
        print("Error while getting the summary", ex)

