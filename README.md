[Product Page](https://products.groupdocs.com/redaction/python-net/) | [Docs](https://docs.groupdocs.com/redaction/python-net/) | [Free Web Demo](https://products.groupdocs.app/redaction/family) | [API Reference](https://reference.groupdocs.com/redaction/python-net/) | [Blog](https://blog.groupdocs.com/category/redaction/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/redaction/) | [Temporary License](https://purchase.groupdocs.com/temporary-license/)

# GroupDocs.Redaction for Python via .NET

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-redaction-common-banner.png)](https://releases.groupdocs.com/conversion/python-net/)

[GroupDocs.Redaction for Python via .NET](https://products.groupdocs.com/redaction/python-net) is a powerful tool for protecting sensitive information in business files across many formats. It lets you redact text, images, metadata, annotations, and other hidden data to keep your documents secure. 

<br>
<p align="center">
  <a title="Download complete GroupDocs.Redaction for Python via .NET source code" href="https://github.com/groupdocs-redaction/GroupDocs.Redaction-for-Python-via-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

## Document Redaction Features

- Remove sensitive or confidential information from [30+ different file formats](https://docs.groupdocs.com/redaction/python-net/supported-document-formats).
- Remove document metadata, comments and annotations.
- Make a rasterized PDF version of the redacted document for better security.
- Keep the document in its original format after the redaction process.
- Set the redaction scope to a specific worksheet or column.
- Modify compliance level from PDF/A-1b to PDF/A-1a during rasterizing PDF.

## Supported Redaction Types

**Text:** Hide or replace text in a document body with a colored overlay.\
**Image:** Cover selected areas of an image with a solid color.\
**Metadata:** Clear or replace metadata values.\
**Annotation:** Remove or redact annotations.

## Develop & Deploy Anywhere

**Operation Systems:** Windows, Linux, Mac OS\
**Supported IDE:** IDLE, PyCharm, Visual Studio Code\
**Environment:** Python 3.9+ and .Net 6+

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.9](https://www.python.org/downloads/) and the [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) runtime (or higher) are installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
    git clone https://github.com/groupdocs-redaction/GroupDocs.Redaction-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd GroupDocs.Redaction-for-Python-via-.NET\Examples
   ```

4. **Install Package**: To install the package, run `pip install groupdocs-redaction-net`. If you need to use a different package version, you can update the requirements.txt file accordingly.

   Alternatively, you can download the `whl` file for your operating system from the official [GroupDocs Releases](https://releases.groupdocs.com/redaction/python-net/#direct-download) website. To install the package manually, copy the whl file to the `Examples` directory and run the following command:
   
   ```bash
   pip install groupdocs_redaction_net-*.whl
   ```

5. **Configure License (Optional)**: If you have a license file, you can set the license path in the `utils.py` file. By default, GroupDocs.Conversion for Python via .NET checks for the `GROUPDOCS_REDACTION_PYTHON_LIC` environment variable. You can also [get a temporary license](https://purchase.groupdocs.com/temporary-license) to test all the features.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python run_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script files.

7. **Check results**: Redacted files are saved in the `Examples\Output` folder.


## Example: Case-Sensitive Phrase Redaction in DOCX

```python
    # Specify the redaction options
    case_sensitive = True
    repl_opt = grr.ReplacementOptions("[personal]")
    ex_red = grr.ExactPhraseRedaction("John Doe", case_sensitive, repl_opt)

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(ex_red)
```

## Example: Redact Strings in PDF Annotations

```python
    # Specify the redaction options
    a_red = grr.AnnotationRedaction("(?im:john)", "[redacted]")

    # Load the document to be redacted
    with gr.Redactor(source_file) as redactor:

        # Apply the redaction
        result = redactor.apply(a_red)
```

[Product Page](https://products.groupdocs.com/redaction/python-net/) | [Docs](https://docs.groupdocs.com/redaction/python-net/) | [Free Web Demo](https://products.groupdocs.app/redaction/family) | [API Reference](https://reference.groupdocs.com/redaction/python-net/) | [Blog](https://blog.groupdocs.com/category/redaction/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/redaction/) | [Temporary License](https://purchase.groupdocs.com/temporary-license/)
