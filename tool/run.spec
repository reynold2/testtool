# -*- mode: python -*-

block_cipher = None


a = Analysis(['G:\\Python3\\layout\\tool\\Run.py', 'G:\\Python3\\layout\\tool\\MainWindow.py', 'G:\\Python3\\layout\\tool\\TableWidget.py', 'G:\\Python3\\layout\\tool\\DataIo.py'],
             pathex=['G:\\Python3\\layout\\tool'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Run',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
