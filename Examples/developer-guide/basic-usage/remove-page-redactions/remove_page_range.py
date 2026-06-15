from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import RemovePageRedaction, PageSeekOrigin


def remove_page_range():
    # Load the document to be redacted
    with Redactor("./multipage_sample.pdf") as redactor:
        # Get document info
        doc_info = redactor.get_document_info()

        # Requires at least 4 pages
        if doc_info.page_count > 3:
            # Remove 3 pages starting from the 2nd one (zero-based index 1)
            rem_opt = RemovePageRedaction(PageSeekOrigin.BEGIN, 1, 3)

            # Apply the redaction
            result = redactor.apply(rem_opt)

            # Save the redacted document next to the source file
            so = SaveOptions()
            so.add_suffix = True
            so.rasterize_to_pdf = False
            so.redacted_file_suffix = "redacted"
            redactor.save(so)


if __name__ == "__main__":
    remove_page_range()