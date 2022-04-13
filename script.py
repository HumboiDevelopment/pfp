from PIL import Image
import numpy as np



def combine_props(props):
    "props' z-index is equal to their position in the props list"
    final = props[-1]
    for attr in reversed(props):
        final = np.where(attr[:, :, 3:4] == 0, final, attr)
    return final

props = [np.array(Image.open('0.png')),
         np.array(Image.open('1.png')),
         np.array(Image.open('2.png'))]

final = combine_props(props)
img = Image.fromarray(final)
img.save('final.png')
