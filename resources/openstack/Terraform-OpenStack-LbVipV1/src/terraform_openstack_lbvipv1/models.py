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
    Address: Optional[str]
    AdminStateUp: Optional[bool]
    ConnLimit: Optional[float]
    Description: Optional[str]
    FloatingIp: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Persistence: Optional[Sequence["_Persistence"]]
    PoolId: Optional[str]
    Port: Optional[float]
    PortId: Optional[str]
    Protocol: Optional[str]
    Region: Optional[str]
    SubnetId: Optional[str]
    TenantId: Optional[str]
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
            Address=json_data.get("Address"),
            AdminStateUp=json_data.get("AdminStateUp"),
            ConnLimit=json_data.get("ConnLimit"),
            Description=json_data.get("Description"),
            FloatingIp=json_data.get("FloatingIp"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Persistence=json_data.get("Persistence"),
            PoolId=json_data.get("PoolId"),
            Port=json_data.get("Port"),
            PortId=json_data.get("PortId"),
            Protocol=json_data.get("Protocol"),
            Region=json_data.get("Region"),
            SubnetId=json_data.get("SubnetId"),
            TenantId=json_data.get("TenantId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Persistence:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Persistence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Persistence"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Persistence = Persistence


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


