from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical


def load_and_preprocess_data():
    """
    Loads and preprocesses the MNIST dataset.
    """

    # Load dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Normalize pixel values
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    # Reshape for CNN
    X_train = X_train.reshape(-1, 28, 28, 1)
    X_test = X_test.reshape(-1, 28, 28, 1)

    # One-hot encode labels
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    return X_train, X_test, y_train, y_test
