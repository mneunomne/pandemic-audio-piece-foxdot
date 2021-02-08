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

def get_audio_by_id(_id):
  with urllib.request.urlopen(server_url + '/audio_id/' + _id) as url:
    audio_data = json.loads(url.read())
    audio_data['file'] = assets_path + audio_data['file']
    audio_data['duration_seconds'] = Clock.seconds_to_beats(audio_data['duration_seconds']+0.8)
    return audio_data

def get_audio_by_text(_text):
  with urllib.request.urlopen(server_url + '/audio_text/' + _text) as url:
    audio_list = json.loads(url.read())
    audio_data = audio_list[randrange(len(audio_list))]
    audio_data['file'] = assets_path + audio_data['file']
    audio_data['duration_seconds'] = Clock.seconds_to_beats(audio_data['duration_seconds']+0.8)
    return audio_data

## AUDIO PIECE

_a = get_audio_from_speaker('bojana')
p1 >> loop(_a['file'], dur=[_a['duration_seconds'], rest(8)], amp=[1, 0.8], room=linvar([1, 10], 20), mix=linvar([1, 5], 20), lpr=0.0075, lpf=linvar([120, 140, 110,180], 20), spin=[0, 1, 2], blur=linvar([0, 1.5]), hpf=linvar([100, 600], 30))


def kzkz():
    _a2 = get_audio_from_speaker('kazuki')
    p2 >> loop(_a2['file'], dur=_a2['duration_seconds'], amp=var([0.35, 0, 0.1], [1]), delay=[1/2, 1], room=linvar([0.8, 0.2], 10), mix=linvar([0.4, 4, 0.2, 5]), lpr=linvar([0.2, 0.1]), lpf=linvar([320, 420, 200, 500, 800, 500], 1), spin=linvar([2, 0, 1],10), blur=0.7, formant=linvar([2, 0]))
kzkz()

def vitor():
    _a3 = get_audio_from_speaker('victor')
    ~p3 >> loop(_a3['file'], dur=[_a3['duration_seconds'], rest(12)], amp=[1.1, 0.1], delay=[1/2, 1.5], room=var([0.3, 0.7], 100), mix=linvar([0.4, 7], 200), lpr=linvar([0.1, 0.05]), spin=[0, 2, 0, 1])
vitor()

def sc():
    _a4 = get_audio_from_speaker('s.')
    p4 >> loop(_a4['file'], dur=[_a4['duration_seconds'], rest(3)], amp=linvar([1.4, 0, 0.5]), delay=1, room=linvar([0.5, 1], 10), mix=linvar([7, 0], 20), spin=linvar([0, 2]), hpr=0.1, lpf=linvar([800, 1200], 50))

def lucca():
    _a5 = get_audio_from_speaker('lucca')
    p5 >> loop(_a5['file'], dur=[_a5['duration_seconds'], rest(randrange(3, 12))], amp=[1], delay=0.1, room=linvar([0.2, 0.7], 25), mix=linvar([3, 0.1], 100), spin=linvar([1, 2, 1, 0]))

def bonas():
    _a6 = get_audio_from_speaker('bonasladybug')
    p6 >> loop(_a6['file'], dur=[_a6['duration_seconds'], rest(6)], amp=linvar([2, 0]), delay=[0.5, 1, 0.25], room=linvar([0.1, 0.5], 10), mix=linvar([0.5, 10], 10), spin=linvar([0, 2]), chop=0, hpf=0)
bonas()

def nilya():
    _a6 = get_audio_by_text('tiki')
    ~p6 >> loop(_a6['file'], dur=[_a6['duration_seconds'], rest(7)], amp=linvar([2, 0]), delay=[0.5, 1, 0.25], room=linvar([0.1, 0.7], 100), mix=linvar([0.2, 2], 31), spin=linvar([0, 2]),  chop=0)
nilya()

def pelin():
    _a7 = get_audio_from_speaker('pelin')
    ~p7 >> loop(_a7['file'], dur=[_a7['duration_seconds'], rest(10)], amp=linvar([2, 0]), delay=[0.5, 1, 0.25], room=linvar([0.1, 0.9], 100), lpf=linvar([2000, 200], 100), mix=linvar([0.2, 7], 31), spin=linvar([0, 1], 10), lpr=2, echotime=5, chop=[0], formant=linvar([1, 0]))
pelin()

def ayse():
    _a8 = get_audio_from_speaker('ayse')
    ~p8 >> loop(_a8['file'], dur=[_a8['duration_seconds'], rest(10)], amp=var([1.5, 1.7, 1], 100), delay=[0.5, 1, 0.25], room=linvar([0.1, 0.9]), mix=linvar([0.2, 5], 80), spin=linvar([0, 1], 10), blur=randrange(1, 3), pshift=linvar([-0.3,0.3, 0.5, -0.7]))
ayse()

def ruoxi():
    _a8 = get_audio_from_speaker('ruoxi')
    ~p8 >> loop(_a8['file'], dur=[_a8['duration_seconds']-0.3, rest(18)], amp=linvar([1.5, 2, 1], 20), delay=[1, 2, 0.25], room=linvar([0.1, 2.9], 100), mix=linvar([0, 20], 80), spin=linvar([0, 2], 10), chop=linvar([0,2,0,1,0],80), blur=1.5)
