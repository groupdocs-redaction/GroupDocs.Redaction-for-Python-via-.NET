from io import BytesIO

from groupdocs.redaction import Redactor, RedactionStatus
from groupdocs.redaction.options import RasterizationOptions
from groupdocs.redaction.redactions import ImageAreaRedaction, RegionReplacementOptions
from groupdocs.pydrawing import Point, Size, Color


def create_pdf_with_image_redaction():
    # Create an in-memory binary stream
    stream = BytesIO()

    # Load the document and rasterize it to a PDF in the stream
    with Redactor("./sample.docx") as redactor:

        # Save the rasterized document to the stream
        ro = RasterizationOptions()
        ro.enabled = True
        redactor.save(stream, ro)
        stream.seek(0)

    # Define the position on the image
    sample_point = Point(40, 160)
    # Define the size of the area which needs to be redacted
    sample_size = Size(350, 75)
    # Define the color of redaction
    color = Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = RegionReplacementOptions(color, sample_size)
    img_red = ImageAreaRedaction(sample_point, repl_opt)

    # Load the stream to be redacted
    with Redactor(stream) as redactor:

        # Apply the redaction
        result = redactor.apply(img_red)

        # Re-open the rasterized PDF document to redact its pages as images
        if result.status != RedactionStatus.FAILED:
            # Save the document to a file and convert its pages to images
            ro = RasterizationOptions()
            ro.enabled = True
            with open("./redacted-sample.pdf", "wb") as stream_out:
                redactor.save(stream_out, ro)
            print("Document redacted successfully.\nCheck output in ./redacted-sample.pdf")
        else:
            print("Redaction failed!")


if __name__ == "__main__":
    create_pdf_with_image_redaction()