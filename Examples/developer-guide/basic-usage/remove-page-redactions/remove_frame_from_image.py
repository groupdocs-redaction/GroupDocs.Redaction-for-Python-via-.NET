from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import RemovePageRedaction, PageSeekOrigin


def remove_frame_from_image():
    # Remove frames starting from the 3rd one (zero-based index 2)
    rem_opt = RemovePageRedaction(PageSeekOrigin.BEGIN, 2, 5)

    # Load the multi-frame image to be redacted
    with Redactor("./sample.gif") as redactor:
        # Get document info
        doc_info = redactor.get_document_info()

        # Requires at least 7 frames
        if doc_info.page_count >= 7:
            # Apply the redaction
            result = redactor.apply(rem_opt)

            # Save the redacted image next to the source file
            so = SaveOptions()
            so.add_suffix = True
            so.rasterize_to_pdf = False
            so.redacted_file_suffix = "redacted"
            redactor.save(so)


if __name__ == "__main__":
    remove_frame_from_image()