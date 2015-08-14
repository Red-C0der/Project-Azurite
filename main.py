# coding=utf-8
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Name: Project-Azurite                                                       |
#  |   Version: 0.0.1                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0776                                                            |
#  |   GitHub-Page: http://red-c0der.github.io/Project-Azurite                     |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/




import logging
class System:
    class Logger:
        def write(self, level, message, logfile="latest.log"):
            logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
            if level == "i":
                logging.info(message)
            if level == "w":
                logging.warning(message)
            if level == "e":
                logging.error(message)
            if level == "c":
                logging.critical(message)
            if level == "ex":
                logging.exception(message)
            if level == "d":
                logging.debug(message)
            if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
                logging.exception("Logging level [" + level +  "] not recognized!")

System = System()
Logger = System.Logger()


class Input:
    pass




class Output:
    def Cout(text, fgc=500, bgc=500, attrc="", newline=True):
        if newline is True:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        print(fg(fgc) + text + style.RESET)
                    else:
                        print(fg(fgc) + attr(attrc) + text + style.RESET)
                else:
                    if attrc == "":
                        print(fg(fgc) + bg(bgc) + text + style.RESET)
                    else:
                        print(fg(fgc) + bg(bgc) + attr(attrc) + text + style.RESET)
            else:
                if bgc != 500:
                    if attrc == "":
                        print(bg(bgc) + text + style.RESET)
                    else:
                        print(bg(bgc) + attr(attrc) + text + style.RESET)
        else:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        sys.stdout.write(fg(fgc) + text + style.RESET)
                    else:
                        sys.stdout.write(fg(fgc) + attr(attrc) + text + style.RESET)
                else:
                    if attrc == "":
                        sys.stdout.write(fg(fgc) + bg(bgc) + text + style.RESET)
                    else:
                        sys.stdout.write(fg(fgc) + bg(bgc) + attr(attrc) + text + style.RESET)
            else:
                if bgc != 500:
                    if attrc == "":
                        sys.stdout.write(bg(bgc) + text + style.RESET)
                    else:
                        sys.stdout.write(bg(bgc) + attr(attrc) + text + style.RESET)

Output = Output()

Logger.write("i", "|==========================================|")
Logger.write("i", "|                                          |")
Logger.write("i", "|               New Execution              |")
Logger.write("i", "|                                          |")
Logger.write("i", "|==========================================|")

try:
    import colorama
    Logger.write("i", "Imported colorama")
except:
    Logger.write("e", "Could not import colorama!")
    print "ERROR: Could not import colorama!"
try:
    import mysql.connector
    Logger.write("i" ,"Imported mysql.connector")
except:
    Logger.write("e" ,"Could not import mysql.connector!")
    print "ERROR: Could not import mysql.connector!"

try:
    import pyprind
    Logger.write("i" ,"Imported pyprind")
except:
    Logger.write("e" ,"Could not import pyprind!")
    print "ERROR: Could not import pyprind!"

try:
    import progressbar
    Logger.write("i" ,"Imported progressbar")
except:
    Logger.write("e","Could not import progressbar!")
    print "ERROR: Could not import progressbar!"

try:
    import time
    Logger.write("i" ,"Imported time")
except:
    Logger.write("e" ,"Could not import time!")
    print "ERROR: Could not import time!"

try:
    import termcolor
    Logger.write("i" ,"Imported termcolor")
except:
    Logger.write("e" ,"Could not import termcolor!")
    print "ERROR: Could not import termcolor!"

try:
    import multiprocessing
    Logger.write("i" ,"Imported multiprocessing")
except:
    Logger.write("e" ,"Could not import multiprocessing!")
    print "ERROR: Could not import multiprocessing!"

try:
    from multiprocessing import Queue
    Logger.write("i" ,"Imported Queue from multiprocessing")
except:
    Logger.write("e" ,"Could not import Queue!")
    print "ERROR: Could not import Queue!"

try:
    from multiprocessing import Manager
    Logger.write("i" ,"Imported Manager from multiprocessing")
except:
    Logger.write("e" ,"Could not import Manager!")
    print "ERROR: Could not import Manager!"

try:
    from multiprocessing import Value
    Logger.write("i" ,"Imported Value from multiprocessing")
except:
    Logger.write("e" ,"Could not import Value!")
    print "ERROR: Could not import Value!"

try:
    import socket
    Logger.write("i" ,"Imported socket")
except:
    Logger.write("e" ,"Could not import socket!")
    print "ERROR: Could not import socket!"

try:
    import sys
    Logger.write("i" ,"Imported sys")
except:
    Logger.write("e" ,"Could not import sys!")
    print "ERROR: Could not import sys!"

try:
    import os
    Logger.write("i" ,"Imported os")
except:
    Logger.write("e" ,"Could not import os!")
    print "ERROR: Could not import os!"

try:
    import getpass
    Logger.write("i" ,"Imported getpass")
except:
    Logger.write("e" ,"Could not import getpass!")
    print "ERROR: Could not import getpass!"

try:
    import ConfigParser
    Logger.write("i" ,"Imported ConfigParser")
except:
    Logger.write("e" ,"Could not import ConfigParser!")
    print "ERROR: Could not import ConfigParser!"

try:
    import speech_recognition as sr
    Logger.write("i" ,"Imported speech_recognition as sr")
except:
    Logger.write("e" ,"Could not import speech_recognition as sr!")
    print "ERROR: Could not import speech_recognition as sr!"

try:
    import random
    Logger.write("i" ,"Imported random")
except:
    Logger.write("e" ,"Could not import random!")
    print "ERROR: Could not import random!"

try:
    import npyscreen
    Logger.write("i" ,"Imported npyscreen")
except:
    Logger.write("e" ,"Could not import npyscreen!")
    print "ERROR: Could not import npyscreen!"

try:
    from colored import fg, bg, attr, style
    Logger.write("i" ,"Imported fg, bg, attr, style from colored")
except:
    Logger.write("e" ,"Could not import fg, bg, attr, style from colored!")
    print "ERROR: Could not import fg, bg, attr, style from colored!"

try:
    from unicurses import *
    Logger.write("i" ,"Imported * from unicurses")
except:
    Logger.write("e" ,"Could not import * from unicurses!")
    print "ERROR: Could not import * from unicurses!"