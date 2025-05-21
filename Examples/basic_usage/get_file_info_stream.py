import groupdocs.redaction as gr
import test_files

# The following example demonstrates how to get document information for a file from stream

def run():

    print("\n[Example Basic Usage] # get_file_info_stream.py : Getting file info from stream")

    with open(test_files.sample_docx, "rb") as stream:
        with gr.Redactor(stream) as redactor:
            info = redactor.get_document_info()

    print(f"File type: {info.file_type}")
    print(f"Number of pages: {info.page_count}")
    print(f"Document size: {info.size} bytes")
 
    print("\nDocument stream info retrieved successfully.")
    print("======================================.")
