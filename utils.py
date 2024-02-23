import math
import logging


def print(*args):
    msg = ' '.join([str(arg) for arg in args])
    logging.log(logging.WARNING, msg)


def to_euler(q):
    x = q[0]
    y = q[2] * -1
    z = q[1]
    w = q[3]

    t0 = 2.0 * (w * x + y * z)
    t1 = 1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(t0, t1)

    t2 = 2.0 * (w * y - z * x)
    t2 = 1.0 if t2 > 1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = math.asin(t2)

    t3 = 2.0 * (w * z + x * y)
    t4 = 1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(t3, t4)

    # sinr_cosp = 2 * (w * x + y * z)
    # cosr_cosp = 1 - 2 * (x * x + y * y)
    # roll = math.atan2(sinr_cosp, cosr_cosp)
    #
    # sinp = math.sqrt(1 + 2 * (w * y - x * z))
    # cosp = math.sqrt(1 - 2 * (w * y - x * z))
    # pitch = 2 * math.atan2(sinp, cosp) - math.pi / 2
    #
    # siny_cosp = 2 * (w * z + x * y)
    # cosy_cosp = 1 - 2 * (y * y + z * z)
    # yaw = math.atan2(siny_cosp, cosy_cosp)

    return [roll, pitch, yaw]


def eulerToQuaternion(rx, ry, rz):
    cy = math.cos(rx * 0.5)
    sy = math.sin(rx * 0.5)
    cp = math.cos(ry * 0.5)
    sp = math.sin(ry * 0.5)
    cr = math.cos(rz * 0.5)
    sr = math.sin(rz * 0.5)
    q = [0.0, 0.0, 0.0, 0.0]
    q[3] = cy * cp * cr + sy * sp * sr
    q[0] = cy * cp * sr - sy * sp * cr
    q[1] = sy * cp * sr + cy * sp * cr
    q[2] = sy * cp * cr - cy * sp * sr
    return q
