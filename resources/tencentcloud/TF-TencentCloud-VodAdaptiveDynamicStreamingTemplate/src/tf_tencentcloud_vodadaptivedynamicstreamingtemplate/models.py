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
    CreateTime: Optional[str]
    DisableHigherVideoBitrate: Optional[bool]
    DisableHigherVideoResolution: Optional[bool]
    DrmType: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SubAppId: Optional[float]
    UpdateTime: Optional[str]
    StreamInfo: Optional[Sequence["_StreamInfoDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            DisableHigherVideoBitrate=json_data.get("DisableHigherVideoBitrate"),
            DisableHigherVideoResolution=json_data.get("DisableHigherVideoResolution"),
            DrmType=json_data.get("DrmType"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SubAppId=json_data.get("SubAppId"),
            UpdateTime=json_data.get("UpdateTime"),
            StreamInfo=deserialize_list(json_data.get("StreamInfo"), StreamInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StreamInfoDefinition(BaseModel):
    RemoveAudio: Optional[bool]
    Audio: Optional[Sequence["_AudioDefinition"]]
    Video: Optional[Sequence["_VideoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StreamInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            RemoveAudio=json_data.get("RemoveAudio"),
            Audio=deserialize_list(json_data.get("Audio"), AudioDefinition),
            Video=deserialize_list(json_data.get("Video"), VideoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamInfoDefinition = StreamInfoDefinition


@dataclass
class AudioDefinition(BaseModel):
    AudioChannel: Optional[str]
    Bitrate: Optional[float]
    Codec: Optional[str]
    SampleRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AudioDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioDefinition"]:
        if not json_data:
            return None
        return cls(
            AudioChannel=json_data.get("AudioChannel"),
            Bitrate=json_data.get("Bitrate"),
            Codec=json_data.get("Codec"),
            SampleRate=json_data.get("SampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioDefinition = AudioDefinition


@dataclass
class VideoDefinition(BaseModel):
    Bitrate: Optional[float]
    Codec: Optional[str]
    FillType: Optional[str]
    Fps: Optional[float]
    Height: Optional[float]
    ResolutionAdaptive: Optional[bool]
    Width: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VideoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoDefinition"]:
        if not json_data:
            return None
        return cls(
            Bitrate=json_data.get("Bitrate"),
            Codec=json_data.get("Codec"),
            FillType=json_data.get("FillType"),
            Fps=json_data.get("Fps"),
            Height=json_data.get("Height"),
            ResolutionAdaptive=json_data.get("ResolutionAdaptive"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoDefinition = VideoDefinition


