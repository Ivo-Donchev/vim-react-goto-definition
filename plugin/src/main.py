import glob

from .utils import search_in_file


def search_in_current_file(*, word, filename):
    return search_in_file(word=word, file=filename)


def hard_scraping(*, word, filename):
    for extension in ['js', 'jsx']:
        for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
            result = search_in_file(file=file, word=word)

            if result:
                return


def soft_scraping(*, word, filename):
    # in_current_file = search_in_file(word=word, file=filename)

    # if in_current_file:
    #     return
    pass


def goto_definition(*, word, filename):
    found = search_in_current_file(word=word, filename=filename)
    if found:
        return

    found = hard_scraping(word=word, filename=filename)
    if found:
        return
