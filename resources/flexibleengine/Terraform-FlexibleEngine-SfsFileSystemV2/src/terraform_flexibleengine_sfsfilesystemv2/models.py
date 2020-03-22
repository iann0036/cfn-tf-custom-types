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
    AccessRuleStatus: Optional[str]
    AccessTo: Optional[str]
    AccessType: Optional[str]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    ExportLocation: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    IsPublic: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Region: Optional[str]
    ShareAccessId: Optional[str]
    ShareProto: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    VolumeType: Optional[str]
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
            AccessRuleStatus=json_data.get("AccessRuleStatus"),
            AccessTo=json_data.get("AccessTo"),
            AccessType=json_data.get("AccessType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            ExportLocation=json_data.get("ExportLocation"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            IsPublic=json_data.get("IsPublic"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ShareAccessId=json_data.get("ShareAccessId"),
            ShareProto=json_data.get("ShareProto"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            VolumeType=json_data.get("VolumeType"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
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


