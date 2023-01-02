# image-compare
A simple image comparison tool, in OpenCV

## Installation
```bash
git clone https://github.com/sjjeong94/image-compare
cd image-compare
pip install -e .
```

## Usage
```
python -m image_compare path/to/images/
```

```python
import cv2
from image_compare import compare

image1 = cv2.imread("image1.png")
image2 = cv2.imread("image2.png")
image3 = cv2.imread("image3.png")

compare([image1, image2, image3])
```

### License
MIT