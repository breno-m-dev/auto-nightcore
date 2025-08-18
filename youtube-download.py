import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pytubefix.helpers import safe_filename

def download_audio_from_url(url):
    """
    Download the audio from a youtube video through its URL
    """
    #following try tests if the URL is valid and if the connection is functioning


    try:

        yt = YouTube(url, on_progress_callback=on_progress)
    except:
        print("Connection or URL Error")
    else:
        dowload_audio_from_object(yt)
        # print(yt.title)
        # print("Downloading...") 
        
        # try:
        #     ys = yt.streams.get_audio_only()
        #     ys.download()
        # except:
        #     print("An download error has occured")
        # else:
        #     print("Download is completed successfully")

def dowload_audio_from_object(yt, outpath):
    """
    Baixa o áudio de um objeto do tipo YouTube.
    """
    print(yt.title)
    print("Downloading...") 
    try:
        ys = yt.streams.get_audio_only()
        ys.download(output_path = outpath)
    except:
        print("An download error has occured")
    else:
        print("Download is completed successfully")




def download_audio_playlist(url: str):
    """
    Baixa o áudio de todos os vídeos em uma playlist do YouTube.
    """
    try:
        playlist = Playlist(url)
        print(f"Baixando a playlist: {playlist.title}")

        # Cria um diretório para a playlist
        playlist_folder = safe_filename(playlist.title)
        if not os.path.exists(playlist_folder):
            os.makedirs(playlist_folder)

        print(f"Salvando os arquivos em: {os.path.abspath(playlist_folder)}")

        for video in playlist.videos:
            print("-" * 40)
            # Passa o caminho da pasta da playlist para a função de download
            print(playlist_folder)
            dowload_audio_from_object(video, playlist_folder)

        print("\n✅ Download da playlist concluído.")

    except Exception as e:
        print(f"❌ Ocorreu um erro com a playlist {url}: {e}")


url = input("Enter the YouTube video or playlist URL: ")

download_audio_playlist(url)

# def main():
#     """
#     Função principal para lidar com a entrada do usuário e decidir se
#     baixa um único vídeo ou uma playlist.
#     """
#     url = input("Enter the YouTube video or playlist URL: ")

#     if "playlist?list=" in url:
#         download_audio_playlist(url)
#     else:
#         download_audio(url)

# if __name__ == "__main__":
#     main()
