import glob

from .services import search_in_file, soft_scrape_from_file


def search_in_current_file(*, word, filename):
    return search_in_file(word=word, file=filename)


def hard_scraping(*, word, filename):
    for extension in ['js', 'jsx']:
        for file in glob.glob('src/**/*.{}'.format(extension), recursive=True):
            result = search_in_file(file=file, word=word)

            if result:
                return


def soft_scraping(*, word, filename):
    return soft_scrape_from_file(wanted_definition=word, filename=filename)


def goto_definition(*, word, filename):
    for search_func in [soft_scraping, hard_scraping]:
        found = search_func(word=word, filename=filename)
        if found:
            return
