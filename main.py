import subprocess
import os


def download_video(url, output_path='Videos'):
    try:
        print(f"Obteniendo Video desde {url}")
        os.makedirs(output_path, exist_ok=True)

        command = [
            'yt-dlp',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            url
        ]
        subprocess.run(command, check=True)
        print('Descarga exitosa!')
    except subprocess.CalledProcessError:
        print('Error, verificar la url')
    except Exception as e:
        print(f"Ocurrio un error durante la descarga: {e}")


def download_playlist(url, output_path='Playlist'):
    try:
        print(f"Empezando descar de playlist: {url}")
        output_template = os.path.join(
            output_path, '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s')

        command = [
            'yt-dlp',
            '-o', output_template,
            '--yes-playlist',
            url
        ]

        subprocess.run(command, check=True)

        print('\n Playlist descargada')
    except subprocess.CalledProcessError:
        print('Error: Descarga fallida')
    except Exception as e:
        print(f"Error con la url de la Playlist: {e}")


def main():
    print('Youtube Downloader')

    while True:
        mode = input(
            "\nDo you want to download a (1) single video or a (2) playlist? (Enter 1 or 2, or 'q' to quit): ")

        if mode.lower() == 'q':  # Exit if user enters 'q'
            print("Goodbye! 👋")
            break
        elif mode == '1':  # If downloading a video
            video_url = input("Enter the YouTube video URL: ")
            download_video(video_url)
        elif mode == '2':  # If downloading a playlist
            playlist_url = input("Enter the YouTube playlist URL: ")
            download_playlist(playlist_url)
        else:  # If wrong option selected
            print("That's not a valid option. Please try again.")


if __name__ == "__main__":
    main()
