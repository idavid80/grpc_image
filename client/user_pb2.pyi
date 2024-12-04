from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserRequest(_message.Message):
    __slots__ = ("name", "pow", "image")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POW_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    pow: int
    image: bytes
    def __init__(self, name: _Optional[str] = ..., pow: _Optional[int] = ..., image: _Optional[bytes] = ...) -> None: ...

class GetAllReply(_message.Message):
    __slots__ = ("name", "pow", "image")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POW_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    pow: int
    image: bytes
    def __init__(self, name: _Optional[str] = ..., pow: _Optional[int] = ..., image: _Optional[bytes] = ...) -> None: ...

class GetUserReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetImage(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    def __init__(self, image: _Optional[bytes] = ...) -> None: ...

class GetImageReply(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    def __init__(self, image: _Optional[bytes] = ...) -> None: ...
