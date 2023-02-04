from os.path import exists

if not exists("list.txt"):
    err = True
    while err == True:
        getfrom = input("File to search in: ")
        if exists(getfrom):
            err = False
        else:
            if not getfrom.endswith(".txt"):
                print("path does not lead to a .txt file")
            else:
                print("file not found")

def getargs(file_):
    """gets the lines of the specified file without '\\n' and empty lines."""
    
    args = []
    with open(file_, 'r') as _file_:
        args = _file_.readlines()
        for a in range(len(args)):
            if args[a] == "\n":
                args -= args[a]
            elif "\n" in args[a]:
                args[a] = args[a][:-1]
    
    return args

def search(query, args):
    """
    Searches the list items that contain the query and returns them as a list.
    'query' is the query,
    'args' is the list to search in.
    """

    while query.startswith(" "): # removes starting spaces
        try:
            query = query[1:]
        except:
            query = ""
    while query.endswith(" "): # removes ending spaces
        query = query[:-1]
    
    results = []
    for count in range(len(args)): # search results
        if query.lower() in args[count].lower():
            results.append(args[count])

    return results

def printres(res):
    """
    Prints the results.
    'res' is the list of results.
    """
    if len(res) > 0:
        if len(res) == 1:
            print("Found 1 result:")
        else:
            print("Found ",len(res)," results:")

        for a in range(len(res)):
            print(str((a+1))+". "+res[a])
    else:
        print("No results found.")

while True:
    _in = input("\nQuery: ")
    res = search(_in, getargs(getfrom))
    printres(res)