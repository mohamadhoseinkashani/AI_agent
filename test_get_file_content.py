from functions.get_file_content import get_file_content

# result = get_file_content("calculator", "lorem.txt")
# print(f"lorem.txt length: {len(result)}")
# print(f"lorem.txt truncated: {'truncated' in result}")

# print(get_file_content("calculator", "lorem.txt"))
# print(get_file_content("calculator", "lorem.txt"))
# print(get_file_content("calculator", "lorem.txt"))
# print(get_file_content("calculator", "lorem.txt"))



def summery_result(working_dir, file):
    result = get_file_content(working_dir, file)
    if "Error" not in result:
        print(f"{file} length: {len(result)}")
        print(f"{file} truncated: {'truncated' in result}") 
    else:
        print(result)


if "__main__" == __name__:
    summery_result("calculator", "lorem.txt")
    summery_result("calculator", "main.py")
    summery_result("calculator", "pkg/calculator.py")
    summery_result("calculator", "/bin/cat")
    summery_result("calculator", "pkg/does_not_exist.py")