import csv
import sys


music_library_file = "library.csv"
playlist_file = "playlist.csv"


def read_music_library():
    """"""
    with open(music_library_file, 'r') as file:
        reader = csv.DictReader(file)
        songs_list = []
        for row in reader:
            title = row['Title']
            artist = row['Artist']
            songs_list.append({'title': title, 'artist': artist})
    return songs_list


def read_playlist():
    """"""
    with open(playlist_file, 'r') as file:
        reader = csv.DictReader(file)
        playlist = []
        for row in reader:
            title = row['Title']
            artist = row['Artist']
            playlist.append({'title': title, 'artist': artist})
    return playlist


def write_playlist(playlist):
    with open(playlist_file, 'w') as file:
        fieldnames = ['Title', 'Artist']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for song in playlist:
            writer.writerow({'Title': song['title'], 'Artist': song['artist']})


def find_artist(library, playlist):
    """"""
    print("\n==============================================================="
          "===============================")
    print("Find Artist")
    print("\nYou You can enter a song name and it will return the artist")
    print("==============================================================="
          "===============================")
    while True:
        title = input("\nEnter the song title: ")
        found = False
        for song in library:
            if song['title'].lower() == title.lower():
                print(f"Artist: {song['artist']}")
                found = True
                break
        if not found:
            print("Song not found.\n")
            print("Please select an option:")
            print("1. Search again")
            print("2. Go to Main Menu")
            selection = input("\nEnter an option: ")
            if selection == "1":
                continue
            elif selection == "2":
                break
            else:
                print("Invalid option. Returning to main menu.")
                break
        else:
            print("\nPlease select an option:")
            print("1. Search again")
            print("2. Add song to playlist")
            print("3. Go to Main Menu")
            selection = input("\nEnter an option: ")
            if selection == "1":
                continue
            elif selection == "2":
                add_songs_direct(playlist, song['title'], song['artist'])
                break
            elif selection == "3":
                break
            else:
                print("Invalid option. Returning to main menu.")
                break


def find_songs():
    """"""
    pass


def add_songs_list():
    """"""
    pass


def add_songs_direct(playlist, title, artist):
    """"""
    playlist.append({'title': title, 'artist': artist})
    write_playlist(playlist)
    print(f"'{title}' by {artist} has been added to your playlist.\n")


def add_songs_manually(playlist):
    """"""
    title = input("\nEnter song name: ")
    artist = input("Enter artist's name: ")
    add_songs_direct(playlist, title, artist)


def delete_songs(playlist):
    """"""
    if not playlist:
        print("Your playlist is empty.")
        return
    else:
        print("\nYour Playlist:\n")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song['title']} by {song['artist']}")
        choice = int(input("\nSelect the number of the song to delete: "))
        if 1 <= choice <= len(playlist):
            confirmation = input(f"Are you sure you want to delete '{playlist[choice -1]['title']}' by '{playlist[choice -1]['artist']}' from your playlist? This action is not recoverable. Enter 'yes' to continue or 'no' to cancel: ").lower()
            if confirmation == 'yes':
                removed_song = playlist.pop(choice - 1)
                write_playlist(playlist)
                print(f"Removed '{removed_song['title']}' by '{removed_song['artist']}' from the playlist.")
                return
            else:
                print("Deletion canceled. You will return to the main menu.\n")
                return
        else:
            print("Invalid selection. You will return to the main menu\n")


def view_playlist(playlist):
    """"""
    print("==============================================================="
          "===============================")
    print("View Playlist")
    print("\nKeep track of your favorite songs")
    print("==============================================================="
          "===============================")
    if not playlist:
        print("\nYour playlist is empty.\n")
    else:
        print("\nYour Playlist:\n")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song['title']} by {song['artist']}")
    print("\n\nPlease select an option:")
    print("1. Go to main menu")
    print("2. Delete a song in your playlist")
    selection = input("\nEnter an option: ")
    if selection == "1":
        return
    elif selection == "2":
        delete_songs(playlist)
    else:
        print("Invalid option. Returning to main menu.\n")


def about():
    print("\nThis program was developed as simple way for users to search for")
    print("artists based on a song title, or look up songs from a certain")
    print("artist. This app also allows users to keep track of their favorite")
    print("songs.\n")
    print("Users can also look forward to future services.\n")


def main():
    """"""
    library = read_music_library()
    playlist = read_playlist()
    while True:
        print("==============================================================="
              "===============================")
        print("Music Application")
        print("\nYou can search for songs and artists and create playlists to"
              " keep track of your favorite songs.")
        print("==============================================================="
              "===============================")
        print("\n\nPlease select an option:")
        print("1. Find Artist")
        print("2. Find Songs")
        print("3. Add Songs to Playlist")
        print("4. View Playlist")
        print("5. About")
        print("9. Exit Program")

        selection = input("\nEnter an option: ")
        if selection == "1":
            find_artist(library, playlist)
        elif selection == "2":
            pass
        elif selection == "3":
            add_songs_manually(playlist)
        elif selection == "4":
            view_playlist(playlist)
        elif selection == "5":
            about()
        elif selection == "9":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
