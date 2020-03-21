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
    AccessLevel: Optional[str]
    AccessState: Optional[str]
    AccessTo: Optional[str]
    AccessType: Optional[str]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    ExportLocation: Optional[str]
    ExportLocations: Optional[Sequence[str]]
    Host: Optional[str]
    IsPublic: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Region: Optional[str]
    ShareAccessId: Optional[str]
    ShareProto: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
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
            AccessLevel=json_data.get("AccessLevel"),
            AccessState=json_data.get("AccessState"),
            AccessTo=json_data.get("AccessTo"),
            AccessType=json_data.get("AccessType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            ExportLocation=json_data.get("ExportLocation"),
            ExportLocations=json_data.get("ExportLocations"),
            Host=json_data.get("Host"),
            IsPublic=json_data.get("IsPublic"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ShareAccessId=json_data.get("ShareAccessId"),
            ShareProto=json_data.get("ShareProto"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


