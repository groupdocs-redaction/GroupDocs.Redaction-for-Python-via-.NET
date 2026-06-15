from groupdocs.redaction import Redactor


def get_local_file_info():
    # Load the document from local disk
    with Redactor("./sample.docx") as redactor:
        # Retrieve general document information
        info = redactor.get_document_info()

        print(f"File type: {info.file_type}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")


if __name__ == "__main__":
    get_local_file_info()