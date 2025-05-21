import groupdocs.redaction as gr
import test_files

# The following example demonstrates how to get supported file formats list

def run():

    print("\n[Example Basic Usage] # get_supported_file_formats.py : Getting GroupDocs.Redaction supported file formats")

    supported_file_types = gr.FileType.get_supported_file_types()

    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)

    print("\nSupported file types retrieved successfully.")
    print("======================================.")
