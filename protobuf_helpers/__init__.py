from collections import OrderedDict

from clang.cindex import TypeKind


CLANG_TYPE_KIND_TO_PROTOBUF_TYPE = OrderedDict([
    (TypeKind.BOOL, 'bool'),
    (TypeKind.CHAR_S, 'sint32'),
    (TypeKind.CHAR_U, 'uint32'),
    (TypeKind.FLOAT, 'float'),
    (TypeKind.INT, 'sint32'),
    (TypeKind.LONGLONG, 'sint64'),
    (TypeKind.SHORT, 'sint32'),
    (TypeKind.UCHAR, 'uint32'),
    (TypeKind.UINT, 'uint32'),
    (TypeKind.ULONGLONG, 'uint64'),
    (TypeKind.USHORT, 'uint32'),
    (TypeKind.VOID, None)])
