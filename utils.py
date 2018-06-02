import snake
import re


IMPORT_PATTERN = "import (?:[\"'\s]*([\w*{}\n, ]+) from \s*)?[\"'\s]*(([\.]+)?[@\w\/_-]+)[\"'\s]*;?"


def check_if_import_exists_in_current_file(import_name):
    current_filename = snake.get_current_file()
    import_found = False

    with open(current_filename) as current_file:
        content = current_file.read()
        imports = re.findall(IMPORT_PATTERN, content)

        return any(
            [
                any([ import_name in _ for _ in imp])
                for imp in imports
            ]
        )
