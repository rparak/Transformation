# System (Default)
import sys
sys.path.append('..')
# Numpy (Array computing) [pip3 install numpy]
import numpy as np
# Custom Lib.:
#   ../Lib/Transformation/Core
import Lib.Transformation.Core as Transformation

def main():
    """
    Description:
        A simple script to evaluate a class for working with three-dimensional (3D) vector.
    """
    
    # Generate a random vector of three elements.
    v3_rnd = np.random.uniform(-100, 100, 3)

    # Initialization of the class.
    Vec3_Cls = Transformation.Vector3_Cls(v3_rnd, np.float64)

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
