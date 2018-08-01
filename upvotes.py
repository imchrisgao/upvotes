class window:
    def __init__(self, sli):
        self.window = tuple(sli)
#*************************************
def upvotes(n, k, *args):
    if len(args) != n:
        print("# of days of upvotes != n")
        return
    
    days = list(args)
    windows = []
    for index in range(len(days)-k+1):
        windows.append(tuple(days[index:index+k]))
    print('Windows: '), 
    print(windows)

    
    for window in windows:
        subranges = []
        #Build subranges first
        for i in range(len(window)-1): #iterate through window from beginning until second to last element
            for end in range(i+2, len(window)+1): #range is awkward because 'end' is not inclusive
                subranges.append(window[i:end])
        print('subranges: ' ), 
        print(subranges)
        
        nondec = 0
        noninc = 0
        for subrange in subranges:
            decrease = True
            increase = True
            for index in range(len(subrange)-1): #iterate until second to last element
                if subrange[index] < subrange[index+1]:
                    decrease = False
                if subrange[index] > subrange[index+1]:
                    increase = False
            if decrease is True:
                noninc-=1
            if increase is True:
                nondec+=1
        print(nondec + noninc)
#--------------------------------------
def main():
    upvotes(5, 4, 1,2,3,1,1)

if __name__ == "__main__":
    main()