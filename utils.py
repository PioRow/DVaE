import dataGenerator
def direct_build_20(n=1000):
    return (dataGenerator.dataGenerator(n)
            .generate_relevant(0, 3, 1, 1, 5)
            .generate_irrelevant(1, 5)
            .generate_correlated(5)
            .generate_redundant(5)
            .build())
def direct_build_200(n=1000):
    return (dataGenerator.dataGenerator(n)
            .generate_relevant(0, 3, 1, 1, 50)
            .generate_irrelevant(1.5, 50)
            .generate_correlated(50)
            .generate_redundant(50)
            .build())