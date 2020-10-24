import os
import re
from PIL import Image


def slice_spect(verbose=0, mode=None):
    if mode=="Train":
        if os.path.exists('SlicedImagesForTrain'):
            return
        labels = []
        image_folder = "SlicedImagesForTrain"
        filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder)
                       if f.endswith(".jpg")]
        counter = 0
        if(verbose > 0):
            print "Slicing Spectograms ..."
        if not os.path.exists('SlicedImagesForTrain'):
            os.makedirs('SlicedImagesForTrain')
        for f in filenames:
            genre_variable = re.search('SpectogramImagesForTrain/.*_(.+?).jpg', f).group(1)
            img = Image.open(f)
            subsample_size = 128
            width, height = img.size
            number_of_samples = width / subsample_size
            for i in range(number_of_samples):
                start = i*subsample_size
                img_temporary = img.crop((start, 0., start + subsample_size, subsample_size))
                img_temporary.save("SlicedImagesForTrain/"+str(counter)+"_"+genre_variable+".jpg")
                counter = counter + 1
        return

    elif mode=="Test":
        if os.path.exists('SlicedImagesForTest'):
            return
        labels = []
        image_folder = "SlicedImagesForTest"
        filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder)
                       if f.endswith(".jpg")]
        counter = 0
        if(verbose > 0):
            print "Slicing Spectograms ..."
        if not os.path.exists('SlicedImagesForTest'):
            os.makedirs('SlicedImagesForTest')
        for f in filenames:
            song_variable = re.search('SpectogramImagesForTest/(.+?).jpg', f).group(1)
            img = Image.open(f)
            subsample_size = 128
            width, height = img.size
            number_of_samples = width / subsample_size
            for i in range(number_of_samples):
                start = i*subsample_size
                img_temporary = img.crop((start, 0., start + subsample_size, subsample_size))
                img_temporary.save("SlicedImagesForTest/"+str(counter)+"_"+song_variable+".jpg")
                counter = counter + 1
        return
