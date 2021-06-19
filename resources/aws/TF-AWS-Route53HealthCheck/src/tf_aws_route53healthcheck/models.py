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
    ChildHealthThreshold: Optional[float]
    ChildHealthchecks: Optional[Sequence[str]]
    CloudwatchAlarmName: Optional[str]
    CloudwatchAlarmRegion: Optional[str]
    Disabled: Optional[bool]
    EnableSni: Optional[bool]
    FailureThreshold: Optional[float]
    Fqdn: Optional[str]
    Id: Optional[str]
    InsufficientDataHealthStatus: Optional[str]
    InvertHealthcheck: Optional[bool]
    IpAddress: Optional[str]
    MeasureLatency: Optional[bool]
    Port: Optional[float]
    ReferenceName: Optional[str]
    Regions: Optional[Sequence[str]]
    RequestInterval: Optional[float]
    ResourcePath: Optional[str]
    SearchString: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]

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
            ChildHealthThreshold=json_data.get("ChildHealthThreshold"),
            ChildHealthchecks=json_data.get("ChildHealthchecks"),
            CloudwatchAlarmName=json_data.get("CloudwatchAlarmName"),
            CloudwatchAlarmRegion=json_data.get("CloudwatchAlarmRegion"),
            Disabled=json_data.get("Disabled"),
            EnableSni=json_data.get("EnableSni"),
            FailureThreshold=json_data.get("FailureThreshold"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            InsufficientDataHealthStatus=json_data.get("InsufficientDataHealthStatus"),
            InvertHealthcheck=json_data.get("InvertHealthcheck"),
            IpAddress=json_data.get("IpAddress"),
            MeasureLatency=json_data.get("MeasureLatency"),
            Port=json_data.get("Port"),
            ReferenceName=json_data.get("ReferenceName"),
            Regions=json_data.get("Regions"),
            RequestInterval=json_data.get("RequestInterval"),
            ResourcePath=json_data.get("ResourcePath"),
            SearchString=json_data.get("SearchString"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


