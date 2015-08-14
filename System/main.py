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
#  |   Version: 0.0.2                                                              |
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
        UsersDict = {"azurite": {"passwd": "017762", "rights": "full"}, "me": {"passwd": "", "rights": "normal"}}
        curr_user = "azurite"
        MachineName = "DevMachine"
        version = 0
        cpu_count = 0
        cpu_count_logical = 0
        memory_total_mb = 0
        memory_total_gb = 0
        curr_pid = 0
        uname = ""
        curr_dir = ""
        def getsysinfo(self):
            Logger.write("i", "Collecting System Information")
            try:
                self.version = Settings.getsetting("version")
            except:
                Logger.write("e", "Could not get System version!")
                return False
            try:
                self.cpu_count = psutil.cpu_count(logical=False)
            except:
                Logger.write("e", "Could not get System cpu count!")
                return False
            try:
                self.cpu_count_logical = psutil.cpu_count()
            except:
                Logger.write("e", "Could not get System cpu count (only physical)!")
                return False
            try:
                self.tmp = psutil.virtual_memory()
            except:
                Logger.write("e", "Could not get System total virtual memory!")
                return False
            try:
                self.tmp2 = str(self.tmp)
                self.tmp2 = self.tmp2.strip("svmem('")
                self.tmp = self.tmp2.split(", ")
                self.tmp_total = self.tmp[0].strip("total=L")
                Logger.write("e", "Could not get System version!")
                self.memory_total_mb = self.tmp_total * 1024
                self.memory_total_mb = self.memory_total_mb * 1024
                self.memory_total_gb = self.memory_total_mb * 1024
            except:
                Logger.write("e", "Could not recalculate virtual memory!")
                return False
            try:
                self.curr_pid = os.getpid()
            except:
                Logger.write("e", "Could not get current pid!")
                return False
            try:
                self.uname = os.uname()
            except:
                Logger.write("e", "Could not get System uname!")
                return False
            try:
                self.curr_dir = os.path.curdir()
            except:
                Logger.write("e", "Could not get current directory!")
                return False
            return True
    class CMDHandler():
        def processcmd(self, cmd):
            # Processing command: Extracting Arguments
            cstring = cmd.split(" ")
            cmd = cstring[0]
            args = []
            for item in cstring:
                if item != cmd:
                    args.append(item)
            # Checking if command is known by the system
            # If command is listed here write "knowncommand = True" before the other stuff
            # If command has finished its stuff, write "finishedcmd = True"
            knowncommand = False
            finishedcmd = False
            if cmd == "exit":
                sys.exit(0)
            if cmd == "test":
                finishedcmd = True
                knowncommand = True

            # Creating Return Dict
            rdict = {}
            if knowncommand is True:
                rdict["kcmd"] = True
            else:
                rdict["kcmd"] = False
            if finishedcmd is True:
                rdict["state"] = True
            else:
                rdict["state"] = False
            rdict["cmd"] = cmd
            i = 0
            for item in args:
                rdict["arg"+str(i)] = args[0]
            return rdict
    class Console:
        def start(self):
            Logger.write("i", "Starting Console")
            Output.CSPrint("sys", "Starting Console")
            #Logger.write("i", "Collecting System-information")
            #DataHandler.getsysinfo()
            Logger.write("i", "Initialising Console main loop!")
            self.loop()
        def loop(self):
            exit = False
            while exit is False:
                input = raw_input("["+DataHandler.curr_user+"-"+DataHandler.MachineName+"] ~$ ")
                Logger.write("i", "Recieved user input through console! ["+str(input)+"]")
                Logger.write("i", "Handing input over to CommandProcessing")
                rdict = CMDHandler.processcmd(input)
                if rdict["state"] is True:
                    if rdict["kcmd"] is True:
                        Logger.write("i", "CommandProcessing returned no error! Command was processed successful!")
                    else:
                        Logger.write("d", "Found error in CommandProcessing! CP processed cmd successful BUT cmd is not known by the system -> Statement IMPOSSIBLE!")
                else:
                    if rdict["kcmd"] is True:
                        Logger.write("i", "CommandProcessing could not finish processing! But command is known by the system!")
                        print(termcolor.colored(rdict["cmd"], "red") + termcolor.colored(": ","yellow") + termcolor.colored("Command exists but could not be processed!", "blue"))
                    else:
                        Logger.write("i", "CommandProcessing could not finish processing and command is not known by the system!")
                        print(termcolor.colored(rdict["cmd"], "red") + termcolor.colored(": ","yellow") + termcolor.colored("Command does not exist!", "blue"))


System = System()
Settings = System.Settings()
Logger = System.Logger()
DataHandler = System.DataHandler()
ErrorHandler = System.ErrorHandler()
Console = System.Console()
CMDHandler = System.CMDHandler()

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
CPrint = Output.CPrint()
#CSPrint = Output.CSPrint()

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
    import psutil
    Logger.write("i" ,"Imported psutil")
except:
    Logger.write("e" ,"Could not import psutil!")
    print "ERROR: Could not import psutil!"

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

Console.start()