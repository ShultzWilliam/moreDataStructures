#moduleTest.py
#This module is a part of the extraDataStructures repository
#It contains a few functions (only one at the moment) to test for the functionality of the data structures contained within this repository
#Currently it contains a function to test listModule.py
#Written by: William Shultz
#Initial Upload: January 21, 2022
#Last Updated: January 21, 2022

import listModule as ll

def testLinkedListModule() -> None:
    randomSingleNode = ll.linkedListNode("Alan")
    randomDoubleNode = ll.doublyLinkedListNode("Anime")

    singleTestList = ll.linkedList()
    doubleTestList = ll.doublyLinkedList()
    print("--PRINTING EMPTY LIST--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")


    singleTestList.append("Anna")
    doubleTestList.append("Amiino")
    print("--PRINTING LISTS WITH ONE NODE--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")

    singleTestList.append("Beta")
    doubleTestList.append("Baka")

    print("--PRINTING LISTS WITH TWO ELEMENTS--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")

    singleTestList.prepend("Carter")
    doubleTestList.prepend("Katako")

    print("--PRINTING AFTER PREPREND, 3 ELEMENTS--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")

    singleTestList.insertAfter("Devin","Anna")
    doubleTestList.insertAfter("Deetou","Amiino")

    print("--PRINTING AFTER INSERTION, 4 ELEMENTS--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")


    singleTestList.remove("Devin")
    doubleTestList.remove("Deetou")
    print("--PRINTING AFTER REMOVAL, 3 ELEMENTS--")
    print(str(singleTestList))
    print(str(doubleTestList) + "\n")

    print("--PRINTING STRING VALUES FOR EACH NODE IN SINGLE LIST--")
    curSingle = singleTestList.head
    while curSingle != None:
        print(str(curSingle))
        curSingle = curSingle.next
    print("")

    print("--PRINTING STRING VALUES FOR EACH NODE IN DOUBLE LIST, FORWARD--")
    curDouble = doubleTestList.head
    while curDouble != None:
        print(str(curDouble))
        curDouble = curDouble.next
    print("")
    print("--PRINTING STRING VALUES FOR EACH NODE IN DOUBLE LIST, BACKWARD--")
    curDouble = doubleTestList.head
    while curDouble.next != None:
        curDouble = curDouble.next
    while curDouble != None:
        print(str(curDouble))
        curDouble = curDouble.previous