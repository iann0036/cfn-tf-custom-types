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
    Arn: Optional[str]
    Container: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    VideoCodecOptions: Optional[Sequence["_VideoCodecOptionsDefinition"]]
    Audio: Optional[Sequence["_AudioDefinition"]]
    AudioCodecOptions: Optional[Sequence["_AudioCodecOptionsDefinition"]]
    Thumbnails: Optional[Sequence["_ThumbnailsDefinition"]]
    Video: Optional[Sequence["_VideoDefinition"]]
    VideoWatermarks: Optional[Sequence["_VideoWatermarksDefinition"]]

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
            Arn=json_data.get("Arn"),
            Container=json_data.get("Container"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            VideoCodecOptions=deserialize_list(json_data.get("VideoCodecOptions"), VideoCodecOptionsDefinition),
            Audio=deserialize_list(json_data.get("Audio"), AudioDefinition),
            AudioCodecOptions=deserialize_list(json_data.get("AudioCodecOptions"), AudioCodecOptionsDefinition),
            Thumbnails=deserialize_list(json_data.get("Thumbnails"), ThumbnailsDefinition),
            Video=deserialize_list(json_data.get("Video"), VideoDefinition),
            VideoWatermarks=deserialize_list(json_data.get("VideoWatermarks"), VideoWatermarksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VideoCodecOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoCodecOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoCodecOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoCodecOptionsDefinition = VideoCodecOptionsDefinition


@dataclass
class AudioDefinition(BaseModel):
    AudioPackingMode: Optional[str]
    BitRate: Optional[str]
    Channels: Optional[str]
    Codec: Optional[str]
    SampleRate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioDefinition"]:
        if not json_data:
            return None
        return cls(
            AudioPackingMode=json_data.get("AudioPackingMode"),
            BitRate=json_data.get("BitRate"),
            Channels=json_data.get("Channels"),
            Codec=json_data.get("Codec"),
            SampleRate=json_data.get("SampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioDefinition = AudioDefinition


@dataclass
class AudioCodecOptionsDefinition(BaseModel):
    BitDepth: Optional[str]
    BitOrder: Optional[str]
    Profile: Optional[str]
    Signed: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioCodecOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioCodecOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            BitDepth=json_data.get("BitDepth"),
            BitOrder=json_data.get("BitOrder"),
            Profile=json_data.get("Profile"),
            Signed=json_data.get("Signed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioCodecOptionsDefinition = AudioCodecOptionsDefinition


@dataclass
class ThumbnailsDefinition(BaseModel):
    AspectRatio: Optional[str]
    Format: Optional[str]
    Interval: Optional[str]
    MaxHeight: Optional[str]
    MaxWidth: Optional[str]
    PaddingPolicy: Optional[str]
    Resolution: Optional[str]
    SizingPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AspectRatio=json_data.get("AspectRatio"),
            Format=json_data.get("Format"),
            Interval=json_data.get("Interval"),
            MaxHeight=json_data.get("MaxHeight"),
            MaxWidth=json_data.get("MaxWidth"),
            PaddingPolicy=json_data.get("PaddingPolicy"),
            Resolution=json_data.get("Resolution"),
            SizingPolicy=json_data.get("SizingPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailsDefinition = ThumbnailsDefinition


@dataclass
class VideoDefinition(BaseModel):
    AspectRatio: Optional[str]
    BitRate: Optional[str]
    Codec: Optional[str]
    DisplayAspectRatio: Optional[str]
    FixedGop: Optional[str]
    FrameRate: Optional[str]
    KeyframesMaxDist: Optional[str]
    MaxFrameRate: Optional[str]
    MaxHeight: Optional[str]
    MaxWidth: Optional[str]
    PaddingPolicy: Optional[str]
    Resolution: Optional[str]
    SizingPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoDefinition"]:
        if not json_data:
            return None
        return cls(
            AspectRatio=json_data.get("AspectRatio"),
            BitRate=json_data.get("BitRate"),
            Codec=json_data.get("Codec"),
            DisplayAspectRatio=json_data.get("DisplayAspectRatio"),
            FixedGop=json_data.get("FixedGop"),
            FrameRate=json_data.get("FrameRate"),
            KeyframesMaxDist=json_data.get("KeyframesMaxDist"),
            MaxFrameRate=json_data.get("MaxFrameRate"),
            MaxHeight=json_data.get("MaxHeight"),
            MaxWidth=json_data.get("MaxWidth"),
            PaddingPolicy=json_data.get("PaddingPolicy"),
            Resolution=json_data.get("Resolution"),
            SizingPolicy=json_data.get("SizingPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoDefinition = VideoDefinition


@dataclass
class VideoWatermarksDefinition(BaseModel):
    HorizontalAlign: Optional[str]
    HorizontalOffset: Optional[str]
    Id: Optional[str]
    MaxHeight: Optional[str]
    MaxWidth: Optional[str]
    Opacity: Optional[str]
    SizingPolicy: Optional[str]
    Target: Optional[str]
    VerticalAlign: Optional[str]
    VerticalOffset: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoWatermarksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoWatermarksDefinition"]:
        if not json_data:
            return None
        return cls(
            HorizontalAlign=json_data.get("HorizontalAlign"),
            HorizontalOffset=json_data.get("HorizontalOffset"),
            Id=json_data.get("Id"),
            MaxHeight=json_data.get("MaxHeight"),
            MaxWidth=json_data.get("MaxWidth"),
            Opacity=json_data.get("Opacity"),
            SizingPolicy=json_data.get("SizingPolicy"),
            Target=json_data.get("Target"),
            VerticalAlign=json_data.get("VerticalAlign"),
            VerticalOffset=json_data.get("VerticalOffset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoWatermarksDefinition = VideoWatermarksDefinition


