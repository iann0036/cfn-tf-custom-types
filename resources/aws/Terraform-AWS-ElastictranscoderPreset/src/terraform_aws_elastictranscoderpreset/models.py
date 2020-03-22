# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Container: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    VideoCodecOptions: Optional[Sequence["_VideoCodecOptions"]]
    Audio: Optional[Sequence["_Audio"]]
    AudioCodecOptions: Optional[Sequence["_AudioCodecOptions"]]
    Thumbnails: Optional[Sequence["_Thumbnails"]]
    Video: Optional[Sequence["_Video"]]
    VideoWatermarks: Optional[Sequence["_VideoWatermarks"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Container=json_data.get("Container"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            VideoCodecOptions=json_data.get("VideoCodecOptions"),
            Audio=json_data.get("Audio"),
            AudioCodecOptions=json_data.get("AudioCodecOptions"),
            Thumbnails=json_data.get("Thumbnails"),
            Video=json_data.get("Video"),
            VideoWatermarks=json_data.get("VideoWatermarks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VideoCodecOptions:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoCodecOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoCodecOptions"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoCodecOptions = VideoCodecOptions


@dataclass
class Audio:
    AudioPackingMode: Optional[str]
    BitRate: Optional[str]
    Channels: Optional[str]
    Codec: Optional[str]
    SampleRate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Audio"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Audio"]:
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
_Audio = Audio


@dataclass
class AudioCodecOptions:
    BitDepth: Optional[str]
    BitOrder: Optional[str]
    Profile: Optional[str]
    Signed: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioCodecOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioCodecOptions"]:
        if not json_data:
            return None
        return cls(
            BitDepth=json_data.get("BitDepth"),
            BitOrder=json_data.get("BitOrder"),
            Profile=json_data.get("Profile"),
            Signed=json_data.get("Signed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioCodecOptions = AudioCodecOptions


@dataclass
class Thumbnails:
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
        cls: Type["_Thumbnails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Thumbnails"]:
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
_Thumbnails = Thumbnails


@dataclass
class Video:
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
        cls: Type["_Video"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Video"]:
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
_Video = Video


@dataclass
class VideoWatermarks:
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
        cls: Type["_VideoWatermarks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoWatermarks"]:
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
_VideoWatermarks = VideoWatermarks


