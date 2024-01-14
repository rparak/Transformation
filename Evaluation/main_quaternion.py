# System (Default)
import sys
#   Add access if it is not in the system path.
if '../' + 'src' not in sys.path:
    sys.path.append('../' + 'src')
# Numpy (Array computing) [pip3 install numpy]
import numpy as np
# Custom Lib.:
#   ../Transformation/Core
import Transformation.Core as Transformation
#   ../Transformation/Utilities/Mathematics
import Transformation.Utilities.Mathematics as Mathematics

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
    EA_Cls = Transformation.Euler_Angle_Cls(ea_rnd, axes_sequence_cfg, np.float64)

    # Get the Unit-Quaternion.
    q = EA_Cls.Get_Quaternion()

    # Initialization of the class.
    Quaternion_Cls = Transformation.Quaternion_Cls(q.all(), np.float64)

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
