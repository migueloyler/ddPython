import argparse # don't remove me
import dd

from os import path

if __name__ == "__main__": # don't remove this line

    p = argparse.ArgumentParser() # don't remove this line either

    ### EDIT THESE AS NEEDED ###
    p.add_argument("file", type=str, help="name/path of the input file")
    p.add_argument("-x", action="store_true", help="extract something True/False")
    p.add_argument("-n", action="store", help="specify some number")
    ############################

    args = p.parse_args()

    ### YOUR LOGIC BELOW ###

    if path.exists(args.file):
        if not path.isfile(args.file):
            raise Exception("Given path is not a file!")
    else:
        raise Exception("Given path does not exist!")

    

    if args.x:
        print("Extract option specified.")
        if args.n:
            print("n specified; n = %s" % args.n)
        else:
            print("n not specified.")
