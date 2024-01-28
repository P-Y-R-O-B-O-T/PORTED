import sys
import math
import time
import json
import base64
import socket
import random
import threading

# python3 main.py <HOST> <SP> <EP> <FLAG> <SPLIT_PARTS>
# CONSTRAINTS :
#     SP >= 2000
#     65000 > EP > SP
#     SPLIT_PARTS < len(FLAG)

STATUS = True

HOST = sys.argv[1]
START_PORT = int(sys.argv[2])
END_PORT = int(sys.argv[3])
FLAG = sys.argv[4]
PARTS = int(sys.argv[5])

SPLIT_PART_LEN = math.ceil(len(FLAG)/PARTS)
FLAG_SPLIT = [FLAG[_ : _+(len(FLAG)//PARTS)+1] for _ in range(0,
                                                              len(FLAG),
                                                              SPLIT_PART_LEN)]

CURR_PORT = START_PORT

#$$$$$$$$$$#

def CREATE_RUN_SERVER() :
    global CURR_PORT
    global STRING
    global CURR_PORT

    SEQ_NO = min(int(PARTS*((CURR_PORT-START_PORT)/(END_PORT-START_PORT))),
                 len(FLAG_SPLIT)-1)

    BYTES = FLAG_SPLIT[SEQ_NO].encode("ascii")
    B64_BYTES = base64.b64encode(BYTES)
    B64_STR = B64_BYTES.decode("ascii")

    D = {"SEQ": SEQ_NO+1, "STR": B64_STR, "TOTAL": len(FLAG_SPLIT)}
    J = json.dumps(D)

    print("[$] RUNNING ON {0} SERVES FOR : {1:<10} ; ENCODED : {2:<10} ; PART_NO : {3}".format(CURR_PORT,
                                                                               FLAG_SPLIT[SEQ_NO],
                                                                               B64_STR, SEQ_NO+1))

    SS = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
    SS.setsockopt(socket.SOL_SOCKET,
                  socket.SO_REUSEADDR,
                  1)
    SS.bind((HOST,
             CURR_PORT))
    SS.settimeout(1)
    SS.listen(500)
    START_TIME = time.time()
    TIME_TO_RUN = 60

    while (time.time() - START_TIME) < TIME_TO_RUN :
        try :
            C, A = SS.accept()
            print("\t\t[@] GOT CONNECTION FROM {0}".format(A))
            C.sendall(J.encode("utf-8"))
            time.sleep(1/1000)
            C.close()
        except : 
            pass
    SS.close()

#$$$$$$$$$$#

def RUN_SERVER() :
    global CURR_PORT
    global START_PORT
    global END_PORT
    global STATUS

    while STATUS :
        CURR_PORT = random.randint(START_PORT,
                                   END_PORT)
        CREATE_RUN_SERVER()
        time.sleep(1/1000)

#$$$$$$$$$$#

if __name__ == "__main__" :
    print("SPLIT FLAG :", FLAG_SPLIT)
    THREAD = threading.Thread(target=RUN_SERVER)
    THREAD.start()
    input()
    STATUS = False
