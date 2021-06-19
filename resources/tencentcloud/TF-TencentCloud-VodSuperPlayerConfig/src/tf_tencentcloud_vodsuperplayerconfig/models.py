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
    AdaptiveDynamicStreamingDefinition: Optional[str]
    Comment: Optional[str]
    CreateTime: Optional[str]
    Domain: Optional[str]
    DrmSwitch: Optional[bool]
    Id: Optional[str]
    ImageSpriteDefinition: Optional[str]
    Name: Optional[str]
    Scheme: Optional[str]
    SubAppId: Optional[float]
    UpdateTime: Optional[str]
    DrmStreamingInfo: Optional[Sequence["_DrmStreamingInfoDefinition"]]
    ResolutionNames: Optional[Sequence["_ResolutionNamesDefinition"]]

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
            AdaptiveDynamicStreamingDefinition=json_data.get("AdaptiveDynamicStreamingDefinition"),
            Comment=json_data.get("Comment"),
            CreateTime=json_data.get("CreateTime"),
            Domain=json_data.get("Domain"),
            DrmSwitch=json_data.get("DrmSwitch"),
            Id=json_data.get("Id"),
            ImageSpriteDefinition=json_data.get("ImageSpriteDefinition"),
            Name=json_data.get("Name"),
            Scheme=json_data.get("Scheme"),
            SubAppId=json_data.get("SubAppId"),
            UpdateTime=json_data.get("UpdateTime"),
            DrmStreamingInfo=deserialize_list(json_data.get("DrmStreamingInfo"), DrmStreamingInfoDefinition),
            ResolutionNames=deserialize_list(json_data.get("ResolutionNames"), ResolutionNamesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DrmStreamingInfoDefinition(BaseModel):
    SimpleAesDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DrmStreamingInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrmStreamingInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleAesDefinition=json_data.get("SimpleAesDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrmStreamingInfoDefinition = DrmStreamingInfoDefinition


@dataclass
class ResolutionNamesDefinition(BaseModel):
    MinEdgeLength: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResolutionNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolutionNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            MinEdgeLength=json_data.get("MinEdgeLength"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolutionNamesDefinition = ResolutionNamesDefinition


