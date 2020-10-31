"Для удаления плагина сначала выведите список установленных плагинов :PluginList. Затем установите курсор на том плагине, который хотите удалите и нажмите сочетание клавиш Shift + D . Также удалите запись об этом плагине в файле ~/. vimrc


set nocompatible              " be iMproved, required
filetype off                  " required

"=====================================================
" Vundle settings
"=====================================================
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'		" let Vundle manage Vundle, required

Plugin 'tomasr/molokai'         "Тема в стиле Sublime Text
Plugin 'matze/vim-move'         "Быстрое перемещение строк вверх / вниз
Plugin 'tomtom/tcomment_vim'         "Плагин tComment. Удобное комментирование кода
Plugin 'vim-syntastic/syntastic'         "проверка синтаксиса
Plugin 'romainl/flattened'  "Tema
Plugin 'tell-k/vim-autopep8'  "Авто исправление синтаксиса
"---------=== Code/project navigation ===-------------
Plugin 'scrooloose/nerdtree' 	    	" Project and file navigation
"Plugin 'majutsushi/tagbar'          	" Class/module browser

"------------------=== Other ===----------------------
"Plugin 'bling/vim-airline'   	    	" Lean & mean status/tabline for vim
"Plugin 'fisadev/FixedTaskList.vim'  	" Pending tasks list
Plugin 'rosenfeld/conque-term'      	" Consoles as buffers
"Plugin 'tpope/vim-surround'	   	" Parentheses, brackets, quotes, XML tags, and more

"--------------=== Snippets support ===---------------
"Plugin 'garbas/vim-snipmate'		" Snippets manager
"Plugin 'MarcWeber/vim-addon-mw-utils'	" dependencies #1
"Plugin 'tomtom/tlib_vim'		" dependencies #2
"Plugin 'honza/vim-snippets'		" snippets repo

"---------------=== Languages support ===-------------
" --- Python ---
Plugin 'klen/python-mode'	        " Python mode (docs, refactor, lints, highlighting, run and ipdb and more)
Plugin 'davidhalter/jedi-vim' 		" Jedi-vim autocomplete plugin
"Plugin 'mitsuhiko/vim-jinja'		" Jinja support for vim
"Plugin 'mitsuhiko/vim-python-combined'  " Combined Python 2/3 for Vim

call vundle#end()            		" required
filetype on
filetype plugin on
filetype plugin indent on


syntax enable
set number
set ts=4
set autoindent
set expandtab
set shiftwidth=4
set cursorline
set showmatch
let python_highlight_all=1

"let g:rehash256 = 1
"let g:molokai_original=1

"set background=light
"color solarized
"colorscheme blue

set lines=50 columns=88 "125
set visualbell t_vb=
set novisualbell
"set enc=utf-8
set ls=2
set hlsearch
set nu
set guioptions+=m
set guioptions+=T
map <F2> :w<CR>
map <F3> :so %<CR>
map <F10> :q<CR>

" NerdTree настройки ===Plugin===
" показать NERDTree на F3
map <F4> :NERDTreeToggle<CR>
"игноррируемые файлы с расширениями
let NERDTreeIgnore=['\~$', '\.pyc$', '\.pyo$', '\.class$', 'pip-log\.txt$', '\.o$']


""""
" Python mode
"
"    Bundle 'klen/python-mode'
    " Python-mode
    " Activate rope
    " Keys:
    " K             Show python docs
    " <Ctrl-Space>  Rope autocomplete
    " <Ctrl-c>g     Rope goto definition
    " <Ctrl-c>d     Rope show documentation
    " <Ctrl-c>f     Rope find occurrences
    " <Leader>b     Set, unset breakpoint (g:pymode_breakpoint enabled)
    " [[            Jump on previous class or function (normal, visual, operator modes)
    " ]]            Jump on next class or function (normal, visual, operator modes)
    " [M            Jump on previous class or method (normal, visual, operator modes)
    " ]M            Jump on next class or method (normal, visual, operator modes)

" отключаем автокомплит по коду (у нас вместо него используется jedi-vim)
let g:pymode_rope = 1
let g:pymode_rope_completion = 1
let g:pymode_rope_complete_on_dot = 1    

" документация
let g:pymode_doc = 1
let g:pymode_doc_key = 'K'
" Documentation
"let g:pymode_doc = 1
"let g:pymode_doc_key = '<F1>'

" проверка кода
let g:pymode_lint = 1
let g:pymode_lint_checker = "pyflakes,pep8"
let g:pymode_lint_ignore="E501,W601,C0110"
" провека кода после сохранения
let g:pymode_lint_write = 1
let g:pymode_lint_on_fly = 1

    " Support virtualenv
let g:pymode_virtualenv = 1

" Enable breakpoints plugin
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_key = '<leader>b'

" syntax highlighting
let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all

    " Don't autofold code
let g:pymode_folding = 0

    " replace pdb to ipdb
iab ipdb import ipdb; ipdb.set_trace()
    " возможность запускать код
let g:pymode_run = 0
let g:pymode_python = 'python3'

"=====================================================
" User hotkeys
"=====================================================
" ConqueTerm
" запуск интерпретатора на F5
nnoremap <F5> :ConqueTermSplit ipython<CR>
"nnoremap <F5> :!python %<CR>
" а debug-mode на <F6>
nnoremap <F6> :exe "ConqueTermSplit ipython " . expand("%")<CR>
"nnoremap <F6>
let g:ConqueTerm_StartMessages = 0
let g:ConqueTerm_CloseOnEnd = 0
let g:ConqueTerm_PyVersion = 3

let mapleader=","

" проверка кода в соответствии с PEP8 через <leader>8
"autocmd FileType python map <buffer> <leader>8 :PymodeLint<CR>
autocmd FileType python map <buffer> <F8> :call Autopep8()<CR>

" автокомплит через <Ctrl+Space>
inoremap <C-space> <C-x><C-o>


" syntastic opts
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
