def get_screen_res():
    """
    Function that checks current screen resolution. Raises OSError if it can't recognise the OS.
    :return: [width, height] list with screen resolution.
    """
    import platform

    system = platform.system()
    if 'Darwin' in system:  # macOS
        from AppKit import NSScreen
        frame = NSScreen.mainScreen().frame()
        width = int(frame.size.width)
        height = int(frame.size.height)
    elif 'Windows' in system:
        from win32api import GetSystemMetrics
        width = int(GetSystemMetrics(0))
        height = int(GetSystemMetrics(1))
    else:  # can't recognise OS
        raise OSError("get_screen_res function can't recognise your OS")

    return [width, height]
