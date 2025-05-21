import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils

# The following example demonstrates how to remove 3 frames from an animated GIF image

def run():
    
    print("\n[Example Basic Usage] # remove_frame_from_image.py : Remove multi-page image frames")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_gif)

    # Specify the redaction options
    rem_opt = grr.RemovePageRedaction(grr.PageSeekOrigin.BEGIN, 2, 5)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Remove 3 frames starting from 3nd one, requires at least 7 frames
        doc_info = redactor.get_document_info()

        if doc_info.page_count >= 7:
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
