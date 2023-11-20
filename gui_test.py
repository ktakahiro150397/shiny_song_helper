import pyautogui
from pyhooked import Hook, KeyboardEvent, MouseEvent


# 現在位置から上に指定pxだけフリックする(または相対値での指定が必要？)
# 設定値を受け入れる(GUI / iniのようなファイル)

# 指定位置をクリック
# pyautogui.click()

def handle_events(args):
    if isinstance(args, KeyboardEvent):
        print(args.key_code)
        if args.current_key == 'A' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print("Ctrl + A was pressed")
        elif args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            hk.stop()
            print('Quitting.')

    if isinstance(args, MouseEvent):
        print(f"Mouse is at ({args.mouse_x}, {args.mouse_y})")


hk = Hook()  # make a new instance of PyHooked
hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
hk.hook()  # hook into the events, and listen to the presses

