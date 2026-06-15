from groupdocs.redaction import Redactor


def get_file_info_from_stream():
    # Open the document as a binary stream
    with open("./sample.docx", "rb") as stream:
        # Load the document from the stream
        with Redactor(stream) as redactor:
            # Retrieve general document information
            info = redactor.get_document_info()

            print(f"File type: {info.file_type}")
            print(f"Number of pages: {info.page_count}")
            print(f"Document size: {info.size} bytes")


if __name__ == "__main__":
    get_file_info_from_stream()