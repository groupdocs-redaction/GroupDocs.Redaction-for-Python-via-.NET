import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.redaction.configuration as grc
import groupdocs.pydrawing as grd
import test_files
import utils
from io import BytesIO
import os
from os.path import join

# The following example demonstrates how to create a rasterized PDF from a Microsoft Word document and apply image redactions to its pages

def run():
    
    print("\n[Example Advanced Usage] # create_pdf_with_image_redaction.py : Word to PDF rasterization")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)
    output_file = join(output_directory, "redacted.pdf")

    # Create an in-memory binary stream
    stream = BytesIO()

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Save the redacted document
        ro = gro.RasterizationOptions()
        ro.enabled = True
        redactor.save(stream, ro)
        stream.seek(0)

    # Define the position on image
    sample_point = grd.Point(40, 160)
    # Define the size of the area which need to be redacted
    sample_size = grd.Size(350, 75)
    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = grr.RegionReplacementOptions(color, sample_size)
    img_red = grr.ImageAreaRedaction(sample_point, repl_opt)

    # Load the stream to be redacted
    with gr.Redactor(stream) as redactor:

        # Apply the redaction
        result = redactor.apply(img_red)
        
        # Re-open the rasterized PDF document to redact its pages as images
        if (result.status != gr.RedactionStatus.FAILED):
            # Save the document to a custom location and convert its pages to images
            ro = gro.RasterizationOptions()
            ro.enabled = True
            with open(output_file, "wb") as stream_out:
                redactor.save(stream_out, ro)

            print(f"Document redacted successfully.\nCheck output in {output_file}")
        else:
            print(f"Redaction failed!")

    print("======================================.")
