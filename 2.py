def vernam_cipher(self, text, key):
    result = ""
    for i in range(len(text)):
        text_char = ord(text[i]) - ord('а')
        key_char = ord(key[i]) - ord('а')
        encrypted_char = (text_char + key_char) % 32
        result += chr(encrypted_char + ord('а'))
    return result


def is_valid_input(self, input_text):
    return all('а' <= char <= 'я' for char in input_text)


def show_error(self, title, message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()