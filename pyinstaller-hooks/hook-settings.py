# pyinstaller-hooks/hook-settings.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_dynamic_libs
hiddenimports = collect_submodules('settings')
datas = collect_data_files('settings')
binaries = collect_dynamic_libs('settings')