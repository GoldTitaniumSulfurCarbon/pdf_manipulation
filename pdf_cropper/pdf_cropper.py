from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
# The user gives the directory of a PDF file and then is prompted to give the range of pages (one indexed) to crop.
# The user then chooses what to name the PDF, and is outputted in a folder where the script is.
def pdfCropper(directory):
    file_directory = Path(directory) # Creates path to desired pdf
    output_directory = Path("outputs") # Output path in the folder of this script is created.

    if not output_directory.exists(): # Creates the aforementioned folder if it does not already exist.
        output_directory.mkdir()
        print("Output folder has been created in the folder this script is located.")

    if file_directory.exists():
        input_pdf = PdfReader(file_directory)
        cropped_pdf = PdfWriter()
        print(f"The given PDF has {len(input_pdf.pages)} total pages.")

        starting_point = int(input("Please put in the index you want to begin the cropping at:\n"))
        ending_point = int(input("Please put in the index you want to end the cropping at:\n"))

        for page in input_pdf.pages[starting_point-1:ending_point]: # starting_point is decreased by one to account for that page to begin at.
            cropped_pdf.add_page(page)

        cropped_pdf_name = input("What do you want to name the cropped pdf? File extension not needed:\n")
        cropped_pdf_name += ".pdf"
        output_file = output_directory / cropped_pdf_name
        with output_file.open(mode="wb") as output:
            cropped_pdf.write(output)
        print(f"Success! You can find your file {cropped_pdf_name} inside the \"outputs\" folder located where this script is.")

    else:
        raise Exception("The given path is not valid")

# User input if they want to keep running the program and if they want to change the file they're cropping from.
user_input = "y"
change_directory = "y"
while user_input == "y" :
    while change_directory == "y":
        file_directory = input("""Please enter in the directory of the desired pdf files.
The formatting should be like this: D:\\Downloads\\Downloads\\mp4s\n\n\n""")
        change_directory = "n"

    pdfCropper(file_directory)
    user_input = input("Do you want to keep running this? \"y\" for yes, and any other for no.\n").casefold()
    if user_input == "y":
        change_directory = input("Do you want to change the directory? \"y\" for yes, and any other for no.\n").casefold()
