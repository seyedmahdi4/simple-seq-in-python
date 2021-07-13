import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a1",type=int,nargs='?',action='store')
parser.add_argument('a2', type=int, nargs='?',action='store')
parser.add_argument("a3",type=int,nargs='?',action='store')
parser.add_argument("-f",type=str,action='store',required=False)
parser.add_argument("-s",type=str,nargs='?',action='store',const=' ')
parser.add_argument("-w",action='store_true')
args = parser.parse_args()

first , last , step  = 1,0,1
s = args.s
w = args.w
f = args.f

if not f: f=''
if not s: s='\n'

if args.a3:
    last = args.a3
    step = args.a2
    first = args.a1
elif args.a2:
    last = args.a2
    first = args.a1
elif args.a1:
    last = args.a1
else:
    print("error")

if w: w = len(str(last))

def seq(first,last,step,s,w):
    for i in range(first,last+1,step):
        print(f + str(i).zfill(w),end=s)

seq(first,last,step,s,w)