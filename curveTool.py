from typing import List, Dict, Union
import numpy as np
import struct


# from .utils import print


class Flags:
    """ Flag Property options """

    # bit flags for header
    DDSD_CAPS = 0X00000001
    DDSD_HEIGHT = 0X00000002
    DDSD_WIDTH = 0X00000004
    DDSD_PITCH = 0X00000008
    DDSD_PIXELFORMAT = 0X00001000
    DDSD_MIPMAPCOUNT = 0X00020000
    DDSD_LINEARSIZE = 0X00080000
    DDSD_DEPTH = 0X00800000
    # flags for pixel formats
    DDPF_ALPHAPIXELS = 0X00000001
    DDPF_ALPHA = 0X00000002
    DDPF_FOURCC = 0X00000004
    DDPF_RGB = 0X00000040
    DDPF_RGBA = 0X00000041
    DDPF_YUV = 0X00000200
    DDPF_LUMINANCE = 0X00020000
    # flags for complex caps
    DDSCAPS_COMPLEX = 0X00000008
    DDSCAPS_MIPMAP = 0X00400000
    DDSCAPS_TEXTURE = 0X00001000
    # flags for cubemaps
    DDSCAPS2_CUBEMAP = 0X00000200
    DDSCAPS2_CUBEMAP_POSITIVEX = 0X00000400
    DDSCAPS2_CUBEMAP_NEGATIVEX = 0X00000800
    DDSCAPS2_CUBEMAP_POSITIVEY = 0X00001000
    DDSCAPS2_CUBEMAP_NEGATIVEY = 0X00002000
    DDSCAPS2_CUBEMAP_POSITIVEZ = 0X00004000
    DDSCAPS2_CUBEMAP_NEGATIVEZ = 0X00008000
    DDSCUBEMAP_ALL_FACES = (DDSCAPS2_CUBEMAP_POSITIVEX | DDSCAPS2_CUBEMAP_NEGATIVEX | DDSCAPS2_CUBEMAP_POSITIVEY | DDSCAPS2_CUBEMAP_NEGATIVEY | DDSCAPS2_CUBEMAP_POSITIVEZ | DDSCAPS2_CUBEMAP_NEGATIVEZ)
    DDSCAPS2_VOLUME = 0X00200000


class DDSDxgiFormat:
    """ Format Flags """

    DDS_DXGI_FORMAT_R32G32B32A32_FLOAT = 2
    DDS_DXGI_FORMAT_R32G32B32_FLOAT = 6
    DDS_DXGI_FORMAT_R16G16B16A16_FLOAT = 10
    DDS_DXGI_FORMAT_R32G32_FLOAT = 16
    DDS_DXGI_FORMAT_R8G8B8A8_UNORM = 28
    DDS_DXGI_FORMAT_R16G16_FLOAT = 34
    DDS_DXGI_FORMAT_R32_FLOAT = 41
    DDS_DXGI_FORMAT_R8G8_UNORM = 49
    DDS_DXGI_FORMAT_R16_FLOAT = 54
    DDS_DXGI_FORMAT_R8_UNORM = 61
    DDS_DXGI_FORMAT_BC1_UNORM = 71
    DDS_DXGI_FORMAT_BC2_UNORM = 74
    DDS_DXGI_FORMAT_BC3_UNORM = 77
    DDS_DXGI_FORMAT_BC4_UNORM = 80
    DDS_DXGI_FORMAT_BC4_SNORM = 81
    DDS_DXGI_FORMAT_BC5_UNORM = 83
    DDS_DXGI_FORMAT_BC5_SNORM = 84
    DDS_DXGI_FORMAT_B8G8R8A8_UNORM = 87
    DDS_DXGI_FORMAT_BC6H_UF16 = 95
    DDS_DXGI_FORMAT_BC6H_SF16 = 96
    DDS_DXGI_FORMAT_BC7_UNORM = 98


