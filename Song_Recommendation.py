import Camera
import pandas as pd
import random
import Camera

def song_recommendations():
    emotion = Camera.snapshot()
    print(emotion)
    
    #emotion2=Camera.emotion_from_camera()

    if emotion == "Happy":
        exec(open('Happy.py').read())
    elif emotion =="Angry":
        exec(open('Angry.py').read())
    elif emotion =="Disgust":
        exec(open('Disgust.py').read())
    elif emotion =="Fear":
        exec(open('Fear.py').read())
    elif emotion =="Neutral":
        exec(open('Neutral.py').read())
    elif emotion =="Sad":
        exec(open('Sad.py').read())
    else:
        exec(open('Surprise.py').read())
        
    return emotion
    
    
