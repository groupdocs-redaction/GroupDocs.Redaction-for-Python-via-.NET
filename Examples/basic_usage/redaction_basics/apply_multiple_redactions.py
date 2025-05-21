import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to apply a list of redactions

def run():
    
    print("\n[Example Basic Usage] # apply_multiple_redactions.py : Redact file with multiple redactions")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_docx)

    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Provide redaction options
    redactionList = [
        grr.ExactPhraseRedaction("John Doe", grr.ReplacementOptions("[Client]")),
        grr.RegexRedaction("Redaction", grr.ReplacementOptions("[Product]")),
        grr.RegexRedaction("\\d{2}\\s*\\d{2}[^\\d]*\\d{6}", grr.ReplacementOptions(color)),
        grr.DeleteAnnotationRedaction(),
        grr.EraseMetadataRedaction(grr.MetadataFilters.ALL)
    ]

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(redactionList)

        if (result.status != gr.RedactionStatus.FAILED):
            # By default, the redacted document is saved in PDF format
            result_path = redactor.save()
            print(f"Document redacted successfully.\nCheck output in {result_path}")
        else:
            # Dump all failed or skipped redactions
            print(f"Redaction failed!")
            for log_entry in result.redaction_log:
                if (log_entry.result.status != gr.RedactionStatus.APPLIED):
                    print(f"Status is {log_entry.result.status}, details: {log_entry.result.error_message}")

    print("======================================.")
