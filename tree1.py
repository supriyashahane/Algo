string = "a_b a_c c_d a_e"
def immediate_children(tree,node):
    w = string.replace('_',' ',4).split(' ')
    d = len(w)
    for i in range (d):
        if word in w[i]:
            print w[i+1],

def all_child(tree,node):
    w = string.replace('_',' ',4).split(' ')
    d = len(w)
    arry = []
    arry1 = []
    if True:
        for i in range (d):
            if word in w[i]:
                print w[i+1],
            if w[i+1] in w:
                if w[i+3] == word or w[i+2]== word or w[i+1] == word:
                    continue
                arry =  w[i+3],
                wid1 = len(arry)
                print w[i+3],
def ispost_child(tree,word,chil):

    w = string.replace('_',' ',4).split(' ')
    d = len(w)
    arry = []
    arry1 = []
    if True:
        for i in range (d):
            if word in w[i]:
                print w[i+1],
            if w[i+1] in w:
                if w[i+3] == word or w[i+2]== word or w[i+1] == word:
                    continue
                arry =  w[i+3],
                wid1 = len(arry)
                print w[i+3],
                if chil in w[i+3]:
                    print "is post child of",word,
    
def all_child(tree,node):
    w = string.replace('_',' ',4).split(' ')
    d = len(w)
    arry = []
    arry1 = []
    if True:
        for i in range (d):
            if word in w[i]:
                print w[i+1],
            if w[i+1] in w:
                if w[i+3] == word or w[i+2]== word or w[i+1] == word:
                    continue
                arry =  w[i+3],
                wid1 = len(arry)
                print w[i+3],
print string
word = raw_input()
#print type(word)
#print type(stringi)

print "immediate children of",word,"=",
wrd = immediate_children(string,word)
print "all childern of",word,"=",
wrd1= all_child(string,word)
chil = raw_input()
print chil,"ispost_child of",word,"="
wrd2 = ispostchild(string,word,chil)
