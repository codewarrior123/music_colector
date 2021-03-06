

def find_all_albums(file_name):
    all_albums = []
    with open(file_name, "r") as file:
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            all_albums.append(all_info[1])
        return "\n".join(all_albums)


def find_albums_by_genre(file_name, genre):
    genres_dictionary = {}
    albums = []
    with open(file_name, "r") as file:
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            genres_dictionary[all_info[1]] = all_info[3]
        for key, value in genres_dictionary.items():
            if value == genre:
                albums.append(key)
        return "\n".join(albums)


def find_albums_by_time_range(file_name, year1, year2):
    albums_dictionary = {}
    albums = []
    with open(file_name, "r") as file:
        for line in file:
            all_info = line.strip()
            all_info = all_info.split(",")
            albums_dictionary[all_info[1]] = int(all_info[2])
        for key, value in albums_dictionary.items():
            if value >= year1 and value <= year2:
                albums.append(key)
        return "\n".join(albums)


def find_shortest_longest_album(file_name, parameter):
    with open(file_name, "r") as file:
        albums = []
        for line in file:
            all_info = line.strip()
            all_info = all_info.replace(":", ".")
            all_info = all_info.split(",")
            albums.append((float(all_info[4]), all_info[1]))
            range_of_sort = 1
        if parameter == "shortest":
            albums = sorted(albums)
            top_shortest = []
            for index in range(3):
                top_shortest.append(albums[index][range_of_sort])
            return top_shortest
        if parameter == "longest":
            albums = sorted(albums, reverse=True)
            top_longest = []
            for index in range(3):
                top_longest.append(albums[index][range_of_sort])
            return top_longest


def find_albums_by_artist(file_name, artist):
    with open(file_name, "r") as file:
        albums_dictionary = {}
        albums = []
        for line in file:
            all_info = line.strip()
            all_info = all_info.replace(":", ".")
            all_info = all_info.split(",")
            albums_dictionary[all_info[1]] = all_info[0]
        for key, value in albums_dictionary.items():
            if value == artist:
                albums.append(key)
        return "\n".join(albums)
