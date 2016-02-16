M=10*9*8*7
N=4
T=10000
P=13
#_resultTable=[[0 for j in range(M)] for i in range(M)]#it's a table of answers between every two numbers
#_arrange=[[0 for j in range(N)]for i in range(M)]
_number=set()
resultToIndex=dict()
indexToResult=dict()

class Node:
    def __init__(self, parent=None, d=0):
        self.childList=[]
        self.cand_list=set()
        global _progress
        if parent == None:
            self.cand_count=M
            #self.index=0
            self.step=1
            self.end=False
            self.val=123
            print ('0'+str(self.val) if self.val<1000 else str(self.val)) +"      step: "+str(self.step)
            for i in _number:#5040
                self.cand_list.add(i)
            self.cand_list.remove(123)
            for i in range(P):
                self.childList.append(Node(self,i))

        else:
            self.result=indexToResult[d]#result is as 4A0B
            self.cand_count=0
            self.step=parent.step+1

            ''' to fill with all the candidates '''
            for candidate in parent.cand_list:
                if estimate(candidate,parent.val)==self.result:
                    self.cand_list.add(candidate)
            for delete in self.cand_list:
                parent.cand_list.remove(delete)

            if len(self.cand_list)>1:
                self.val=self.cand_list.pop()# If you want to get a better result, you should consider more at here, make more loops
                for i in range(P):
                    self.childList.append(Node(self,i))
                self.end=False
            elif len(self.cand_list)==1:
                self.val=self.cand_list.pop()
                self.end=True
                ''' each Node complete will print '''
                print ('0'+str(self.val) if self.val<1000 else str(self.val)) +"      step: "+str(self.step)
            else:#if there isn't any candidates satisfy, this node will be empty
                self.val=0
                self.end=True
    


def estimate(answer, guess):#return a string for example 2A2B
    a=0
    b=0
    temp1=answer
    temp2=guess
    for i in range(N):
        t1=temp1%10
        t2=temp2%10
        if t1==t2:
            a+=1
        else:
            temp3=guess
            for j in range(N):
                t2=temp3%10
                if t1==t2:
                    b+=1
                    break
                temp3/=10
        temp1/=10
        temp2/=10
    #return a*10+b
    return str(a)+'A'+str(b)+'B'

'''initial all the number(from 0123 to 9876) and index(from 0 to 5039)'''
'''initial both indexToResult and resultToIndex'''
def init():
    num=123#the first number
    for i in range(M): 
        while not checkNumber(num):# check if the num has repeated digits
            num+=1
        _number.add(num)
        num+=1
    resultToIndex["0A0B"]=0
    resultToIndex["0A1B"]=1
    resultToIndex["0A2B"]=2
    resultToIndex["0A3B"]=3
    resultToIndex["0A4B"]=4
    resultToIndex["1A0B"]=5
    resultToIndex["1A1B"]=6
    resultToIndex["1A2B"]=7
    resultToIndex["1A3B"]=8
    resultToIndex["2A0B"]=9
    resultToIndex["2A1B"]=10
    resultToIndex["2A2B"]=11
    resultToIndex["3A0B"]=12
    resultToIndex["4A0B"]=13
    for result in resultToIndex:
        indexToResult[resultToIndex[result]]=result


def guessNode(root):# interact with player
    ''' need to think again about the situation of over range'''
    print "guess",root.step,":",'0'+str(root.val) if root.val<1000 else root.val
    while True:
        a=raw_input( "Please input result in form of *A*B(q to quit): ")
        if a=='q':
            return
        elif a in resultToIndex:
            break
        else:
            print "Wrong input!"
    if a=="4A0B":
        print "Fininsh!"
        print "Total steps:", root.step
    elif root.end==True:
        print "Can not find the answer! Your results are wrong."
    else:
        nextNode=root.childList[resultToIndex[a]]
        if nextNode.end==True:
            print "Can not find the answer! Your results are wrong."
        else:
            guessNode(nextNode)


def searchNode(root, answer):# return the number of steps you need to find this answer
    ''' print each step to find the answer '''
    print "guess",root.step,":",'0'+str(root.val) if root.val<1000 else root.val,"=>",
    if root.val==answer:
        print "4A0B"
        return root.step
    else:
        #result=judge(answer, root.val)
        result=estimate(answer,root.val)
        print result
        index=resultToIndex[result]
        return searchNode(root.childList[index],answer)

''' check if the input is the right number '''
def checkNumber(a):# non-repeated 4 digits, need to be improved
    #if a>9999 or a<0: return False
    #if type(a)!=int: return False
    '''check for repeated'''
    List=[]
    for i in range(N):
        List.append(a%10)
        a/=10
    for i in range(N):
        for j in range(i+1,N):
            if List[i]==List[j]:
                return False
    return True

def main():
    init()
    root=Node()
    totalStep=0
    steps=[0]*10

    for i in _number:# check all the number from 0123 to 9876, return the step each number need
        step=searchNode(root,i)
        totalStep+=step
        steps[step]+=1
    print "\n\n\nHow many nodes each step"
    for i in range(1,10):
        print i,"=>",steps[i],"node(s)"
    print "average:",1.0*totalStep/M
    print "\n\nLet's begin Master Mind now!"
    quit=False
    while not quit:
        a=raw_input("What do you want to play, 1 for standard play, 2 for interesting play, else to quit: ")
        if a=='1':
            while True:
                b=raw_input("Please input a number, then I will show all the steps I guess, input q to quit: ")
                if b=='q':
                    quit=True
                    break
                elif b.isdigit():
                    if int(b) in _number:
                        searchNode(root,int(b))
                        continue
                print "I don't recognise what you input, please input again"
        elif a=='2':
            while True:
                guessNode(root)
                c=raw_input("Do you want to play again? Input y for yes, else to quit: ")
                if c!='y': 
                    quit=True
                    break
        else:
            quit=True
main()











