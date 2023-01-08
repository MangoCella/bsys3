#!/usr/bin/env python3
import os
import threading
import slowsort

# calc can run twice at the same time
SEMAPHORE = threading.Semaphore(2)


def calc(num):
    """
    The calc.sh output needs to be an integer, casting int
    f"" is an fstring that can be used for variable substitution with curly brackets
    :param num:
    :return:
    """
    # The calc.sh output needs to be an integer, casting int
    # f"" is an fstring that can be used for variable substitution with curly brackets
    return int(os.popen(f"./calc.sh {num}").read().strip())


def createresultfile(inputlist):
    """
    create result file
    :param inputlist:
    :return:
    """
    # get first and last value to construct the filename
    first = inputlist[0]
    last = inputlist[-1]
    # create the corresponding new filename
    file = open(f"{first}-{last}.csv", 'w')
    for item in inputlist:
        file.write(f"{item}\n")
        #os.popen(f"chmod {first}-{last}.csv 600")
        #os.chmod(file, 0o600)
    file.close()
    # set permissions of the file to 600



def runperfile(files):
    """
    run per file
    :param files:
    :return:
    """
    for file in files:
        with open(file, "r") as openf:
            # Read the file and convert its lines into a python list with list comprehension
            numberslist = [int(x) for x in openf.read().split()]
            SEMAPHORE.acquire()
            multipliedlist = [calc(number) for number in numberslist]
            SEMAPHORE.release()
        sortedmultipliedlist = slowsort.slowsort(multipliedlist)
        print(sortedmultipliedlist)
        createresultfile(sortedmultipliedlist)


# runperfile("101-200.csv")


# thread.start_new_thread( print_time, ("Thread-1", 2, ) )
B1 = ["1-100.csv", "101-200.csv", "201-300.csv"]
B2 = ["301-400.csv", "401-500.csv", "501-600.csv"]
BATCHES = [B1, B2]
for b in BATCHES:
    try:
        print("start")
        #thread.start_new_thread(runperfile, (b,))
        THREAD1 = threading.Thread(target=runperfile, args=(b,))
        THREAD1.start()
        THREAD1.join()
    except Exception as e:
        raise e

while 1:
    pass
