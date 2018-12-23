" -------------------
" Add to path
" -------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:p:h")'))

" -------------------
"  Functions
" -------------------

function! ReactGotoDef()
python3 << endOfPython
from src.main import goto_definition

vim.command('set iskeyword+=_');
current_word = vim.eval('expand("<cword>")')
vim.command('set iskeyword-=_');

current_filename = vim.current.buffer.name
goto_definition(
    word=current_word,
    filename=current_filename
)
endOfPython
endfunction
