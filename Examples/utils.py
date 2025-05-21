# utils.py
# This module provides utility functions and constants.

import os
from os.path import join
import inspect
import shutil

license_path = os.environ.get('GROUPDOCS_REDACTION_PYTHON_LIC')
samples_path = "./Resources/SampleFiles"
fonts_path = "./Resources/Fonts"
output_path = "./Output"
    
def get_output_directory_path():
    caller_frame = inspect.currentframe().f_back
    caller_file_path = caller_frame.f_globals.get("__file__")
    caller_file_name = os.path.basename(caller_file_path)
    output_directory = join(output_path, os.path.splitext(caller_file_name)[0])

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    return os.path.abspath(output_directory)
    
def prepare_output_directory(output_directory, source_file):
    source_file_copy = join(output_directory, os.path.basename(source_file))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    shutil.copy(source_file, source_file_copy)

    return source_file_copy
    
def prepare_directory(output_directory, nested_directory):
    new_directory = join(output_directory, nested_directory)

    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    return new_directory
