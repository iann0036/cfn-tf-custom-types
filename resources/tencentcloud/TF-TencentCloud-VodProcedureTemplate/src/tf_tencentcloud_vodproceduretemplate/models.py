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
    Id: Optional[str]
    Name: Optional[str]
    SubAppId: Optional[float]
    UpdateTime: Optional[str]
    MediaProcessTask: Optional[Sequence["_MediaProcessTaskDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SubAppId=json_data.get("SubAppId"),
            UpdateTime=json_data.get("UpdateTime"),
            MediaProcessTask=deserialize_list(json_data.get("MediaProcessTask"), MediaProcessTaskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MediaProcessTaskDefinition(BaseModel):
    AdaptiveDynamicStreamingTaskList: Optional[Sequence["_AdaptiveDynamicStreamingTaskListDefinition"]]
    AnimatedGraphicTaskList: Optional[Sequence["_AnimatedGraphicTaskListDefinition"]]
    CoverBySnapshotTaskList: Optional[Sequence["_CoverBySnapshotTaskListDefinition"]]
    ImageSpriteTaskList: Optional[Sequence["_ImageSpriteTaskListDefinition"]]
    SampleSnapshotTaskList: Optional[Sequence["_SampleSnapshotTaskListDefinition"]]
    SnapshotByTimeOffsetTaskList: Optional[Sequence["_SnapshotByTimeOffsetTaskListDefinition"]]
    TranscodeTaskList: Optional[Sequence["_TranscodeTaskListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MediaProcessTaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MediaProcessTaskDefinition"]:
        if not json_data:
            return None
        return cls(
            AdaptiveDynamicStreamingTaskList=deserialize_list(json_data.get("AdaptiveDynamicStreamingTaskList"), AdaptiveDynamicStreamingTaskListDefinition),
            AnimatedGraphicTaskList=deserialize_list(json_data.get("AnimatedGraphicTaskList"), AnimatedGraphicTaskListDefinition),
            CoverBySnapshotTaskList=deserialize_list(json_data.get("CoverBySnapshotTaskList"), CoverBySnapshotTaskListDefinition),
            ImageSpriteTaskList=deserialize_list(json_data.get("ImageSpriteTaskList"), ImageSpriteTaskListDefinition),
            SampleSnapshotTaskList=deserialize_list(json_data.get("SampleSnapshotTaskList"), SampleSnapshotTaskListDefinition),
            SnapshotByTimeOffsetTaskList=deserialize_list(json_data.get("SnapshotByTimeOffsetTaskList"), SnapshotByTimeOffsetTaskListDefinition),
            TranscodeTaskList=deserialize_list(json_data.get("TranscodeTaskList"), TranscodeTaskListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MediaProcessTaskDefinition = MediaProcessTaskDefinition


@dataclass
class AdaptiveDynamicStreamingTaskListDefinition(BaseModel):
    Definition: Optional[str]
    WatermarkList: Optional[Sequence["_WatermarkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdaptiveDynamicStreamingTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdaptiveDynamicStreamingTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            WatermarkList=deserialize_list(json_data.get("WatermarkList"), WatermarkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdaptiveDynamicStreamingTaskListDefinition = AdaptiveDynamicStreamingTaskListDefinition


@dataclass
class WatermarkListDefinition(BaseModel):
    Definition: Optional[str]
    EndTimeOffset: Optional[float]
    StartTimeOffset: Optional[float]
    SvgContent: Optional[str]
    TextContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarkListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            EndTimeOffset=json_data.get("EndTimeOffset"),
            StartTimeOffset=json_data.get("StartTimeOffset"),
            SvgContent=json_data.get("SvgContent"),
            TextContent=json_data.get("TextContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WatermarkListDefinition = WatermarkListDefinition


@dataclass
class AnimatedGraphicTaskListDefinition(BaseModel):
    Definition: Optional[str]
    EndTimeOffset: Optional[float]
    StartTimeOffset: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AnimatedGraphicTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnimatedGraphicTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            EndTimeOffset=json_data.get("EndTimeOffset"),
            StartTimeOffset=json_data.get("StartTimeOffset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnimatedGraphicTaskListDefinition = AnimatedGraphicTaskListDefinition


@dataclass
class CoverBySnapshotTaskListDefinition(BaseModel):
    Definition: Optional[str]
    PositionType: Optional[str]
    PositionValue: Optional[float]
    WatermarkList: Optional[Sequence["_WatermarkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CoverBySnapshotTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoverBySnapshotTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            PositionType=json_data.get("PositionType"),
            PositionValue=json_data.get("PositionValue"),
            WatermarkList=deserialize_list(json_data.get("WatermarkList"), WatermarkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoverBySnapshotTaskListDefinition = CoverBySnapshotTaskListDefinition


@dataclass
class ImageSpriteTaskListDefinition(BaseModel):
    Definition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageSpriteTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageSpriteTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageSpriteTaskListDefinition = ImageSpriteTaskListDefinition


@dataclass
class SampleSnapshotTaskListDefinition(BaseModel):
    Definition: Optional[str]
    WatermarkList: Optional[Sequence["_WatermarkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SampleSnapshotTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SampleSnapshotTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            WatermarkList=deserialize_list(json_data.get("WatermarkList"), WatermarkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SampleSnapshotTaskListDefinition = SampleSnapshotTaskListDefinition


@dataclass
class SnapshotByTimeOffsetTaskListDefinition(BaseModel):
    Definition: Optional[str]
    ExtTimeOffsetList: Optional[Sequence[str]]
    WatermarkList: Optional[Sequence["_WatermarkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotByTimeOffsetTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotByTimeOffsetTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            ExtTimeOffsetList=json_data.get("ExtTimeOffsetList"),
            WatermarkList=deserialize_list(json_data.get("WatermarkList"), WatermarkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotByTimeOffsetTaskListDefinition = SnapshotByTimeOffsetTaskListDefinition


@dataclass
class TranscodeTaskListDefinition(BaseModel):
    Definition: Optional[str]
    MosaicList: Optional[Sequence["_MosaicListDefinition"]]
    WatermarkList: Optional[Sequence["_WatermarkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TranscodeTaskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranscodeTaskListDefinition"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
            MosaicList=deserialize_list(json_data.get("MosaicList"), MosaicListDefinition),
            WatermarkList=deserialize_list(json_data.get("WatermarkList"), WatermarkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranscodeTaskListDefinition = TranscodeTaskListDefinition


@dataclass
class MosaicListDefinition(BaseModel):
    CoordinateOrigin: Optional[str]
    EndTimeOffset: Optional[float]
    Height: Optional[str]
    StartTimeOffset: Optional[float]
    Width: Optional[str]
    XPos: Optional[str]
    YPos: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MosaicListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MosaicListDefinition"]:
        if not json_data:
            return None
        return cls(
            CoordinateOrigin=json_data.get("CoordinateOrigin"),
            EndTimeOffset=json_data.get("EndTimeOffset"),
            Height=json_data.get("Height"),
            StartTimeOffset=json_data.get("StartTimeOffset"),
            Width=json_data.get("Width"),
            XPos=json_data.get("XPos"),
            YPos=json_data.get("YPos"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MosaicListDefinition = MosaicListDefinition


