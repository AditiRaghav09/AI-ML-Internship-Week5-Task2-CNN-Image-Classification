# Convolutional Neural Networks (CNNs) for Image Classification

## 📌 Project Overview

This project demonstrates the implementation of a **Convolutional Neural Network (CNN)** for handwritten digit image classification using **TensorFlow** and the **MNIST dataset**.

The objective is to build a deep learning model capable of automatically learning image features through convolution and pooling operations, and accurately classifying handwritten digits (0–9).

This project was completed as part of an **AI & Machine Learning Internship**.

---

## 🎯 Objectives

* Load and preprocess the MNIST dataset.
* Build a CNN architecture using TensorFlow/Keras.
* Train the CNN model for image classification.
* Apply Dropout regularization to improve generalization.
* Evaluate model performance on the test dataset.
* Generate a confusion matrix and classification report.
* Visualize training and validation accuracy/loss curves.

---

## 🗂️ Dataset

**Dataset:** MNIST Handwritten Digit Dataset

* 70,000 grayscale handwritten digit images
* 60,000 training images
* 10,000 testing images
* Image size: 28 × 28 pixels
* Number of classes: 10 (Digits 0–9)

---

## 🧠 CNN Architecture

The model consists of:

* Conv2D Layer (32 Filters)
* MaxPooling2D Layer
* Conv2D Layer (64 Filters)
* MaxPooling2D Layer
* Dropout Layer
* Flatten Layer
* Dense Layer (128 Neurons)
* Dropout Layer
* Output Layer (10 Neurons with Softmax)

---

## ⚙️ Hyperparameters

| Parameter        | Value                    |
| ---------------- | ------------------------ |
| Optimizer        | Adam                     |
| Loss Function    | Categorical Crossentropy |
| Epochs           | 10                       |
| Batch Size       | 32                       |
| Validation Split | 20%                      |

---

## 📊 Results

The trained CNN achieved high classification accuracy on the MNIST test dataset.

Evaluation includes:

* Test Accuracy
* Test Loss
* Confusion Matrix
* Classification Report
* Training Accuracy Curve
* Validation Accuracy Curve
* Training Loss Curve
* Validation Loss Curve

---

## 📁 Repository Structure

```
README.md
requirements.txt

notebooks/
    cnn_image_classification.ipynb

src/
    cnn_model.py
    dataset.py

docs/
    evaluation_report.md

models/
    saved_cnn_model.keras

assets/
    training_accuracy.png
    training_loss.png
    confusion_matrix.png
```

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 How to Run

1. Clone this repository.
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Open the notebook:

```
notebooks/cnn_image_classification.ipynb
```

4. Run all cells in sequence.

---

## 📚 Key Learning Outcomes

* Image preprocessing
* Convolutional Neural Networks (
