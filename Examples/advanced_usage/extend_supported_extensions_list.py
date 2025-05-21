import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.redaction.configuration as grc
import test_files
import utils

# The following example demonstrates how to add a custom file extension to the list of supported extensions

def run():
    
    print("\n[Example Advanced Usage] # extend_supported_extensions_list.py : Extend supported formats list")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_dump)

    # Add .dump format to the list of supported formats
    config = grc.RedactorConfiguration.get_instance()

    settings = config.find_format(".txt")

    settings.extension_filter = settings.extension_filter + ",.dump";

    # Specify the redaction options
    repl_opt = grr.ReplacementOptions("[redacted]")
    ex_red = grr.ExactPhraseRedaction("dolor", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        # Save the redacted document
        result_path = redactor.save()

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
