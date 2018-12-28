{\rtf1\ansi\ansicpg1252\cocoartf1671
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red79\green123\blue61;\red23\green23\blue23;\red202\green202\blue202;
\red70\green137\blue204;\red212\green212\blue212;\red194\green126\blue101;}
{\*\expandedcolortbl;;\cssrgb\c37647\c54510\c30588;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Spell check in Python... open files for  correctly spelled vocab list, and a file with the correct spelling on the left and common misspellings on the right if it isn't found on the misspellings, correct spellings, or vocab list, then replace with 'unknown'\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # uses filestream, list, dictionary, and started getting comfortable with built-in functions\cf4 \cb1 \strokec4 \
\cb3 fmis = \cf5 \strokec5 open\cf6 \strokec6 (\cf7 \strokec7 'misspellings.csv'\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3 fvocab = \cf5 \strokec5 open\cf6 \strokec6 (\cf7 \strokec7 'vocab.txt'\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3 master = \cf5 \strokec5 dict\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3 vHold = \cf5 \strokec5 list\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3 rightSp = \cf5 \strokec5 list\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3 found = \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 for\cf4 \strokec4  v \cf5 \strokec5 in\cf4 \strokec4  fvocab \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3   v = v.rstrip\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3   vHold.append\cf6 \strokec6 (\cf4 \strokec4 v\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 for\cf4 \strokec4  m \cf5 \strokec5 in\cf4 \strokec4  fmis \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3   m = m.rstrip\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3   allRight\cf6 \strokec6 ,\cf4 \strokec4  allMis = m.split\cf6 \strokec6 (\cf7 \strokec7 ','\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3   allMis = allMis.split\cf6 \strokec6 (\cf7 \strokec7 '|'\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3   master\cf6 \strokec6 [\cf4 \strokec4 allRight\cf6 \strokec6 ]\cf4 \strokec4  = allMis\cb1 \
\
\cb3 inp = \cf5 \strokec5 input\cf6 \strokec6 (\cf7 \strokec7 "Please enter in a sentence to correct\\n"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3 inp = inp.lower\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3 inp = inp.split\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3 s = \cf7 \strokec7 ''\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 for\cf4 \strokec4  it \cf5 \strokec5 in\cf4 \strokec4  inp \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 for\cf4 \strokec4  key\cf6 \strokec6 ,\cf4 \strokec4  value \cf5 \strokec5 in\cf4 \strokec4  master.items\cf6 \strokec6 ()\cf4 \strokec4  \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 for\cf4 \strokec4  sepVal \cf5 \strokec5 in\cf4 \strokec4  value \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3       \cf5 \strokec5 if\cf4 \strokec4  it == sepVal.lower\cf6 \strokec6 ()\cf4 \strokec4  \cf5 \strokec5 and\cf4 \strokec4  found == \cf5 \strokec5 False\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         rightSp.append\cf6 \strokec6 (\cf4 \strokec4 key.lower\cf6 \strokec6 ())\cf4 \cb1 \strokec4 \
\cb3         found = \cf5 \strokec5 True\cf4 \cb1 \strokec4 \
\cb3       \cf5 \strokec5 elif\cf4 \strokec4  it == key.lower\cf6 \strokec6 ()\cf4 \strokec4  \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         rightSp.append\cf6 \strokec6 (\cf4 \strokec4 it.lower\cf6 \strokec6 ())\cf4 \cb1 \strokec4 \
\cb3         found = \cf5 \strokec5 True\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 if\cf4 \strokec4  found == \cf5 \strokec5 False\cf4 \strokec4  \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 for\cf4 \strokec4  voc \cf5 \strokec5 in\cf4 \strokec4  vHold \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3       \cf5 \strokec5 if\cf4 \strokec4  voc.lower\cf6 \strokec6 ()\cf4 \strokec4  == it \cf5 \strokec5 and\cf4 \strokec4  found == \cf5 \strokec5 False\cf4 \strokec4  \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         rightSp.append\cf6 \strokec6 (\cf4 \strokec4 it.lower\cf6 \strokec6 ())\cf4 \cb1 \strokec4 \
\cb3         found = \cf5 \strokec5 True\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 if\cf4 \strokec4  found == \cf5 \strokec5 False\cf4 \strokec4  \cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3     rightSp.append\cf6 \strokec6 (\cf7 \strokec7 'unknown'\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3   found = \cf5 \strokec5 False\cf4 \cb1 \strokec4 \
\
\cb3 s = \cf7 \strokec7 ' '\cf4 \strokec4 .join\cf6 \strokec6 (\cf4 \strokec4 rightSp\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 print\cf4 \strokec4  \cf6 \strokec6 (\cf4 \strokec4 s\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
}