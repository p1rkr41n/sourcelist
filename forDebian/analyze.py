from dataclasses import replace
import os 
with open("sources.listold", "r") as input:
    with open("downloadSource.txt", "r") as listSource:
        listSource = listSource.read().split("\n")
        input = input.read()
        for checker in listSource:
            if input.find(checker) != -1:
                # print(checker)
                break
            else:
                print("not found ")
                checker = "0"
        if checker != "0":
            input = input.replace(checker, "%s")
        print(input)
