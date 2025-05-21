import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# This example demonstrates how to set a Metered license.
# Learn more about Metered license at https://purchase.groupdocs.com/faqs/licensing/metered.

def run():
    print("\n[Quick Start] # set_metered_license.py : Set metered license")

    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    gr.Metered().set_metered_key(public_key, private_key)
    print("License set successfully.")

    # Process document
    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)

    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = grr.ReplacementOptions(color)
    ex_red = grr.ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        # Get consumption statistics
        consumption_quantitity = gr.Metered.get_consumption_quantity()
        consumption_credit = gr.Metered.get_consumption_credit()

        print(f"Consumption Quantity:{consumption_quantitity} Credit:{consumption_credit}")


    print("======================================.")
