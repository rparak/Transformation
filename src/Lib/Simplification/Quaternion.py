# System (Default)
import sys
# Sympy (Symbolic mathematics) [pip3 install sympy]
import sympy as sp

def Get_Homogeneous_Transformation_Matrix_T1_Sympy(q):
    """
    Description:
        Get the simplified homogeneous transformation matrix {T} from the Quaternion (w, x, y, z) representation 
        of orientation.

        This method is called homogeneous expression.

        Equation:
            Q(q): Quaternion matrix
                Q(q) = [   q_{0},              -q_{1..3}^T
                        q_{1..3}, q_{0}I_{3} + C(q_{1..3})],

            Q_conj(q): Conjugate quaternion matrix
                Q(q) = [   q_{0},              -q_{1..3}^T
                        q_{1..3}, q_{0}I_{3} - C(q_{1..3})],

            where C is the skew-symmetric cross product matrix defined as:
                C(x) = [[     0, -x_{3},  x_{2}],
                        [ x_{3},      0, -x_{1}], 
                        [-x_{2},  x_{1},     0]]]

            if z' is the same vector in fixed body coordinates, then the following relationships 
            hold:
                [0; z'] = Q_conj(q)^T @ Q(q) [0; z]
                [0; z'] = [[1 0^T]; [0, R_{q}(q)]] [0; z]

                z' = (R_{q}(q)^T)z

            T = [R_{q}(q)^T, 0_{3x1}
                    0_{1x3}, 1_{1x1}],

        Reference:
            Diebel, James. (2006). Representing Attitude: Euler Angles, Unit Quaternions, and Rotation Vectors. Matrix. 58.

    Returns:
        (1) parameter [Matrix<cls_data_type> 4x4]: Simplified homogeneous transformation matrix {T}.

    """

    T = sp.Matrix(sp.Identity(4))

    # Quaternion matrix: Q -> Homogenouse Transformation Matrix {T: 4x4}
    Q = sp.Matrix([[q[0], -q[1], -q[2], -q[3]],
                   [q[1],  q[0],  q[3], -q[2]],
                   [q[2], -q[3],  q[0],  q[1]],
                   [q[3],  q[2], -q[1],  q[0]]])
    # Conjugate quaternion matrix: Q_conj -> Homogenouse Transformation Matrix {T: 4x4}
    Q_conj = sp.Matrix([[q[0], -q[1], -q[2], -q[3]],
                        [q[1],  q[0], -q[3],  q[2]],
                        [q[2],  q[3],  q[0], -q[1]],
                        [q[3], -q[2],  q[1],  q[0]]])

    #print(sp.Matrix((Q_conj.T @ Q))[1:, 1:])
    T[:3, :3] = sp.Matrix((Q_conj.T @ Q)[1:, 1:]).T

    return sp.nsimplify(T)
    
def Get_Homogeneous_Transformation_Matrix_T2_Sympy(q):
    """
    Description:
        Get the simplified homogeneous transformation matrix {T} from the Quaternion (w, x, y, z) representation 
        of orientation.

        This method is called inhomogeneous expression.

        General representation:
            T = [[1.0 - 2*(q_{2}**2 + q_{3}**2), 2*(q_{1}*q_{2} - q_{3}*q_{0}), 2*(q_{1}*q_{3} + q_{2}*q_{0}), 0.0], 
                 [2*(q_{1}*q_{2} + q_{3}*q_{0}), 1.0 - 2*(q_{1}**2 + q_{3}**2), 2*(q_{2}*q_{3} - q_{1}*q_{0}), 0.0], 
                 [2*(q_{1}*q_{3} - q_{2}*q_{0}), 2*(q_{2}*q_{3} + q_{1}*q_{0}), 1.0 - 2*(q_{1}**2 + q_{2}**2), 0.0], 
                 [                          0.0,                           0.0,                           0.0, 1.0]]

        Reference:
            SICILIANO, Bruno a KHATIB, Oussama, ed. Springer handbook of robotics. 2nd edition. 
            Berlin: Springer, [2016]. ISBN 978-3-319-32550-7.

    Returns:
        (1) parameter [Matrix<cls_data_type> 4x4]: Simplified homogeneous transformation matrix {T}.
    """

    T = sp.Matrix(sp.Identity(4))

    T[0, 0] = 1.0 - 2*(q[2]**2 + q[3]**2)
    T[0, 1] = 2*(q[1]*q[2] - q[3]*q[0])
    T[0, 2] = 2*(q[1]*q[3] + q[2]*q[0])
    T[1, 0] = 2*(q[1]*q[2] + q[3]*q[0])
    T[1, 1] = 1.0 - 2*(q[1]**2 + q[3]**2)
    T[1, 2] = 2*(q[2]*q[3] - q[1]*q[0])
    T[2, 0] = 2*(q[1]*q[3] - q[2]*q[0])
    T[2, 1] = 2*(q[2]*q[3] + q[1]*q[0])
    T[2, 2] = 1.0 - 2*(q[1]**2 + q[2]**2)

    return sp.nsimplify(T)

def main():
    """
    Description:
       Get simplified equations for fast conversion (Quaternion -> Matrix).
    """

    # Initialize a string containing the symbol assigned with the variable.
    #   Quaternion: q_{0..3} -> q_{w, x, y, z}
    q = [sp.symbols(f'q[{i}]') for i in range(4)]

    """
    Description:
        Get the simplified homogeneous transformation matrix from the Quaternion (w, x, y, z).
    """     
    M_simpl = Get_Homogeneous_Transformation_Matrix_T1_Sympy(q)
    for i, M_i_simpl in enumerate(M_simpl.tolist()):
        for j, M_ij_simpl in enumerate(M_i_simpl):
            # Replace (convert) the old value string to the new one.
            M_ij_simpl_new = str(sp.nsimplify(M_ij_simpl, tolerance=1e-5, rational=True).evalf())
            print(f'T[{i},{j}] = 'f'{M_ij_simpl_new}')

if __name__ == '__main__':
    sys.exit(main())