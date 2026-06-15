# GroupDocs.Redaction for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-redaction-python-net-banner.png)](https://releases.groupdocs.com/redaction/python-net/)

[Product Page](https://products.groupdocs.com/redaction/python-net/) | [Docs](https://docs.groupdocs.com/redaction/python-net/) | [Demos](https://products.groupdocs.app/redaction/family) | [API Reference](https://reference.groupdocs.com/redaction/python-net/) | [Blog](https://blog.groupdocs.com/category/redaction/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/redaction) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Redaction for Python via .NET](https://products.groupdocs.com/redaction/python-net/) permanently removes sensitive content from documents: redact text by exact phrase or regular expression, scrub or rewrite metadata, cover image areas, remove annotations and pages, and optionally save a rasterized PDF so the underlying data can never be recovered — all on-premise, with no MS Office or OpenOffice installation required.

## Features

- **Text Redaction**: Replace or hide text matched by an exact phrase or a regular expression, with a colored overlay or replacement string.
- **Metadata Redaction**: Erase or rewrite document metadata, either wholesale or filtered by property.
- **Image Redaction**: Cover selected areas of an image with a solid color and clean embedded image metadata.
- **Annotation & Page Redaction**: Remove or redact annotations, and delete pages or page ranges.
- **Rasterized Output**: Optionally flatten the redacted document to a rasterized PDF (with adjustable PDF/A compliance) so redacted content cannot be recovered.
- **Redaction Policies**: Describe a reusable set of redactions as a policy and apply it across many documents.
- **On-Premise**: No MS Office or OpenOffice installation required.

## Supported File Formats

GroupDocs.Redaction for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, and image formats. See the [full list of supported formats](https://docs.groupdocs.com/redaction/python-net/supported-document-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.5+](https://www.python.org/downloads/) is installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-redaction/GroupDocs.Redaction-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Redaction-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/redaction/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_redaction_net-26.6.0-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: `run_all_examples.py` automatically applies a license when one is available, looking in two places:

   - The `GROUPDOCS_LIC_PATH` environment variable — set it to the absolute path of your `.lic` file (recommended).
   - Any `*.lic` file in the repository root.

   With a license applied, examples run with the full feature set; without one, the library runs in evaluation mode (the trial build limits how many documents a single process may open and marks the output). Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the .NET runtime dependencies (`libicu-dev`, `libgdiplus`, `libfontconfig1`), and the `groupdocs-redaction-net` package preinstalled.

```bash
# Build the image
docker build -t redaction-examples .

# Run unlicensed (evaluation mode)
docker run --rm redaction-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    redaction-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-redaction-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/redaction/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting.

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/redaction/python-net/agents-and-llm-integration/) page for the per-tool setup snippets.

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Redaction for Python via .NET documentation](https://docs.groupdocs.com/redaction/python-net/).

We also offer **GroupDocs.Redaction** packages for other platforms:
* [**GroupDocs.Redaction for .NET**](https://products.groupdocs.com/redaction/net/)
* [**GroupDocs.Redaction for Java**](https://products.groupdocs.com/redaction/java/)
* [**GroupDocs.Redaction for Node.js via Java**](https://products.groupdocs.com/redaction/nodejs-java/)

---

[Product Page](https://products.groupdocs.com/redaction/python-net/) | [Docs](https://docs.groupdocs.com/redaction/python-net/) | [Demos](https://products.groupdocs.app/redaction/family) | [API Reference](https://reference.groupdocs.com/redaction/python-net/) | [Blog](https://blog.groupdocs.com/category/redaction/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/redaction) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
