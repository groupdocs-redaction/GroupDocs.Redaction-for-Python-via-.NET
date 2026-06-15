FROM python:3.13-slim

# System dependencies for the .NET runtime: libicu-dev (globalization)
# and libgdiplus + libfontconfig1 (System.Drawing / GDI+, required by the
# image-redaction and PDF-rasterization paths on Linux)
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libgdiplus libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package from PyPI
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
