import youtube_download
import music_to_nightcore
import auto_video_editor
import os


def main():
    """
    Main function to orchestrate the auto-nightcore process.
    """
    
    url = input("Enter the YouTube video or playlist URL: ")
    if youtube_download.is_playlist(url):
        run_through_playlist(url)
    else:
        run_through_single_video(url)
    #auto_video_editor.make_video("night_core_taste_the_blood.mp3", "./images/dog.png")

#Does the whole process for a playlist
def run_through_playlist(url):
    youtube_download.download_audio_playlist(url)
    for musica in youtube_download.lista_musicas:
        print("PATH:"+musica.path)
        music_to_nightcore.make_nightcore(musica.path, "NIGHTCORE-"  + musica.title +  ".mp3")

#Does the whole process for a single video
def run_through_single_video(url):
        youtube_download.download_audio_from_url(url)
        print("PATH:"+youtube_download.lonely_music.path)
        # print(youtube_download.lonely_music.title)
        # print(youtube_download.lonely_music.path)
        music_to_nightcore.make_nightcore(youtube_download.lonely_music.path, "NIGHTCORE-"+youtube_download.lonely_music.title +".mp3")
        
        auto_video_editor.make_video("NIGHTCORE "+youtube_download.lonely_music.title +".mp3", "./images/dog.png")




if __name__ == "__main__":
    main()