# choir on the archive of voices 

# SETUP --------------------------------------------------------------------#

import json
from random import *

a = {}
b = {}

def get_audio_from_speaker(name):
  audios_from_speaker = []
  for i in data:
    if i['from'] == name:
      audios_from_speaker.append(i)
  audio = audios_from_speaker[randrange(len(audios_from_speaker))]
  return audio['file']

def get_random_audio():
    audio =data[randrange(len(data))]
    return audio['file']

with open('/Users/asharres/pandemic-audio-piece-foxdot/data.json') as f:
  data = json.load(f)

def set_a():
  a['amp'] = 1
  a['echo'] = 0
  a['echotime']= 0
  a['room'] = 0
  a['hpf']= 0
  a['lpf']= 0
  a['dur']= 5
  a['pan'] = -0.5

def set_b():
  b['amp'] = 1
  b['echo'] = 0
  b['echotime']= 0
  b['room'] = 0
  b['hpf']= 0
  b['lpf']= 0
  b['dur']= 10
  b['pan'] = 0.5

def play_a():
  l1 >> loop(a['audio'], dur=a['dur'], room=a['room'], echo=a['echo'], echotime=a['echotime'], hpf=a['hpf'], lpf=a['lpf'], amp=a['amp'], pan=a['pan'])

def stop_a():
  l1.stop()

def play_b():
  l2 >> loop(b['audio'], delay=b['dur']/2, dur=b['dur'], room=b['room'], mix=1, echo=b['echo'], echotime=b['echotime'], hpf=b['hpf'], lpf=b['lpf'],amp=b['amp'], pan=b['pan'])

def stop_b():
  l2.stop()

# END SETUP -------------------------------------------------------------------#

# voice a
set_a()

a['audio'] = get_audio_from_speaker('Sangbong Lee')
play_a()

a['amp'] = [1.2, 1.5]
a['dur'] = 5
a['lpf'] = 1500
a['room'] = 0.2
play_a()

# voice b
set_b()

b['audio'] = get_audio_from_speaker('S. C.')
play_b()

b['dur'] = 10
b['echo'] = var([1, 0.1, 2], 1)
b['room'] = linvar([0.1, 1], 8)
b['echotime'] = 10
play_b()

# exp

b['audio'] = get_random_audio()


# refs of good effects
# swell=linvar([10, 0], 100)

# exp 19.01.2021 14:30 

l3 >> loop(get_random_audio(), dur=5, lpf=linvar([2000, 200], 5), hpf=linvar([2000, 200], 10), room=10, mix=10, chop=linvar([12, 0, 1, 2, 0], 4), spin=linvar([1, -1], 8))

l6 >> loop(b['audio'], dur=5, formant=linvar([0, 2], 100), swell=linvar([5, 0], 200), room=linvar([1, 0], 50), mix=linvar([0, 1], 70), spin=linvar([0.5, -0.5], 8), chop=linvar([12, 0, 1, 2, 0], 4))

l3 >> loop(get_random_audio(), dur=6, spin=linvar([1, -1], 8), pshift=[-0.9, 0.35, 0.5, -0.4], lpf=linvar([2000, 100], 6), room=sinvar([1,0.1], 8), mix=linvar([0.3, 1],4), chop=[2, 1, 0])

l4 >> loop(get_random_audio(), dur=3, spin=linvar([1, -1], 8), pshift=[-0.9, 0.35, 0.5, -0.4], lpf=linvar([2000, 100], 100), room=sinvar([1,0.1], 100), mix=linvar([0.3, 1],4), chop=linvar([0, 10, 0], 20))

l5 >> loop(get_random_audio(), dur=6, spin=linvar([-1, 1], 8), pshift=linvar([-0.9, 0.35, 0.5, -0.4], 4), lpf=0, room=sinvar([1,0.1], 10), mix=linvar([0.3, 1],40), chop=0)

l7 >> loop(get_random_audio(), dur=8, spin=linvar([1, -1], 80), pshift=[-0.9, 0.35, 0.5, -0.4], lpf=linvar([0, 1000], 100), room=sinvar([1,0.1], 80), mix=linvar([0.3, 1],4), chop=[0,10])


# exp 2 19.01.2021 16:14

_a = get_random_audio()

_b = get_random_audio()

_c = get_random_audio()

_d = get_random_audio()

p1 >> loop(_a, dur=4, pshift=[-0.9, 0.35, 0.5, -0.4], room=sinvar([0.2, 1], 100), mix=linvar([0.3, 10], 50), lpf=linvar([2000, 100], 1000), amp=[0.4, 0, 0], spin=1, sus=4, blur=[2, 1, 0])

p2 >> loop(_b, dur=5, room=sinvar([0.2, 1], 100), amp=[0, 1, 0], mix=linvar([0, 10], 50), chop=[0, 5, 3, 10], spin=1)

p3 >> loop(_c, dur=5, chop=[2, 0, 1, 3], lpf=linvar([2000, 100], 6), mix=linvar([0.3, 1],4), room=sinvar([0.2, 1], 10), amp=0.7)

p4 >> loop(_d, dur=5, room=sinvar([0.2, 1], 100), mix=linvar([0.3, 0.6],40), lpf=linvar([0, 1000], 100), formant=linvar([0.1, 0.3], 10))


# exp 3 19.01.2021 17:51

def play_a(v):
    _a = get_random_audio()
    v >> loop(_a, dur=5, pshift=P[-0.9, 0.35, 0.5, -0.4].shuffle(), room=sinvar([0.2, 1], 100), mix=linvar([0.3, 10], 50), lpf=linvar([2000, 100], 1000), amp=[1, 0, 0])

def play_b(v):
    _b = get_random_audio()
    v >> loop(_b, dur=5, room=sinvar([0.2, 1], 100), amp=[0, 1, 0], mix=linvar([0, 10], 50), chop=[0, 5, 3, 10], spin=[1, 2])

def play_c(v):
    _c = get_random_audio()
    v >> loop(_c, dur=5, chop=[2, 0, 1, 3], lpf=linvar([2000, 100], 6), mix=linvar([0.3, 5],4), room=sinvar([0.2, 1], 10), amp=1)
    
def play_d(v):
    _d = get_random_audio()
    v >> loop(_d, dur=5, room=sinvar([0.2, 1], 100), mix=linvar([0.3, 5],40), lpf=linvar([0, 1000], 100), formant=linvar([0.1, 0.7], 10))

Clock.every(300, lambda: play_a(l2))
Clock.every(100, lambda: play_b(l3))
Clock.every(600, lambda: play_c(l4))
Clock.every(1000, lambda: play_d(l5))

Clock.every(30, lambda: play_a(l1))
Clock.every(40, lambda: play_b(l6))
Clock.every(60, lambda: play_c(l7))

Clock.every(5, lambda: play_d(l8))

Clock.every(5, lambda: play_a(l9))

play_a(l2)
play_b(l3)
play_c(l4)
play_d(l5)

Clock.clear()
