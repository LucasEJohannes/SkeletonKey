import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.patheffects as pe
import base64
from io import BytesIO
import webbrowser

#Sets up the figure, plot, and gridlines
fig, ax = plt.subplots()
fig.set_figheight(4.5)
fig.set_figwidth(75)
y_ticks = [0,1,2,3,4,5,6,7]
y_labels = ["","E","A","D","G","B","e",""]
x_ticks = [0,36.482,70.916,103.417,134.095,163.05,190.381,216.177,240.526,263.508,285.2,305.674,325,343.241,360.458,376.709,392.047,406.525,420.192,433.091,445.265,456.756,467.602,477.839,487.502]
x_labels = ["Open",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
ax.set_xticks(ticks=x_ticks,labels=x_labels)
ax.set_yticks(ticks=y_ticks,labels=y_labels)
ax.set_xlim(0,487.502)
ax.set_ylim(.5,6.5)
ax.grid(c='black')
tfont = {'fontname':'DejaVu Sans',
          'weight':'bold',
          'size':40}
afont = {'fontname':'DejaVu Sans',
         'weight':'bold',
         'size':11,
         }
ax.set_title('Skeleton Key',**tfont)


#Data for creating scales and patterns
notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
strings = [['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#'],
           ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#'],
           ['D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#'],
           ['G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#'],
           ['B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#'],
           ['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#']]


scales = [[2,2,1,2,2,2,1],
          [2,1,2,2,1,2,2],
          [3,2,1,1,3,2],
          [2,1,1,3,2,3],
          [2,2,1,2,2,1,2],
          [2,1,2,2,2,1,2],
          [2,2,3,2,3]]

#Lists that will be filled with xpos, ypos, labels, and colors for points
xs = []
ys = []
annotations = []
colors = []

#Gives each note in the scale a xpos, ypos, label, and color
def notePlacer(scale):
    xplacer = 0
    for i in range(len(strings)):
        for fret in strings[i]:
            for note in scale:
                if note == fret and xplacer <= 24:
                    if xplacer == 0:
                        xs.append(x_ticks[xplacer])
                    else:
                        xs.append((x_ticks[xplacer]+x_ticks[xplacer-1])/2)
                    ys.append(i+1)
                    annotations.append(note)
                    colors.append(-xplacer)
            xplacer += 1
            if xplacer > 24:
                xplacer = 0

#returns list of all the notes in that scale of that key
def scaleMaker(key,pattern):
    output = []
    note = notes.index(key)
    for i in pattern:
        if note == 12:
            note = 0
        elif note == 13:
            note = 1
        output.append(notes[note])
        note += i
    return(output)

#prompts user for musical key and assigns pattern to the scale they pick
key = input("What key are you playing in?\nInput keys as shown below.\nA, A#, B, C, C#, D, D#, E, F, F#, G, G#\nKey:").capitalize()
userinp = int(input("What scale do you want to see?\nInput scales as shown below. (capitalization does not matter)"
                "\nMajor: 1\nMinor: 2\nMajor Blues: 3\nMinor Blues: 4\nMixolydian: 5\nDorian: 6\nPentatonic: 7\nScale:"))

def patternPicker(userinp):
    return scales[userinp-1]

notePlacer(scaleMaker(key,patternPicker(userinp)))

#adds color and stroke to labels
for i, label in enumerate(annotations):
    ax.annotate(label,(xs[i],ys[i]),**afont, path_effects=[pe.withStroke(linewidth=.5,foreground='gray')])

#adds 'guitar strings' to the grid
ax.plot([0,0],[1,6],zorder=1)
def gtrStrings():
    thickness = 3
    for i in range(1,7):
        ax.plot((0,487.502),(i,i),linewidth = thickness,c='gray')
        thickness -= .5
gtrStrings()

#creates the image
ax.scatter(xs,ys,s=60,c=colors,cmap='autumn',edgecolors='black',zorder=2)
plt.show()


