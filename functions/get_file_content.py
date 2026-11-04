import os
from config import MAX_CHARS



def get_file_content(working_directory: str, file_path: str) -> str :

    absolute_working_dir: str = os.path.abspath(working_directory)
    absolute_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))

    if absolute_working_dir != os.path.commonpath([absolute_file_path, absolute_working_dir]):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    #content_of_dir: list[str] = os.listdir(absolute_working_dir)

    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    
    try:
        with open(absolute_file_path, "r") as f:
            content_of_file = f.read(MAX_CHARS)
        
            if f.read(1):
                content_of_file += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except OSError as e:
        return f'Error: An error occurred while reading "{file_path}": {e}'

    return content_of_file  