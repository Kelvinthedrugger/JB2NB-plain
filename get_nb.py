#eg = "http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/unique_chars/unique_chars_challenge.ipynb"

#ref = "github"

#print(eg.index(ref)): 28

#TODO
# make this (url converter) a github host webapp
#  simple html + js would do the job
#  so that i don't have to run it from cmd and copy every time

def get_url(*args):
    # args: a tuple, shxt
    # this is the right way
    # for ele in args[0]:
    #  idx = ele.index("github"); a + ele[idx:]
    idx = 28
    a = "https://colab.research.google.com/"
    return [a + ele[idx:] for ele in args[0]]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("python get_nb.py url_of_github_nb")
    else:
        ret = get_url(sys.argv[1:])
        for ele in ret:
            print("\n%s" % ele)


