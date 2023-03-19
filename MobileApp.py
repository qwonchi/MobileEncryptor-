from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomnavigation.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView
from kivymd.uix.dialog import MDDialog
from Encryptor import decode_img, encode_img


class MobileApp(MDApp):
    def __init__(self):
        super().__init__()
        self.load_img_decbutton = None
        self.load_img_button = None
        self.decode_img_path_input = None
        self.encr_img_path_input = None
        self.encr_text_input = None
        self.decode_button = None
        self.dialog = None
        self.encode_button = None

    def build(self):

        self.theme_cls.theme_style = "Dark"  # main window color "Dark" "Light"
        self.theme_cls.primary_palette = "Green"  # text on main window color
        self.title = "Stegano Tool"  # application window title name
        self.dialog = MDDialog(
            buttons=[MDRectangleFlatButton(text='Ok', on_release=self.close_dialog)]
        )

        # Buttons initialization

        self.load_img_decbutton = Button(text="Загрузить изображение", on_release=self.load_img_button_callback)
        self.load_img_button = Button(text="Загрузить изображение", on_release=self.load_img_button_callback)
        self.encode_button = Button(text="Закодировать изображение", on_release=self.encode_button_callback)
        self.decode_button = Button(text="Раскодировать изображение", on_release=self.decode_button_callback)

        for button in [self.encode_button, self.decode_button, self.load_img_button, self.load_img_decbutton]:
            # Configure common elements
            button.height = 50
            button.size_hint_y = None
            button.background_color = get_color_from_hex("#336fde")
            button.color = get_color_from_hex("#b8c3d6")
            button.font_name = "Arial"
            button.font_size = 24
            button.padding_x = 100

        self.encr_text_input = TextInput(
            size_hint_y=None,
            width=30,
            multiline=False,
            text=""
        )

        self.encr_img_path_input = TextInput(
            text=r"C:\Users\Ник\Desktop\ENCODE % DECODE\boy.jpg"
        )

        self.decode_img_path_input = TextInput(
            text=r"C:\Users\Ник\Desktop\ENCODE % DECODE\boy_encrypted.jpg"
        )

        for input in [self.encr_img_path_input, self.decode_img_path_input]:
            input.size_hint_y = None
            input.width = 30
            input.multiline = False

        return MDBoxLayout(
            MDBottomNavigation(
                MDBottomNavigationItem(
                    MDBoxLayout(
                        MDLabel(
                            text="Введите текст который хотите закодировать:",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.encr_text_input,
                        MDLabel(
                            text="Выберите расположение изображения:",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.load_img_button,
                        self.encr_img_path_input,
                        self.encode_button,
                        orientation="vertical"
                    ),

                    text="Закодировать",
                    name="EncodeScreen",
                    icon="plus"
                ),
                MDBottomNavigationItem(
                    MDBoxLayout(
                        MDLabel(
                            text="Enter image path to decode",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.decode_img_path_input,
                        self.load_img_decbutton,
                        self.decode_button,
                        orientation="vertical"
                    ),

                    text="Раскодировать",
                    name="DecodeScreen",
                    icon="minus"
                )
            ),
            orientation='vertical',
        )

    def encode_button_callback(self, button):
        """Listener for Encode button"""
        destination: str = self.encr_img_path_input.text
        destination = destination[:destination.rfind('.')] + '_encrypted.png'
        err = encode_img(self.encr_img_path_input.text, destination, self.encr_text_input.text)
        self.dialog.text = f"Successfully encrypted: saved in {destination}"
        if err:
            self.dialog.text = "Error! Check image path!"
        self.dialog.open()

    def decode_button_callback(self, button):
        """Listener for Decode button"""
        message = decode_img(self.decode_img_path_input.text)
        if not message:
            self.dialog.text = "Nothing to decode!"
        else:
            self.dialog.text = f"Message Decoded:\n{message}"
        self.dialog.open()

    def load_img_button_callback(self, button):
        ### получаешь изображение с андроид системы ###
        ###...
        ###

        img_path = r"C:\Users\Ник\Desktop\ENCODE % DECODE\boy2.jpg"
        self.encr_img_path_input.text = img_path
        self.dialog.text = "Path successfully changed!"
        self.dialog.open()

    def close_dialog(self, button):
        """This method close dialogue window"""
        self.dialog.dismiss()


if __name__ == '__main__':
    MobileApp().run()
