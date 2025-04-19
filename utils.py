import dataGenerator
import os
def direct_build_20(n=1000):
    return (dataGenerator.dataGenerator(n)
            .generate_relevant(0, 3, 1, 1, 5)
            .generate_irrelevant(1, 5)
            .generate_correlated(5)
            .generate_redundant(5)
            .build())
def direct_build_40(n=1000):
    return (dataGenerator.dataGenerator(n)
            .generate_relevant(0, 3, 1, 1, 10)
            .generate_irrelevant(1.5, 10)
            .generate_correlated(10)
            .generate_redundant(10)
            .build())
def direct_build_32(n=1000):
        return (dataGenerator.dataGenerator(n)
                .generate_relevant(0, 3, 1, 1, 8)
                .generate_irrelevant(1.5, 8)
                .generate_correlated(8)
                .generate_redundant(8)
                .build())

def generate_frames(path,out="out.txt"):
        base=""" \\begin{{frame}}{{}}
        \\begin{{figure}}
                \includegraphics[width=1\linewidth]{{{val}}}
        \\end{{figure}}
        \\end{{frame}}
        """
        with open(out,"w") as o:
                for f in os.listdir(path):
                        print("generating {}".format(f))
                        o.write(base.format(val=(path+"/"+f)))

