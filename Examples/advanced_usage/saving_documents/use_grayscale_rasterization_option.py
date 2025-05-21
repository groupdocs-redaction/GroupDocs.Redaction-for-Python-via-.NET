import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils

# The following example demonstrates how to apply the grayscale advanced rasterization option

def run():
    
    print("\n[Example Advanced Usage] # use_grayscale_rasterization_option.py : Save document using grayscale rasterization")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Save the document with the custom grayscale effect
        so = gro.SaveOptions()
        so.rasterization.enabled = True
        so.redacted_file_suffix = "_scan"
        so.rasterization.add_advanced_option(gro.AdvancedRasterizationOptions.GRAYSCALE)
        result_path = redactor.save(so)

    print(f"Document redacted successfully.\nCheck output in {result_path}")
    print("======================================.")
