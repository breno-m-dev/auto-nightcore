from moviepy import *




def make_video(input_audio: str, input_img: str ):
    
   

    # Carregar áudio (mp3)
    audio = AudioFileClip(input_audio)

    # Carregar imagem (png/jpg)
    image = ImageClip(input_img, duration= audio.duration)  # duração em segundos

    # Definir o áudio do vídeo
    video = image.with_audio(audio)
    
    # Exportar vídeo
    video.write_videofile("nightcoreExport.mp4", fps=24, codec="libx264", audio_codec="aac")