ruoxi()

def soumya():
    _a9 = get_audio_from_speaker('soumya')
    ~p9 >> loop(_a9['file'], dur=[_a9['duration_seconds'], rest(20)], room=sinvar([0.2, 0.8], 100), mix=linvar([0, 8],40), lpf=linvar([1000, 2000], 200), formant=linvar([0.1, 1], 200), amp=[1.2, 0], spin=[0, 1, 0])
soumya()

def hem():
    _b1 = get_audio_from_speaker('hem')
    ~p1 >> loop(_b1['file'], dur=[_b1['duration_seconds'], rest(15)], amp=1.3, delay=[0.5, 1, 0.25], room=linvar([0.1, 0.8], 100), mix=linvar([0.1, 1], 100), spin=linvar([0, 2]))
hem()

def alberto():
    _b2 = get_audio_from_speaker('alberto')
    ~p1 >> loop(_b2['file'], dur=[_b2['duration_seconds'], rest(13)], delay=[0.5, 1, 0.25], amp=1.3, room=linvar([0.1, 0.8], 100), mix=linvar([0.1, 3], 100), spin=linvar([0, 1]), chop=[0, 1, 0, 2])
alberto()

def antonio():
    _b3 = get_audio_from_speaker('ant')
    ~p2 >> loop(_b3['file'], dur=[_b3['duration_seconds'], rest(randrange(5, 20))], amp=1.0, room=linvar([0.1, 0.8], 100), mix=linvar([0.1, 3], 100), spin=linvar([0, 2]), lpf=linvar([800, 2000], 50), blur=linvar([0, 2]))
antonio()

def ivett():
    _b4 = get_audio_from_speaker('ivett')
    ~p3 >> loop(_b4['file'], dur=[_b4['duration_seconds'], rest(randrange(5, 10))], amp=linvar([1.0,1.2,0.7]), room=linvar([0.1, 1.8], 100), mix=linvar([0.1, 3], 100), spin=linvar([0, 2]), lpf=linvar([800, 2000], 50), blur=linvar([0, 1], 17))
ivett()

def josh(_p):
    t = 50
    v = get_audio_from_speaker('josh')
    ~_p >> loop(v['file'], dur=[v['duration_seconds'], rest(15)], amp=[0.7], room=sinvar([0.3, 1], t), mix=sinvar([0, 10], t), lpf=linvar([1500, 200],t),formant=[0.05,0], spin=sinvar([-0.3,0.3], t))
josh(p9)


def chihim(_p):
    t = 50
    v = get_audio_from_speaker('him')
    ~_p >> loop(v['file'], dur=[v['duration_seconds'], rest(14)], amp=linvar([1.1, 0.7]), delay=1, room=linvar([0.5, 1], 50), mix=linvar([7, 0], 20), spin=linvar([-0.2, 0.2]), hpr=0.1, lpf=linvar([800, 1200], 50))
chihim(p9)


def slava():
    _b2 = get_audio_from_speaker('slava')
    ~p1 >> loop(_b2['file'], dur=[_b2['duration_seconds'], rest(13)], delay=[0.5, 1, 0.25], amp=1.3, room=linvar([0.1, 0.8], 100), lpf=linvar([600, 1000], 100), mix=linvar([0.1, 3], 100), spin=linvar([0]), chop=[0, 1, 0, 2])
slava()

def hannah():
    _b2 = get_audio_from_speaker('anna')
    ~p1 >> loop(_b2['file'], dur=[_b2['duration_seconds'], rest(11)], delay=[0.5, 1, 0.25], amp=1.3, room=linvar([0.1, 1.8], 100), lpf=linvar([600, 1000], 100), mix=linvar([0.1, 3], 100), spin=linvar([0]), chop=[0, 1, 0, 2])
hannah()


_a = get_audio_from_speaker('marcela')
p1 >> loop(_a['file'], dur=[_a['duration_seconds'], rest(12)], amp=[1, 0.8], room=linvar([1, 5], 20), mix=linvar([1, 3], 20), lpr=1, lpf=linvar([800], 20), spin=[0], blur=linvar([0]), hpf=linvar([100, 600], 30))

Clock.every(15, lambda: hannah())

#########

start = Clock.now()

print(sinvar([0, 1], 100))

print('test', now - start)

def josh(_p):
    t = 120
    v = get_audio_from_speaker('josh')
    _p >> loop(v['file'], dur=[v['duration_seconds'], rest(8)], amp=[0.7], room=sinvar([0.3, 1], t), mix=sinvar([0, 10], t), lpf=linvar([1500, 200],t),formant=[0.05,0], spin=sinvar([0, 2], t))
    print(linvar([0, 100], t))
josh(p1)

def hannah(_p):
    t = 40
    v = get_audio_from_speaker('anna')
    _p >> loop(v['file'], dur=[v['duration_seconds'],  rest(5)], amp=[0.5], room=linvar([1, 0.1], t), spin=2, tremolo=0)
hannah(p2)
