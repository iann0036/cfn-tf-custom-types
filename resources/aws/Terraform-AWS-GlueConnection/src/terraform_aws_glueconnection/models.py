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
    CatalogId: Optional[str]
    ConnectionProperties: Optional[Sequence["_ConnectionProperties"]]
    ConnectionType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    MatchCriteria: Optional[Sequence[str]]
    Name: Optional[str]
    PhysicalConnectionRequirements: Optional[Sequence["_PhysicalConnectionRequirements"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CatalogId=json_data.get("CatalogId"),
            ConnectionProperties=json_data.get("ConnectionProperties"),
            ConnectionType=json_data.get("ConnectionType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Name=json_data.get("Name"),
            PhysicalConnectionRequirements=json_data.get("PhysicalConnectionRequirements"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionProperties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionProperties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionProperties = ConnectionProperties


@dataclass
class PhysicalConnectionRequirements:
    AvailabilityZone: Optional[str]
    SecurityGroupIdList: Optional[Sequence[str]]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhysicalConnectionRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhysicalConnectionRequirements"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            SecurityGroupIdList=json_data.get("SecurityGroupIdList"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhysicalConnectionRequirements = PhysicalConnectionRequirements