class DDSPixelFormats:
    """ DDS pixel format options """

    DDS_UNKNOWN = 0
    DDS_R8G8B8 = 20
    DDS_A8R8G8B8 = 21
    DDS_X8R8G8B8 = 22
    DDS_R5G6B5 = 23
    DDS_X1R5G5B5 = 24
    DDS_A1R5G5B5 = 25
    DDS_A4R4G4B4 = 26
    DDS_R3G3B2 = 27
    DDS_A8 = 28
    DDS_A8R3G3B2 = 29
    DDS_X4R4G4B4 = 30
    DDS_A2B10G10R10 = 31
    DDS_A8B8G8R8 = 32
    DDS_X8B8G8R8 = 33
    DDS_G16R16 = 34
    DDS_A2R10G10B10 = 35
    DDS_A16B16G16R16 = 36
    DDS_A8P8 = 40
    DDS_P8 = 41
    DDS_L8 = 50
    DDS_A8L8 = 51
    DDS_A4L4 = 52
    DDS_V8U8 = 60
    DDS_L6V5U5 = 61
    DDS_X8L8V8U8 = 62
    DDS_Q8W8V8U8 = 63
    DDS_V16U16 = 64
    DDS_A2W10V10U10 = 67
    DDS_UYVY = 0X32595559  # GS_MAKEFOURCC('U', 'Y', 'V', 'Y')
    DDS_R8G8_B8G8 = 0X32595559  # GS_MAKEFOURCC('R', 'G', 'B', 'G')
    DDS_YUY2 = 0X32595559  # GS_MAKEFOURCC('Y', 'U', 'Y', '2')
    DDS_G8R8_G8B8 = 0X42475247  # GS_MAKEFOURCC('G', 'R', 'G', 'B')
    DDS_BC1 = 0X33545844  # GS_MAKEFOURCC('D', 'X', 'T', '1')
    DDS_BC2 = 0X33545844  # GS_MAKEFOURCC('D', 'X', 'T', '3')
    DDS_BC3 = 0X35545844  # GS_MAKEFOURCC('D', 'X', 'T', '5')
    DDS_ATI1 = 0X55344342  # GS_MAKEFOURCC('A', 'T', 'I', '1')     # = 'B', 'C', '4', 'U'
    DDS_BC4 = 0X55344342  # GS_MAKEFOURCC('B', 'C', '4', 'U')     # = 'A', 'T', 'I', '1'
    DDS_BC4S = 0X53344342  # GS_MAKEFOURCC('B', 'C', '4', 'S')
    DDS_ATI2 = 0X55354342  # GS_MAKEFOURCC('A', 'T', 'I', '2')     # = 'B', 'C', '5', 'U'
    DDS_BC5 = 0X55354342  # GS_MAKEFOURCC('B', 'C', '5', 'U')     # = 'A', 'T', 'I', '2'
    DDS_BC5S = 0X53354342  # GS_MAKEFOURCC('B', 'C', '5', 'S')
    DDS_DX10 = 0X30315844  # GS_MAKEFOURCC('D', 'X', '1', '0')
    DDS_D16_LOCKABLE = 70
    DDS_D32 = 71
    DDS_D15S1 = 73
    DDS_D24S8 = 75
    DDS_D24X8 = 77
    DDS_D24X4S4 = 79
    DDS_D16 = 80
    DDS_D32F_LOCKABLE = 82
    DDS_D24FS8 = 83
    DDS_L16 = 81
    DDS_VERTEXDATA = 100
    DDS_INDEX16 = 101
    DDS_INDEX32 = 102
    DDS_Q16W16V16U16 = 110
    DDS_MULTI2_ARGB8 = 0X3154454D  # GS_MAKEFOURCC('M','E','T','1')
    # Floating point surface formats
    # s10e5 formats (16-bits per channel)
    DDS_R16F = 111
    DDS_G16R16F = 112
    DDS_A16B16G16R16F = 113
    # IEEE s23e8 formats (32-bits per channel)
    DDS_R32F = 114
    DDS_G32R32F = 115
    DDS_A32B32G32R32F = 116
    DDS_CxV8U8 = 117
    DDS_FORCE_DWORD = 0X7fffffff


class DDS_EXTENDED_FLAGS:
    """ GIANTS specific extended flags (stored in reserved1[2] of the dds header) """

    DDS_EXTENDED_FLIPPED_Y = 0X00000001  # 1U<<0
    DDS_EXTENDED_ALLOW_RAW = 0X00000002  # 1U<<1


