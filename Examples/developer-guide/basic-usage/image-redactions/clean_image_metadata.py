from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import EraseMetadataRedaction, MetadataFilters


def clean_image_metadata():
    # Specify the redaction options to remove all image metadata (e.g. EXIF)
    er_opt = EraseMetadataRedaction(MetadataFilters.ALL)

    # Load the image to be redacted
    with Redactor("./sample.jpg") as redactor:
        # Apply the redaction
        result = redactor.apply(er_opt)

        # Save the redacted image next to the source file
        so = SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        so.redacted_file_suffix = "redacted"
        redactor.save(so)


if __name__ == "__main__":
    clean_image_metadata()