from moviepy import *
import os
import random


#input_img is a optional parameter. It will only be used if random_image == false
def make_video(input_audio: str, use_random_image: bool , input_img: str = None):
    
   

    # Carregar áudio (mp3)
    audio = AudioFileClip(input_audio)

    # Carregar imagem (png/jpg)
    if(use_random_image):
        video_image = random_image("./images")
        image = ImageClip(video_image, duration= audio.duration)  # duração em segundos
    else:
        image = ImageClip(input_img, duration= audio.duration)  # duração em segundos

    # Definir o áudio do vídeo
    video = image.with_audio(audio)
    
    # Exportar vídeo
    video.write_videofile("nightcoreExport.mp4", fps=24, codec="libx264", audio_codec="aac")


def random_image(folder: str):
    imagens = [
        nome for nome in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, nome))
    ]
    #print(imagens)
    
    return folder+"/"+random.choice(imagens)