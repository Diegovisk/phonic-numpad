from guizero import App, Text, TextBox, PushButton
from utils.play_key_sound import play_key_sound


def get_app_instance():
    def Keypad__1():
        play_key_sound('1')

    def Keypad__2():
        play_key_sound('2')

    def Keypad__3():
        play_key_sound('3')

    def Keypad__4():
        play_key_sound('4')

    def Keypad__5():
        play_key_sound('5')

    def Keypad__6():
        play_key_sound('6')

    def Keypad__7():
        play_key_sound('7')

    def Keypad__8():
        play_key_sound('8')

    def Keypad__9():
        play_key_sound('9')

    def Keypad__0():
        play_key_sound('0')

    def Keypad__star():
        play_key_sound('*')

    def Keypad__hash():
        play_key_sound('#')


    app = App(title="KeyPad", width=252, height=350, layout="grid")

    # submit = PushButton(app, fetch_response, text="Submit", grid=[410, 300])
    # Clear_app = PushButton(app, Clearapp, text="Clear", grid=[410, 325])
    Keypad_1 = PushButton(app, Keypad__1, text="1", grid=[0, 400])
    Keypad_1.width = 8
    Keypad_1.height = 4
    Keypad_2 = PushButton(app, Keypad__2, text="2", grid=[50, 400])
    Keypad_2.width = 8
    Keypad_2.height = 4
    Keypad_3 = PushButton(app, Keypad__3, text="3", grid=[100, 400])
    Keypad_3.width = 8
    Keypad_3.height = 4
    Keypad_4 = PushButton(app, Keypad__4, text="4", grid=[0, 450])
    Keypad_4.width = 8
    Keypad_4.height = 4
    Keypad_5 = PushButton(app, Keypad__5, text="5", grid=[50, 450])
    Keypad_5.width = 8
    Keypad_5.height = 4
    Keypad_6 = PushButton(app, Keypad__6, text="6", grid=[100, 450])
    Keypad_6.width = 8
    Keypad_6.height = 4
    Keypad_7 = PushButton(app, Keypad__7, text="7", grid=[0, 500])
    Keypad_7.width = 8
    Keypad_7.height = 4
    Keypad_8 = PushButton(app, Keypad__8, text="8", grid=[50, 500])
    Keypad_8.width = 8
    Keypad_8.height = 4
    Keypad_9 = PushButton(app, Keypad__9, text="9", grid=[100, 500])
    Keypad_9.width = 8
    Keypad_9.height = 4
    Keypad_0 = PushButton(app, Keypad__0, text="0", grid=[50, 550])
    Keypad_0.width = 8
    Keypad_0.height = 4
    Keypad_Star = PushButton(app, Keypad__star, text="*", grid=[0, 550])
    Keypad_Star.width = 8
    Keypad_Star.height = 4
    keypad_Hash = PushButton(app, Keypad__hash, text="#", grid=[100, 550])
    keypad_Hash.width = 8
    keypad_Hash.height = 4


    def keyPressEvent(event):
        try:
            play_key_sound(event.key)
        except:
            pass


    app.when_key_released = keyPressEvent

    return app
