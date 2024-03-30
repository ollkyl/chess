# pyinstaller-hooks/hook-images.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_dynamic_libs
hiddenimports = collect_submodules('images')
datas = collect_data_files('images')
binaries = collect_dynamic_libs('images')