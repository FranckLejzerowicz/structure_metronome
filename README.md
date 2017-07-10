# structure_metronome
A visual metronome that might not show exact tick at each beat but helps playing complicated song structures without counting


## usage
´´´
metronome.py [-h] [-t [T]] [-n [N]] [-nt [NT]] [-l] -p [P [P ...]]
´´´

## optional arguments

´´´
  -h, --help      show help message and exit
  -t [T]          tempo
  -n [N]          number of taps before (default = 4)
  -nt [NT]        tap duration (default = 1)
  -l              show all measures numbers
  -p [P [P ...]]  numbers of repeats per part (either space-separated numbers
                  of repeats [e.g. 4 4 12 8 4]; or also after '-'-separation
                  for the duration factor of each part [4-1 4-2 12 8-1 4]; or
                  also after '/'-separations for part name [e.g. 4-1/intro
                  4-2/A 12/B 8-1/chorus 4/outro])
´´´

## Example

