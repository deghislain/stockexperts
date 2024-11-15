from datetime import date
from xhtml2pdf import pisa
from markdown_it import MarkdownIt
from io import BytesIO
import os


OUTCOME_MSG = "PDF successfully exported. You can find it here: reports/pdf within this project"

PATH_TO_GENERATED_CONTENT = 'reports/md/'
PATH_TO_PDF = 'reports/pdf/'


def generate_pdf():
    global OUTCOME_MSG
    print("generate_pdf Start")

    pdf_name = ""

    today = str(date.today())
    file_path = PATH_TO_GENERATED_CONTENT + today + "_search_stock_report.md"
    pdf_name = "_search_stock_report.pdf"
    if not os.path.exists(file_path):
        file_path = PATH_TO_GENERATED_CONTENT + today + "_compare_stock_report.md"
        pdf_name = "_compare_stock_report.pdf"
    print(pdf_name, "********************")
    print(file_path, "********************")


    try:
        md = MarkdownIt()
        with open(file_path, 'r') as f:
            markdown_string = f.read()
        html_content = md.render(markdown_string)
        pdf_output = BytesIO()

        pisa.CreatePDF(html_content, dest=pdf_output, encoding='utf-8')

        # Open a PDF file for writing in binary mode
        with open(PATH_TO_PDF + today + pdf_name, "wb") as pdf_file:
            # Write the PDF content to the file
            pdf_file.write(pdf_output.getvalue())

    except Exception as ex:
        OUTCOME_MSG = "Error while generating the pdf file. Please, try again"
        print("Error while getting the summary", ex)

    return OUTCOME_MSG
