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
    Attachable: Optional[bool]
    CheckDuplicate: Optional[bool]
    Driver: Optional[str]
    Ingress: Optional[bool]
    Internal: Optional[bool]
    IpamDriver: Optional[str]
    Ipv6: Optional[bool]
    Name: Optional[str]
    Options: Optional[Sequence["_Options"]]
    Scope: Optional[str]
    IpamConfig: Optional[Sequence["_IpamConfig"]]
    Labels: Optional[Sequence["_Labels"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Attachable=json_data.get("Attachable"),
            CheckDuplicate=json_data.get("CheckDuplicate"),
            Driver=json_data.get("Driver"),
            Ingress=json_data.get("Ingress"),
            Internal=json_data.get("Internal"),
            IpamDriver=json_data.get("IpamDriver"),
            Ipv6=json_data.get("Ipv6"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            Scope=json_data.get("Scope"),
            IpamConfig=json_data.get("IpamConfig"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Options:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class IpamConfig:
    AuxAddress: Optional[Sequence["_AuxAddress"]]
    Gateway: Optional[str]
    IpRange: Optional[str]
    Subnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpamConfig"]:
        if not json_data:
            return None
        return cls(
            AuxAddress=json_data.get("AuxAddress"),
            Gateway=json_data.get("Gateway"),
            IpRange=json_data.get("IpRange"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpamConfig = IpamConfig


@dataclass
class AuxAddress:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuxAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuxAddress"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuxAddress = AuxAddress


@dataclass
class Labels:
    Label: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


