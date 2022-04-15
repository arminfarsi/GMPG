# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:42:32 2021

@author: Armin Farsi
"""

import os
from bs4 import BeautifulSoup
import shutil

input_load = str(input("""Please Enter Your Groove Playlists Address:
Example: C:\\Users\*user*\Music\Playlists
"""))
while not os.path.exists(input_load):
    input_load = str(input("""Input Loading Path Does Not Exist. Enter a Valid Address:
"""))

input_save = str(input("""Please Enter Where You Want Your Playlists Saved:
"""))
while not os.path.exists(input_save):
    input_save = str(input("""Input Saving Path Does Not Exist. Enter a Valid Address:
"""))

playlists = os.listdir(input_load)
playlists_names = []

for file in playlists:
    if file.endswith('.zpl'):
        playlists_names.append(file)

playlists_dictionary = {}
tracktitles_dictionary = {}

for playlist in playlists_names:
    name = playlist[:-4]
    playlists_dictionary[name] = []
    tracktitles_dictionary[name] = []
    with open(input_load + '\\' + playlist, encoding='utf-8') as musics:
        music_raw_list = BeautifulSoup(musics.read(), 'html.parser').find_all('media')
        for media in music_raw_list:
            music_source = str(media.get('src'))
            music_title = str(media.get('tracktitle'))
            if music_source not in playlists_dictionary[name]:
                playlists_dictionary[name].append(music_source)
                tracktitles_dictionary[name].append(music_title)
    print('')
    print('Playlists Found:')
    print('')
    print(name)
    print('')

answer = input("""Please specify Which Playlist You Want to Copy.
You Can Copy All Playlists By Typing: all
""")

while answer not in playlists_dictionary:
    if answer == 'all':
        for playlist in playlists_dictionary:
            copy_dest = f'{input_save}' + '\\' + f'{playlist}'
            os.mkdir(copy_dest)
            for music_index in range(len(playlists_dictionary[playlist])):
                copy_source = playlists_dictionary[playlist][music_index]
                shutil.copy2(copy_source, copy_dest)
        break
    else:
        answer = str(input('The Specified Playlist Does Not Exist. Enter a Valid Name: '))

if answer in playlists_dictionary:
    copy_dest = f'{input_save}' + '\\' + f'{answer}'
    os.mkdir(copy_dest)
    for music_index in range(len(playlists_dictionary[answer])):
        copy_source = playlists_dictionary[answer][music_index]
        shutil.copy2(copy_source, copy_dest)

