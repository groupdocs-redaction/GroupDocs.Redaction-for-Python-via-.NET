from quick_start import *
from basic_usage import *
from advanced_usage import *


if __name__ == '__main__':
    # Quick Start
    set_license_from_file.run()  
    #set_license_from_stream.run()
    #set_metered_license.run()
    hello_world.run()

    # Basic Usage    

    redact_annotations.run()
    remove_all_annotations.run()
    remove_annotations.run()

    clean_image_metadada.run()
    redact_embedded_images.run()
    redact_image_area.run()

    clean_metadata.run()
    clean_metadata_with_filter.run()
    redact_metadata.run()
    redact_metadata_with_filter.run()

    apply_multiple_redactions.run()
    apply_redaction.run()

    remove_frame_from_image.run()
    remove_last_page.run()
    remove_page_range.run()

    redact_spreadsheet.run()

    use_colored_rectangle.run()
    use_exact_phrase_case_sensitive.run()
    use_exact_phrase_redaction.run()
    use_exact_phrase_right_to_left.run()
    use_regex_for_paragraph.run()
    use_regular_expression.run()

    get_file_info_file.run()
    get_file_info_stream.run()
    get_supported_file_formats.run()
   
    # Advanced Usage

    load_from_local_disc.run()
    load_from_stream.run()
    load_password_protected_file.run()
    pre_rasterize.run()

    save_in_original_format.run()
    save_in_rasterized_pdf.run()
    save_overwriting_original_file.run()
    save_to_stream.run()
    save_with_default_options.run()
    select_specific_pages_for_rasterized_pdf.run()
    use_advanced_rasterization_options.run()
    use_grayscale_rasterization_option.run()

    use_pdf_redaction_filters.run()

    create_pdf_with_image_redaction.run()
    create_redaction_policy.run()
    extend_supported_extensions_list.run()
    use_redaction_policy.run()


