from groupdocs.redaction import Redactor, RedactionPolicy
from groupdocs.redaction.options import SaveOptions

def use_redaction_policy():
    # Load the redaction policy from an XML file
    policy = RedactionPolicy.load("./redaction_policy.xml")

    # Load the document and apply the whole policy in one call
    with Redactor("./sample.docx") as redactor:
        redactor.apply(policy)

        # Keep the original format and append a suffix to the output name
        save_options = SaveOptions()
        save_options.add_suffix = True
        save_options.rasterize_to_pdf = False
        save_options.redacted_file_suffix = "redacted"
        result_path = redactor.save(save_options)

    print(f"Redaction policy applied. Output saved to {result_path}.")

if __name__ == "__main__":
    use_redaction_policy()