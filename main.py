#!/usr/bin/env python
# encoding: utf-8

import thread
import time
import Getch
import music


def print_help():
    print """
        i
    j   k   l
    i - volume up
    k - volume down
    j - previous music
    l - next music
    s - start
    S - stop
    p - pause music
    P - unpause music
    r - restart music
    q - quit
    """

def get_input(musicBox):
    getch  = Getch.Getch()
    while True:
        action = getch()
        print action
        if action == 'h':   # help
            print_help()
        elif action == 's': # play music
            musicBox.play()
        elif action == 'S':
            musicBox.stop()
        elif action == 'p': # pause music
            musicBox.pause()
            print 'music is pause'
        elif action == 'P':
            musicBox.unpause()
        elif action == 'i':
            musicBox.volume_up()
        elif action == 'k':
            musicBox.volume_down()
        elif action == 'j':
            musicBox.play_previous()
        elif action == 'l':
            musicBox.play_next()
        elif action == 'q':
            musicBox.stop()
            break
    thread.exit()

if __name__ == '__main__':

    m = music.MusicPlayer()
    thread.start_new_thread(m.start, ())
    thread.start_new_thread(get_input, (m,))

    while 1:
        time.sleep(9)

