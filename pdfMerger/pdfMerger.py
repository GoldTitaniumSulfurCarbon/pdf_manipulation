from PyPDF2 import PdfMerger
from pathlib import Path

# Asks user to input a directory containing .pdf files, returns all .pdf files in the directory in a sorted order,
# asks the user if they want to proceed, and then returns the merged .pdf file in the folder WHERE THE SCRIPT is
# located.

merged_file_name = "merged_pdfs"

input_directory = input("""Please enter in the directory of the desired pdf files.
The formatting should be like this: D:\\Downloads\\Downloads\\mp4s\n\n\n"""
                        )
directory = Path(input_directory)  # Put in the path of the .pdf files you want to merge

if directory.exists():
    individual_pages = list(directory.glob("*.pdf"))
    individual_pages.sort()

    for file in individual_pages:  # Gives the user each .pdf file in the given directory.
        print(file.name)

    merge_confirmation = input(
        """\n\n\nIs this the order you want to merge the individual pdfs in? Type \"y\" for yes, or any other key for no.\n\n\n"""
    )  # Asks user if they want to proceed with the merging or not.

    if merge_confirmation.casefold() == 'y':
        merger = PdfMerger()
        for pdf in individual_pages:
            merger.append(pdf)

        merger.write(merged_file_name + ".pdf")
        print(f"""Success! You can find the merged file in the folder where this script is located.
Filename: {merged_file_name}"""
              )
        merger.close()
    else:
        print("Process aborted.")
else:
    raise Exception("Directory is invalid. Please give a valid directory.")
