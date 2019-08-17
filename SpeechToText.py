#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nl8590687
用于测试整个一套语音识别系统的程序
语音模型 + 语言模型
"""
import warnings
warnings.filterwarnings('ignore')
import platform as plat
from warnings import filterwarnings as fff
fff('ignore')
from SpeechModel251 import ModelSpeech
from LanguageModel2 import ModelLanguage
from keras import backend as K
import os

datapath = ''
modelpath = 'model_speech'

system_type = plat.system()
if(system_type == 'Windows'):
	datapath = '.'
	modelpath = modelpath + '\\'
elif(system_type == 'Linux'):
	datapath = 'dataset'
	modelpath = modelpath + '/'
else:
	print('*[Message] Unknown System\n')
	datapath = 'dataset'
	modelpath = modelpath + '/'

ms = ModelSpeech(datapath)

ms.LoadModel(modelpath + 'speech_model251_e_0_step_625000.model')

os.system('ffmpeg -i commands/test.wav -ar 16000 commands/test1.wav')

r = ms.RecognizeSpeech_FromFile('commands/test1.wav')

K.clear_session()

ml = ModelLanguage('model_language')
ml.LoadModel()

str_pinyin = r
str_pinyin

r = ml.SpeechToText(str_pinyin)














