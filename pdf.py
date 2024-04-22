# import PyPDF2
#
#
# def extract_text_from_pdf(pdf_path):
#     pdf_file = open(pdf_path, 'rb')
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     pages = pdf_reader.pages
#
#     text = ""
#     for page in pages:
#         text += page.extract_text()
#
#     pdf_file.close()
#     for string in text.split('\n'):
#         if string == 'alteration':
#             # print(string)




x = "python"
print(x[1:4])




# Example usage
pdf_path = "COI.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

print(extracted_text)
