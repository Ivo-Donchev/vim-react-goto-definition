import vim

from .utils import get_import_from_file_content

CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)
GENERATOR_FUNCTION_DECLARATION = lambda f_name: 'function* {} '.format(f_name)
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = '.format(f_name)

DECLARATIONS = (
    CLASS_DECLARATION,
    FUNCTION_DECLARATION,
    ARROW_FUNCTION_DECLARATION,
    GENERATOR_FUNCTION_DECLARATION,
)


def search_in_file(*, file, word):
    with open(file) as f:
        for idx, row in enumerate(f):
            for func in DECLARATIONS:
                match = func(word)

                if match in row:
                    vim.command(f'edit {file}|{idx+1}')
                    row.index(word)

                    return True

    return False


def get_import_from_file(import_name: str, filename: str) -> str:
    f = open(filename)
    content = f.read()
    f.close()

    return get_import_from_file_content(
        file_content=content,
        import_name=import_name
    )
