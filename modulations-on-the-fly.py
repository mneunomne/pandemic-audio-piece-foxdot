# modulations-on-fly

import json, urllib.request
from random import *

server_url = 'http://127.0.0.1:3000'
assets_path =  '/Users/asharres/pandemic-archive-of-voices-DB/'

def get_audio_from_speaker(name):
  with urllib.request.urlopen(server_url + '/speaker/' + name) as url:
    audio_list = json.loads(url.read())
    audio_data = audio_list[randrange(len(audio_list))]
    audio_data['file'] = assets_path + audio_data['file']
    audio_data['duration_seconds'] = Clock.seconds_to_beats(audio_data['duration_seconds']+0.8)
    return audio_data
    

audio = get_audio_from_speaker('victor')

p4 >> loop(audio['file'], dur=audio['duration_seconds'], pshift=[0], room=sinvar([1], 100), mix=linvar([10], 50), lpf=linvar([180, 100, 120, 240, 220], 16), lpr=[0.001], amp=var([0.2, 0], 16))

audio2 = get_audio_from_speaker('s.')
p2 >> loop(audio2['file'], dur=audio2['duration_seconds'], room=[1], mix=[10], amp=var([0.7, 0, 0, 0], 8))

audio3 = get_audio_from_speaker('kazuki')
p3 >> loop(audio3['file'], dur=audio3['duration_seconds'], room=sinvar([0.2, 1], 1000), mix=linvar([0.3, 10], 50), amp=[0.5, 0, 0, 0], spin=0)

audio4 = get_audio_from_speaker('victor')
p5 >> loop(audio4['file'], dur=audio4['duration_seconds'], room=sinvar([10, 0.2], 1000), mix=linvar([10, 1], 50), amp=[0, 0, 0, 0, 0.5], spin=0)


p1 >> play('x', amp=0.1, lpf=[200, 120, 180, 220, 100], lpr=0, dur=5)

p2 >> play('x', amp=0.1, hpf=[120, 100, 200], hpr=0, dur=5, delay=2)

