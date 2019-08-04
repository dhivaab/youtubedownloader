from __future__ import unicode_literals
import youtube_dl

mp3_playlist_options = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestaudio/best', # choice of quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': '%(title)s.%(ext)s.',
        'noplaylist' : False,        # only download single song, not playlist
}
playlist ='https://www.youtube.com/playlist?list=PLloxhkoIi9rDjzSsVNW8QA23l7HvyczFz'
with youtube_dl.YoutubeDL(mp3_playlist_options) as ydl:
    ydl.download([playlist])

