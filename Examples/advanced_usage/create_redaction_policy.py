import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import utils
import os
from os.path import join

# The following example demonstrates how to create and save redaction policy for future use
# A set of redactions, configured in code, can be saved for future use as an XML file with redaction policy

def run():
    
    print("\n[Example Advanced Usage] # create_redaction_policy.py : Using redaction policies")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    output_file = join(output_directory, "sample_policy.xml")

    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Configure Redactions
    redactions = [
        grr.ExactPhraseRedaction("Redaction", grr.ReplacementOptions("[Product]")),
        grr.RegexRedaction("\\d{2}\\s*\\d{2}[^\\d]*\\d{6}", grr.ReplacementOptions(color)),
        grr.DeleteAnnotationRedaction(),
        grr.EraseMetadataRedaction(grr.MetadataFilters.ALL)
    ]

    # Create policy
    policy = gr.RedactionPolicy(redactions)

    # Save RedactionPolicy
    policy.save(output_file)
    print(f"Redactions policy saved to {output_file}")
    print("======================================.")
