#coding=utf-8
from gtts import gTTS
import os
import argparse
import logging
import codecs

 
# getting all the arguments from the CLI
parser=argparse.ArgumentParser()
parser.add_argument("--location",help="enter the location of the file",default='sample')
parser.add_argument("--language",help="enter the language of the audio",default='hi')
args=parser.parse_args()

# defining function for taking text input
def input_text():
    str=raw_input("enter the text ")
    text = codecs.decode(str,"utf-8")
    return text

#taking the input for language

def input_lang():
    str=raw_input("enter the language ")
    return str


#creating a class for opening the file and reading the text from it
class file_handler:
    def opening_file(str):
        temp = str + ".txt"
        f = open(str,"r")
        text_in_file = f.read()
        f.close()
        return text_in_file

# defining functions for choosing the language of the audio 

def lang_select(str):
    if str == "english":
      audio_language = 'en'
    if str=="hindi":
      audio_language = 'hi'
    else:
      audio_language = 'hi'
    return audio_language


# class converting the text in the file to speech
class audio:
    
    def create_audio(self):
        
        audio_text=input_text()
        language=input_lang()
        au_language=lang_select(language)



        file_val=file_handler()
        #audio_text=file_val.opening_file(location);
	
        audio_object=gTTS(text=audio_text,lang=au_language,slow=False)
        temp=raw_input("enter the name of the audio file you want?")
        temp=temp+".mp3"
       
        audio_object.save(temp)
        os.system("mpg321 "+temp)


#function for saving the produced mp3 to a desired location

def save_location:
    print("enter the location where you want to save the file")
    temp=input()
    
    
    
    
          
          


a1=audio()
a1.create_audio()





















