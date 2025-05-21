import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
from datetime import datetime
import utils

# The following example demonstrates how to save file in its original format

def run():
    
    print("\n[Example Advanced Usage] # save_in_original_format.py : Save redacted document to original format")

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
        
        # Save the redacted document
        so = gro.SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        date_time_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        so.redacted_file_suffix = date_time_str

        result_path = redactor.save(so)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
