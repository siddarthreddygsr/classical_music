import librosa
import matplotlib.pyplot as plt

# Load the MP3 file
y, sr = librosa.load('song1.mp3')

# Calculate the chromagram using a Fourier transform and a mapping to the chromatic scale
chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

# Plot the chromagram data
plt.figure(figsize=(10, 4))
librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', cmap='coolwarm')
plt.title('Chromagram')
# plt.colorbar()
plt.tight_layout()
plt.show()
