from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import MetadataSearchRedaction, MetadataFilters


def redact_metadata_with_filter():
    # Specify the redaction options: search pattern and replacement string
    met_red = MetadataSearchRedaction("Company Ltd.", "--company--")

    # Limit the redaction scope to the Company metadata item only
    met_red.filter = MetadataFilters.COMPANY

    # Load the document to be redacted
    with Redactor("./sample.docx") as redactor:
        # Apply the redaction
        result = redactor.apply(met_red)

        # Save the redacted document next to the source file
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        so.redacted_file_suffix = "redacted"
        redactor.save(so)


if __name__ == "__main__":
    redact_metadata_with_filter()