from datetime import datetime

from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions


def save_in_original_format():
    # Specify the redaction options
    repl_opt = ReplacementOptions("[personal]")
    ex_red = ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with Redactor("./sample.docx") as redactor:

        # Apply the redaction
        redactor.apply(ex_red)

        # Save the redacted document in its original format with the current date as a suffix
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        date_time_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        so.redacted_file_suffix = date_time_str

        result_path = redactor.save(so)
        print(f"Document redacted successfully.\nCheck output in {result_path}.")


if __name__ == "__main__":
    save_in_original_format()