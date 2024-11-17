import win32clipboard


def clip_board_text():
    #win32clipboard.OpenClipboard()
    #win32clipboard.EmptyClipboard()
    #win32clipboard.SetClipboardText("testing")
    #win32clipboard.CloseClipboard()
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()#всегда текст в буфере обмена
    win32clipboard.CloseClipboard()
    return data


print(clip_board_text())