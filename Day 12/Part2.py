from os import pardir, path
import graph


def main():
    part1 = TreatInput()
    print(part1)

def TreatInput():
    vertices = []
    paths = []
    rawInput = open("input")
    
    for line in rawInput:
        paths.append(line.strip())
        for word in line.strip().split("-"):
            if word not in vertices:
                vertices.append(word)
    mygraph = graph.Graph(len(vertices))

    for path in paths:
        start, end = path.split("-")
        mygraph.addEdge(start, end)
        if start != "start" and end != "end":
            mygraph.addEdge(end, start)
    
    paths = mygraph.printAllPaths("start", "end", vertices)
    part1 = len(paths)
    return part1

if __name__ == "__main__":
    main()