from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import AnnotationRedaction


def redact_annotations():
    # Specify the redaction options: search pattern and replacement string
    a_red = AnnotationRedaction("(?im:john)", "[redacted]")

    # Load the document to be redacted
    with Redactor("./annotated.xlsx") as redactor:
        # Apply the redaction
        result = redactor.apply(a_red)

        # Save the redacted document next to the source file
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        so.redacted_file_suffix = "redacted"
        redactor.save(so)


if __name__ == "__main__":
    redact_annotations()