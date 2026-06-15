from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions, AdvancedRasterizationOptions


def use_grayscale_rasterization_option():
    # Load the document to be redacted
    with Redactor("./sample.docx") as redactor:

        # Save the document with the custom grayscale effect
        so = SaveOptions()
        so.rasterization.enabled = True
        so.redacted_file_suffix = "_scan"
        so.rasterization.add_advanced_option(AdvancedRasterizationOptions.GRAYSCALE)
        result_path = redactor.save(so)
        print(f"Document redacted successfully.\nCheck output in {result_path}")


if __name__ == "__main__":
    use_grayscale_rasterization_option()