#!/usr/bin/env python

# TODO:
# - [DONE] Implement saving results to a .txt file --save/f
# - [DONE] Possibly implement a custom file format --save/-f FILENAME.EXTENSION (.reslt file)
# - [DONE] Implement verbosity --verbose/-v
# - [PDONE] Hopefully not break the program
# - Generate a calculation and combine argument flags --example/-e and --verbose/-v
# - [DONE] Interaction Mode (extra) 
# - Implement verbosity with file saving
# - [DONE] Implement --clean/-c to delete result files that were made by the program [Finish when implement custom file extension]

import argparse
import sys
import os

def tax(subtotal, percentage):
    totalt = float(subtotal) * (float(percentage) / 100)
    total = float(subtotal) + float(totalt)
    return round(total, 2)

parser = argparse.ArgumentParser(
    description='tax calculator'
)

parser.add_argument(
    '--subtotal', '-s',
    help='total before taxes'
)

parser.add_argument(
    '--percentage','-p',
    help='percentage of state sales tax'
)

parser.add_argument(
    '--save', '-f',
    help='log to file',
    metavar='FILE.RESLT'
)

parser.add_argument(
    '--clean', '-c',
    help='remove .reslt files created by the program',
    action='store_true'
)

parser.add_argument(
    '--interactive', '-i',
    help='throws user into an interactive prompt (emulated prompt)',
    action='store_true'
)

parser.add_argument(
    '--verbose', '-v',
    help='spits the calculation into stdout',
    action='store_true'
)

args = parser.parse_args()

def usage_example():
    parser.print_help()
    print("\nexample usage: {} --subtotal/-s 0.99 --percentage/-s 5.9 <- [AZ Sales Tax]".format(sys.argv[0]))
    print("result: {} ".format(tax(0.99, 5.9)))

def verbose():
    print("${} subtotal".format(args.subtotal))
    print("{}% tax".format(args.percentage))
    print("total = {}".format(tax(args.subtotal, args.percentage)))

def fileVerbose():
    fdata = open(args.save, "w")
    fdata.write("${} subtotal\n".format(args.subtotal))
    fdata.write("{}% tax\n".format(args.percentage))
    fdata.write("total = {}\n".format(tax(args.subtotal, args.percentage)))
    fdata.close()

def interactive_usage():
    print("interactive > [COMMAND]\n")
    print("commands: \n")
    print("     help        displays usage")
    print("     txc         tax calculator")
    print("     clear       clears the screen")
    print("     exit        exits interactive mode\n")

if args.subtotal and args.percentage:
    if args.save:
        if args.verbose:
            if args.save.endswith('.reslt'):
                if not os.path.isfile(args.save):
                    fileVerbose()
                    print("saved to {} with --verbose/-v".format(args.save))
                else:
                    fileVerbose()
                    print("overwritten {} with --verbose/v".format(args.save))
            else:
                print("invalid extension, accepted extension(s) [.reslt]")
        else:
            if args.save.endswith('.reslt'):
                if not os.path.isfile(args.save):
                    fdata = open(args.save, "w")
                    fdata.write("total = {}".format(tax(args.subtotal, args.percentage)))
                    fdata.close()
                    print("saved to", args.save)
                else:
                    fdata = open(args.save, "w")
                    fdata.write("total = {}".format(tax(args.subtotal, args.percentage)))
                    fdata.close()
                    print("overwritten", args.save)
            else:
                print("invalid extension, accepted extension(s) [.reslt]")    

    elif args.verbose:
        verbose()

    else:
        total = tax(args.subtotal, args.percentage)
        print(total)

elif args.subtotal and args.percentage is None:
    print("--subtotal/-s requires --percentage/-p to calculate the total after taxes")

elif args.subtotal is None and args.percentage:
    print("--percentage/-p requires --subtotal/-s to apply percentage to the subtotal")

else:
    if args.clean:
        for File in os.listdir('.'):
            if File.endswith('.reslt'):
                os.system('rm *.reslt')
                print('data was removed')
                break
        else:
            print('there is nothing to clean')

    elif args.interactive:
        while True:
            prompt = input("interactive > ")
            if prompt in ("help"):
                interactive_usage()

            elif prompt in ("exit"):
                break

            elif prompt in ("clear"):
                os.system("clear")

            elif prompt in ("txc"):
                subtotal_i = float(input("subtotal: "))
                percentage_i = float(input("percentage: "))

                total_i = tax(subtotal_i, percentage_i)
                print(total_i)
            else:
                print("invalid command")
    else:
        usage_example()