import re
from .constants import IMPORT_REGEX


def normalize_import(import_str: str) -> list:
    imports_strings = [el.strip() for el in import_str.split(',')]
    internal = any('{' in el for el in import_str)

    result = []
    for el in imports_strings:
        el = ''.join([ch for ch in el if ch not in ['{', '}']]).strip()
        if ' as ' in el:
            imported_as, used_as = [name.strip() for name in el.split(' as ')]
        else:
            imported_as, used_as = el, el

        result.append({
            'imported_as': imported_as,
            'used_as': used_as,
            'default': not internal or imported_as == 'default'
        })

    return result


def get_imports_from_file_content(file_content: str) -> list:
    return [
        {
            'imports': normalize_import(imports),
            'source': source
        }
        for imports, source in re.findall(IMPORT_REGEX, file_content)
    ]


def get_import_from_file_content(file_content: str, import_name) -> str:
    imports = get_imports_from_file_content(file_content=file_content)
    wanted_import = [
        el for el in imports
        if any(
            el_import for el_import in el['imports']
            if el_import['used_as'] == import_name
        )
    ]

    if len(wanted_import) > 0:
        result = wanted_import[0]
        import_data = [
            el for el in result['imports']
            if el['used_as'] == import_name
        ][0]

        return {
            'name': import_data['imported_as'],
            'source': result['source'],
            'default': import_data['default']
        }
