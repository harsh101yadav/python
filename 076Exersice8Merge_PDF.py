'''Write a program to manipulate pdf files using pyPDF. 
Your programs should be able to merge multiple pdf files into a single pdf. 
You are welcome to add more functionalities pypdf is a free and 
open-source pure-python PDF library capable of splitting, merging, cropping, 
and transforming the pages of PDF files. It can also add custom data, 
viewing options, and passwords to PDF files. pypdf can retrieve text and 
metadata from PDFs as well.'''
from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_file)
    merger.close()

# Directory containing the PDF files to merge
pdf_directory = "D:\Study Material\Subjects\Python\pdf"

# List of PDF files to merge
pdf_files = [os.path.join(pdf_directory, "file1.pdf"),
             os.path.join(pdf_directory, "file2.pdf"),
             os.path.join(pdf_directory, "file3.pdf")]

# Output file name for the merged PDF
output_file = os.path.join(pdf_directory, "merged_file.pdf")

# Merge the PDF files
merge_pdfs(pdf_files, output_file)
