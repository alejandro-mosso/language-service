from googletrans import Translator


class TranslateService:

    translator = Translator()

    def __init__(self):
        return

    def translate(self, text, src, dest):
        t = self.translator.translate(text, src=src, dest=dest)
        return t.text
