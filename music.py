#!/usr/bin/env python
# encoding: utf-8

import time

import pygame

class MusicBox():

    def __init__(self, musics):
        self.__musics = musics
        self.pos = 0

    def get_next(self):
        self.pos = 0 if self.pos == (len(self.__musics)-1) else self.pos + 1
        return self.__musics[self.pos]

    def get_previous(self):
        self.pos = len(self.__musics) - 1 if self.pos == 0 else self.pos - 1
        return self.__musics[self.pos]

    def get_now(self):
        return self.__musics[self.pos]

    def get_first(self):
        return self.__musics[0]

    def get_last(self):
        return self.__musics[-1]

class MusicPlayer():

    def __init__(self):
        self.__musicBox = MusicBox(['a.mp3', 'b.mp3', 'c.mp3', 'm.mp3'])
        self.__isPause = False
        self.__initMixer()

    def __initMixer(self):
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN = self.__getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

    def __getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def start(self):
        """Stream music with mixer.music module in blocking manner.
        This will stream the sound from disk while playing.
        """
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()
        pygame.mixer.music.load(self.__musicBox.get_now())
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
        pygame.mixer.music.load(self.__musicBox.get_next())
        pygame.mixer.music.play()

    def play_previous(self):
        pygame.mixer.music.load(self.__musicBox.get_previous())
        pygame.mixer.music.play()


if __name__ == '__main__':

    m = MusicPlayer()
    m.start()
    m.play()
    m.play_next()
    time.sleep(5)
    m.previous()


