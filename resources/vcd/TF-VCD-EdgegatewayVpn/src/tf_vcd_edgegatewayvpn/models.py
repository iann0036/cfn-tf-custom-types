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
    LocalSubnets: Optional[Sequence["_LocalSubnetsDefinition"]]
    PeerSubnets: Optional[Sequence["_PeerSubnetsDefinition"]]

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
            LocalSubnets=deserialize_list(json_data.get("LocalSubnets"), LocalSubnetsDefinition),
            PeerSubnets=deserialize_list(json_data.get("PeerSubnets"), PeerSubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocalSubnetsDefinition(BaseModel):
    LocalSubnetGateway: Optional[str]
    LocalSubnetMask: Optional[str]
    LocalSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalSubnetGateway=json_data.get("LocalSubnetGateway"),
            LocalSubnetMask=json_data.get("LocalSubnetMask"),
            LocalSubnetName=json_data.get("LocalSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSubnetsDefinition = LocalSubnetsDefinition


@dataclass
class PeerSubnetsDefinition(BaseModel):
    PeerSubnetGateway: Optional[str]
    PeerSubnetMask: Optional[str]
    PeerSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeerSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            PeerSubnetGateway=json_data.get("PeerSubnetGateway"),
            PeerSubnetMask=json_data.get("PeerSubnetMask"),
            PeerSubnetName=json_data.get("PeerSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerSubnetsDefinition = PeerSubnetsDefinition


