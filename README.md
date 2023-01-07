# OpenCV Compare
A simple image comparison tool, in OpenCV

## Installation
```bash
pip install opencv-compare
```

## Usage
```
python -m opencv_compare path/to/images/
```

```python
import cv2
from opencv_compare import compare

image1 = cv2.imread("image1.png")
image2 = cv2.imread("image2.png")
image3 = cv2.imread("image3.png")

compare([image1, image2, image3])
```

## Commands
| Key Input | Action                 |
| --------- | ---------------------- |
| ESC       | exit                   |
| C         | capture cropped images |
| A         | decrease the crop size |
| S         | increase the crop size |
| Z         | decrease the zoom size |
| X         | increase the zoom size |

### License
MIT