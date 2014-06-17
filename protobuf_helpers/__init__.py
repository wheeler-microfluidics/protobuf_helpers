from collections import OrderedDict

from path_helpers import path
from clang_helpers.clang.cindex import TypeKind


CLANG_TYPE_KIND_TO_PROTOBUF_TYPE = OrderedDict([
    (TypeKind.BOOL, 'bool'),
    (TypeKind.CHAR_S, 'sint32'),
    (TypeKind.SCHAR, 'sint32'),
    (TypeKind.CHAR_U, 'uint32'),
    (TypeKind.FLOAT, 'float'),
    (TypeKind.INT, 'sint32'),
    (TypeKind.LONG, 'sint32'),
    (TypeKind.LONGLONG, 'sint64'),
    (TypeKind.SHORT, 'sint32'),
    (TypeKind.UCHAR, 'uint32'),
    (TypeKind.UINT, 'uint32'),
    (TypeKind.ULONG, 'uint64'),
    (TypeKind.USHORT, 'uint32'),
    (TypeKind.VOID, None),
    ((TypeKind.POINTER, TypeKind.UCHAR), 'bytes')])


def underscore_to_camelcase(value):
    return ''.join(x.capitalize() if x else '_' for x in value.split('_'))


def get_protobuf_type(clang_type_kind):
    try:
        return CLANG_TYPE_KIND_TO_PROTOBUF_TYPE[clang_type_kind]
    except TypeError:
        # This is an array type.
        return (CLANG_TYPE_KIND_TO_PROTOBUF_TYPE[clang_type_kind['atom_type']],
                'repeated')


def package_path():
    return path(__file__).parent
