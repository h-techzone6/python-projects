import moviepy.editor

video = moviepy.editor.VideoClip("YOUR FILE PATH HERE")

audio=video.audio

audio.write_audiofile("YOUR FILE PATH HERE")