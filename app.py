import os 
import string

alphabet_string = string.ascii_lowercase
directory = list(alphabet_string)
parent_dir = "<folder path>"


for i in directory:
    path = os.path.join(parent_dir, i)
    os.mkdir(path)
    for j in directory:
        parentj=parent_dir+"\\"+i
        path=os.path.join(parentj, j)
        os.mkdir(path)
        for k in directory:
            parentk=parentj+"\\"+j
            path=os.path.join(parentk,k)
            os.mkdir(path)
            for l in directory:
                parentl=parentk+"\\"+k
                path=os.path.join(parentl,l)
                os.mkdir(path)
                for m in directory:
                    parentm=parentl+"\\"+l
                    path=os.path.join(parentm,m)
                    os.mkdir(path)
                    for n in directory:
                        parentn=parentm+"\\"+m
                        path=os.path.join(parentn,n)
                        os.mkdir(path)
                        for o in directory:
                            parento=parentn+"\\"+n
                            path=os.path.join(parento,o)
                            os.mkdir(path)
                            for p in directory:
                                parentp=parento+"\\"+o
                                path=os.path.join(parentp,p)
                                os.mkdir(path)
                                for q in directory:
                                    parentq=parentp+"\\"+p
                                    path=os.path.join(parentq,q)
                                    os.mkdir(path)
                                    for r in directory:
                                        parentr=parentq+"\\"+q
                                        path=os.path.join(parentr,r)
                                        os.mkdir(path)
                                        for s in directory:
                                            parents=parentr+"\\"+r
                                            path=os.path.join(parents,s)
                                            os.mkdir(path)
                                            for t in directory:
                                                parentt=parents+"\\"+s
                                                path=os.path.join(parentt,t)
                                                os.mkdir(path)
                                                
print("folder creation completed")
