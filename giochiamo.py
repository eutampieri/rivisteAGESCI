import common

inizio = int(input("Anno di inizio: "))
fine = int(input("Anno di fine: "))
for (anno, links) in common.get_links("wpfb-cat-119").items():
    if anno >= inizio and anno <= fine:
        for link in links:
            common.download_file(link[0], link[1]+".pdf")
