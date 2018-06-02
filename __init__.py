import snake

import os
import glob


CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = ('.format(f_name)

DECLARATIONS = (
    CLASS_DECLARATION,
    FUNCTION_DECLARATION,
    ARROW_FUNCTION_DECLARATION
)

@snake.key_map("<leader>D")
def react_dummy_goto_def():
    word = snake.get_word()

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

