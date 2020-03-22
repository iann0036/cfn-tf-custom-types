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
    AcceptStatus: Optional[str]
    AutoAccept: Optional[bool]
    Id: Optional[str]
    PeerOwnerId: Optional[str]
    PeerRegion: Optional[str]
    PeerVpcId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    VpcPeeringConnectionId: Optional[str]
    Accepter: Optional[Sequence["_Accepter"]]
    Requester: Optional[Sequence["_Requester"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptStatus=json_data.get("AcceptStatus"),
            AutoAccept=json_data.get("AutoAccept"),
            Id=json_data.get("Id"),
            PeerOwnerId=json_data.get("PeerOwnerId"),
            PeerRegion=json_data.get("PeerRegion"),
            PeerVpcId=json_data.get("PeerVpcId"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
            Accepter=json_data.get("Accepter"),
            Requester=json_data.get("Requester"),
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
class Accepter:
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Accepter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Accepter"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Accepter = Accepter


@dataclass
class Requester:
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Requester"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Requester"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Requester = Requester


