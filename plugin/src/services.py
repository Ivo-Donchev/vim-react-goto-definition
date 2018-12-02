import vim

from .utils import get_import_from_file_content, get_source_paths
from .constants import ROOT

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
    try:
        with open(file) as f:
            for idx, row in enumerate(f):
                for func in DECLARATIONS:
                    match = func(word)

                    if match in row:
                        vim.command(f'edit {file}|{idx+1}')
                        row.index(word)

                        return True
    except Exception:
        pass

    return False


def get_import_from_file(import_name: str, filename: str) -> str:
    try:
        f = open(filename)
        content = f.read()
        f.close()

        return get_import_from_file_content(
            file_content=content,
            import_name=import_name
        )
    except Exception:
        pass


def soft_scrape_from_file(wanted_definition: str, filename: str) -> str:
    found = get_import_from_file(
        import_name=wanted_definition,
        filename=filename
    )

    if found:
        source_paths = get_source_paths(
            source=found['source'],
            filename=filename
        )

        for source_path in source_paths:
            result = soft_scrape_from_file(
                wanted_definition=wanted_definition,
                filename=source_path
            )
            if result:
                return result

    return search_in_file(file=filename, word=wanted_definition)
