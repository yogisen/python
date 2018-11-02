import datetime  # import global package

import sound.decoder_wav as wav  # alias import
from sound import decoder_mp3

supported_types = ('wav', 'mp3',)


class AudioFile:
    def from_wav(path):
        return AudioFile(path, 'wav')

    def from_mp3(path):
        return AudioFile(path, 'mp3')

    def __init__(self, path, file_type):
        self.path = path
        self.file_type = file_type
        print("Loading audio file on date:", datetime.date.today())

    def play(self):
        if self.file_type == 'wav':
            wav.decode(self.path)
        elif self.file_type == 'mp3':
            decoder_mp3.decode(self.path)
