"""Music tracks saved here."""

playlist = {
    "Green Day": {
        "American Idiot": {
            "Songs": ["American Idiot",
                      "Holiday / Boulevard of Broken Dreams",
                      "Give Me Novacaine / She's a Rebel",
                      "Wake Me up When September Ends"]
        },
    },
    "Metallica": {
        "Ride the Lightening": {
            "Songs": ["Fight Fire With Fire",
                      "For Whom The Bell Tolls",
                      "Fade To Black"]
        }
    },
    "U2": {
        "How to Dismantle an Atomic Bomb": {
            "Songs": ["Vertigo",
                      "City of Blinding Lights",
                      "One Step Closer"]
        },
        "Songs of Surrender": {
            "Songs": ["One",
                      "Stories for Boys",
                      "Pride (In the Name of Love)"]}}}

# ARTIST_NUM = 1
# for key in playlist:
#     print(f"{ARTIST_NUM} - {key}")
#     ARTIST_NUM += 1

# choice = int(input("Choose: "))

# artist_choice = list(playlist)[choice - 1]

# user_album = playlist[artist_choice]


# def selection(user_dict):
#     """function to display all keys within a dictionary,
#     allow a user to choose one then return the chosen dictionary."""
#     count = 1
#     for key in user_dict:
#         print(f"{count} - {key}")
#         count += 1

#     choice = int(input("Choose: "))

#     user_choice = list(user_dict)[choice - 1]

#     new_dict = user_dict[user_choice]

#     return new_dict


# new_user_dict = selection(playlist)

# new_user_dict = selection(new_user_dict)

# new_user_dict = selection(new_user_dict)

# print(new_user_dict)
# # ALBUM_NUM = 1
# # for key in user_album:
# #     print(f"{ALBUM_NUM} - {key}")
# #     ALBUM_NUM += 1

# # choice = int(input("Choose: "))

# # album_choice = list(user_album)[choice - 1]

# # user_songs = user_album[album_choice]

# SONG_NUM = 1
# for key in user_songs["Songs"]:
#     print(f"{SONG_NUM} - {key}")
#     SONG_NUM += 1
