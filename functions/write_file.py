import os

schema_Write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "write a given content to a given file that exist in a given working_directory (the content is being written at the end of the file it does not rewrite the file itself)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to file from, relative to the working directory and the content that has to be written to end of the file(the defult is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "the content that has to be written at the end of the file"
                },
            },
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    absolute_working_dir: str = os.path.abspath(working_directory)
    absolute_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))

    if os.path.commonpath([absolute_working_dir, absolute_file_path]) != absolute_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(absolute_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)
    try:
        with open(absolute_file_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: could not write the content at '{file_path}'"
