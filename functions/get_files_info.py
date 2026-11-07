import os


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    absolute_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_working_directory, directory))
    list_of_descriptions: list[str] = []
    list_of_descriptions.append("Result for current directory:" if directory == "." else f"Result for '{directory}' directory:")



    if os.path.commonpath([absolute_working_directory, target_dir]) != absolute_working_directory:

        list_of_descriptions.append(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        

    elif not os.path.isdir(target_dir):
        list_of_descriptions.append(f'    Error: "{directory}" is not a directory')
        
    else:
        content_of_directory: list[str] = os.listdir(target_dir)
        content_description: str = ""


        for item in content_of_directory:
            absolute_path = target_dir + "/" + item
            content_description = f"  - {item}: file_size={os.path.getsize(absolute_path) } bytes, is_dir={os.path.isdir(absolute_path)}"
            list_of_descriptions.append(content_description)
    
    return "\n".join(list_of_descriptions)


