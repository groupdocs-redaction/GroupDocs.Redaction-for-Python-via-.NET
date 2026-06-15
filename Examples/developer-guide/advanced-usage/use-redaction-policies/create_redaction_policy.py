from groupdocs.redaction import RedactionPolicy
from groupdocs.redaction.redactions import (
    ExactPhraseRedaction,
    ReplacementOptions,
    RegexRedaction,
    DeleteAnnotationRedaction,
    EraseMetadataRedaction,
    MetadataFilters,
)
from groupdocs.pydrawing import Color


def create_redaction_policy():
    # Define the color of redaction
    color = Color.from_argb(255, 220, 20, 60)

    # Configure the redactions
    redactions = [
        ExactPhraseRedaction("Redaction", ReplacementOptions("[Product]")),
        RegexRedaction("\\d{2}\\s*\\d{2}[^\\d]*\\d{6}", ReplacementOptions(color)),
        DeleteAnnotationRedaction(),
        EraseMetadataRedaction(MetadataFilters.ALL),
    ]

    # Create the policy
    policy = RedactionPolicy(redactions)

    # Save the redaction policy to an XML file
    policy.save("./sample_policy.xml")
    print("Redactions policy saved to ./sample_policy.xml")


if __name__ == "__main__":
    create_redaction_policy()