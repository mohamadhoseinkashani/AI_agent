import os
from config import MAX_CHARS


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "reading file of the provided directory and save it inside a sting up to 10_000 character of the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to file from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}



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