import librosa

y, sr = librosa.load('input.mp4', sr=44100)
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4) # shifted by 4 half steps
librosa.output.write_wav('output.wav', y_shifted, sr)

import moviepy.editor as mp

audio = mp.AudioFileClip("output.wav")
video = mp.VideoFileClip("input.mp4").set_audio(audio)
video.write_videofile("output_final.mp4")

