import os
import subprocess
import sys

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# output that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Redaction.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Redaction for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to load, redact, and save documents with GroupDocs.Redaction.
Each example demonstrates different use cases and functionalities such as:

- Redacting text by exact phrase or regular expression.
- Erasing or rewriting document metadata.
- Covering image areas and cleaning embedded image metadata.
- Rewriting or deleting annotations and removing pages.
- Loading documents from a file path or stream, including password-protected files.
- Saving in the original format or as a rasterized PDF.
- Applying reusable redaction policies.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def announce_license():
    """Print whether GROUPDOCS_LIC_PATH points at a usable license file.

    The license itself is applied inside each subprocess by _run_example.py —
    setting it here would only license the runner process, not the children.
    """
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        print(f"{GREEN}License available at: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example as a subprocess via the _run_example.py wrapper.

    Subprocess isolation gives every example a fresh .NET runtime, which matters
    under the current evaluation build: unlicensed, only one document may be
    opened per process, so an in-process runner would raise
    TrialLimitationsException on the second example. The wrapper also makes
    eval-mode trial-limit errors non-fatal so the suite stays green unlicensed.
    """
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)
    wrapper = os.path.join(base_dir, "_run_example.py")

    result = subprocess.run(
        [sys.executable, wrapper, full_path],
        cwd=example_dir,
        env=os.environ.copy(),
    )
    if result.returncode != 0:
        raise RuntimeError(f"subprocess exited with code {result.returncode}")

examples = [
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "getting-started/hello-world/hello_world.py",
    "developer-guide/basic-usage/get-supported-file-formats/list_supported_formats.py",
    "developer-guide/basic-usage/get-file-info/get_local_file_info.py",
    "developer-guide/basic-usage/get-file-info/get_file_info_from_stream.py",
    "developer-guide/basic-usage/redaction-basics/apply_redaction.py",
    "developer-guide/basic-usage/redaction-basics/apply_multiple_redactions.py",
    "developer-guide/basic-usage/text-redactions/redact_exact_phrase.py",
    "developer-guide/basic-usage/text-redactions/redact_case_sensitive_phrase.py",
    "developer-guide/basic-usage/text-redactions/redact_with_color_box.py",
    "developer-guide/basic-usage/text-redactions/redact_right_to_left_text.py",
    "developer-guide/basic-usage/text-redactions/redact_with_regex.py",
    "developer-guide/basic-usage/text-redactions/redact_whole_paragraph.py",
    "developer-guide/basic-usage/metadata-redactions/clean_all_metadata.py",
    "developer-guide/basic-usage/metadata-redactions/redact_metadata.py",
    "developer-guide/basic-usage/metadata-redactions/redact_metadata_with_filter.py",
    "developer-guide/basic-usage/annotation-redactions/remove_all_annotations.py",
    "developer-guide/basic-usage/annotation-redactions/redact_annotations.py",
    "developer-guide/basic-usage/spreadsheet-redactions/redact_spreadsheet_content.py",
    "developer-guide/basic-usage/image-redactions/redact_image_area.py",
    "developer-guide/basic-usage/image-redactions/clean_image_metadata.py",
    "developer-guide/basic-usage/image-redactions/redact_embedded_images.py",
    "developer-guide/basic-usage/remove-page-redactions/remove_page_range.py",
    "developer-guide/basic-usage/remove-page-redactions/remove_last_page.py",
    "developer-guide/basic-usage/remove-page-redactions/remove_frame_from_image.py",
    "developer-guide/advanced-usage/loading-documents/load-from-local-disc/load_from_local_disc.py",
    "developer-guide/advanced-usage/loading-documents/load-from-stream/load_from_stream.py",
    "developer-guide/advanced-usage/loading-documents/load-password-protected-file/load_password_protected_file.py",
    "developer-guide/advanced-usage/loading-documents/pre-rasterize/pre_rasterize_document.py",
    "developer-guide/advanced-usage/saving-documents/save-in-original-format/save_in_original_format.py",
    "developer-guide/advanced-usage/saving-documents/save-in-rasterized-pdf/save_in_rasterized_pdf.py",
    "developer-guide/advanced-usage/saving-documents/save-overwriting-original-file/save_overwriting_original_file.py",
    "developer-guide/advanced-usage/saving-documents/save-with-default-options/save_with_default_options.py",
    "developer-guide/advanced-usage/saving-documents/save-to-stream/save_to_stream.py",
    "developer-guide/advanced-usage/saving-documents/select-specific-pages-for-rasterized-pdf/select_specific_pages_for_rasterized_pdf.py",
    "developer-guide/advanced-usage/saving-documents/use-advanced-rasterization-options/use_advanced_rasterization_options.py",
    "developer-guide/advanced-usage/saving-documents/use-advanced-rasterization-options/use_grayscale_rasterization_option.py",
    "developer-guide/advanced-usage/using-redaction-filters/use-pdf-redaction-filters/use_pdf_redaction_filters.py",
    "developer-guide/advanced-usage/use-redaction-policies/create_redaction_policy.py",
    "developer-guide/advanced-usage/use-redaction-policies/use_redaction_policy.py",
    "developer-guide/advanced-usage/extend-supported-extensions-list/extend_supported_extensions_list.py",
    "developer-guide/advanced-usage/create-pdf-with-image-redaction/create_pdf_with_image_redaction.py",
]

print_intro()
announce_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
