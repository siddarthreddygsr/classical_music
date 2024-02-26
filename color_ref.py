import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import librosa

# Define a list of pitch class names
pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Define a list of colors for each pitch class
colors = plt.get_cmap('tab10')(range(12))

chromagram = librosa.feature.chroma_stft(y=y, sr=sr)
# plot the chromagram with increased height
fig, ax = plt.subplots(figsize=(10, 50))
img = librosa.display.specshow(chromagram, y_axis='chroma', ax=ax)

# set the title and axis labels
ax.set(title='Chromagram', xlabel='Time', ylabel='Pitch Class')

# create the color legend
patches = []
for i, pc in enumerate(pitch_classes):
    patches.append(mpatches.Rectangle((0, 0), 1, 1, fc=colors[i]))
legend = ax.legend(patches, pitch_classes, loc='upper right', framealpha=1)

# save the plot as a PDF file
fig.savefig('chromagram_legend.pdf', bbox_inches='tight')
