from SpeechToText import str_pinyin
from readFile import getStrTargetList
from readSimDict import data
from TextToSpeech import engine
import os

clist2=['sh', 'zh', 'ch']
clist1=['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'b', 'n', 'm']


print('str_pinyin:')
print(str_pinyin)


class syllable:
    def __init__(self, pinyin=None):
        self.consonant = None
        self.vowel = None
        self.accent = None
        if pinyin == None:
            return
        self.accent = pinyin[len(pinyin)-1]
        tempcons2 = pinyin[:2]
        tempcons1 = pinyin[0]
        if tempcons2 in clist2:
            self.consonant = tempcons2
            self.vowel = pinyin[2:len(pinyin)-1]
        elif tempcons1 in clist1:
            self.consonant = tempcons1
            self.vowel = pinyin[1:len(pinyin) - 1]
        else:
            self.vowel = pinyin[:len(pinyin)-1]
    def __str__(self):
        return self.consonant+self.vowel+self.accent

def compare(sy1, sy2):
    rate = 0
    if sy1.consonant == sy2.consonant:
        rate += 1
    elif sy2.consonant in data and sy1.consonant in data[sy2.consonant]:
        rate += 0.5
    if sy1.vowel == sy2.vowel:
        rate += 1
    elif sy2.vowel in data and sy1.vowel in data[sy2.vowel]:
        rate += 0.5
    if sy1.accent == sy2.accent:
        rate += 1
    elif sy2.accent in data and sy1.accent in data[sy2.accent]:
        rate += 0.5
    return rate

def toSyList(pinyin):
    SyList = []
    for str in pinyin:
        SyList.append(syllable(str))
    return SyList

def toTargetList(str_targerList):
    targetList = []
    for sen in str_targerList:
        targetList.append(toSyList(sen))
    return targetList

def maxSim(test, target):
    if len(test) < len(target) or len(test)-len(target) > 2:
        return 0
    else:
        max = 0
        for i in range(0, len(test)-len(target)+1):
            m = 0
            for j in range(0, len(target)):
                m += compare(test[i+j], target[j])
            if m > max: max = m
        return max/(3*len(target))

def show(dict):
    str_target = []
    for sy in dict['target']:
        str_target.append(sy.consonant+sy.vowel+sy.accent)
    print({'target': str_target, 'maxSim': dict['maxSim']})
    return  targetList.index(dict['target'])

def maxSimOverall(test, targetList):
    max = 0
    result = None
    for target in targetList:
        if maxSim(test, target) > max:
            max = maxSim(test, target)
            result = target
    return {'target': result, 'maxSim': max}

test = toSyList(str_pinyin)
targetList = toTargetList(getStrTargetList("str_target_list.py"))
if maxSimOverall(test,targetList)['maxSim'] < 0.6:
    engine.say('听不清，请再说一遍')
else:
    print(maxSimOverall(test,targetList)['maxSim'])
    engine.say(getStrTargetList('str_origin.py')[show(maxSimOverall(test, targetList))])
engine.runAndWait()
os.system('del commands\\test1.wav')