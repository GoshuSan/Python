mat=[[0,1,0,0,0],[1,0,1,1,0],[0,0,0,1,0],[1,1,1,0,0],[0,1,1,0,1]]
node=-1
for k in mat:
    node+=1
    count=0
    near=[]
    for j in k:
        if(j==1):
            near.append(count)
        count+=1
    print("node " + str(node) + " is linked with" + str(near))