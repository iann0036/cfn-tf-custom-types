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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ScaleUnit: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    VirtualHubId: Optional[str]
    VpnServerConfigurationId: Optional[str]
    ConnectionConfiguration: Optional[Sequence["_ConnectionConfiguration"]]
    Timeouts: Optional["_Timeouts"]
    VpnClientAddressPool: Optional[Sequence["_VpnClientAddressPool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScaleUnit=json_data.get("ScaleUnit"),
            Tags=json_data.get("Tags"),
            VirtualHubId=json_data.get("VirtualHubId"),
            VpnServerConfigurationId=json_data.get("VpnServerConfigurationId"),
            ConnectionConfiguration=json_data.get("ConnectionConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VpnClientAddressPool=json_data.get("VpnClientAddressPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ConnectionConfiguration:
    Name: Optional[str]
    VpnClientAddressPool: Optional[Sequence["_VpnClientAddressPool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            VpnClientAddressPool=json_data.get("VpnClientAddressPool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionConfiguration = ConnectionConfiguration


@dataclass
class VpnClientAddressPool:
    AddressPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpnClientAddressPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnClientAddressPool"]:
        if not json_data:
            return None
        return cls(
            AddressPrefixes=json_data.get("AddressPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnClientAddressPool = VpnClientAddressPool


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


