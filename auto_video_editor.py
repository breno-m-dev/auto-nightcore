from moviepy import *




def make_video(input_img: str, input_audio: str):
    
   

    # Carregar áudio (mp3)
    audio = AudioFileClip(input_audio)

    # Carregar imagem (png/jpg)
    image = ImageClip("input_img", duration= audio.duration)  # duração em segundos

    # Definir o áudio do vídeo
    video = image.set_audio(audio)
    
    # Exportar vídeo
    video.write_videofile("nightcore.mp4", fps=24, codec="libx264", audio_codec="aac")
