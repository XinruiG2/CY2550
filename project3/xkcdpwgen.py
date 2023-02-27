#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, getopt, random

words = 4
caps = 0
nums = 0
symbols = 0
f = open("words.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
password = ""
chooseSymbols = "~!@#$%^&*.:;"
chooseNumbers = "0123456789"
word_list = []
other_list = {}
should_display = True

argList = sys.argv[1:]
short_options = "hw:c:n:s:"
long_options = ["help", "words=", "caps=", "numbers=", "symbols="]

arguments, values = getopt.getopt(argList, short_options, long_options)

for currArgument, currValue in arguments:
  if currArgument == "-h" or currArgument == "--help":
    print('''usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS] 
    Generate a secure, memorable password using the XKCD method
    
    optional arguments:
    -h, --help               show this help message and exit
    -w WORDS, --words WORDS  include WORDS words in the password (default=4)
    -c CAPS, --caps CAPS     capitalize the first letter of CAPS random words
    -n NUMBERS, --numbers NUMBERS
                             insert NUMBERS random numbers in the password
                             (default=0)
    -s SYMBOLS, --symbols SYMBOLS
                             insert SYMBOLS random symbols in the password
                             (default=0)''')
    should_display = False
  elif currArgument in ("-w", "--words"):
    words = int(currValue)
  elif currArgument in ("-c", "--caps"):
    caps = int(currValue)
  elif currArgument in ("-n", "--numbers"):
    nums = int(currValue)
  elif currArgument in ("-s", "--symbols"):
    symbols = int(currValue)

if int(caps) > int(words):
  raise ValueError("error: the number of words to capitalize exceeds the number of words")

randCapIndex = []
randNumIndex = []
randSymIndex = []
already_capped = []

for x in range(0, caps):
  wordIndexC = random.randint(0, words - 1)
  while wordIndexC in already_capped:
   wordIndexC = random.randint(0, words - 1)
  randCapIndex.append(wordIndexC)
  already_capped.append(wordIndexC)
  other_list[wordIndexC] = ""

for x in range(0, nums):
  wordIndexN = random.randint(0, words)
  randNumIndex.append(wordIndexN)
  other_list[wordIndexN] = ""

for x in range(0, symbols):
  wordIndexS = random.randint(0, words)
  randSymIndex.append(wordIndexS)
  other_list[wordIndexS] = ""

index_acc = 0

for x in range(0, words):
  word_list.append(random.choice(f_content_list))
  
for x in randCapIndex:
  other_list[x] += "C"

for x in randNumIndex:
  other_list[x] += random.choice(chooseNumbers)

for x in randSymIndex:
  other_list[x] += random.choice(chooseSymbols)

for x in other_list:
  if x < len(word_list):
    if other_list[x][0] == "C":
      word_list[x] = other_list[x][1:] + word_list[x].capitalize()
    else: 
      word_list[x] = other_list[x] + word_list[x]

for x in word_list:
  password += x

for x in other_list:
  if x >= words:
    password += other_list[x]

if should_display:
  print(password)
