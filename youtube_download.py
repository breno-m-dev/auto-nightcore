import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pytubefix.helpers import safe_filename
import re
class Musica:
    def __init__(self, path, title):
        self.path = path
        self.title = title
    def set_all(self, path, title):
        self.path = path
        self.title = title


lista_musicas = []
lonely_music = Musica("","")


def sanitize_filename(old_filename: str) -> str:
    """
    remove characters that would generate errors
    this was found trying to make a nightcore song out of a song with the following title:
    Demon's Souls Soundtrack - "Tower Knight/Penetrator"
    """
  
    new_filename = re.sub(r'[<>:"/\\|?*]', '', old_filename )
    new_filename = re.sub(r"[']", "", new_filename)
   
    return new_filename


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
        
        folder_name = "oioi"
        #print(yt.title)
        safe_title = dowload_audio_from_object(yt, folder_name)
        lonely_music.set_all(folder_name+"/"+safe_title+".m4a", safe_title)
    


def dowload_audio_from_object(yt, outpath) -> str:
    """
    Baixa o áudio de um objeto do tipo YouTube.
    """
    print(yt.title)
    print("Downloading...")
    safe_name = sanitize_filename(yt.title)
    try:
        ys = yt.streams.get_audio_only()
        ys.download(output_path = outpath, filename = safe_name+".m4a")
        yt.title = safe_name

        #ys.download()
    except:
        print("An download error has occured")
    else:
        print("Download is completed successfully")
        return safe_name



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
        lista_musicas.clear()
        for video in playlist.videos:
            print("-" * 40)
            # Passa o caminho da pasta da playlist para a função de download
            print(playlist_folder)

            safe_title = dowload_audio_from_object(video, playlist_folder)
            lista_musicas.append( Musica( playlist_folder+"/"+safe_title+".m4a" , safe_title))

        print("\n✅ Download da playlist concluído.")

    except Exception as e:
        print(f"❌ Ocorreu um erro com a playlist {url}: {e}")

def is_playlist(url):
    try:
        p = Playlist(url)
        if len(p.video_urls) > 0:
            return True
        else:
            return False
    except Exception:
        return False

#print(sanitize_filename ('a','Demon\'s Souls Soundtrack - "Tower Knight/Penetrator"') )

# url = input("Enter the YouTube video or playlist URL: ")
# download_audio_from_url(url)
# print(is_playlist(url))

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
