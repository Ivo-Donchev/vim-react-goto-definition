import vim

from .utils import (
    get_source_paths,
    get_import_from_file_content,
    get_exports_from_file_content,
)
from .constants import MAX_LEVEL_OF_DEPTH

CLASS_DECLARATION = lambda class_name: 'class {} '.format(class_name)  # noqa
FUNCTION_DECLARATION = lambda f_name: 'function {} '.format(f_name)  # noqa
GENERATOR_FUNCTION_DECLARATION = lambda f_name: 'function* {} '.format(f_name)  # noqa
ARROW_FUNCTION_DECLARATION = lambda f_name: ' {} = '.format(f_name)  # noqa

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

        return get_import_from_file_content(file_content=content, import_name=import_name)
    except Exception:
        pass


def get_exports_from_file(filename):
    try:
        f = open(filename)
        content = f.read()
        f.close()

        return get_exports_from_file_content(file_content=content)
    except Exception:
        pass


def soft_scrape_from_file(wanted_definition: str, filename: str, current_level: int) -> str:
    """
    Steps of soft scraping:
      1) Prevent from endless recursion (current_level should be lower than MAX_LEVEL_OF_DEPTH)
      2) Check for `wanted_definition` in current file
      3) Check for `wanted_definition` import in current file
      4) If there's export **from** some files => repeat steps 1) and 2) for these files
    """
    if current_level > MAX_LEVEL_OF_DEPTH:
        return False

    found_in_current_file = search_in_file(file=filename, word=wanted_definition)

    if found_in_current_file:
        return found_in_current_file

    found_import = get_import_from_file(import_name=wanted_definition, filename=filename)

    if found_import:
        source_paths = get_source_paths(source=found_import['source'], filename=filename)

        for source_path in source_paths:
            result = soft_scrape_from_file(
                wanted_definition=wanted_definition,
                filename=source_path,
                current_level=current_level+1
            )

            if result:
                return result

    """
    NOTE: This implementation should work but it's a bit slower than needed.

    TODO: Scrape exports for `source` as in the import function
    (a.k.a. make it smarter ;))
    """
    found_exports = get_exports_from_file(filename=filename)

    if found_exports:
        for export in found_exports:
            source = export['source']
            source_paths = get_source_paths(source=source, filename=filename)

            for source_path in source_paths:
                result = soft_scrape_from_file(
                    wanted_definition=wanted_definition,
                    filename=source_path,
                    current_level=current_level+1
                )

                if result:
                    return result
