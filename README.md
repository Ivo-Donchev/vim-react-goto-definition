# Vim plugin for goto definition in React JS


## Installation

1) Install [Snake](https://github.com/amoffat/snake) plugin
2) Clone this repo in `~/.vim/bundle/`
3) Create `~/.vimrc.py`
```
# ~/.vimrc.py

from snake.plugins import vim_react_goto_definition_plugin
```

## Usage

`<leader>D` in normal mode while cursor is on the `class/function` 

NOTE: It greps for functions/classes definitions with given pattern in `src/` directory in files with `.js` and `.jsx` extensions
