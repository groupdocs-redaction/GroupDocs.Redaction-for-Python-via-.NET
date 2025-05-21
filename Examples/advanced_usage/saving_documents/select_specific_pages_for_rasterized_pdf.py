import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to select page range and PDF compliance level for rasterization

def run():
    
    print("\n[Example Advanced Usage] # select_specific_pages_for_rasterized_pdf.py : Save redacted document to PDF with specific page rasterization")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.multipage_docx)

    # Define color of redaction
    color = grd.Color.from_argb(255, 220, 20, 60)

    # Specify the redaction options
    repl_opt = grr.ReplacementOptions(color)
    ex_red = grr.ExactPhraseRedaction("John Doe", repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        if (result.status != gr.RedactionStatus.FAILED):
            # Save the processed document
            so = gro.SaveOptions()
            so.rasterization.enabled = True # convert pages to images for compatibility
            so.rasterization.page_index = 5 # start from 6th page (index is 0-based)
            so.rasterization.page_count = 1 # save only one page
            so.rasterization.compliance = gro.PdfComplianceLevel.PDF_A1A # PDF format
            so.add_suffix = False
            result_path = redactor.save(so)

            print(f"Document redacted successfully.\nCheck output in {result_path}")
        else:
            print(f"Redaction failed!")
    print("======================================.")
