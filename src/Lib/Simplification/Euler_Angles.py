# System (Default)
import sys
# Sympy (Symbolic mathematics) [pip3 install sympy]
import sympy as sp

def __Get_Rotation_Matrix_X(theta):
    """
    Description:
        A rotation matrix that rotates the vectors by an angle {theta} about the {x}-axis 
        using a right-hand rule that encodes the alternation of signs.

        Note:
            R_{x}(theta) = [1.0,        0.0,         0.0, 0.0]
                           [0.0, cos(theta), -sin(theta), 0.0]
                           [0.0, sin(theta),  cos(theta), 0.0]
                           [0.0,        0.0,         0.0, 1.0]

    Args:
        (1) theta [float]: Required angle of rotation in radians.

    Returns:
        (1) parameter [Matrix 4x4]: Homogeneous transformation matrix around {x}-axis.
    """

    return sp.Matrix([[ 1.0,           0.0,                  0.0, 0.0],
                      [ 0.0, sp.cos(theta), (-1.0)*sp.sin(theta), 0.0],
                      [ 0.0, sp.sin(theta),        sp.cos(theta), 0.0],
                      [ 0.0,           0.0,                  0.0, 1.0]])

def __Get_Rotation_Matrix_Y(theta):
    """
    Description:
        A rotation matrix that rotates the vectors by an angle {theta} about the {y}-axis 
        using a right-hand rule that encodes the alternation of signs.

        Note:
            R_{y}(theta) = [ cos(theta), 0.0,  sin(theta), 0.0]
                           [        0.0, 1.0,         0.0, 0.0]
                           [-sin(theta), 0.0,  cos(theta), 0.0]
                           [        0.0, 0.0,         0.0, 1.0]

    Args:
        (1) theta [float]: Required angle of rotation in radians.

    Returns:
        (1) parameter [Matrix 4x4]: Homogeneous transformation matrix around {y}-axis.
    """

    return sp.Matrix([[        sp.cos(theta), 0.0, sp.sin(theta), 0.0],
                      [                  0.0, 1.0,           0.0, 0.0],
                      [ (-1.0)*sp.sin(theta), 0.0, sp.cos(theta), 0.0],
                      [                  0.0, 0.0,           0.0, 1.0]])

def __Get_Rotation_Matrix_Z(theta):
    """
    Description:
        A rotation matrix that rotates the vectors by an angle {theta} about the {z}-axis 
        using a right-hand rule that encodes the alternation of signs.

        Note:
            R_{z}(theta) = [cos(theta), -sin(theta), 0.0, 0.0]
                           [sin(theta),  cos(theta), 0.0, 0.0]
                           [       0.0,        0.0,  1.0, 0.0]
                           [       0.0,        0.0,  0.0, 1.0]

    Args:
        (1) theta [float]: Required angle of rotation in radians.

    Returns:
        (1) parameter [Matrix 4x4]: Homogeneous transformation matrix around {z}-axis.
    """

    return sp.Matrix([[ sp.cos(theta), (-1.0)*sp.sin(theta), 0.0, 0.0],
                      [ sp.sin(theta),        sp.cos(theta), 0.0, 0.0],
                      [           0.0,                  0.0, 1.0, 0.0],
                      [           0.0,                  0.0, 0.0, 1.0]])

def Get_Rotation_Matrix(ax, theta):
    """
    Description:
        Get the homogeneous transformation matrix around a specific rotation axis.
        
    Args:
        (1) ax [string]: Axis name.
        (2) theta [float]: Desired absolute joint position in radians / meters.
        
    Returns:
        (1) parameter [Matrix 4x4]: Homogeneous transformation matrix around a specific rotation axis.
    """

    return {
        'X': lambda x: __Get_Rotation_Matrix_X(x),
        'Y': lambda x: __Get_Rotation_Matrix_Y(x),
        'Z': lambda x: __Get_Rotation_Matrix_Z(x),
    }[ax](theta)

def Get_Matrix_From_Euler_Method_Standard(theta, axes_sequence_cfg):
    """
    Description:
        Get the simplified homogeneous transformation matrix from Euler angles in a specified 
        sequence of axes.

        There are six choices of rotation axes for Tait-Bryan angles.
            Note:
                intrinsic rotation (x - y' - z'') -> extrinsic rotation (z - y - x)
                ...
                intrinsic rotation (z - y' - x'') -> extrinsic rotation (x - y - z)

    Args:
        (1) theta [Vector 1x3]: Required angle of rotation in each axis in radians. 
        (2) axes_sequence_cfg [string]: Rotation axis sequence configuration (e.g. 'XYZ').
                Note ('XYZ'):
                    Matrix multiplication - R_{z}(theta_{2}) @ R_{y}(theta_{1}) @ R_{x}(theta_{0})

    Returns:
        (1) parameter [Matrix 4x4]: Simplified homogeneous transformation matrix around {z, y, x}-axis.
    """

    return {
        'XYZ': lambda x: sp.simplify(Get_Rotation_Matrix('Z', x[2]) @ Get_Rotation_Matrix('Y', x[1]) @ Get_Rotation_Matrix('X', x[0])),
        'XZY': lambda x: sp.simplify(Get_Rotation_Matrix('Y', x[1]) @ Get_Rotation_Matrix('Z', x[2]) @ Get_Rotation_Matrix('X', x[0])),
        'YXZ': lambda x: sp.simplify(Get_Rotation_Matrix('Z', x[2]) @ Get_Rotation_Matrix('X', x[0]) @ Get_Rotation_Matrix('Y', x[1])),
        'YZX': lambda x: sp.simplify(Get_Rotation_Matrix('X', x[0]) @ Get_Rotation_Matrix('Z', x[2]) @ Get_Rotation_Matrix('Y', x[1])),
        'ZXY': lambda x: sp.simplify(Get_Rotation_Matrix('Y', x[1]) @ Get_Rotation_Matrix('X', x[0]) @ Get_Rotation_Matrix('Z', x[2])),
        'ZYX': lambda x: sp.simplify(Get_Rotation_Matrix('X', x[0]) @ Get_Rotation_Matrix('Y', x[1]) @ Get_Rotation_Matrix('Z', x[2])),
    }[axes_sequence_cfg](theta)

def main():
    """
    Description:
       Get simplified equations for fast conversion (Euler angles -> Matrix).
    """

    # Initialize a string containing the symbol assigned with the variable.
    #   Euler Angles: theta_{0..2}
    theta = [sp.symbols(f'theta[{i}]') for i in range(3)]

    """
    Description:
        Get the simplified homogeneous transformation matrix from Euler angles in a specified 
        sequence of axes.
    """     
    M_simpl = Get_Matrix_From_Euler_Method_Standard(theta, 'ZYX')
    for i, M_i_simpl in enumerate(M_simpl.tolist()):
        for j, M_ij_simpl in enumerate(M_i_simpl):
            # Replace (convert) the old value string to the new one.
            #   Note: Better conversion to standard form (copy + paste to function).
            M_ij_simpl_new = (str(sp.nsimplify(M_ij_simpl, tolerance=1e-5, rational=True).evalf()).replace('sin', 'np.sin')).replace('cos', 'np.cos')
            print(f'T[{i},{j}] = 'f'{M_ij_simpl_new}')

if __name__ == '__main__':
    sys.exit(main())
