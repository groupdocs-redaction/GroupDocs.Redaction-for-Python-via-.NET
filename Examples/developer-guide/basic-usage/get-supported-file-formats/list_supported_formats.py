from groupdocs.redaction import FileType


def list_supported_formats():
    # Retrieve the collection of supported file types
    supported_file_types = FileType.get_supported_file_types()

    # Enumerate the file types sorted by extension
    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)


if __name__ == "__main__":
    list_supported_formats()