hang = 1
while hang <= 9:
    lie = 1
    while lie <= hang:
        print("%d * %d = %d" % (hang,lie,hang*lie), end="\t")
        lie += 1
    print("\n")
    hang += 1
