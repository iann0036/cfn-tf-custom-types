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
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    ManageDefaultResourceId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    EgressSecurityRules: Optional[Sequence["_EgressSecurityRules"]]
    IngressSecurityRules: Optional[Sequence["_IngressSecurityRules"]]
    Timeouts: Optional["_Timeouts"]
    IcmpOptions: Optional[Sequence["_IcmpOptions"]]
    TcpOptions: Optional[Sequence["_TcpOptions"]]
    UdpOptions: Optional[Sequence["_UdpOptions"]]
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
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            ManageDefaultResourceId=json_data.get("ManageDefaultResourceId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            EgressSecurityRules=json_data.get("EgressSecurityRules"),
            IngressSecurityRules=json_data.get("IngressSecurityRules"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            IcmpOptions=json_data.get("IcmpOptions"),
            TcpOptions=json_data.get("TcpOptions"),
            UdpOptions=json_data.get("UdpOptions"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class EgressSecurityRules:
    Description: Optional[str]
    Destination: Optional[str]
    DestinationType: Optional[str]
    Protocol: Optional[str]
    Stateless: Optional[bool]
    IcmpOptions: Optional[Sequence["_IcmpOptions"]]
    TcpOptions: Optional[Sequence["_TcpOptions"]]
    UdpOptions: Optional[Sequence["_UdpOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressSecurityRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressSecurityRules"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Destination=json_data.get("Destination"),
            DestinationType=json_data.get("DestinationType"),
            Protocol=json_data.get("Protocol"),
            Stateless=json_data.get("Stateless"),
            IcmpOptions=json_data.get("IcmpOptions"),
            TcpOptions=json_data.get("TcpOptions"),
            UdpOptions=json_data.get("UdpOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressSecurityRules = EgressSecurityRules


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
    Max: Optional[float]
    Min: Optional[float]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpOptions"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpOptions = TcpOptions


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
class UdpOptions:
    Max: Optional[float]
    Min: Optional[float]
    SourcePortRange: Optional[Sequence["_SourcePortRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_UdpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpOptions"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpOptions = UdpOptions


@dataclass
class IngressSecurityRules:
    Description: Optional[str]
    Protocol: Optional[str]
    Source: Optional[str]
    SourceType: Optional[str]
    Stateless: Optional[bool]
    IcmpOptions: Optional[Sequence["_IcmpOptions"]]
    TcpOptions: Optional[Sequence["_TcpOptions"]]
    UdpOptions: Optional[Sequence["_UdpOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressSecurityRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressSecurityRules"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourceType=json_data.get("SourceType"),
            Stateless=json_data.get("Stateless"),
            IcmpOptions=json_data.get("IcmpOptions"),
            TcpOptions=json_data.get("TcpOptions"),
            UdpOptions=json_data.get("UdpOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressSecurityRules = IngressSecurityRules


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


