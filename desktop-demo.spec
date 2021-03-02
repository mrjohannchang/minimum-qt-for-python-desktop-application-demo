# -*- mode: python ; coding: utf-8 -*-

import os


block_cipher = None


a = Analysis([os.path.join('.venv', 'Scripts', 'desktop-demo')],
             pathex=[os.path.abspath(SPECPATH)],
             binaries=[],
             datas=[
                 (os.path.join('packages', 'desktop_demo', 'ui', 'main_window.ui'), os.path.join('desktop_demo', 'ui')),
                 (os.path.join('.venv', 'Lib', 'site-packages', 'PySide6', 'plugins'), os.path.join('PySide6', 'plugins'))],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='desktop-demo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
