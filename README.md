# structure_metronome
A visual metronome that might not show exact tick at each beat but helps playing complicated song structures without counting

Sometines a band has to play a song that has a very complicated structure and to learn it, it might be necessary to count, which pull band members out the feeling and makes mistakes more likely. This visual metronome will count for you. It might not tick perfectly accurate but it will be right there with you when you must change part as you play your complex song structure.

## usage
```
metronome.py [-h] [-t [T]] [-n [N]] [-nt [NT]] [-l] -p [P [P ...]]
```

## optional arguments

```
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
```


## Example

I have a song that has 7 parts, with different durations in terms of number measures. Sometimes (i) only the drummer counts the measures according to four 1/4 tempo beat of the metronome (= one real measure), while (ii) the phrase that the guitars players are doing span more than one measure (let's say 2 measures) and therefore should be counted according to a phrase of eight 1/4 beats. Let's have this structure with 7 parts, and their number of measures:
- *Intro*: 4 times [1 measure each]
- *Verse1*: 8 times [1 measure each]
- *Verse2*: 4 times [1 measure each]
- *Chorus*: 2 times [1 measure each]
- *Bridge*: 1 times [1 measure each]
- *Verse1*: 4 times [1 measure each]
- *Outro*: 2 times [1 measure each]

Running this command
```python2.7 metronome.py -t 150 -p 4/Intro 4/Verse1 8/Verse2 2/Chorus 1/Bridge 8/Verse1 4/Outro```
will display at 150 BPM the 4 ticks of *Intro*, 8 ticks for *Verse1*...

But if the 4 measures of *Verse1* are made of 8 itartions of a short, quickly played guitar riff, while the 2 measures *Chorus* is made of 2 phrases that in fact span over the duration of 4 measures, then the durations are:
- *Intro*: 4 times [1 measure each]
- *Verse1*: 8 times [**0.5** measure each]
- *Verse2*: 4 times [1 measure each]
- *Chorus*: 2 times [**2** measures each]
- *Bridge*: 1 times [1 measure each]
- *Verse1*: 4 times [1 measure each]
- *Outro*: 2 times [1 measure each]

It is possible to multiply the duration of the displayed "times" on the screen, as running
```python2.7 metronome.py -t 150 -p 4/Intro 8**-0.5**/Verse1 4/Verse2 2**-2**/Chorus 1/Bridge 4/Verse1 4/Outro```
will display at 150 BPM the 4 ticks of *Intro* and then the 8 ticks for *Verse1* but twice faster than the previous 4 ticks, and the 2 ticks of *Chorus* twice slower than these *Intro* ticks

TIP: don't hesitate to increase the terminal font size so everyone can see :D 

## Dependency
python2.7
