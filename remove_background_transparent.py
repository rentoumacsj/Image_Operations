import os

from rembg.bg import remove
import numpy as np
import io
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

res_dir = './sample_source/'
des_dir = './sample_output/'

file_list = os.listdir(res_dir)
for file in file_list:
    input_path = res_dir + file
    output_path = des_dir + file.replace('.jpg', '_transparent.png')
    print(output_path)
    f = np.fromfile(input_path)
    result = remove(f, alpha_matting=True)
    img = Image.open(io.BytesIO(result)).convert('RGBA')
    img.save(output_path)
