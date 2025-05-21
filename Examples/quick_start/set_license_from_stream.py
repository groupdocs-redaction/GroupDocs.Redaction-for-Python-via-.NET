import groupdocs.redaction as gr
import os
from os.path import join
import utils

# This example demonstrates how to set license from stream.

def run():
    print("\n[Quick Start] # set_license_from_stream.py : Set license from stream")

    if os.path.exists(utils.license_path):
        with open(utils.license_path, "rb") as stream:
            gr.License().set_license(stream)

        print("License set successfully.")
    else:
        print("\nWe do not ship any license with this example. " +
              "\nVisit the GroupDocs site to obtain either a temporary or permanent license. " +
              "\nLearn more about licensing at https://purchase.groupdocs.com/faqs/licensing. " +
              "\nLearn how to request a temporary license at https://purchase.groupdocs.com/temporary-license.")

    print("======================================.")