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

**Vector3_Cls(object):**

```bash
$ ..\Transformation_Lib\src\Evaluation> python3 main_vector3.py
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

**Euler_Angle_Cls(object):**

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
#   ../Lib/Utilities/Mathematics
import Lib.Utilities.Mathematics as Mathematics

def main():
    """
    Description:
        A simple script to evaluate a class for working with Euler angles.
    """
    
    # Generate a random vector of three elements.
    ea_rnd = np.random.uniform(-Mathematics.CONST_MATH_HALF_PI, Mathematics.CONST_MATH_HALF_PI, 3)

    # Initialization of the class.
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, 'ZYX', np.float32)

    # Display the requested class information.
    print(f'[INFO] Euler_Angles<float> {EA_Cls.Shape} = {EA_Cls.all()} [radians]')
    print(f'[INFO] Euler_Angles<float> {EA_Cls.Shape} = {EA_Cls.Degree} [degrees]')
    print('[INFO] Parameters in radians:')
    print(f'[INFO]  [x] = {EA_Cls.x}')
    print(f'[INFO]  [y] = {EA_Cls.y}')
    print(f'[INFO]  [z] = {EA_Cls.z}')
    print('[INFO] Homogeneous transformation matrix (HTM):')
    print('[INFO] T = ')
    print(EA_Cls.Get_Homogeneous_Transformation_Matrix())
    print('[INFO] Unit-Quaternion:')
    print(f'[INFO] Q = {EA_Cls.Get_Quaternion()}')

if __name__ == '__main__':
    sys.exit(main())
```

**Homogeneous_Transformation_Matrix_Cls(object):**

```bash
$ ..\Transformation_Lib\src\Evaluation> python3 main_htm.py
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
#   ../Lib/Utilities/Mathematics
import Lib.Utilities.Mathematics as Mathematics

def main():
    """
    Description:
        A simple script to evaluate a class for working with homogeneous transformation matrix.
    """
    
    # Rotation axis sequence configuration.
    axes_sequence_cfg = 'ZYX'

    # Generate a random vector of three elements (euler angles).
    ea_rnd = np.random.uniform(-Mathematics.CONST_MATH_HALF_PI, Mathematics.CONST_MATH_HALF_PI, 3)

    # Initialization of the class (Euler Angle).
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, axes_sequence_cfg, np.float32)

    # Get the homogeneous transformation matrix.
    T = EA_Cls.Get_Homogeneous_Transformation_Matrix().all()
    # Generate a random vector of three elements (translation part).
    T[:3, 3] = np.random.uniform(-10, 10, 3).reshape(1, 3)
    
    # Initialization of the class (Homogeneous transformation matrix).
    HTM_Cls = Transformation.Homogeneous_Transformation_Matrix_Cls(T, np.float32)

    # Display the requested class information.
    print(f'[INFO] T<float, float> {HTM_Cls.Shape} = ')
    print(f'{HTM_Cls.all()}')
    print('[INFO] Parameters:')
    print(f'[INFO]  [p] = {HTM_Cls.p}')
    print('[INFO]  [R] = ')
    print(f'{HTM_Cls.R}')
    print(f'[INFO] Input Euler_Angles<float> {EA_Cls.Shape} = {EA_Cls.all()} [radians]')
    print('[INFO] Rotation:')
    print(f'[INFO]  Euler Angles = {HTM_Cls.Get_Rotation(axes_sequence_cfg)} [radians]')
    print('[INFO] T^(-1) = ')
    print(f'{HTM_Cls.Inverse()}')
    print(f'[INFO] Diagonal = {HTM_Cls.Diagonal()[0:-1]}')
    print(f'[INFO] Tace = {HTM_Cls.Trace()}')
 
if __name__ == '__main__':
    sys.exit(main())
```

**Quaternion_Cls(object):**

```bash
$ ..\Transformation_Lib\src\Evaluation> python3 main_quaternion.py
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
#   ../Lib/Utilities/Mathematics
import Lib.Utilities.Mathematics as Mathematics

def main():
    """
    Description:
        A simple script to evaluate a class for working with Quaternions.
    """
    
    # Rotation axis sequence configuration.
    axes_sequence_cfg = 'ZYX'

    # Generate a random vector of three elements (euler angles).
    ea_rnd = np.random.uniform(-Mathematics.CONST_MATH_HALF_PI, Mathematics.CONST_MATH_HALF_PI, 3)

    # Initialization of the class (Euler Angle).
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, axes_sequence_cfg, np.float32)

    # Get the Unit-Quaternion.
    q = EA_Cls.Get_Quaternion()

    # Initialization of the class.
    Quaternion_Cls = Transformation.Quaternion_Cls(q.all(), np.float32)

    # Display the requested class information.
    print(f'[INFO] Quaternion<float> {Quaternion_Cls.Shape} = {Quaternion_Cls.all()} [-]')
    print('[INFO] Parameters:')
    print(f'[INFO]  [w] = {Quaternion_Cls.w}')
    print(f'[INFO]  [x] = {Quaternion_Cls.x}')
    print(f'[INFO]  [y] = {Quaternion_Cls.y}')
    print(f'[INFO]  [z] = {Quaternion_Cls.z}')
    print(f'[INFO] Input Euler_Angles<float> {EA_Cls.Shape} = {EA_Cls.all()} [radians]')
    print('[INFO] Rotation:')
    Euler_Angle = Quaternion_Cls.Get_Homogeneous_Transformation_Matrix('Homogeneous').Get_Rotation(axes_sequence_cfg)
    print(f'[INFO]  Euler Angles = {Euler_Angle} [radians]')
    print(f'[INFO] Norm = {Quaternion_Cls.Norm()}')
    print(f'[INFO] Normalized (unit) vector = {Quaternion_Cls.Normalize()}')
    print(f'[INFO] q^(-1) = {Quaternion_Cls.Inverse()}')
    print(f'[INFO] Logarithm = {Quaternion_Cls.Logarithm()}')
    print(f'[INFO] Exponential = {Quaternion_Cls.Exponential()}')

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
