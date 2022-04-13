from PIL import Image
import numpy as np
import os
import random

def combine_props(props):
    """Props' z-index is equal to their position in the props list."""
    final = props[-1]
    for attr in reversed(props):
        final = np.where(attr[:, :, 3:4] == 0, final, attr)
    return final

def sample_props(props_path):
    props = []
    props_names = []
    for path, dirs, files in os.walk(props_path):
        if(len(files) > 0):
            filename = random.choice(files)
            fullpath = os.path.join(path, filename)
            this_file = np.array(Image.open(fullpath))
            props_names.append(fullpath)
            props.append(this_file)
    return props, props_names


generated = []
duplicates = 0
num_images = 10
while len(generated) < num_images:
    props, props_names = sample_props('./properties')
    new_hash = hash(tuple(props_names))
    if new_hash not in generated:
        generated.append(new_hash)
        image = combine_props(props)
        image = Image.fromarray(image)
        image_id = str(len(generated))
        print(image_id)
        image.save('./images/' + image_id + '.png')
    else:
        duplicates += 1
print('duplicates: ' + str(duplicates))
