# Goto definition plugin for React js

# Installation

### Vundle

Add the following line to your ~/.vimrc
```
Plugin 'Ivo-Donchev/goto-definition-plugin-for-react'
```

### Usage

Set you cursor on the imported and type:

```
:ReactGotoDef
```

You can also map this function call with:

```
noremap <leader>D :ReactGotoDef 
```

**NOTE**: Your vim needs to support python3+ scripting. You can check this with:

```
:python3 print('ReactJS')
```
