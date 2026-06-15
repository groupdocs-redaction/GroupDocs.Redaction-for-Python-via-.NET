from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions, LoadOptions
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions


def load_password_protected_file():
    # Specify the load options with the document password
    load_opt = LoadOptions("mypassword")

    # Specify the redaction options
    repl_opt = ReplacementOptions("[personal]")
    ex_red = ExactPhraseRedaction("John Doe", repl_opt)

    # Load the password-protected document to be redacted
    with Redactor("./protected.docx", load_opt) as redactor:

        # Apply the redaction
        redactor.apply(ex_red)

        # Save the redacted document in its original format
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        so.redacted_file_suffix = "redacted"
        result_path = redactor.save(so)
        print(f"Document redacted successfully.\nCheck output in {result_path}.")


if __name__ == "__main__":
    load_password_protected_file()