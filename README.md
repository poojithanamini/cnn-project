# ECG Arrhythmia Classification Using CNN

This project has used CNN to train and test. Used Flask with python to make the webapp.

## About Project:
  This is about classifying the given ECG and predicting which type out of the 6 types. 
  ### Types
  1. Left Bundle Branch Block
  2. Normal
  3. Premature Atrial Contraction
  4. Premature Ventricular Contractions
  5. Right Bundle Branch Block
  6. Ventricular Fibrillation

### Flow

The user is supposed to upload an image of an ECG to be classified and click the upload button. The web app takes the input image and classify it and display the type of ECG. 

### How classification is done:

The model is trained with more than 1000 images of different types od ECG to predict the output. The web app load the model and predict the type of output.
