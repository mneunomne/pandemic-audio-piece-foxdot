# The Pandemic Archive of Voices - Sample Algorithms

Multiple sample codes on how to use [The Pandemic Archive of Voices](https://github.com/mneunomne/pandemic-archive-of-voices-DB) to create a live algorithmic sound piece using [Foxdot](https://foxdot.org/) and [SuperCollider](https://supercollider.github.io/).

# Getting Started

## Install FoxDot + SuperCollider

[FoxDot](https://foxdot.org/) is a live coding environment that runs on top of [SuperCollider](https://supercollider.github.io/), a powerfull sound synthesis engine.

Follow the [FoxDot installation guide](https://foxdot.org/installation/).

## Download The Pandemic Archive of Voices Database

**Download and extract the database (which includes audio and data files) in your prefered folder: [https://pandemic-archive-of-voices.herokuapp.com/db.zip](https://pandemic-archive-of-voices.herokuapp.com/db.zip)**

## Trying out first sample codes

After getting familiar with FoxDot live coding environment you can start trying out the audios samples in FoxDot!

**Sample code on how to set up the pandemic archive of voices requests on your foxdot ebnveiroment:**
```python
import json, urllib.request, urllib.urlencode
from random import *

# api url - either local or remote
api_url = 'http://pandemic-archive-of-voices.herokuapp.com/api'

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
```

**Sample for an ambient voice synth:**
```python
def bojana():
    _a = get_audio_from_speaker('bojana')
    p1 >> loop(_a['file'], dur=[_a['duration_seconds'], rest(8)], amp=[1, 0.8], room=linvar([1, 10], 20), mix=linvar([1, 5], 20), lpr=0.0075, lpf=linvar([120, 140, 110,180], 20), spin=[0, 1, 2], blur=linvar([0, 1.5]), hpf=linvar([100, 600], 30))
bojana()
```

**Sample for a "cleaner" voice:**
```python
def sc():
    _a4 = get_audio_from_speaker('s.')
    ~p4 >> loop(_a4['file'], dur=[_a4['duration_seconds'], rest(3)], amp=linvar([1.4, 0, 0.5]), delay=1, room=linvar([0.5, 1], 10), mix=linvar([7, 0], 20), spin=linvar([0, 2]), hpr=0.1, lpf=linvar([800, 1200], 50))
sc()
```

# Modulations on the Fly

Listen [Here](https://www.mixcloud.com/soundstudies/modulation-18-alberto-harres) to the full audio piece streamed in the podcast Modulations on the Fly.