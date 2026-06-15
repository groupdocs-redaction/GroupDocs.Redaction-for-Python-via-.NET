from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import DeleteAnnotationRedaction


def load_from_local_disc():
    # Specify the redaction options - remove all annotations
    del_red = DeleteAnnotationRedaction()

    # Load the document to be redacted from the local disc
    with Redactor("./sample.docx") as redactor:

        # Apply the redaction
        redactor.apply(del_red)

        # Save the redacted document in its original format next to the source file
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        so.redacted_file_suffix = "redacted"
        result_path = redactor.save(so)
        print(f"Document redacted successfully.\nCheck output in {result_path}.")


if __name__ == "__main__":
    load_from_local_disc()