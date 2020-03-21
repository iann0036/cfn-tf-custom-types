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
    EndpointLocation: Optional[str]
    EndpointMonitorStatus: Optional[str]
    EndpointStatus: Optional[str]
    GeoMappings: Optional[Sequence[str]]
    MinChildEndpoints: Optional[float]
    Name: Optional[str]
    Priority: Optional[float]
    ProfileName: Optional[str]
    ResourceGroupName: Optional[str]
    Target: Optional[str]
    TargetResourceId: Optional[str]
    Type: Optional[str]
    Weight: Optional[float]
    CustomHeader: Optional[Sequence["_CustomHeader"]]
    Subnet: Optional[Sequence["_Subnet"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EndpointLocation=json_data.get("EndpointLocation"),
            EndpointMonitorStatus=json_data.get("EndpointMonitorStatus"),
            EndpointStatus=json_data.get("EndpointStatus"),
            GeoMappings=json_data.get("GeoMappings"),
            MinChildEndpoints=json_data.get("MinChildEndpoints"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ProfileName=json_data.get("ProfileName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Target=json_data.get("Target"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
            CustomHeader=json_data.get("CustomHeader"),
            Subnet=json_data.get("Subnet"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomHeader:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeader = CustomHeader


@dataclass
class Subnet:
    First: Optional[str]
    Last: Optional[str]
    Scope: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet"]:
        if not json_data:
            return None
        return cls(
            First=json_data.get("First"),
            Last=json_data.get("Last"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet = Subnet


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


