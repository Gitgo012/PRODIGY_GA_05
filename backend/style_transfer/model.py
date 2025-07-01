import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow_hub as hub

# Preprocessing functions
def load_img(path_to_img, max_dim=512):
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img

def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = tf.clip_by_value(tensor, 0, 255)
    tensor = tf.cast(tensor[0], tf.uint8)
    return Image.fromarray(tensor.numpy())

# Load model
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def perform_style_transfer(content_path, style_path):
    content_image = load_img(content_path)
    style_image = load_img(style_path)
    stylized_image = hub_model(content_image, style_image)[0]
    return tensor_to_image(stylized_image)
