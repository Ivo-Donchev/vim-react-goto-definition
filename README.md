# Goto definition plugin for React js

# Overview

A python powered vim plugin for goto defintion functionality for functions/components/constants... handling *imports* and *exports* for `Javascript` and especially `React JS`.
The implementation is entirely written in Python 3 using regular expressions.

Covered import types:

 - relative imports (`import Something from '../components/Something'`) - will search for any of:
   - '../components/Something.jsx' or
   - '../components/Something.js' or
   - '../components/Something/index.js' or
   - '../components/Something/index.jsx'

 - absolute imports (`import Page1 from 'pages/Page1'`) - will search into **src/** folder for the import:
   - 'src/pages/Page1.jsx' or
   - 'src/pages/Page1.js' or
   - 'src/pages/Page1/index.js' or
   - 'src/pages/Page1/index.jsx'

 - default imports (`import A from './A'` or `import {default as A} from './A'`) and non-default imports (`import {a, b as c} from 'module')`)

Covered definition types:
  - `class <...>`
  - `function <...>`
  - `function* <...>`
  - `<...> = ` - for variables, constants and arrow functions

Searching algorythm works as follows:

  1. Soft scraping:
      - Search in current file
      - Search for import
      - Search for export from another file

  2. Hard scraping (if soft scraping fails :( ) - searches for wanted definition over the whole project


# Installation

### Vundle

Add the following line to your `~/.vimrc` :
```
Plugin 'Ivo-Donchev/vim-react-goto-definition'
```
and run:

```
:PluginInstall
```

# Usage

Set you cursor on the imported and type:

```
:ReactGotoDef
```

You can also map this function call with:

```
" To map to <leader>D:
noremap <leader>D :call ReactGotoDef()<CR>
```

**NOTE**: Your vim needs to support python3+ scripting. You can check this with:

```
:python3 print('ReactJS')
```
