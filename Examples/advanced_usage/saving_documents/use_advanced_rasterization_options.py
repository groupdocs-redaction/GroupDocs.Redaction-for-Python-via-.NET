import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils

# The following example demonstrates how to apply the advanced rasterization options 

def run():
    
    print("\n[Example Advanced Usage] # use_advanced_rasterization_options.py : Save redacted document using advanced rasterization options")

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
        
        # Save the document with advanced options (convert pages into images, and save PDF with scan-like pages)
        so = gro.SaveOptions()
        so.rasterization.enabled = True
        so.redacted_file_suffix = "_scan"
        so.rasterization.add_advanced_option(gro.AdvancedRasterizationOptions.BORDER)
        so.rasterization.add_advanced_option(gro.AdvancedRasterizationOptions.NOISE)
        so.rasterization.add_advanced_option(gro.AdvancedRasterizationOptions.GRAYSCALE)
        so.rasterization.add_advanced_option(gro.AdvancedRasterizationOptions.TILT)
        result_path = redactor.save(so)

    print(f"Document redacted successfully.\nCheck output in {result_path}")

    print("======================================.")
