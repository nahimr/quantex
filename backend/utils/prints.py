class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Msg(msg, col) -> None:
    print(col + str(msg) + bcolors.ENDC)

def MsgWarn(msg) -> None:
    Msg(msg, bcolors.WARNING)

def MsgError(msg) -> None:
    Msg(msg, bcolors.FAIL)

def MsgSuccess(msg) -> None:
    Msg(msg, bcolors.OKGREEN)

def MsgDebug(msg) -> None:
    Msg(msg, bcolors.OKCYAN)
