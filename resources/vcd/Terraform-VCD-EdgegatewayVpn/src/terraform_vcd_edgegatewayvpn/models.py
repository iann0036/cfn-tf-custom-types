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
    Description: Optional[str]
    EdgeGateway: Optional[str]
    EncryptionProtocol: Optional[str]
    Id: Optional[str]
    LocalId: Optional[str]
    LocalIpAddress: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    Org: Optional[str]
    PeerId: Optional[str]
    PeerIpAddress: Optional[str]
    SharedSecret: Optional[str]
    Vdc: Optional[str]
    LocalSubnets: Optional[Sequence["_LocalSubnets"]]
    PeerSubnets: Optional[Sequence["_PeerSubnets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            EdgeGateway=json_data.get("EdgeGateway"),
            EncryptionProtocol=json_data.get("EncryptionProtocol"),
            Id=json_data.get("Id"),
            LocalId=json_data.get("LocalId"),
            LocalIpAddress=json_data.get("LocalIpAddress"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            PeerId=json_data.get("PeerId"),
            PeerIpAddress=json_data.get("PeerIpAddress"),
            SharedSecret=json_data.get("SharedSecret"),
            Vdc=json_data.get("Vdc"),
            LocalSubnets=json_data.get("LocalSubnets"),
            PeerSubnets=json_data.get("PeerSubnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocalSubnets:
    LocalSubnetGateway: Optional[str]
    LocalSubnetMask: Optional[str]
    LocalSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSubnets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSubnets"]:
        if not json_data:
            return None
        return cls(
            LocalSubnetGateway=json_data.get("LocalSubnetGateway"),
            LocalSubnetMask=json_data.get("LocalSubnetMask"),
            LocalSubnetName=json_data.get("LocalSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSubnets = LocalSubnets


@dataclass
class PeerSubnets:
    PeerSubnetGateway: Optional[str]
    PeerSubnetMask: Optional[str]
    PeerSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeerSubnets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerSubnets"]:
        if not json_data:
            return None
        return cls(
            PeerSubnetGateway=json_data.get("PeerSubnetGateway"),
            PeerSubnetMask=json_data.get("PeerSubnetMask"),
            PeerSubnetName=json_data.get("PeerSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerSubnets = PeerSubnets


