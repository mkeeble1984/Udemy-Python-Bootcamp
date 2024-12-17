import os
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


for num, key in enumerate(playlist, 1):
    print(f"{num} - {key}")

choice = int(
    input("\nWhat would you like to listen to today? (ENTER ARTIST NUMBER): "))
key, value = list(playlist.items())[choice - 1]

print(key, value)
