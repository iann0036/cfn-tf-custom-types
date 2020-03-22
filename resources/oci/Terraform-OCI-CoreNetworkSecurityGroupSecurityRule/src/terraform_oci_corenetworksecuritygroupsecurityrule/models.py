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
    IcmpOptions: Optional[Sequence["_IcmpOptions"]]
    TcpOptions: Optional[Sequence["_TcpOptions"]]
    Timeouts: Optional["_Timeouts"]
    UdpOptions: Optional[Sequence["_UdpOptions"]]
    DestinationPortRange: Optional[Sequence["_DestinationPortRange"]]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

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
            IcmpOptions=json_data.get("IcmpOptions"),
            TcpOptions=json_data.get("TcpOptions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            UdpOptions=json_data.get("UdpOptions"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IcmpOptions:
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpOptions"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpOptions = IcmpOptions


@dataclass
class TcpOptions:
    DestinationPortRange: Optional[Sequence["_DestinationPortRange"]]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpOptions"]:
        if not json_data:
            return None
        return cls(
            DestinationPortRange=json_data.get("DestinationPortRange"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpOptions = TcpOptions


@dataclass
class DestinationPortRange:
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortRange"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortRange = DestinationPortRange


@dataclass
class SourcePortRange:
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortRange"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortRange = SourcePortRange


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class UdpOptions:
    DestinationPortRange: Optional[Sequence["_DestinationPortRange"]]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_UdpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpOptions"]:
        if not json_data:
            return None
        return cls(
            DestinationPortRange=json_data.get("DestinationPortRange"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpOptions = UdpOptions


