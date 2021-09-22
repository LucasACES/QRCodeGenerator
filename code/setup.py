from cx_Freeze import setup, Executable

exe = Executable(
        script="gui.pyw",
        copyright="Copyright (C) 2021 LucasACES",
        base="Win32GUI",
        icon="icon/qricon.ico",
        shortcut_name="QRCode Generator",
        shortcut_dir="QRCodeGenerator",
    )
setup(
    name="QRCodeGenerator",
    version="0.0.1",
    description="",
    executables=[exe],
)
