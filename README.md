# Music Recommendation Using Deep Learning

Music Recommendation using latent feature vectors obtained from a network trained on the Free Music Archive dataset.

## Overview

The basic idea of this project is to recommend music using computer vision through a convolutional neural network. The network is first trained as a classifier with the labels being the 8 different genres of songs from the dataset. The trained network is then modified by discarding the softmax layer i.e. creating a new model which works as an encoder. This encoder takes as input slices of a spectrogram one at a time and outputs a 32 dimensional latent representation of that respective slice. This generates multiple latent vectors for one spectrogram depending on how many slices were generated. These multiple vectors are then averaged to get one latent representation for each spectrogram. The Cosine similarity metric is used to generate a similarity score between one anchor song and the rest of the songs in the test set. The two songs with the highest similarity score with respect to the anchor song are then outputted as the recommendations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For using this project, you need to install Keras, Scikit-learn, PIL, Librosa, OpenCV, and Pandas

```
pip install keras
pip install scikit-learn
pip install pillow
pip install librosa
pip install cv2
pip install pandas
```

### Dataset
The fma_small dataset consists of 8000 mp3 files from the [Free Music Archive](https://github.com/mdeff/fma).

Each file in fma_small is  a 30 second clip of music. The dataset is balanced and has 8 genres ( Hip-Hop, International, Electronic, Folk, Experimental, Rock, Pop, and Instrumental).

The dataset is stored in the folder **Dataset** as *fma_small* *(File too large to upload onto Github)*.


## Training

Run the script *train.ipynb* in the terminal as follows.
```
Python train.ipynb
```

### Data Preprocessing

The *train.ipynb* script runs **import_data.py**, **slice_spectrogram.py**, and **load_data.py** in the back.

### import_data.py
• **Train Mode** - In training mode, the script converts the files from *fma_small* into mel-spectrograms and stores them into a folder called *Train_Spectrogram_Images*.


• **Test Mode** - In testing mode, the script converts the songs from *DLMusicTest_30* into mel-spectrograms and stores them into a folder called *Test_Spectrogram_Images*.



### slice_spectrogram.py
• **Train Mode** - In training mode, the script slices the spectrograms from the *Train_Spectrogram_Images* folder into 128x128 slices and stores them into the *Train_Sliced_Images* folder.


• **Test Mode** - In testing mode, the script slices the spectrograms from the *Test_Spectrogram_Images* folder into 128x128 slices and stores them into the *Test_Sliced_Images* folder.


### load_data.py
• **Train Mode** - In training mode, the script imports images from *Train_Sliced_Images*, converts them into grayscale, and then exports them as numpy matrices for training and testing. This is saved as *train_x.npy*, *train_y.npy*, *test_x.npy*, and *test_y.npy* in the *Training_Data* folder.


• **Test Mode** - In testing mode, the script imports images from *Test_Sliced_Images*, converts them into grayscale, and returns them as images and labels.





