import librosa
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# List of song filenames
song_filenames = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3']

# Set the figure size with increased height
fig, axs = plt.subplots(nrows=5, figsize=(10, 25))
# Loop over each song filename
for i, filename in enumerate(song_filenames):
    # Load the MP3 file
    y, sr = librosa.load(filename)

    # Calculate the chromagram using a Fourier transform and a mapping to the chromatic scale
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

    # Plot the chromagram data
    axs[i].imshow(chromagram, aspect='auto', origin='lower', cmap='coolwarm')
    axs[i].set_title(f'Song {i+1} Chromagram')
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Chroma')
    axs[i].set_xticks([])
    axs[i].set_yticks([])
fig.savefig('chromagram.pdf', bbox_inches='tight')

plt.colorbar()
plt.tight_layout()
plt.show()
