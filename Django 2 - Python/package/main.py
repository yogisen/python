from sound import audio

# display of variable from the audio module
print("Supported codecs:", audio.supported_types)

af = audio.AudioFile.from_mp3("test.mp3")
af.play()
