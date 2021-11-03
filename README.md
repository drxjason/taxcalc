# wtf is this?!?!?

meh its just a program that i made to solve problems. read below if u actually care :D
**btw this readme is unfinished and the program is under development so im pushing this now *november 3rd @ 4:52am* cuz im tired**

## taxcalc.py a simple calculator that calculates taxes (specifically if u were to buy shit) :)

### how to use it

so like execute it with -h for the usage

```console
$ ./taxcalc.py -h
usage: taxcalc.py [-h] [--subtotal SUBTOTAL] [--percentage PERCENTAGE] [--save FILE.RESLT] [--clean] [--interactive] [--verbose]

tax calculator

optional arguments:
  -h, --help            show this help message and exit
  --subtotal SUBTOTAL, -s SUBTOTAL
                        total before taxes
  --percentage PERCENTAGE, -p PERCENTAGE
                        percentage of state sales tax
  --save FILE.RESLT, -f FILE.RESLT
                        log to file
  --clean, -c           remove .reslt files created by the program
  --interactive, -i     interact with the program by inputting values and getting real-time results
  --verbose, -v         spits the calculation into stdout
```

## example usage

```console
$ ./taxcalc.py -s 5.99 -p 6.3
6.37
```

### with verbosity

```console
$ ./taxcalc.py -v -s 5.99 -p 6.3
5.99 subtotal
6.3% tax
total = 6.37
```

### save the result to a file

```console
$ ./taxcalc.py -s 5.99 -p 6.3 -f file.reslt
saved to file.reslt
```
^ creates the file *file.reslt* in the current directory **can save to a specified directory**
uses custom .reslt file cuz why tf not and it sounds like *result* :|

**in file.reslt:**
```
total = 6.37
```

### save with verbosity

```console
$ ./taxcalc.py -v -s 5.99 -p 6.3 -f file.reslt
saved to file.reslt with --verbose/-v
```

**in file.reslt**

```
$5.99 subtotal
6.3% tax
total = 6.37
```
u can also view the example files in the **examples** folder