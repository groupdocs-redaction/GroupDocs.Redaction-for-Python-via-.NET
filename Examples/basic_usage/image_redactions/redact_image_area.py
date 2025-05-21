import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to redact a rectangular area of an image

def run():
    
    print("\n[Example Basic Usage] # redact_image_area.py : Redact image area")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_jpg)

    # Define the position on image
    sample_point = grd.Point(385, 485)
    # Define the size of the area which need to be redacted
    sample_size = grd.Size(1793, 2069)
    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = grr.RegionReplacementOptions(color, sample_size)
    img_red = grr.ImageAreaRedaction(sample_point, repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(img_red)

        if (result.status != gr.RedactionStatus.FAILED):
            # By default, the redacted document is saved in PDF format
            result_path = redactor.save()
            print(f"Document redacted successfully.\nCheck output in {result_path}")
        else:
            print(f"Redaction failed!")
    print("======================================.")
