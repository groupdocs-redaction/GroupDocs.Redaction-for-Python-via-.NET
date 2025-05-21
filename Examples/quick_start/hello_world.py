import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
from groupdocs.pydrawing import Color
import os
from os.path import join
import test_files
import utils

# Basic example of GroupDocs.Redaction usage

def run():
    print("\n[Quick Start] # hello_world.py : Redact text in a document")

    # Prepare files and output directory
    document_path = test_files.sample_docx
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, "redacted_"+os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Specify the redaction options
    color = Color.from_argb(128, 255, 0, 0)
    repl_o = grr.ReplacementOptions(color)
    ep_red = grr.ExactPhraseRedaction("John Doe", repl_o)

    # Load the document to be redacted
    with gr.Redactor(document_path) as redactor:

        # Apply the redaction
        result = redactor.apply(ep_red)
        
        # Save the redacted document
        ras_o = gro.RasterizationOptions()
        ras_o.enabled = False
        with open(output_document_path, 'wb') as stream:
            redactor.save(stream, ras_o)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {output_directory}.")
    print("======================================.")
