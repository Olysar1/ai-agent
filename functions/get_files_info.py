import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abspath = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abspath, directory))
    
        is_valid_target_dir = os.path.commonpath([abspath, target_dir]) == abspath
        is_valid_dir = os.path.isdir(directory)
    except Exception as e:
        return f'Error: {e}'

    if not is_valid_target_dir:
        return ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not is_valid_dir:
        return ValueError(f'Error: "{directory}" is not a directory')

    return f'Success: "{directory}" is within the working directory'
