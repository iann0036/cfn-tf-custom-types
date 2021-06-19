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
    Fqdn: Optional[str]
    Id: Optional[str]
    MaxReturn: Optional[float]
    Name: Optional[str]
    ProfileStatus: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TrafficRoutingMethod: Optional[str]
    TrafficViewEnabled: Optional[bool]
    DnsConfig: Optional[Sequence["_DnsConfigDefinition"]]
    MonitorConfig: Optional[Sequence["_MonitorConfigDefinition"]]
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
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            MaxReturn=json_data.get("MaxReturn"),
            Name=json_data.get("Name"),
            ProfileStatus=json_data.get("ProfileStatus"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TrafficRoutingMethod=json_data.get("TrafficRoutingMethod"),
            TrafficViewEnabled=json_data.get("TrafficViewEnabled"),
            DnsConfig=deserialize_list(json_data.get("DnsConfig"), DnsConfigDefinition),
            MonitorConfig=deserialize_list(json_data.get("MonitorConfig"), MonitorConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class DnsConfigDefinition(BaseModel):
    RelativeName: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RelativeName=json_data.get("RelativeName"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigDefinition = DnsConfigDefinition


@dataclass
class MonitorConfigDefinition(BaseModel):
    ExpectedStatusCodeRanges: Optional[Sequence[str]]
    IntervalInSeconds: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TimeoutInSeconds: Optional[float]
    ToleratedNumberOfFailures: Optional[float]
    CustomHeader: Optional[Sequence["_CustomHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedStatusCodeRanges=json_data.get("ExpectedStatusCodeRanges"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            ToleratedNumberOfFailures=json_data.get("ToleratedNumberOfFailures"),
            CustomHeader=deserialize_list(json_data.get("CustomHeader"), CustomHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorConfigDefinition = MonitorConfigDefinition


@dataclass
class CustomHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeaderDefinition = CustomHeaderDefinition


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


