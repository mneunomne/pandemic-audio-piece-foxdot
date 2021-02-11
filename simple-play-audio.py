import json, urllib.request, urllib.urlencode
from random import *

# api url - either local or remote
api_url = 'http://127.0.0.1:3000/api' # 'http://pandemic-archive-of-voices.herokuapp.com/api'

# path to the "db" folder downloaded from the api /db.zip
assets_path =  '/Users/asharres/downloads/'

# get list of all speakers in the archive
def get_speakers():
  with urllib.request.urlopen(api_url + '/speakers') as url:
    speaker_list = json.loads(url.read())
    return speaker_list

# get an audio object from speaker    
def get_audios_from_speaker(speaker_data):
    # TO DO, clean speaker name for URL request
    name  = urllib.urlencode(speaker_data['speaker'])
    with urllib.request.urlopen(api_url + '/speaker/' + name) as url:
        audio_list = json.loads(url.read())
        return audio_list

# store all speakers in array
speakers = get_speakers()

# get a random speaker
rand_speaker = speakers[randrange(len(speakers))]

speaker_audios = get_audios_from_speaker(rand_speaker)

speaker_rand_audio = speaker_audios[randrange(len(speaker_audios))]

def play_audio(audio_data):
    a = audio_data
    path = assets_path + a['file']
    dur = Clock.seconds_to_beats(a['duration_seconds']+0.2)
    p1 >> loop(path, dur=dur)
    
play_audio(speaker_rand_audio)
