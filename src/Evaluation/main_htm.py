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
        A simple script to evaluate a class for working with homogeneous transformation matrix.
    """
    
    # Rotation axis sequence configuration.
    axes_sequence_cfg = 'ZYX'

    # Generate a random vector of three elements (euler angles).
    ea_rnd = np.random.uniform(-Mathematics.CONST_MATH_HALF_PI, Mathematics.CONST_MATH_HALF_PI, 3)

    # Initialization of the class (Euler Angle).
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, axes_sequence_cfg, np.float64)

    # Get the homogeneous transformation matrix.
    T = EA_Cls.Get_Homogeneous_Transformation_Matrix().all()
    # Generate a random vector of three elements (translation part).
    T[:3, 3] = np.random.uniform(-10, 10, 3).reshape(1, 3)
    
    # Initialization of the class (Homogeneous transformation matrix).
    HTM_Cls = Transformation.Homogeneous_Transformation_Matrix_Cls(T, np.float64)

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
