from fastai.vision.all import *
import time
import cv2
from utils.grabscreen import grab_screen
import torch

def label_func(x): return x.parent.name

def run():
    path = Path("data")
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")


    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=40, num_workers=0)
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    print("Loaded")
    learn.fine_tune(20, base_lr=1.0e-02)

    learn.export()

    interp = ClassificationInterpretation.from_learner(learn)
    print(interp.confusion_matrix())




if __name__ == '__main__':
    # print(torch.cuda.is_available())
    # print(torch.version.cuda)
    run()

