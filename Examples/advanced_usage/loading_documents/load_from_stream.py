import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
from os.path import join
import test_files
import utils

# The following example demonstrates how to load and redact a document using stream

def run():
    
    print("\n[Example Advanced Usage] # load_from_stream.py : Redact a document stored in a stream")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)
    output_file = join(output_directory, "redacted.pdf")

    # Specify the redaction options - remove all annotations
    del_red = grr.DeleteAnnotationRedaction()

    # Load the document as stream to be redacted
    with open(source_file, "rb") as stream_in:
        with gr.Redactor(stream_in) as redactor:

            # Apply the redaction
            result = redactor.apply(del_red)
        
            # Save the redacted document as PDF
            with open(output_file, "wb") as stream_out:
                ro = gro.RasterizationOptions()
                redactor.save(stream_out, ro)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    #print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
