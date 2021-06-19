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
    EndpointLocation: Optional[str]
    EndpointMonitorStatus: Optional[str]
    EndpointStatus: Optional[str]
    GeoMappings: Optional[Sequence[str]]
    Id: Optional[str]
    MinChildEndpoints: Optional[float]
    Name: Optional[str]
    Priority: Optional[float]
    ProfileName: Optional[str]
    ResourceGroupName: Optional[str]
    Target: Optional[str]
    TargetResourceId: Optional[str]
    Type: Optional[str]
    Weight: Optional[float]
    CustomHeader: Optional[Sequence["_CustomHeaderDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
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
            EndpointLocation=json_data.get("EndpointLocation"),
            EndpointMonitorStatus=json_data.get("EndpointMonitorStatus"),
            EndpointStatus=json_data.get("EndpointStatus"),
            GeoMappings=json_data.get("GeoMappings"),
            Id=json_data.get("Id"),
            MinChildEndpoints=json_data.get("MinChildEndpoints"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ProfileName=json_data.get("ProfileName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Target=json_data.get("Target"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
            CustomHeader=deserialize_list(json_data.get("CustomHeader"), CustomHeaderDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class SubnetDefinition(BaseModel):
    First: Optional[str]
    Last: Optional[str]
    Scope: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            First=json_data.get("First"),
            Last=json_data.get("Last"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


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


