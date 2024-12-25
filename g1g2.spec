# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['g1g2.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/*', 'assets'), ('assets2/*', 'assets2'), ('C:/Users/ilyap/AppData/Local/Programs/Python/Python312/Lib/site-packages/CTkColorPicker/*', 'CTkColorPicker')],
    hiddenimports=['CTkColorPicker'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='g1g2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
