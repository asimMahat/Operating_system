#function that find the least recently used pages
def findLRU(time,n):
    minimum=time[0]
    pos=0

    for i in range(n):
        #i=i+1
        if (time[i]<minimum):
            minimum = time [i]
            pos=i
    return pos
#this function asks for the refrence string that needs computaion
def askForReferenceString(no_of_pages):
    pages= []
    # ---------------------------
    for i in range(no_of_pages):
    #    i=i+1
        pages.append(int(input("Enter reference string: ")))
    # ---------------------------
    return pages
#we take user input like frames and pages in main func
def main():
    #initializing required variables
    no_of_frames= 0
    no_of_pages  = 0
    frames = []
    pages = []
    counter  = 0
    time = []
    flag1 = 0
    flag2 = 0
    i = 0
    j = 0
    pos = 0
    faults=0

    no_of_frames = int(input("Enter the number of frames:"))
    no_of_pages = int(input("Enter number of pages:"))
    print()

    pages= askForReferenceString(no_of_pages)

    for i in range(no_of_frames):
    #    i=i+1
        frames.append(-1)

    # ---------------------------

    for i in range(no_of_pages):
    #    i=i+1
        flag1 = 0
        flag2 = 0

        for j in range(no_of_frames):
            # j=j+1
            if(frames[j] == pages[i]):
                counter= counter +1
                time.append(counter)
                flag1 = 1
                flag2 = 1
                break

        if(flag1 == 0):
            for j in range(no_of_frames):
             #   j=j+1
                if(frames[j] == -1):
                    counter=counter +1
                    faults=faults+1
                    frames[j] = pages[i]
                    time.insert(j,counter)
                    flag2 = 1
                    break

        if(flag2 == 0):
            pos = findLRU(time, no_of_frames)
            counter=counter+1
            faults=faults+1
            frames[pos] = pages[i]
            time[pos] = counter

        print("  ")

        for j in range(no_of_frames):
#            j=j+1
            print(f"{frames[j]}\t", )

    print(f"\n\nTotal Page Faults = {faults}", );


if __name__ == "__main__":
    main() #running the main function
    
