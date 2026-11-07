import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "runs python program of given working directory with given argument using the subprocess library",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to file from, relative to the working directory (default is the working directory itself)",
                },
                "arg": {
                    "type": "optional array of string",
                    "description": "a list of argumentsthat is inserted to the subprocess.run method",
                },
            },
        },
    },   
}

def run_python_file(working_directory: str, file_path: str, arg: list[str]|None = None) -> str:

    absolute_working_dir: str = os.path.abspath(working_directory)
    absolute_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))

    if os.path.commonpath([absolute_working_dir, absolute_file_path]) != absolute_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    command: list[str] = ["python", absolute_file_path]
    if arg != None:
        command.extend(arg)
    try:
        processed: subprocess.CompletedProcess = subprocess.run(command, cwd=absolute_working_dir, capture_output=True, text=True, timeout=30)

        processed_result_list: list[str] = []

        if processed.returncode != 0:
            processed_result_list.append(f"Process exited with code {processed.returncode}")
        if not processed.stdout.strip() and not processed.stderr.strip():
            processed_result_list.append("No output produced")
        if processed.stdout.strip():
            Stdout = "STDOUT: " + processed.stdout
            processed_result_list.append(Stdout)
        if processed.stderr.strip():
            Stderr = "STDERR: " + processed.stderr
            processed_result_list.append(Stderr)

        return "\n".join(processed_result_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"
        
    
