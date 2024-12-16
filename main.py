import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filelist = glob.glob("text_files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
for file in filelist:
    filename = Path(file).stem
    with open(file, "r") as fs:
        content = fs.read()
    pdf.add_page()
    pdf.set_font("Times", size=24, style="B")
    pdf.cell(50, 8, txt=filename.capitalize())
    pdf.ln(20)
    pdf.set_font("Arial", size=12, style="B")
    pdf.multi_cell(0, 7, txt=content)

pdf.output("animals.pdf")
