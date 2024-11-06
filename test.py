import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Path of the pdf
PDF_file = r"otr1.pdf"
  
  
def pdf_text():
    
    # Store all the pages of the PDF in a variable
    #The 500 is a parameter that specifies the DPI (dots per inch) for the converted images.
    #The convert_from_path function is part of the pdf2image library, which takes a PDF file and converts each of its pages into an image.

    pages = convert_from_path(PDF_file, 500)
  
    image_counter = 1

    for page in pages:

        # Declare file names
        filename = "page_"+str(image_counter)+".jpg"

        # Save the image of the page in system
        page.save(filename, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1

    # Variable to get count of total number of pages
    filelimit = image_counter-1

    outfile = "out_text.pdf"

    # Open the file in append mode so that all contents of all images are added to the same file
    
    f = open(outfile, "a")

    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):

        filename = "page_"+str(i)+".jpg"

        # Recognize the text as string in image using pytesseract
        result =  pytesseract.image_to_pdf_or_hocr(filename, lang="eng")
        # print(f" type of results = {type(result)} \n\n\n") 
        # print(f"results = {result}")

            
        f = open(outfile, "w+b")
        f.write(bytearray(result))
  
    f.close()

pdf_text()