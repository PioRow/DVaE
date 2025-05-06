import os


def fig_to_tex(path,o="out2.txt"):
    base = """ \\begin{{frame}}{{}}
            \\begin{{figure}}
                    \includegraphics[width=1\linewidth]{{{val}}}
            \\end{{figure}}
            \\end{{frame}}
            """
    with open(o, "w") as op:
        for f in os.listdir(path):
            if str(f).find("png") >= 0:
                print("generating {}".format(f))
                op.write(base.format(val=(path + "/" + f)))



def figure_to_tex(path,ds,o="out.txt"):
    base=""" \\begin{{frame}}{{}}
        \\begin{{figure}}
                \includegraphics[width=1\linewidth]{{{val}}}
        \\end{{figure}}
        \\end{{frame}}
        """
    base_list="""
    \\begin{{frame}}{{}}
    \\begin{{enumerate}}
    {val}
    \\end{{enumerate}}
    \\end{{frame}}
    """
    with open(o,"a") as o:
            o.write("\\subsection{{{ds}}}\n".format(ds=ds))
            o.write(base.format(val=(path+"/"+ds+".png")))
            for f in os.listdir(path):
                if str(f).find(ds)>=0 and str(f).find("txt")>=0:
                    with open(path+"/"+f,"r") as f2:
                        lines=f2.readlines()
                        res=""
                        for l in lines:
                            res+="\\item "+l+" \n"
                        res=res.replace("_"," ")
                        print(res)
                        o.write(base_list.format(val=res))
                if str(f).find(ds)>=0 and str(f)!=ds+".png" and str(f).find("txt")<0:
                    print("generating {}".format(f))
                    o.write(base.format(val=(path+"/"+f)))

print(os.listdir("clusters"))