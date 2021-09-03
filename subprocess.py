def run(command):
    # Prevent cmd.exe window from popping up
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= (
        subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
    )
    startupinfo.wShowWindow = subprocess.SW_HIDE

    std = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo
    )
    out, err = std.communicate()
    return out.decode("utf-8").replace("\r", ""), err
