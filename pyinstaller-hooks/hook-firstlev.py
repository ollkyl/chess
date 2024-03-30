# pyinstaller-hooks/hook-firstlev.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_dynamic_libs
hiddenimports = collect_submodules('firstlev')
datas = collect_data_files('firstlev')
binaries = collect_dynamic_libs('firstlev')