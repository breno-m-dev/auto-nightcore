import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from pytubefix.helpers import safe_filename
import re
DOWNLOAD_FOLDER= "./downloaded_music"

class Musica:
    def __init__(self, path, title):
        self.path = path
        self.title = title
    def set_all(self, path, title):
        self.path = path
        self.title = title


lista_musicas = []
#lonely_music = Musica("","")


def clean_filename(old_filename: str) -> str:
    """
    Remove characters that would generate errors due to reserved symbols in the OS..
    This was found trying to make a nightcore song out of a song with the following title:
    Demon's Souls Soundtrack - "Tower Knight/Penetrator".
    Args:
        old_filename (str): Name of the chosen file.
    Returns:
        str: cleaned version of the file name.

    Example:
        >>> clean_filename("Demon's Souls Soundtrack - \"Tower Knight/Penetrator\"")
        "Returns: 'Demonssoulssoundtrac-towerknightpenetrator"
    """
  
    new_filename = re.sub(r'[<>:"/\\|?*]', '', old_filename )
    new_filename = re.sub(r"[']", "", new_filename)
    new_filename = re.sub(r" ", "", new_filename)
    return new_filename

#started using type hints, even though it doesnt
#change execution. Just because it will help me later on
def download_audio_from_url(url: str) -> Musica:
    """
    Download audio from a single YouTube video from given URL.

    Args:
        url (str): URL of the YouTube video.

    Returns:
        Musica: Object containing the downloaded file path and title.

    Raises:
        Exception: If connection or download fails.
    """

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        
    except:
        print("Connection or URL Error")
    else:
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.makedirs(DOWNLOAD_FOLDER)
        folder_name = DOWNLOAD_FOLDER
        #print(yt.title)
        
        safe_title = download_audio_from_object(yt, folder_name)
        our_music = Musica( os.path.join(folder_name, f"{safe_title}.m4a"),
                           safe_title
        )
        
        return our_music



def download_audio_from_object(yt: YouTube, outpath: str) -> str:
    """
    Download music from a YouTube object.
    Args:
        yt (YouTube): YouTube object representing a video and its metadata.
        outpath (str): path to where the video shall be downloaded into.
    
    Returns:
        str: Sanitized title used as the downloaded file name.
        This is returned, just in case the yt.title differs from the cleaned version.
    
    Raises:
        Exception: If the download process fails.
    """
    print(yt.title)
    print("Downloading...")
    safe_name = clean_filename(yt.title)
    try:
        ys = yt.streams.get_audio_only()
        ys.download(output_path = outpath, filename = safe_name+".m4a")
        yt.title = safe_name

    except:
        print("An download error has occured")
    else:
        print("Download is completed successfully")
        return safe_name



def download_audio_playlist(url: str) -> list:
    """
    Downloads the audio of all videos from a youtube playlist from a given url.
    
    Args:
        url (str): URL of the YouTube playlist.

    Returns:
        list: a list of Musica objects with all the downloaded audios.
    """
    try:
        playlist = Playlist(url)
        print(f"Baixando a playlist: {playlist.title}")
        
        # Cria um diretório para a playlist
        playlist_folder = safe_filename(playlist.title)
        if not os.path.exists(playlist_folder):
            os.makedirs(playlist_folder)

        print(f"Salvando os arquivos em: {os.path.abspath(playlist_folder)}")
        lista_musicas = []
        
        for url in playlist.video_urls:
            print("-" * 40)
            # Passa o caminho da pasta da playlist para a função de download
            print(playlist_folder)
            yt_temp = YouTube(url, on_progress_callback=on_progress)

            safe_title = download_audio_from_object(yt_temp, playlist_folder)
            lista_musicas.append( Musica( playlist_folder+"/"+safe_title+".m4a" , safe_title))

        print("\n✅ Playlist download completed.")
        return lista_musicas;
    except Exception as e:
        print(f"❌ Ocurred an error with the playlist {url}: {e} Insert link of playlist, not the video!")

def is_playlist(url: str) -> bool:
    """
    Checks if the video from an url is a single video or a playlist
    
    Args:
        url (str): the url of a youtube video or youtube playlist.
    
    Returns:
        True if the URL represents a playlist, False otherwise.
    
    Raises:
        Exception: if the video is unavaible. 
        Exception: if the link is not link from a youtube video or playlist.
    """
    try:
        p = Playlist(url)
        if len(p.video_urls) > 0:
            return True
        else:
            return False
    except Exception:
        return False

