import snake

import os
import re
import glob


CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = ('.format(f_name)

DECLARATIONS = (
    CLASS_DECLARATION,
    FUNCTION_DECLARATION,
    ARROW_FUNCTION_DECLARATION
)

IMPORT_PATTERN = "import (?:[\"'\s]*([\w*{}\n, ]+) from \s*)?[\"'\s]*(([\.]+)?[@\w\/_-]+)[\"'\s]*;?"

@snake.key_map("<leader>D")
def react_dummy_goto_def():
    word = snake.get_word()

    current_filename = snake.get_current_file()
    with open(current_filename) as current_file:
        content = current_file.read()
        imports = re.findall(IMPORT_PATTERN, content)

        import_found = False
        for imp in imports:
            if any([word in imp_word for imp_word in imp]):
                import_found = True


        if not import_found:
            print('import not found :(')

    for file in glob.glob('src/**/*.js', recursive=True):
        with open(file) as f:
            contents = f.read()

        for func in DECLARATIONS:
            match = func(word)
            if func(word) in contents:
                snake.command(":e {}".format(file))
                snake.search(match)
                snake.keys('zt')
                return

