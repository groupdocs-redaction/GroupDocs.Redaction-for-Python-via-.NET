from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import RemovePageRedaction, PageSeekOrigin


def remove_last_page():
    # Remove 1 page counting from the end of the document
    rem_opt = RemovePageRedaction(PageSeekOrigin.END, 0, 1)

    # Load the document to be redacted
    with Redactor("./multipage_sample.pdf") as redactor:
        # Get document info
        doc_info = redactor.get_document_info()

        # Requires at least 2 pages so the document is not left empty
        if doc_info.page_count > 1:
            # Apply the redaction
            result = redactor.apply(rem_opt)

            # Save the redacted document next to the source file
            so = SaveOptions()
            so.add_suffix = True
            so.rasterize_to_pdf = False
            so.redacted_file_suffix = "redacted"
            redactor.save(so)


if __name__ == "__main__":
    remove_last_page()