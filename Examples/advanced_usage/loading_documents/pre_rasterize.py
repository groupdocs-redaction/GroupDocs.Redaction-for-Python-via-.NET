import groupdocs.redaction as gr
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to require pre-rasterization for a Microsoft Word document

def run():
    
    print("\n[Example Advanced Usage] # pre_rasterize.py : Use document rasterization")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)

    # Specify the redaction options
    repl_opt = grr.ReplacementOptions("[personal]")
    ex_red = grr.ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)

        if (result.status != gr.RedactionStatus.FAILED):
            # By default, the redacted document is saved in PDF format
            result_path = redactor.save()
            print(f"Document redacted successfully.\nCheck output in {result_path}")
        else:
            print(f"Redaction failed!")
    print("======================================.")
