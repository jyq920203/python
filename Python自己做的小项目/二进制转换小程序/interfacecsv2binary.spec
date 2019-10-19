# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\jiangyq\\Desktop\\Cvs2Binary\\interfacecsv2binary.py'],
             pathex=['C:\\Users\\jiangyq\\Desktop\\Cvs2Binary\\ReadFromCsv.py', 'C:\\Users\\jiangyq\\Desktop\\Cvs2Binary\\loadfont.py', 'C:\\Users\\jiangyq\\Desktop\\Cvs2Binary','C:\\Users\\jiangyq\\Desktop\\Cvs2Binary\\SysCheck.py'],
             binaries=[],
             datas=[('A.ico','.'),('SC.otf','.')],
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
          name='interfacecsv2binary',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\jiangyq\\Desktop\\Cvs2Binary\\A.ico')
