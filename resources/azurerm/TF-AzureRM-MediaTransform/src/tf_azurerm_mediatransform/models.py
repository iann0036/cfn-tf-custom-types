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
    Description: Optional[str]
    Id: Optional[str]
    MediaServicesAccountName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Output: Optional[Sequence["_OutputDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MediaServicesAccountName=json_data.get("MediaServicesAccountName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Output=deserialize_list(json_data.get("Output"), OutputDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OutputDefinition(BaseModel):
    OnErrorAction: Optional[str]
    RelativePriority: Optional[str]
    AudioAnalyzerPreset: Optional[Sequence["_AudioAnalyzerPresetDefinition"]]
    BuiltinPreset: Optional[Sequence["_BuiltinPresetDefinition"]]
    FaceDetectorPreset: Optional[Sequence["_FaceDetectorPresetDefinition"]]
    VideoAnalyzerPreset: Optional[Sequence["_VideoAnalyzerPresetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinition"]:
        if not json_data:
            return None
        return cls(
            OnErrorAction=json_data.get("OnErrorAction"),
            RelativePriority=json_data.get("RelativePriority"),
            AudioAnalyzerPreset=deserialize_list(json_data.get("AudioAnalyzerPreset"), AudioAnalyzerPresetDefinition),
            BuiltinPreset=deserialize_list(json_data.get("BuiltinPreset"), BuiltinPresetDefinition),
            FaceDetectorPreset=deserialize_list(json_data.get("FaceDetectorPreset"), FaceDetectorPresetDefinition),
            VideoAnalyzerPreset=deserialize_list(json_data.get("VideoAnalyzerPreset"), VideoAnalyzerPresetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinition = OutputDefinition


@dataclass
class AudioAnalyzerPresetDefinition(BaseModel):
    AudioAnalysisMode: Optional[str]
    AudioLanguage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioAnalyzerPresetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioAnalyzerPresetDefinition"]:
        if not json_data:
            return None
        return cls(
            AudioAnalysisMode=json_data.get("AudioAnalysisMode"),
            AudioLanguage=json_data.get("AudioLanguage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioAnalyzerPresetDefinition = AudioAnalyzerPresetDefinition


@dataclass
class BuiltinPresetDefinition(BaseModel):
    PresetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BuiltinPresetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuiltinPresetDefinition"]:
        if not json_data:
            return None
        return cls(
            PresetName=json_data.get("PresetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuiltinPresetDefinition = BuiltinPresetDefinition


@dataclass
class FaceDetectorPresetDefinition(BaseModel):
    AnalysisResolution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FaceDetectorPresetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FaceDetectorPresetDefinition"]:
        if not json_data:
            return None
        return cls(
            AnalysisResolution=json_data.get("AnalysisResolution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FaceDetectorPresetDefinition = FaceDetectorPresetDefinition


@dataclass
class VideoAnalyzerPresetDefinition(BaseModel):
    AudioAnalysisMode: Optional[str]
    AudioLanguage: Optional[str]
    InsightsType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoAnalyzerPresetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoAnalyzerPresetDefinition"]:
        if not json_data:
            return None
        return cls(
            AudioAnalysisMode=json_data.get("AudioAnalysisMode"),
            AudioLanguage=json_data.get("AudioLanguage"),
            InsightsType=json_data.get("InsightsType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoAnalyzerPresetDefinition = VideoAnalyzerPresetDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


