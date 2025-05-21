import groupdocs.redaction as gr
import test_files

# The following example demonstrates how to replace matched text with a solid color rectangle

def run():

    print("\n[Example Basic Usage] # get_file_info_file.py : Getting local file info")

    with gr.Redactor(test_files.sample_docx) as redactor:
        info = redactor.get_document_info()

    print(f"File type: {info.file_type}")
    print(f"Number of pages: {info.page_count}")
    print(f"Document size: {info.size} bytes")

   
    print("\nDocument info retrieved successfully.")
    print("======================================.")
