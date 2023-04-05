# Transformation_Lib

## Requirements:

**Programming Language:**

```bash
Python
```

**Import Libraries:**
```bash
More information can be found in the individual scripts (.py).
```

**Supported on the following operating systems:**
```bash
Windows, Linux, macOS
```

## Project Description:
An open-source library for transformation functions useful for robotics.

## Simple Demonstration

Then confirm that dotnet is installed.


**Vector3_Cls(object):**

```bash
$ ..\Transformation_Lib\src\Evaluation> python3 main_euler.py
```

```py 
# System (Default)
import sys
# Numpy (Array computing) [pip3 install numpy]
import numpy as np
# Platform (Platform identification data)
import platform
# System (Default)
import sys
if platform.system() == 'Windows':
    # Windows Path.
    sys.path.append('..')
else:
    # Linux / macOS Path.
    sys.path.append('..') 
# Custom Library:
#   ../Lib/Transformation
import Lib.Transformation as Transformation

def main():
    """
    Description:
        A simple script to evaluate a class for working with three-dimensional (3D) vector.
    """
    
    # Generate a random vector of three elements.
    v3_rnd = np.random.uniform(-100, 100, 3)

    # Initialization of the class.
    Vec3_Cls = Transformation.Vector3_Cls(v3_rnd, np.float32)

    # Display the requested class information.
    print(f'[INFO] Vector<float> {Vec3_Cls.Shape} = {Vec3_Cls.all()}')
    print('[INFO] Parameters:')
    print(f'[INFO]  [x] = {Vec3_Cls.x}')
    print(f'[INFO]  [y] = {Vec3_Cls.y}')
    print(f'[INFO]  [z] = {Vec3_Cls.z}')
    print(f'[INFO] Norm = {Vec3_Cls.Norm()}')
    print(f'[INFO] Normalized (unit) vector = {Vec3_Cls.Normalize()}')

if __name__ == '__main__':
    sys.exit(main())
```

## Contact Info:
Roman.Parak@outlook.com

## Citation (BibTex)
```bash
@misc{RomanParak_DataConverter,
  author = {Roman Parak},
  title = {An open-source library for transformation functions useful for robotics},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://https://github.com/rparak/Data_Converter}}
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
