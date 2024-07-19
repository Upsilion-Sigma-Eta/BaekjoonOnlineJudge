import sys

def actual_code():
    FF, FS, SF, SS = map(int, sys.stdin.readline().strip().split())

    max_music_count = 0
    music_album_string = ""
    while True:
        if (max_music_count == 0) and (FF > 0 or FS > 0):
            if FF > 0:
                music_album_string += "FF"
                FF -= 1
                max_music_count += 1
                continue
            else:
                music_album_string += "FS"
                FS -= 1
                max_music_count += 1
                continue
        else:
            if (max_music_count == 0) and (FF == 0 and FS == 0):
                if (SF > 0 or SS > 0):
                    if SS > 0:
                        music_album_string += "SS"
                        SS -= 1
                        max_music_count += 1
                        continue
                    else:
                        music_album_string += "SF"
                        SF -= 1
                        max_music_count += 1
                        continue
            else:
                if (music_album_string[-1] == "F"):
                    if (FF > 0):
                        music_album_string += "FF"
                        FF -= 1
                        max_music_count += 1
                        continue
                    if (FS > 0 and FS > FF):
                        music_album_string += "FS"
                        FS -= 1
                        max_music_count += 1
                        continue
                elif (music_album_string[-1] == "S"):
                    if (SS > 0):
                        music_album_string += "SS"
                        SS -= 1
                        max_music_count += 1
                        continue
                    if (SF > 0 and SF > SS):
                        music_album_string += "SF"
                        SF -= 1
                        max_music_count += 1
                        continue

            break

    sys.stdout.write(str(max_music_count) + "\n")

if __name__ == '__main__':
    actual_code()
