from pydub import AudioSegment




def make_nightcore(input_file: str, output_file: str, speed: float = 1.25):
    """
    Creates the Nightcore version of a song
    input_file: path to the audio file (m4a )
    output_file: output file name (mp3 )
    speed: speed factor (1.25 = 25% faster)
    """
    # Load Music
    song = AudioSegment.from_file(input_file)

    # Acelerar mudando o frame_rate
    new_song = song._spawn(song.raw_data, overrides={
        "frame_rate": int(song.frame_rate * speed)
    })

    # Voltar frame_rate original (mantém compatibilidade)
    new_song = new_song.set_frame_rate(song.frame_rate)

    # Exportar arquivo
    new_song.export(output_file, format="mp3")
    print(f"Nightcore salvo em: {output_file}")

# Exemplo de uso
#make_nightcore("Devil May Cry 3 - Taste the Blood.m4a", "musica_nightcore.mp3", speed=1.3)
