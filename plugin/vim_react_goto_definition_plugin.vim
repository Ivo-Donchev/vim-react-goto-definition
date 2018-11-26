" -------------------
" Add to path
" -------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:p:h")'))

" -------------------
"  Functions
" -------------------

function! GetFilesWithDefinitions()
python3 << endOfPython
from src.main import goto_definition

current_word = vim.eval('expand("<cword>")')
current_filename = vim.current.buffer.name
goto_definition(
    word=current_word,
    filename=current_filename
)
endOfPython
endfunction

command! ReactGotoDef call GetFilesWithDefinitions()
