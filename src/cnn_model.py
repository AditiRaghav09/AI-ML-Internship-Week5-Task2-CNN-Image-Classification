from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout


def build_cnn_model():

    model = Sequential([

        Conv2D(
            32,
            (3,3),
            activation='relu',
            input_shape=(28,28,1)
        ),

        MaxPooling2D(pool_size=(2,2)),

        Conv2D(
            64,
            (3,3),
            activation='relu'
        ),

        MaxPooling2D(pool_size=(2,2)),

        Dropout(0.25),

        Flatten(),

        Dense(
            128,
            activation='relu'
        ),

        Dropout(0.5),

        Dense(
            10,
            activation='softmax'
        )

    ])

    return model
