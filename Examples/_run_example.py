"""Internal helper: run a single example with evaluation-mode limits made non-fatal.

`run_all_examples.py` invokes this wrapper for each example as a separate
subprocess. Two things this gives us under the current evaluation limits:

  * **Fresh .NET runtime per example.** Without a license the trial build allows
    only **one document to be opened per process** — a second `Redactor(...)`
    raises ``TrialLimitationsException``. Running each example in its own
    subprocess resets that one-document budget for every example, so the suite
    runs green even unlicensed.

  * **Trial-limit errors are non-fatal.** A handful of examples open more than
    one document or apply more than one redaction; unlicensed, those raise
    ``TrialLimitationsException`` ("Trial mode allows only ..."). The wrapper
    catches that specific error, logs a note, and exits 0 — the example still
    demonstrates the API. With a license applied, this never triggers.

The wrapper self-applies the license from ``GROUPDOCS_LIC_PATH`` if it is set in
the environment (the parent runner exports it but does not call
``License().set_license`` in-process, because that would license only the parent
process, not the subprocesses).

Usage (from ``run_all_examples.py``)::

    python Examples/_run_example.py <path/to/example.py>
"""
from __future__ import annotations

import os
import runpy
import sys

from groupdocs.redaction import License


def _apply_license() -> None:
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        try:
            License().set_license(license_path)
        except Exception:
            # If the license can't be applied (corrupted, expired, etc.) just
            # fall back to evaluation mode — the guard below handles the limits.
            pass


def _is_trial_limit(exc: BaseException) -> bool:
    message = str(exc)
    lowered = message.lower()
    return (
        type(exc).__name__ == "TrialLimitationsException"
        or "Trial mode" in message
        or "Evaluation only" in message
        or ("trial" in lowered and "limit" in lowered)
    )


def _is_platform_unsupported(exc: BaseException) -> bool:
    """True for the .NET System.Drawing-on-Linux limitation.

    The 26.6.0 wheel bundles a .NET 10 runtime; `System.Drawing.Common` is
    Windows-only there (the .NET-6 `EnableUnixSupport` switch was removed after
    .NET 6). As a result the rasterize-to-PDF and image-export paths raise
    ``PlatformNotSupportedException`` on Linux/macOS. Text, metadata, annotation,
    and original-format saves are unaffected. We log a clear note and treat it as
    a platform skip so the example suite stays green on Linux CI while making the
    limitation explicit; on Windows these examples run fully.
    """
    message = str(exc)
    return (
        "PlatformNotSupportedException" in message
        or "System.Drawing.Common is not supported" in message
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: _run_example.py <example.py>", file=sys.stderr)
        return 2

    _apply_license()

    try:
        runpy.run_path(argv[1], run_name="__main__")
    except Exception as exc:
        if _is_trial_limit(exc):
            print(
                "Note: example stopped at an evaluation-mode limit — "
                f"{str(exc).splitlines()[0]} "
                "(apply a license to run it fully)."
            )
            return 0
        if _is_platform_unsupported(exc):
            print(
                "Note: this example's rasterization / image-export step is not "
                "supported on this platform (System.Drawing.Common is Windows-only "
                "in the bundled .NET runtime). Text, metadata, and annotation "
                "redaction and original-format saves work on all platforms; run on "
                "Windows to exercise the rasterized-PDF and image paths."
            )
            return 0
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
