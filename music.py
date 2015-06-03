#!/usr/bin/env python
# encoding: utf-8

import pygame
import os.path
import random


class MusicList():
    """ Music List """
    def __init__(self, listName, musics):
        self.__listName = listName
        self.__musics = musics
        self.__pos = 0
        self.__order = 0
        self.__previous = 0

    def get_next(self):
        self.__pos = 0 if self.__pos == (len(self.__musics)-1) else self.__pos + 1
        return self.__musics[self.__pos]

    def get_previous(self):
        self.__previous = self.__pos
        self.__pos = len(self.__musics) - 1 if self.__pos == 0 else self.__pos - 1
        return self.__musics[self.__pos]

    def get_now(self):
        return self.__musics[self.__pos]

    def get_first(self):
        return self.__musics[0]

    def get_last(self):
        return self.__musics[-1]

    def get_random(self):
        self.__previous = self.__pos
        self.__pos = random.randint(0, len(self.__musics)-1)
        return self.__musics[self.__pos]

class MusicBox():
    """ 音乐播放列表 """

    def __init__(self):
        self.__pos = 0
        self.__listIndex = 0
        # [{name:[music1, music2,...],]
        self.musicLists = [MusicList('1', ['music/a.mp3', 'music/b.mp3',  'music/m.mp3'])]
        self.musicList = self.musicLists[self.__listIndex]

    def get_previous(self):
        return self.musicList.get_previous()

    def get_next(self):
        return self.musicList.get_next()

    def get_now(self):
        return self.musicList.get_now()

    def get_first(self):
        return self.musicList.get_first()

    def get_last(self):
        return self.musicList.get_last()

    def get_random(self):
        return self.musicList.get_random()

    def get_list(self):
        pass

    def get_lists(self):
        pass

class MusicPlayer():
    """ 播放音乐类 """

    def __init__(self):
        self.musicBox = MusicBox()
        self.__isPause = False
        self.__initMixer()
        self.__mode = '0'     # 0 顺序, 1 随机, 2 单曲循环, 3 单次播放

    def __initMixer(self):
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN = self.__getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

    def __getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def start(self):
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()
        pygame.mixer.music.load(self.musicBox.get_now())
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # print "Playing..."
            clock.tick(1000)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def volume_up(self):
        v = pygame.mixer.music.get_volume()
        v = 1 if v > 0.9 else v+0.1
        pygame.mixer.music.set_volume(v)

    def volume_down(self):
        v = pygame.mixer.music.get_volume()
        v = 0 if v < 0.1 else v-0.1
        pygame.mixer.music.set_volume(v)

    def play_next(self):
        if self.__mode == '0':
            pygame.mixer.music.load(self.musicBox.get_next())
        elif self.__mode == '1':
            pygame.mixer.music.load(self.musicBox.get_random())
        else:
            pygame.mixer.music.load(self.musicBox.get_now())
        pygame.mixer.music.play()

    def play_previous(self):
        pygame.mixer.music.load(self.musicBox.get_previous())
        pygame.mixer.music.play()

    def set_mode(self, mode):
        self.__mode = mode


if __name__ == '__main__':
    mb = MusicBox()
