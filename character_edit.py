#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import codecs
import os
import datetime
import linecache
import io

import time
import subprocess

#def encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


orgFilePath = 'org.txt'
editFilePath ='edit.txt'




def delete_last_character():
    orgFile = codecs.open(orgFilePath, 'r', 'utf-8')
    editFile = codecs.open(editFilePath, 'w', 'utf-8')

    for i in range(1,6):#数字になる直前に終わる
        editText = linecache.getline(orgFilePath,i)

        #TypeCheck
        # check = isinstance(editText, str)
        # print(check)

        editedText = editText.strip()# 両端の改行や空白を削除　理由：editTextは、linecacheでとった改行込みのデータのため

        editedText = editedText[:-1]#最後の一文字を削除

        editedText = str(editedText)
        print(editedText)


    print('Finish')

    orgFile.close()
    editFile.close()

if __name__ == "__main__":
    delete_last_character()
