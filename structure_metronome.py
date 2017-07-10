#!/usr/bin/env python

import time
import sys
import argparse

__author__ = "Franck Lejzerowicz"
__copyright__ = "Copyright 2017, mx3.ch/taverniers"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Franck Lejzerowicz"
__email__ = "frankwe@hotmail.fr"

def metronome():
    parser=argparse.ArgumentParser()
    parser.add_argument('-t', type = int, nargs = '?', default = 120, help="tempo")
    parser.add_argument('-n', type = int, nargs = '?', default = 4, help="number of taps before (default = 4)")
    parser.add_argument('-nt', type = float, nargs = '?', default = 1., help="tap duration (default = 1)")
    parser.add_argument('-l', action='store_true', default = False, help="show all measures numbers")
    parser.add_argument('-p', nargs = '*', required = True, help="numbers of repeats per part (either space-separated numbers of repeats [e.g. 4 4 12 8 4]; or also after '-'-separation for the duration factor of each part [4-1 4-2 12 8-1 4]; or also after '/'-separations for part name [e.g. 4-1/intro 4-2/A 12/B 8-1/chorus 4/outro])")
    parse=parser.parse_args()
    args=vars(parse)

    tempo = ((60000./args['t'])*4)/1000.
    l = args['l']
    taps = args['n']
    taptem = float(args['nt'])
    partsInput = args['p']

    parts = []
    repeatsFactors = []
    namesList = []

    for i in partsInput:
        if '-' in i and '/' in i:
            parts.append(int(i.split('-')[0]))
            repeatsFactors.append(float(i.split('-')[-1].split('/')[0]))
            namesList.append(i.split('/')[-1])
        elif '-' in i:
            parts.append(int(i.split('-')[0]))
            repeatsFactors.append(float(i.split('-')[-1]))
            namesList.append('')
        elif '/' in i:
            parts.append(int(i.split('/')[0]))
            repeatsFactors.append(1)
            namesList.append(i.split('/')[-1])
        else:
            parts.append(int(i))
            repeatsFactors.append(1)
            namesList.append('')

#    parts = [int(x.split('-')[0]) for x in partsInput]
#    print 'parts'
#    print parts
    R = [range(1,x+1) for x in parts]
#    repeatsFactors = [float(x.split('-')[1]) if '-' in x else 1. for x in partsInput]
#    names = [float(x.split('/')[1]) if '/' in x else 'No Name' for x in partsInput]
    if taps:
        R = [range(1,int(taps+1))] + R
        repeatsFactors = [taptem] + repeatsFactors
        namesList = ['Ready...'] + namesList
    tempos={}
    names={}
    repeats={}
    for idx,i in enumerate(repeatsFactors):
        tempos[idx] = tempo * i
        names[idx] = namesList[idx]
        repeats[idx] = repeatsFactors[idx]
    print 'Song structure:'
    for idx, i in enumerate(R):
        t = tempos[idx]
        n = names[idx]
        r = repeats[idx]
        if n == 'Ready...':
            continue
        else:
            if n:
                print '#%s: %s - %s times (measures: %s)' % (idx, n, len(i), r)
            else:
                print '#%s - %s times (measures: %s)' % (idx, len(i), r)
    start=raw_input('enter to start:')
    if l:
        for rdx, r in enumerate(R):
            t = tempos[rdx]
            n = names[rdx]
            print '#%s %s (%s)' % (rdx, n, len(r))
            for i in r:
                print i
                time.sleep(t)
        print 'END!'
    else:
        for rdx, r in enumerate(R):
            t = tempos[rdx]
            n = names[rdx]
            print '#%s %s (%s)' % (rdx, n, len(r))
            for i in r:
                print '\r', i,
                sys.stdout.flush()
                time.sleep(t)
            print
        print 'END!'

metronome()
