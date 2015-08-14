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
        def write(self, level, message, LogFile=""):
            if LogFile == "":
                from time import gmtime, strftime
                LogName = strftime("%d-%m-%Y %H:%M", gmtime())
                LogLoc = "../Logs/"
                LogFile = LogLoc+LogName+".log"
            else:
                pass
            logging.basicConfig(filename=LogFile, level=logging.DEBUG, format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
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
    class Settings:
        def getsetting(self, identifier, sfile=""):
            Logger.write("i", "Try getting setting: ["+str(identifier)+"]")
            if sfile == "":
                Logger.write("i", "Opening settings.acf File")
                try:
                    sfile = open("settings.acf", "r")
                except:
                    Logger.write("e", "Could not open settings.acf File")
                    return False
                Logger.write("i", "Scanning File for identifier: ["+str(identifier)+"]")
                for line in sfile:
                    bypass = False
                    if "#" in line:
                        bypass = True
                    if bypass is False:
                        value = line.split(": ")
                        if value[0] == identifier:
                            value = value[1]
                            Logger.write("i", "Found identifier!")
                            return value
                            break
            else:
                Logger.write("i", "Opening "+sfile)
                try:
                    sfile = open(sfile, "r")
                except:
                    Logger.write("i", "Could not open "+sfile+" File")
                    return False
                Logger.write("i", "Scanning File for identifier: ["+str(identifier)+"]")
                for line in sfile:
                    bypass = False
                    if "#" in line:
                        bypass = True
                    if bypass is False:
                        value = line.split(": ")
                        if value[0] == identifier:
                            value = value[1]
                            Logger.write("i", "Found identifier!")
                            return value
                            break
        def setsetting(self, identifier, value, sfile=""):
            if sfile == "":
                Logger.write("i", "Try opening settings.acf")
                try:
                    sfileo = open("settings.acf", "r")
                except:
                    Logger.write("e", "Could not open settings.acf")
                    return False
                Logger.write("i", "Try reading settings.acf")
                try:
                    oldfiledata = sfileo.read()
                except:
                    Logger.write("e", "Could not read settings.acf")
                    return False
                if not identifier in oldfiledata:
                    Logger.write("e", "Identifier ["+identifier+"] is not in settings.acf!")
                    return False
                else:
                    ival = Settings.getsetting(identifier, sfile)
                    line = identifier + ": " + ival
                    Logger.write("d", "line = " + str(line))
                    Logger.write("i", "Try replacing line in oldfiledata")
                    try:
                        newfiledata = oldfiledata.replace(line, identifier+": "+value)
                    except:
                        Logger.write("e", "Could not replace line in oldfiledata!")
                        return False
                    Logger.write("i", "Try overwriting settingsfile")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove("settings.acf")
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open("settings.acf", "w")
                        except:
                            Logger.write("e", "Could not create new settings.acf File!")
                            return False
                        try:
                            nsfo.write(newfiledata)
                        except:
                            Logger.write("e", "Could not write newfiledata to settingsfile!")
                            return False
                        return True
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
            else:
                Logger.write("i", "Try opening "+sfile)
                try:
                    sfile = open(sfile, "r")
                except:
                    Logger.write("e", "Could not open "+sfile)
                    return False
                Logger.write("i", "Try reading settings.acf")
                try:
                    oldfiledata = sfile.reado()
                except:
                    Logger.write("e", "Could not read settings.acf")
                    return False
                if not identifier in oldfiledata:
                    Logger.write("e", "Identifier ["+identifier+"] is not in settings.acf!")
                    return False
                else:
                    ival = Settings.getsetting(identifier, sfile)
                    line = identifier + ": " + ival
                    Logger.write("d", "line = " + str(line))
                    Logger.write("i", "Try replacing line in oldfiledata")
                    try:
                        newfiledata = oldfiledata.replace(line, identifier+": "+value)
                    except:
                        Logger.write("e", "Could not replace line in oldfiledata!")
                        return False
                    Logger.write("i", "Try overwriting settingsfile")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove(sfile)
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open(sfile, "w")
                        except:
                            Logger.write("e", "Could not create new " + sfile)
                            return False
                        try:
                            nsfo.write(newfiledata)
                        except:
                            Logger.write("e", "Could not write newfiledata to settingsfile!")
                            return False
                        return True
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
        def addsetting(self, identifier, value, sfile=""):
            if sfile == "":
                Logger.write("i", "Try opening settings.acf")
                try:
                    sfileo = open("settings.acf", "w")
                except:
                    Logger.write("e", "Could not open settings.acf")
                    return False
                Logger.write("i", "Try adding new section")
                line = identifier + ": " + value + "\n"
                try:
                    sfileo.write(line)
                except:
                    Logger.write("e", "Could not create new section!")
                    return False
                return True
            else:
                Logger.write("i", "Try opening " + sfile)
                try:
                    sfileo = open(sfile, "w")
                except:
                    Logger.write("e", "Could not open " + sfile)
                    return False
                Logger.write("i", "Try adding new section")
                line = identifier + ": " + value + "\n"
                try:
                    sfileo.write(line)
                except:
                    Logger.write("e", "Could not create new section!")
                    return False
                return True
        def restoredefault(self, sfile="", tfile=""):
            if sfile == "":
                Logger.write("i", "Restoring default Settings file!")
                Logger.write("i", "Try opening /Setup/DefaultSettings.acf")
                try:
                    sfileo = open("../Setup/DefaultSettings.acf", "r")
                except:
                    Logger.write("e", "Could not open /Setup/DefaultSettings.acf")
                    return False
                Logger.write("i", "Try reading DSettings.acf")
                try:
                    filedata = sfileo.read()
                except:
                    Logger.write("e", "Could not read DSettings.acf")
                    return False
                if tfile == "":
                    Logger.write("i", "Try overwriting /System/settings.acf")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove("settings.acf")
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open("settings.acf", "w")
                        except:
                            Logger.write("e", "Could not create new settings.acf File!")
                            return False
                        try:
                            nsfo.write(filedata)
                        except:
                            Logger.write("e", "Could not write filedata to settingsfile!")
                            return False
                        return True
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
                else:
                    Logger.write("i", "Try overwriting /System/settings.acf")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove(tfile)
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open(tfile, "w")
                        except:
                            Logger.write("e", "Could not create new settings.acf File!")
                            return False
                        try:
                            nsfo.write(filedata)
                        except:
                            Logger.write("e", "Could not write filedata to settingsfile!")
                            return False
                        return True
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
            else:
                Logger.write("i", "Restoring default Settings file!")
                Logger.write("i", "Try opening /Setup/DefaultSettings.acf")
                try:
                    sfileo = open(sfile, "r")
                except:
                    Logger.write("e", "Could not open /Setup/DefaultSettings.acf")
                    return False
                Logger.write("i", "Try reading DSettings.acf")
                try:
                    filedata = sfileo.read()
                except:
                    Logger.write("e", "Could not read DSettings.acf")
                    return False
                if tfile == "":
                    Logger.write("i", "Try overwriting /System/settings.acf")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove("settings.acf")
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open("settings.acf", "w")
                        except:
                            Logger.write("e", "Could not create new settings.acf File!")
                            return False
                        try:
                            nsfo.write(filedata)
                        except:
                            Logger.write("e", "Could not write filedata to settingsfile!")
                            return False
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
                else:
                    Logger.write("i", "Try overwriting /System/settings.acf")
                    try:
                        Logger.write("i", "Try removing settings.acf")
                        try:
                            os.remove(tfile)
                        except:
                            Logger.write("e", "Could not remove settings.acf")
                            return False
                        try:
                            nsfo = open(tfile, "w")
                        except:
                            Logger.write("e", "Could not create new settings.acf File!")
                            return False
                        try:
                            nsfo.write(filedata)
                        except:
                            Logger.write("e", "Could not write filedata to settingsfile!")
                            return False
                    except:
                        Logger.write("e", "Could not overwrite settingsfile")
                        return False
    class ErrorHandler:
        def createdict(self, dictid):
            Logger.write("i", "Try creating new ErrorDict ["+dictid+"]")
            try:
                DataHandler.ErrorDict[dictid] = {}
            except:
                Logger.write("e", "Could not create ErrorDict ["+dictid+"]")
                return False
            return True
        def cleardict(self, dictid):
            Logger.write("i", "Try clearing ErrorDict ["+dictid+"]")
            try:
                DataHandler.ErrorDict[dictid] = {}
            except:
                Logger.write("e", "Could not clear ErrorDict ["+dictid+"]")
                return False
            return True
        def addentry(self, dictid, entryid, entry):
            Logger.write("i", "Try adding entry to ErrorDict ["+dictid+" - "+entryid+" - "+entry+"]")
            if dictid in DataHandler.ErrorDict:
                dict = DataHandler.ErrorDict[dictid]
                try:
                    dict[entryid] = entry
                except:
                    Logger.write("e", "Could not add Error entry ["+dictid+" - "+entryid+" - "+entry+"]")
                    return False
                return True
            else:
                Logger.write("e", "Dictionary ["+dictid+"] is not in ErrorDict!")
                return False
        def clearentry(self, dictid, entryid):
            Logger.write("i", "Try cleaning entry ["+entryid+"] in dict ["+dictid+"]")
            try:
                dict = DataHandler.ErrorDict[dictid]
            except:
                Logger.write("e", "Could not find dict ["+dictid+"] in ErrorDict!")
                return False
            try:
                i = {}
                dict[entryid] = None
            except:
                Logger.write("e", "Could clear entry ["+entryid+"]")
                return False
            return True
        def resetall(self):
            Logger.write("i", "Try resetting ErrorsDict")
            try:
                DataHandler.ErrorDict = {}
            except:
                Logger.write("e", "Could not reset ErrorDict!")
                return False
            return True
    class DataHandler:
        ErrorDict = {}


System = System()
Settings = System.Settings()
Logger = System.Logger()
DataHandler = System.DataHandler()
ErrorHandler = System.ErrorHandler()


class Input:
    pass


class Output:
    def CPrint(text, fgc=500, bgc=500, attrc="", newline=True):
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
    def CSPrint(self, state, message):
        if state == "":
            print("[....] " + message)
        if state == "ok":
            print("[ " + termcolor.colored("OK", "green", attrs=["bold"]) + " ] " + termcolor.colored(message, "green", attrs=["bold"]))
        if state == "error":
            print("[" + termcolor.colored("ERROR", "red", attrs=["blink", "bold"]) + "] " + termcolor.colored(message, "red", attrs=["bold"]))
        if state == "warning":
            # 208
            print("[" + fg(241) + attr("bold") + attr("blink") + "WARNING" + style.RESET + "] " + fg(241) + attr("bold") + message + style.RESET)
        if state == "info":
            print("[" + termcolor.colored("INFO", "cyan", attrs=["bold"]) + "] " + termcolor.colored(message, "cyan", attrs=["bold"]))
        if state == "debug":
            print("[" + termcolor.colored("DEBUG", "magenta", attrs=["bold"]) + "] " + termcolor.colored(message, "magenta", attrs=["bold"]))
        if state == "sys":
            print("[" + termcolor.colored("SYSTEM", "blue", attrs=["bold"]) + "] " + termcolor.colored(message, "blue", attrs=["bold"]))

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