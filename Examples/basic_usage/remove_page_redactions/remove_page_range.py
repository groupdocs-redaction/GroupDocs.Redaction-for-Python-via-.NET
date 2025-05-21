import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils

# The following example demonstrates how to remove a specific page range from a document

def run():
    
    print("\n[Example Basic Usage] # remove_page_range.py : Remove document pages")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.multipage_pdf)

    # Specify the redaction options
    start_index = 1
    pages_to_delete = 1;
    rem_opt = grr.RemovePageRedaction(grr.PageSeekOrigin.BEGIN, start_index, pages_to_delete)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:
        
        # Get document info
        doc_info = redactor.get_document_info()

        # Removes 1 page starting from 2nd one, requires at least 2 pages
        if doc_info.page_count >= 2:
            # Apply the redaction
            result = redactor.apply(rem_opt)
        
            # Save the redacted document
            so = gro.SaveOptions()
            so.add_suffix = True
            so.rasterize_to_pdf = False
            result_path = redactor.save(so)

            # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
            print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
