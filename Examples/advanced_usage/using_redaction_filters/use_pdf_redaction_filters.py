import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import groupdocs.pydrawing as grd
import test_files
import utils

# The following example demonstrates how to apply redaction to the bottom half of the last page in a PDF document

def run():
    
    print("\n[Example Advanced Usage] # use_pdf_redaction_filters.py : Using redaction filters")

    # Prepare files and output directory
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.multipage_pdf)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:
        doc_info = redactor.get_document_info()
        lastPage = doc_info.pages[doc_info.page_count - 1]

        # Define the redaction area start point
        sample_point = grd.Point(0, int(lastPage.height/2))
        # Define the redaction area size
        sample_size = grd.Size(lastPage.width, int(lastPage.height/2))

        # Filters array
        filters = [
            grr.PageRangeFilter(grr.PageSeekOrigin.END, 0, 1),
            grr.PageAreaFilter(sample_point, sample_size)
        ]

        # Specify the redaction options
        repl_opt = grr.ReplacementOptions("[secret]")
        repl_opt.filters = filters
        ex_red = grr.ExactPhraseRedaction("bibliography", False, repl_opt)

        # Apply the redaction
        result = redactor.apply(ex_red)
        
        # Save the redacted document
        result_path = redactor.save()

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")