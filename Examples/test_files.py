# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import utils

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(utils.samples_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, utils.samples_path, file_path)

fonts_path = utils.fonts_path

# PDFs
sample_pdf = get_sample_file_path("sample.pdf")
multipage_pdf = get_sample_file_path("multipage_sample.pdf")
lorem_ipsum_pdf = get_sample_file_path("lorem_ipsum.pdf")
arabic_pdf = get_sample_file_path("arabic.pdf")

# Spreadsheets
sample_xlsx = get_sample_file_path("sample.xlsx")
sample_annotated_xlsx = get_sample_file_path("annotated.xlsx")

# Word Processing documents
sample_docx = get_sample_file_path("sample.docx")
protected_docx = get_sample_file_path("protected.docx")
multipage_docx = get_sample_file_path("multipage_sample.docx")
sample_txt = get_sample_file_path("sample.txt")
sample_dump = get_sample_file_path("sample.dump")

# Images
sample_jpg = get_sample_file_path("sample.jpg")
sample_gif = get_sample_file_path("sample.gif")

# Other
redaction_policy = get_sample_file_path("redaction_policy.xml")



    