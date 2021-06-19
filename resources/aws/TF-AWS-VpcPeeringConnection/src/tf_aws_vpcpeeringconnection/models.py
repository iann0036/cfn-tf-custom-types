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
    AcceptStatus: Optional[str]
    AutoAccept: Optional[bool]
    Id: Optional[str]
    PeerOwnerId: Optional[str]
    PeerRegion: Optional[str]
    PeerVpcId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
    Accepter: Optional[Sequence["_AccepterDefinition"]]
    Requester: Optional[Sequence["_RequesterDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AcceptStatus=json_data.get("AcceptStatus"),
            AutoAccept=json_data.get("AutoAccept"),
            Id=json_data.get("Id"),
            PeerOwnerId=json_data.get("PeerOwnerId"),
            PeerRegion=json_data.get("PeerRegion"),
            PeerVpcId=json_data.get("PeerVpcId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            Accepter=deserialize_list(json_data.get("Accepter"), AccepterDefinition),
            Requester=deserialize_list(json_data.get("Requester"), RequesterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AccepterDefinition(BaseModel):
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccepterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccepterDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccepterDefinition = AccepterDefinition


@dataclass
class RequesterDefinition(BaseModel):
    AllowClassicLinkToRemoteVpc: Optional[bool]
    AllowRemoteVpcDnsResolution: Optional[bool]
    AllowVpcToRemoteClassicLink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequesterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequesterDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowClassicLinkToRemoteVpc=json_data.get("AllowClassicLinkToRemoteVpc"),
            AllowRemoteVpcDnsResolution=json_data.get("AllowRemoteVpcDnsResolution"),
            AllowVpcToRemoteClassicLink=json_data.get("AllowVpcToRemoteClassicLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequesterDefinition = RequesterDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


