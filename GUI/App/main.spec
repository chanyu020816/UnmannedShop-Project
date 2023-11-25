# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'constant.py', 'ImageConvertResult.py', 'LoginPage.py', 'CreateAccountPage.py', 'AddFaceEncode.py', 'ObjectDetectionPage.py', 'FinishPurchasePage.py', 'DonePurchasePage.py'],
    pathex=['/Users/chenyuliu/Desktop/Unmanned Shop/GUI/App'],
    binaries=[],
    datas=[('EncodeFile.p', './'), ('best.pt', './')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
