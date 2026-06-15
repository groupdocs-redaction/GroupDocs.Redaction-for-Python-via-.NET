from groupdocs.redaction import Redactor, RedactionStatus
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import ImageAreaRedaction, RegionReplacementOptions
from groupdocs.pydrawing import Color, Point, Size


def redact_image_area():
    # Define the top-left position of the area to redact
    sample_point = Point(385, 485)
    # Define the size of the area which needs to be redacted
    sample_size = Size(1793, 2069)
    # Define the color of the redaction box
    color = Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = RegionReplacementOptions(color, sample_size)
    img_red = ImageAreaRedaction(sample_point, repl_opt)

    # Load the document to be redacted
    with Redactor("./sample.jpg") as redactor:
        # Apply the redaction
        result = redactor.apply(img_red)

        if result.status != RedactionStatus.FAILED:
            # By default, the redacted document is saved in PDF format
            save_options = SaveOptions()
            save_options.add_suffix = True
            save_options.rasterize_to_pdf = True
            save_options.redacted_file_suffix = "redacted"
            redactor.save(save_options)


if __name__ == "__main__":
    redact_image_area()