class DDSResourceDimensions:
    """ DDS_RESOURCE_DIMENSION_TEXTURE1D values"""

    DDS_RESOURCE_DIMENSION_TEXTURE1D = 2
    DDS_RESOURCE_DIMENSION_TEXTURE2D = 3
    DDS_RESOURCE_DIMENSION_TEXTURE3D = 4


def readData(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data


class DataReader:
    def __init__(self, data: bytes):
        self.data = data
        self.index = 0

    def STR(self, length=None) -> str:
        if length is None:
            length = self.UINT32()
        value = self.data[self.index:self.index + length].decode('utf-8')
        self.index += length
        if length % 4 != 0:
            self.index += 4 - length % 4
        return value

    def UINT32(self) -> np.uint32:
        value = struct.unpack('@I', self.data[self.index:self.index + 4])[0]
        self.index += 4
        return np.uint32(value)

    def FLOAT16(self) -> np.float16:
        value = struct.unpack('@e', self.data[self.index:self.index + 2])[0]
        self.index += 2
        return np.float16(value)


class DDSFile:
    def __init__(self, data: str):
        self._reader = DataReader(data)
        self._magic = self._reader.STR(4)
        self._header_size = self._reader.UINT32()
        self._flags = self._readFlags(self._reader.UINT32())
        self._height = self._reader.UINT32()
        self._width = self._reader.UINT32()
        self._pitch_or_linear_size = self._reader.UINT32()  # TODO maybe read this
        self._depth = self._reader.UINT32()
        self._mip_map_count = self._reader.UINT32()
        self._reserved1 = self._read_n_times(11, 'UINT32')
        self._pixel_format: Dict[str, np.uint32] = self._readPixelFormat()
        self._caps = self._reader.UINT32()
        self._caps2 = self._reader.UINT32()
        self._caps3 = self._reader.UINT32()
        self._caps4 = self._reader.UINT32()
        self._reserved2 = self._reader.UINT32()
        self._dx10_header: Union[Dict[str, np.uint32], None] = None
        self._configuration: Union[Dict[str, Union[bool, int, None]], None] = None
        self._objects: Union[Dict[str, Dict[str, List[List[np.float16]]]], None] = None

        if self._pixel_format['flags'] == Flags.DDPF_FOURCC and self._pixel_format['four_cc'] == DDSPixelFormats.DDS_DX10:
            self._dx10_header = self._read_dx10_header()

        self._data_len = 4 * self._dx10_header['array_size'] * self._width * self._height if self._dx10_header is not None else 0

        if self._data_len > 0:
            self._data: List[np.float16] = self._get_data()
            self._configuration = self._get_configuration()
            if self._configuration is not None:
                self._objects = self._get_objects()

    # TODO refractor this
    def _get_objects(self) -> Dict[str, Dict[str, List[List[np.float16]]]]:
        number_of_poses = self.configuration['number_of_poses']
        number_of_parents = self.configuration['number_of_parents']
        max_num_of_objects = self.configuration['max_num_of_objects']
        objects_dict: Dict = dict()
        loc: List[List[np.float16]] = list()
        rot: List[List[np.float16]] = list()
        sca: List[List[np.float16]] = list()
        just_loc: List[List[np.float16]] = list()

        location = list()
        rotation = list()
        scale = list()

        for idx in range(number_of_poses):
            loc.clear()
            rot.clear()
            sca.clear()
            location.clear()
            rotation.clear()
            scale.clear()

            current_pose = idx * 4 * number_of_parents * max_num_of_objects * (3 if self.configuration['scale'] else 2)
            for idx2, obj_idx in enumerate(range(0, number_of_parents * max_num_of_objects * 4, 4)):
                location.append(self._data[current_pose + obj_idx:current_pose + obj_idx + 4])
                location2 = self._data[current_pose + obj_idx:current_pose + obj_idx + 4]
                rotation.append(self._data[current_pose + number_of_parents * max_num_of_objects * 4 + obj_idx:current_pose + number_of_parents * max_num_of_objects * 4 + obj_idx + 4])
                if self.configuration['scale']:
                    scale.append(self._data[current_pose + 2 * number_of_parents * max_num_of_objects * 4 + obj_idx:current_pose + 2 * number_of_parents * max_num_of_objects * 4 + obj_idx + 4])
                else:
                    sca.append([1.0, 1.0, 1.0, 1.0])

                just_loc.append(location2[3])
                if idx2 % max_num_of_objects == max_num_of_objects - 1:
                    loc = location + loc
                    rot = rotation + rot
                    if self.configuration['scale']:
                        sca = scale + sca
                    location.clear()
                    rotation.clear()
                    scale.clear()

            objects_dict['pose' + str(idx)] = {'location': loc.copy(), 'rotation': rot.copy(), 'scale': sca.copy()}

        # split just_loc into parents
        just_loc = [just_loc[i:i + max_num_of_objects] for i in range(0, len(just_loc), max_num_of_objects)]

        max_idx, max_sum = max(enumerate(map(sum, just_loc)), key=lambda x: x[1])

        if just_loc[max_idx][0] == 0.0 and just_loc[max_idx][-1] == 0.0:
            self._configuration['hide_first_and_last'] = True
        else:
            self._configuration['hide_first_and_last'] = False

        return objects_dict

    def _get_configuration(self) -> Dict[str, Union[bool, int, None]]:
        number_of_parents = self._height
        number_of_objects = self._width

        scale_w = [int(self._data[i] == 1.0) for i in range(-1, -1 * number_of_objects * 4, -4)]
        scale = all(scale_w)

        if scale:
            number_of_poses = self._dx10_header['array_size'] / 3
        else:
            number_of_poses = self._dx10_header['array_size'] / 2

        return {'location': True,
                'rotation': True,
                'scale': scale,
                'hide_first_and_last': None,
                'number_of_parents': int(number_of_parents),
                'max_num_of_objects': int(number_of_objects),
                'number_of_poses': int(number_of_poses),
                }

    def _get_data(self) -> List[np.float16]:
        return [self._reader.FLOAT16() for _ in range(self._data_len)]

    def _read_n_times(self, n, byte_type) -> List:
        return [getattr(self._reader, byte_type)() for _ in range(n)]

    def _readPixelFormat(self) -> Dict[str, np.uint32]:
        return {
            'size': self._reader.UINT32(),
            'flags': self._reader.UINT32(),
            'four_cc': self._reader.UINT32(),
            'rgb_bit_count': self._reader.UINT32(),
            'r_bit_mask': self._reader.UINT32(),
            'g_bit_mask': self._reader.UINT32(),
            'b_bit_mask': self._reader.UINT32(),
            'a_bit_mask': self._reader.UINT32(),
        }

    def _read_dx10_header(self) -> Dict[str, np.uint32]:
        return {
            'dxgi_format': self._reader.UINT32(),
            'resource_dimension': self._reader.UINT32(),
            'misc_flag': self._reader.UINT32(),
            'array_size': self._reader.UINT32(),
            'misc_flags2': self._reader.UINT32(),
        }

    @staticmethod
    def _readFlags(flags) -> Dict[str, bool]:
        return {
            'caps': bool(flags & 0x00000001),
            'height': bool(flags & 0x00000002),
            'width': bool(flags & 0x00000004),
            'pixel_format': bool(flags & 0X00001000),
        }

    @property
    def configuration(self) -> Union[Dict[str, Union[bool, int, None]], None]:
        return self._configuration

    @property
    def objects(self) -> Union[Dict[str, Dict[str, List[List[np.float16]]]], None]:
        return self._objects


if __name__ == '__main__':
    index = 0
    file_data = readData('aaa.dds')

    dds_file = DDSFile(file_data)

    print(dds_file.objects)
    print(dds_file.configuration)

# list = ['BezierCurve_Y_000', 'BezierCurve_Y_000.006']
# print(sorted(list, key=lambda x: x))
# print()
# if dds_file.objects is not None:
#     for key, value in dds_file.objects.items():
#         print(key)
#         for k, v in value.items():
#             print(k)
#             for i in range(0, len(v), dds_file.configuration['max_num_of_objects']):
#                 print(v[i:i + dds_file.configuration['max_num_of_objects']])
#         print()
