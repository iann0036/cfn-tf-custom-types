# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Guest: Optional[Sequence["_GuestDefinition"]]
    GuestVoiceSignaling: Optional[Sequence["_GuestVoiceSignalingDefinition"]]
    Softphone: Optional[Sequence["_SoftphoneDefinition"]]
    StreamingVideo: Optional[Sequence["_StreamingVideoDefinition"]]
    VideoConferencing: Optional[Sequence["_VideoConferencingDefinition"]]
    VideoSignaling: Optional[Sequence["_VideoSignalingDefinition"]]
    Voice: Optional[Sequence["_VoiceDefinition"]]
    VoiceSignaling: Optional[Sequence["_VoiceSignalingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Guest=deserialize_list(json_data.get("Guest"), GuestDefinition),
            GuestVoiceSignaling=deserialize_list(json_data.get("GuestVoiceSignaling"), GuestVoiceSignalingDefinition),
            Softphone=deserialize_list(json_data.get("Softphone"), SoftphoneDefinition),
            StreamingVideo=deserialize_list(json_data.get("StreamingVideo"), StreamingVideoDefinition),
            VideoConferencing=deserialize_list(json_data.get("VideoConferencing"), VideoConferencingDefinition),
            VideoSignaling=deserialize_list(json_data.get("VideoSignaling"), VideoSignalingDefinition),
            Voice=deserialize_list(json_data.get("Voice"), VoiceDefinition),
            VoiceSignaling=deserialize_list(json_data.get("VoiceSignaling"), VoiceSignalingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GuestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestDefinition = GuestDefinition


@dataclass
class GuestVoiceSignalingDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GuestVoiceSignalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestVoiceSignalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestVoiceSignalingDefinition = GuestVoiceSignalingDefinition


@dataclass
class SoftphoneDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SoftphoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftphoneDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftphoneDefinition = SoftphoneDefinition


@dataclass
class StreamingVideoDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StreamingVideoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamingVideoDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamingVideoDefinition = StreamingVideoDefinition


@dataclass
class VideoConferencingDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VideoConferencingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoConferencingDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoConferencingDefinition = VideoConferencingDefinition


@dataclass
class VideoSignalingDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSignalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSignalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSignalingDefinition = VideoSignalingDefinition


@dataclass
class VoiceDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VoiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoiceDefinition = VoiceDefinition


@dataclass
class VoiceSignalingDefinition(BaseModel):
    Dscp: Optional[float]
    Priority: Optional[float]
    Status: Optional[str]
    Tag: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VoiceSignalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoiceSignalingDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoiceSignalingDefinition = VoiceSignalingDefinition


