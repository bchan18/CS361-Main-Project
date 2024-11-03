import csv
import sys


music_library_file = "library.csv"
playlist_file = "playlist.csv"


def load_music_library():
    """"""
    with open(music_library_file, 'r') as file:
        reader = csv.DictReader(file)
        songs_list = []
        for row in reader:
            title = row['Title']
            artist = row['Artist']
            songs_list.append({'title': title, 'artist': artist})
    return songs_list


def load_playlist():
    """"""
    with open(playlist_file, 'r') as file:
        reader = csv.DictReader(file)
        playlist = []
        for row in reader:
            title = row['Title']
            artist = row['Artist']
            playlist.append({'title': title, 'artist': artist})
    return playlist


def find_artist(library):
    print("\n==============================================================="
          "===============================")
    print("Find Artist")
    print("\nYou You can enter a song name and it will return the artist")
    print("==============================================================="
          "===============================")
    title = input("\nEnter the song title: ")
    found = False
    for song in library:
        if song['title'].lower() == title.lower():
            print(f"Artist: {song['artist']}")
            found = True
            break
    if not found:
        print("Song not found.\n")


def find_songs():
    pass


def add_songs():
    pass


def view_playlist(playlist):
    """"""
    if not playlist:
        print("\nYour playlist is empty.\n")
    else:
        print("\nYour Playlist:")
        for idx, song in enumerate(playlist, 1):
            print(f"{idx}. {song['title']} by {song['artist']}")
        print("\n")


def main():
    """"""
    library = load_music_library()
    playlist = load_playlist()
    while True:
        print("==============================================================="
              "===============================")
        print("Music Application")
        print("\nYou can search for songs and artists and create playlists to"
              " keep track of your favorite songs")
        print("==============================================================="
              "===============================")
        print("\n\nPlease select an option:")
        print("1. Find Artist")
        print("2. Find Songs")
        print("3. Add Songs to Playlist")
        print("4. View Playlist")
        print("9. Exit Program")

        selection = input("\nEnter an option: ")
        if selection == "1":
            find_artist(library)
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "4":
            view_playlist(playlist)
        elif selection == "9":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
