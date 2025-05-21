import groupdocs.redaction as gr
import utils
import os

# This example demonstrates how to set license from file.
# The SetLicense method attempts to set a license from several locations relative to the executable.
# You can also use the additional overload to load a license from a stream, this is useful for instance when the 
# License is stored as an embedded resource. 

def run():
    print("\n[Quick Start] # set_license_from_file.py : Set license from file")

    if os.path.exists(utils.license_path):    
        license = gr.License()
        license.set_license(utils.license_path)
        print("License set successfully - GroupDocs.Redaction for Python via .NET")
    else:
       print("We do not ship any license with this example.")
       print("Visit the GroupDocs site to obtain either a temporary or permanent license.")
       print("Learn more about licensing at https://purchase.groupdocs.com/faqs/licensing.")
       print("Learn how to request a temporary license at https://purchase.groupdocs.com/temporary-license.")

    print("======================================.")

