from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions, AdvancedRasterizationOptions
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions


def use_advanced_rasterization_options():
    # Specify the redaction options
    repl_opt = ReplacementOptions("[personal]")
    ex_red = ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with Redactor("./sample.docx") as redactor:

        # Apply the redaction
        redactor.apply(ex_red)

        # Save the document with advanced options (convert pages into images, and save PDF with scan-like pages)
        so = SaveOptions()
        so.rasterization.enabled = True
        so.redacted_file_suffix = "_scan"
        so.rasterization.add_advanced_option(AdvancedRasterizationOptions.BORDER)
        so.rasterization.add_advanced_option(AdvancedRasterizationOptions.NOISE)
        so.rasterization.add_advanced_option(AdvancedRasterizationOptions.GRAYSCALE)
        so.rasterization.add_advanced_option(AdvancedRasterizationOptions.TILT)
        result_path = redactor.save(so)
        print(f"Document redacted successfully.\nCheck output in {result_path}")


if __name__ == "__main__":
    use_advanced_rasterization_options()