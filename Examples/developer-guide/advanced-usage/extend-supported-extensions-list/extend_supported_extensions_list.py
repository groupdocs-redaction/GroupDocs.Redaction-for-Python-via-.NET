from groupdocs.redaction import Redactor
from groupdocs.redaction.configuration import RedactorConfiguration
from groupdocs.redaction.options import SaveOptions
from groupdocs.redaction.redactions import ExactPhraseRedaction, ReplacementOptions


def extend_supported_extensions_list():
    # Add the .dump format to the list of supported formats, handled as plain text
    config = RedactorConfiguration.get_instance()

    settings = config.find_format(".txt")

    settings.extension_filter = settings.extension_filter + ",.dump"

    # Specify the redaction options
    repl_opt = ReplacementOptions("[redacted]")
    ex_red = ExactPhraseRedaction("dolor", repl_opt)

    # Load the document with the newly supported extension
    with Redactor("./sample.dump") as redactor:

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
    extend_supported_extensions_list()