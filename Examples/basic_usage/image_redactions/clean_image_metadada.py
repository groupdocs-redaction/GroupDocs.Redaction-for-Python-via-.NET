import groupdocs.redaction as gr
import groupdocs.redaction.options as gro
import groupdocs.redaction.redactions as grr
import test_files
import utils

# The following example demonstrates how to edit exif data (erase them) from a photo or any other image

def run():
    
    print("\n[Example Basic Usage] # clean_image_metadada.py : Clean all image metadata")

    # Prepare output directory and source file
    output_directory = utils.get_output_directory_path()
    source_file = utils.prepare_output_directory(output_directory, test_files.sample_jpg)

    # Specify the redaction options to remove all metadata
    er_opt = grr.EraseMetadataRedaction(grr.MetadataFilters.ALL)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(er_opt)

        # Save the redacted document
        so = gro.SaveOptions()
        so.add_suffix = True
        so.rasterize_to_pdf = False
        result_path = redactor.save(so)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"Document redacted successfully.\nCheck output in {result_path}.")
    print("======================================.")
