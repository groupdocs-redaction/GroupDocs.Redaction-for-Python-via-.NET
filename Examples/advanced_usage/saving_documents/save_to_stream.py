import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils
from os.path import join

# The following example demonstrates how to save a document to stream

def run():
    
    print("\n[Example Advanced Usage] # save_to_stream.py : Save redacted document to stream")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)
    output_file = join(output_directory, "redacted.pdf")

    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = grr.ReplacementOptions(color)
    ex_red = grr.ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        if (result.status != gr.RedactionStatus.FAILED):
            # Save the document to a custom location and convert its pages to images
            ro = gro.RasterizationOptions()
            ro.enabled = True
            with open(output_file, "wb") as stream_out:
                redactor.save(stream_out, ro)

            print(f"Document redacted successfully.\nCheck output in {source_file}")
        else:
            print(f"Redaction failed!")
    print("======================================.")
