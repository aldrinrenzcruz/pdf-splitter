import PyPDF2
import os

def split_pdf(file_path, num_parts):
    with open(file_path +'.pdf', 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        total_pages = len(pdf.pages)
        part_size = total_pages // num_parts
        remainder = total_pages % num_parts
        for i in range(num_parts):
            part = PyPDF2.PdfWriter()
            start = i * part_size
            end = start + part_size
            if i == num_parts - 1:
                end += remainder
            for j in range(start, end):
                part.add_page(pdf.pages[j])
            filename, ext = os.path.splitext(os.path.basename(file_path +'.pdf'))
            with open(f"{filename}_Part{i+1}{ext}", 'wb') as out_file:
                part.write(out_file)

file_path = input("Enter the file name: ")
num_parts = int(input("Enter the number of parts to split the pdf into: "))

split_pdf(file_path, num_parts)
