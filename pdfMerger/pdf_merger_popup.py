from PyPDF2 import PdfMerger
from pathlib import Path
import PySimpleGUI as sg
# Asks user to input a directory containing .pdf files, returns all .pdf files in the directory in a sorted order,
# asks the user if they want to proceed, and then returns the merged .pdf file in the folder WHERE THE SCRIPT is
# located.

input_directory = sg.popup_get_folder("Please enter in the directory of the desired pdf files.")

directory = Path(input_directory)  # Put in the path of the .pdf files you want to merge


if directory.exists():
    # Extracts each directory for each .pdf file within the folder, then sorts in alphabetical order
    individual_pages = list(directory.glob("*.pdf"))
    individual_pages.sort()

    list_of_pdfs = ""
    i = 0
    for file in individual_pages: # Gives the user each .pdf file in the given directory.
        i += 1
        list_of_pdfs += f"{i}: {file.name}\n"
    merge_confirmation = sg.popup_yes_no(
        f"""\n\n\nIs this the order you want to merge the individual pdfs in?\n\n\n{list_of_pdfs}"""

    )  # Asks user if they want to proceed with the merging or not.

    if merge_confirmation == 'Yes':
        # Gets each directory for the individual PDFs, writes it to a single PDF, then sets it to be equal to user input for name.
        merged_file_name = sg.popup_get_text("What wold you like to name your file?")

        merger = PdfMerger()
        for pdf in individual_pages:
            merger.append(pdf)

        merger.write(merged_file_name + ".pdf")
        sg.popup(f"""Success! You can find the merged file in the folder where this script is located.
Filename: {merged_file_name}"""
              )
        merger.close()
    else:
        sg.popup("Process aborted.")
else:
    raise Exception("Directory is invalid. Please give a valid directory.")
