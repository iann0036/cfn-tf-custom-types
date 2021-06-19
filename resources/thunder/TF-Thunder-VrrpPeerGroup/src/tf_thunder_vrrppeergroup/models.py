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
    Id: Optional[str]
    Uuid: Optional[str]
    Peer: Optional[Sequence["_PeerDefinition"]]

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
            Id=json_data.get("Id"),
            Uuid=json_data.get("Uuid"),
            Peer=deserialize_list(json_data.get("Peer"), PeerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PeerDefinition(BaseModel):
    IpPeerAddressCfg: Optional[Sequence["_IpPeerAddressCfgDefinition"]]
    Ipv6PeerAddressCfg: Optional[Sequence["_Ipv6PeerAddressCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerDefinition"]:
        if not json_data:
            return None
        return cls(
            IpPeerAddressCfg=deserialize_list(json_data.get("IpPeerAddressCfg"), IpPeerAddressCfgDefinition),
            Ipv6PeerAddressCfg=deserialize_list(json_data.get("Ipv6PeerAddressCfg"), Ipv6PeerAddressCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerDefinition = PeerDefinition


@dataclass
class IpPeerAddressCfgDefinition(BaseModel):
    IpPeerAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpPeerAddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPeerAddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpPeerAddress=json_data.get("IpPeerAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPeerAddressCfgDefinition = IpPeerAddressCfgDefinition


@dataclass
class Ipv6PeerAddressCfgDefinition(BaseModel):
    Ipv6PeerAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6PeerAddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6PeerAddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv6PeerAddress=json_data.get("Ipv6PeerAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6PeerAddressCfgDefinition = Ipv6PeerAddressCfgDefinition


