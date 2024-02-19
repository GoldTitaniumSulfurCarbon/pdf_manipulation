from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# TODO: Allow user to enter path of desired folder through user input
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

        starting_point = int(input("Please put in the index you want to begin the cropping at"))
        ending_point = int(input("Please put in the index you want to end the cropping at"))

        for page in input_pdf.pages[starting_point-1:ending_point]: # starting_point is decreased by one to account for that page to begin at.
            cropped_pdf.add_page(page)

        cropped_pdf_name = input("What do you want to name the cropped pdf? File extension not needed")
        cropped_pdf_name += ".pdf"
        output_file = output_directory / cropped_pdf_name
        with output_file.open(mode="wb") as output:
            cropped_pdf.write(output)
        print(f"Success! You can find your file {cropped_pdf_name} inside the \"outputs\" folder located where this script is.")

    else:
        raise Exception("The given path is not valid")



# User input if they want to keep going.
file_directory = "E:\Desktop\Calculus Transcendentals 8E.pdf"
user_input = "y"
while user_input == "y" :
    pdfCropper(file_directory)
    user_input = input("Do you want to keep running this? \"y\" for yes, and any other for no.")
    user_input = user_input.casefold()