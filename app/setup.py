from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pyautogui", "webbrowser", "pynput", "tkinter"],  # Dependências
}

setup(
    name="InstagramLikeRobot",
    version="1.0",
    description="Um projeto simples de automação de like para Instagram.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Win32GUI")]
)