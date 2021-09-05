from RPA.PDF import PDF

pdf = PDF()

list_of_files = [
    'img1.png',
    'img2.png',
    'img3.png',
    'img4.png',
]


def example_keyword():
    pdf.add_files_to_pdf(
        files=list_of_files,
        target_document="output/output.pdf"
    )
