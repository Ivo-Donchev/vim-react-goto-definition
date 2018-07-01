import snake

import os
import re
import glob
from .utils import check_if_import_exists_in_current_file


CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = '.format(f_name)

DECLARATIONS = (
    CLASS_DECLARATION,
    FUNCTION_DECLARATION,
    ARROW_FUNCTION_DECLARATION
)

@snake.key_map("<leader>D")
def react_goto_def():
    word = snake.get_word()

    exists = check_if_import_exists_in_current_file(word)

    if not exists:
        snake.search(word)
        snake.keys('zt')
        return

    for extension in ['js', 'jsx']:
        for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
            with open(file) as f:
                contents = f.read()

            for func in DECLARATIONS:
                match = func(word)

                if func(word) in contents:
                    snake.command(":e {}".format(file))
                    snake.search(match)
                    snake.keys('zt')
                    return
