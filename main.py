#!/usr/bin/env python
# encoding: utf-8

import sys
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

def print_MenuHelp():
    print """
    l - list list songs
    L - list list names
    m - set mode
    l - next music
    s - start
    """

def menu(musicPlayer):
    """ 功能菜单
    列出播放列表
    添加播放列表
    设置播放次序
    """
    print 'setting...'
    getch  = Getch.Getch()
    while True:
        action = getch()
        print action
        if action == 'h':   # help
            print_MenuHelp()
        if action == 'l':   # list musicList songs
            print musicPlayer.musicBox.get_list()
        if action == 'L':
            print musicPlayer.musicBox.get_lists()
        if action == 'm':
            m = getch()
            musicPlayer.set_mode(m)
            print 'mode is set to %s' %(m)
        if action == 'l':
            pass
        if action == 'l':
            pass
        elif action == 'q':
            print 'quit setting'
            break

def get_input(musicPlayer):
    """ 处理输入 """
    getch  = Getch.Getch()
    while True:
        action = getch()
        print action
        if action == 'h':   # help
            print_help()
        elif action == 's': # play music
            musicPlayer.play()
        elif action == 'S':
            musicPlayer.stop()
        elif action == 'p': # pause music
            musicPlayer.pause()
            print 'music is pause'
        elif action == 'P':
            musicPlayer.unpause()
        elif action == 'i':
            musicPlayer.volume_up()
        elif action == 'k':
            musicPlayer.volume_down()
        elif action == 'j':
            musicPlayer.play_previous()
        elif action == 'l':
            musicPlayer.play_next()
        elif action == 'm':
            menu(musicPlayer)
        elif action == 'q':
            musicPlayer.stop()
            break

if __name__ == '__main__':

    mp = music.MusicPlayer()
    thread.start_new_thread(mp.start, ())
    thread.start_new_thread(get_input, (mp,))

    while 1:
        time.sleep(10)

