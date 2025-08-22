# GroupDocs.Redaction-for-Python-via-.NET

[GroupDocs.Redaction for Python via .NET](https://products.groupdocs.com/redaction/python-net) is a powerful tool for protecting sensitive information in business files across many formats. It lets you redact text, images, metadata, annotations, and other hidden data to keep your documents secure. 

<p align="center">
  <a title="Download complete GroupDocs.Redaction for Python via .NET source code" href="https://github.com/groupdocs-redaction/GroupDocs.Redaction-for-Python-via-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

Directory | Description
--------- | -----------
[Examples](https://github.com/groupdocs-redaction/GroupDocs.Redaction-for-Python-via-.NET/tree/master/Examples)  | This folder includes all Python examples and sample files to help you quickly learn and work with the API features. 

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

## Redaction Support for Documents & Metadata

**Fixed Layout:** PDF\
**Microsoft Word:** DOC, DOT, DOCX, DOCM, DOTX, DOTM, RTF\
**Microsoft Excel:** XLSX, XLSM, XLTX, XLTM, XLS, XLT, CSV\
**Microsoft PowerPoint:** PPT, PPTX, PPSX, POT, PPS, PPTM, PPSM, POTM\
**Image:** JPEG, TIF, TIFF, PNG, BMP, GIF

## Redaction Support for Annotations & Comments

**Fixed Layout:** PDF\
**Microsoft Word:** DOC, DOT, DOCX, DOCM, DOTX, DOTM, RTF\
**Microsoft Excel:** XLSX, XLSM, XLTX, XLTM, XLS, XLT, CSV\
**Microsoft PowerPoint:** PPT, PPTX, PPSX, POT, PPS, PPTM, PPSM, POTM

## Develop & Deploy Anywhere

**Operation Systems:** Windows, Linux, Mac OS\
**Supported IDE:** IDLE, PyCharm, Visual Studio Code\
**Environment:** Python 3.9+ and .Net 6+

## How to run examples

To install the library, run the following command: `pip install groupdocs-redaction-net`. To upgrade to the latest version: `pip install --upgrade groupdocs-redaction-net` to get the latest version.
To start examples call `python .\Examples\run_examples.py`. See results in `.\Examples\Output` folder.

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

