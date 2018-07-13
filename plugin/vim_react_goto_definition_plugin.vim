" -------------------
" Add to path
" -------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

" -------------------
"  Functions
" -------------------

function! GetFilesWithDefinitions()
python3 << endOfPython
import re
import vim
import glob


IMPORT_PATTERN = "import (?:[\"'\s]*([\w*{}\n, ]+) from \s*)?[\"'\s]*(([\.]+)?[@\w\/_-]+)[\"'\s]*;?"

CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = '.format(f_name)

DECLARATIONS = (
    CLASS_DECLARATION,
    FUNCTION_DECLARATION,
    ARROW_FUNCTION_DECLARATION
)

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

    for extension in ['js', 'jsx']:
        for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
            with open(file) as f:
                for idx, row in enumerate(f):
                    for func in DECLARATIONS:
                        match = func(word)

                        if match in row:
                            vim.command(f'edit {file}|{idx+1}')
                            row.index(word)
                            return




current_word = vim.eval('expand("<cword>")')
current_filename = vim.current.buffer.name
react_goto_def(current_word)


endOfPython
endfunction

command! Example call GetFilesWithDefinitions()
