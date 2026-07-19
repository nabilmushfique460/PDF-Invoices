import pandas as pd
import glob
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Invoice nr.{invoice_nr}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Date: {date}")

    pdf.output(f"PDFs/{filename}.pdf")
