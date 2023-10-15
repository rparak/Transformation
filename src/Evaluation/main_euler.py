# System (Default)
import sys
sys.path.append('..')
# Numpy (Array computing) [pip3 install numpy]
import numpy as np
# Custom Lib.:
#   ../Lib/Transformation/Core
import Lib.Transformation.Core as Transformation
#   ../Lib/Transformation/Utilities/Mathematics
import Lib.Transformation.Utilities.Mathematics as Mathematics

def main():
    """
    Description:
        A simple script to evaluate a class for working with Euler angles.
    """
    
    # Generate a random vector of three elements.
    ea_rnd = np.random.uniform(-Mathematics.CONST_MATH_HALF_PI, Mathematics.CONST_MATH_HALF_PI, 3)

    # Initialization of the class.
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, 'ZYX', np.float64)

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
