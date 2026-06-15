from groupdocs.redaction import Redactor
from groupdocs.redaction.options import RasterizationOptions
from groupdocs.redaction.redactions import DeleteAnnotationRedaction


def load_from_stream():
    # Specify the redaction options - remove all annotations
    del_red = DeleteAnnotationRedaction()

    # Load the document as a stream to be redacted
    with open("./sample.docx", "rb") as stream_in:
        with Redactor(stream_in) as redactor:

            # Apply the redaction
            redactor.apply(del_red)

            # Save the redacted document to a stream as a rasterized PDF
            with open("./redacted-sample.pdf", "wb") as stream_out:
                ro = RasterizationOptions()
                redactor.save(stream_out, ro)
                print("Document redacted successfully.")


if __name__ == "__main__":
    load_from_stream()