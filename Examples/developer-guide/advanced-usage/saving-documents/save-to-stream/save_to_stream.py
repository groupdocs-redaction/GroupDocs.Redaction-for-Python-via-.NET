from groupdocs.redaction import Redactor, RedactionStatus
from groupdocs.redaction.options import RasterizationOptions
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions
from groupdocs.pydrawing import Color


def save_to_stream():
    # Define the color of redaction
    color = Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = ReplacementOptions(color)
    ex_red = ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with Redactor("./sample.docx") as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)

        if result.status != RedactionStatus.FAILED:
            # Save the document to a stream and convert its pages to images
            ro = RasterizationOptions()
            ro.enabled = True
            with open("./redacted-sample.pdf", "wb") as stream_out:
                redactor.save(stream_out, ro)

            print("Document redacted successfully.\nCheck output in ./redacted-sample.pdf")
        else:
            print("Redaction failed!")


if __name__ == "__main__":
    save_to_stream()