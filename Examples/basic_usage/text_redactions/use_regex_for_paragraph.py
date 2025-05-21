import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to redact the whole paragraph in a PDF document

def run():
    
    print("\n[Example Basic Usage] # use_regex_for_paragraph.py : Redact paragraphs content")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.lorem_ipsum_pdf)

    # Specify the redaction options
    color = grd.Color.from_argb(255, 220, 20, 60)
    repl_opt = grr.ReplacementOptions(color)
    ex_red = grr.ExactPhraseRedaction("(Lorem(\n|.)+?urna)", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        # Save the redacted document
        so = gro.SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        result_path = redactor.save(so)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
