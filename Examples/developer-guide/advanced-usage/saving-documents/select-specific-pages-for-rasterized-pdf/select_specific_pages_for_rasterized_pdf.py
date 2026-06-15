from groupdocs.redaction import Redactor, RedactionStatus
from groupdocs.redaction.options import SaveOptions, PdfComplianceLevel
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions
from groupdocs.pydrawing import Color


def select_specific_pages_for_rasterized_pdf():
    # Define the color of redaction
    color = Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = ReplacementOptions(color)
    ex_red = ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with Redactor("./multipage_sample.docx") as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)

        if result.status != RedactionStatus.FAILED:
            # Save the processed document, selecting the page range and compliance level
            so = SaveOptions()
            so.rasterization.enabled = True  # convert pages to images for compatibility
            so.rasterization.page_index = 5  # start from 6th page (index is 0-based)
            so.rasterization.page_count = 1  # save only one page
            so.rasterization.compliance = PdfComplianceLevel.PDF_A1A  # PDF/A-1a format
            so.add_suffix = False
            result_path = redactor.save(so)

            print(f"Document redacted successfully.\nCheck output in {result_path}")
        else:
            print("Redaction failed!")


if __name__ == "__main__":
    select_specific_pages_for_rasterized_pdf()