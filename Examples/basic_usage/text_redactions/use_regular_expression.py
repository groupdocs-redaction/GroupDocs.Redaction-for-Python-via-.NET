import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to use regular expressions to redact textual documents

def run():
    
    print("\n[Example Basic Usage] # use_regular_expression.py : Redact content using regular expressions")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)

    # Specify the redaction options
    color = grd.Color.from_argb(255, 220, 20, 60)
    repl_opt = grr.ReplacementOptions(color)
    reg_red = grr.RegexRedaction("\\d{2}\\s*\\d{2}[^\\d]*\\d{6}", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(reg_red)
        
        # Save the redacted document
        so = gro.SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        result_path = redactor.save(so)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
