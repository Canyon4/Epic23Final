# import required module
from pydub import AudioSegment
from pydub.playback import play

# for playing mp3 file
def carhorn():
    # variable song is assigned to pathway of audio file
    song = AudioSegment.from_mp3("audio file pathway")
    play(song) # plays song
carhorn() # calls function
