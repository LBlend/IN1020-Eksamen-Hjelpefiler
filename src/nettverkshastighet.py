"""
Du ønsker å laste ned en fil på 200 megabyte, 
og den maksimale nedlastingshastigheten på din Internettforbindelse er 20 megabit per sekund. 
Hva er den teoretisk korteste overføringstiden?
"""


def antall_sekunder(filesize_MB, network_speed_Mb):
    filesize_Mb = filesize_MB * 8
    return int(filesize_Mb / network_speed_Mb)

print(antall_sekunder(200, 20))
