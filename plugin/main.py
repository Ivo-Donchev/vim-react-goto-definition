import re
import vim
import glob


IMPORT_PATTERN = "import (?:[\"'\s]*([\w*{}\n, ]+) from \s*)?[\"'\s]*(([\.]+)?[@\w\/_-]+)[\"'\s]*;?"

def check_if_import_exists_in_current_file(import_name):
    current_filename = vim.current.buffer.name

    with open(current_filename) as current_file:
        content = current_file.read()
        imports = re.findall(IMPORT_PATTERN, content)

        return any(
            [
                any([import_name in _ for _ in imp])
                for imp in imports
            ]
        )


def react_goto_def(word):
    exists = check_if_import_exists_in_current_file(word)
    print(exists)

    # if not exists:
    #     snake.search(word)
    #     snake.keys('zt')
    #     return

    # for extension in ['js', 'jsx']:
    #     for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
    #         with open(file) as f:
    #             contents = f.read()

    #         for func in DECLARATIONS:
    #             match = func(word)

    #             if func(word) in contents:
    #                 snake.command(":e {}".format(file))
    #                 snake.search(match)
    #                 snake.keys('zt')
    #                 return
