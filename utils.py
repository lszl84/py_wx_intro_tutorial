def ensure_hdpi():
    import platform
    import ctypes

    if platform.system() == "Windows":
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
