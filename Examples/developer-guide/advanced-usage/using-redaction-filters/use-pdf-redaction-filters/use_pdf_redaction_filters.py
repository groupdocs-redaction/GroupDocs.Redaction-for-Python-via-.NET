from groupdocs.redaction import Redactor
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import (
    ExactPhraseRedaction,
    ReplacementOptions,
    PageRangeFilter,
    PageAreaFilter,
    PageSeekOrigin,
)
from groupdocs.pydrawing import Point, Size


def use_pdf_redaction_filters():
    # Load the document to be redacted
    with Redactor("./multipage_sample.pdf") as redactor:

        # Get the actual size information for the last page
        doc_info = redactor.get_document_info()
        last_page = doc_info.pages[doc_info.page_count - 1]

        # Define the redaction area start point
        sample_point = Point(0, int(last_page.height / 2))
        # Define the redaction area size
        sample_size = Size(last_page.width, int(last_page.height / 2))

        # Combine page-range and page-area filters to scope the redaction
        filters = [
            PageRangeFilter(PageSeekOrigin.END, 0, 1),
            PageAreaFilter(sample_point, sample_size),
        ]

        # Specify the redaction options with the filters
        repl_opt = ReplacementOptions("[secret]")
        repl_opt.filters = filters
        ex_red = ExactPhraseRedaction("bibliography", False, repl_opt)

        # Apply the redaction
        redactor.apply(ex_red)

        # Save the redacted document
        save_options = SaveOptions()
        save_options.add_suffix = True
        save_options.rasterize_to_pdf = True
        save_options.redacted_file_suffix = "redacted"
        result_path = redactor.save(save_options)
        print(f"Document redacted successfully.\nCheck output in {result_path}.")


if __name__ == "__main__":
    use_pdf_redaction_filters()