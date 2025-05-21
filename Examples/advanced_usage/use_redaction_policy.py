import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils
import os
from os.path import join

# The following example demonstrates how to load and apply a redaction policy
# The policy is loaded from a file and applied to all files in given folder. The redacted files are saved in different folders, depending on their processing status (success/failure)

def run():
    
    print("\n[Example Advanced Usage] # use_redaction_policy.py : Using redaction policies")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    policy_file = utils.prepare_output_directory(output_directory, test_files.redaction_policy)
    inbound_dir = utils.prepare_directory(output_directory, "inbound")
    utils.prepare_output_directory(inbound_dir, test_files.sample_docx)
    utils.prepare_output_directory(inbound_dir, test_files.sample_jpg)
    utils.prepare_output_directory(inbound_dir, test_files.sample_pdf)
    utils.prepare_output_directory(inbound_dir, test_files.sample_xlsx)
    out_bound_done_dir = utils.prepare_directory(output_directory, "out_bound_done")
    out_bound_failed_dir = utils.prepare_directory(output_directory, "out_bound_failed")

    # Initialize RedactionPolicy
    policy = gr.RedactionPolicy.load(policy_file)

    for file_entry in os.listdir(inbound_dir):
        cur_file = os.path.join(inbound_dir, file_entry)

        # Load the document to be redacted
        with gr.Redactor(cur_file) as redactor:

            # Apply the redaction
            result = redactor.apply(policy)

            # Get output folder
            result_dir = out_bound_done_dir
            if (result.status == gr.RedactionStatus.FAILED):
                result_dir = out_bound_failed_dir

            output_file = join(result_dir, os.path.basename(cur_file))

            # Save file
            ro = gro.RasterizationOptions()
            ro.enabled = False
            with open(output_file, "wb") as stream_out:
                redactor.save(stream_out, ro)
                print(f"Document saved to {output_file}.")

    print("======================================.")
