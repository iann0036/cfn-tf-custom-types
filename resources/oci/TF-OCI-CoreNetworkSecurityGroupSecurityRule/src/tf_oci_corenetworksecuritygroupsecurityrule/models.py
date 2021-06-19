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
    Destination: Optional[str]
    DestinationType: Optional[str]
    Direction: Optional[str]
    Id: Optional[str]
    IsValid: Optional[bool]
    NetworkSecurityGroupId: Optional[str]
    Protocol: Optional[str]
    Source: Optional[str]
    SourceType: Optional[str]
    Stateless: Optional[bool]
    TimeCreated: Optional[str]
    IcmpOptions: Optional[Sequence["_IcmpOptionsDefinition"]]
    TcpOptions: Optional[Sequence["_TcpOptionsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UdpOptions: Optional[Sequence["_UdpOptionsDefinition"]]

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
            Destination=json_data.get("Destination"),
            DestinationType=json_data.get("DestinationType"),
            Direction=json_data.get("Direction"),
            Id=json_data.get("Id"),
            IsValid=json_data.get("IsValid"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourceType=json_data.get("SourceType"),
            Stateless=json_data.get("Stateless"),
            TimeCreated=json_data.get("TimeCreated"),
            IcmpOptions=deserialize_list(json_data.get("IcmpOptions"), IcmpOptionsDefinition),
            TcpOptions=deserialize_list(json_data.get("TcpOptions"), TcpOptionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UdpOptions=deserialize_list(json_data.get("UdpOptions"), UdpOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IcmpOptionsDefinition(BaseModel):
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpOptionsDefinition = IcmpOptionsDefinition


@dataclass
class TcpOptionsDefinition(BaseModel):
    DestinationPortRange: Optional[Sequence["_DestinationPortRangeDefinition"]]
    SourcePortRange: Optional[Sequence["_SourcePortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationPortRange=deserialize_list(json_data.get("DestinationPortRange"), DestinationPortRangeDefinition),
            SourcePortRange=deserialize_list(json_data.get("SourcePortRange"), SourcePortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpOptionsDefinition = TcpOptionsDefinition


@dataclass
class DestinationPortRangeDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortRangeDefinition = DestinationPortRangeDefinition


@dataclass
class SourcePortRangeDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortRangeDefinition = SourcePortRangeDefinition


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


@dataclass
class UdpOptionsDefinition(BaseModel):
    DestinationPortRange: Optional[Sequence["_DestinationPortRangeDefinition"]]
    SourcePortRange: Optional[Sequence["_SourcePortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UdpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationPortRange=deserialize_list(json_data.get("DestinationPortRange"), DestinationPortRangeDefinition),
            SourcePortRange=deserialize_list(json_data.get("SourcePortRange"), SourcePortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpOptionsDefinition = UdpOptionsDefinition


