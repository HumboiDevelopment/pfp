from PIL import Image
import numpy as np



def combine_attrs(attrs):
    "attrs' z-index is equal to their position in the attrs list"
    final = attrs[-1]
    for attr in reversed(attrs):
        final = np.where(attr[:, :, 3:4] == 0, final, attr)
    return final

attrs = [np.array(Image.open('0.png')),
         np.array(Image.open('1.png')),
         np.array(Image.open('2.png'))]

final = combine_attrs(attrs)
img = Image.fromarray(final)
img.save('final.png')
