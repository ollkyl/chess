# pyinstaller-hooks/hook-fonts.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_dynamic_libs
hiddenimports = collect_submodules('fonts')
datas = collect_data_files('fonts')
binaries = collect_dynamic_libs('fonts')