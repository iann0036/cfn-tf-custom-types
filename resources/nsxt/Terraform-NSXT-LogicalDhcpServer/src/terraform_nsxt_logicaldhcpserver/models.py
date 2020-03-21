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
    AttachedLogicalPortId: Optional[str]
    Description: Optional[str]
    DhcpProfileId: Optional[str]
    DhcpServerIp: Optional[str]
    DisplayName: Optional[str]
    DnsNameServers: Optional[Sequence[str]]
    DomainName: Optional[str]
    GatewayIp: Optional[str]
    Revision: Optional[float]
    DhcpGenericOption: Optional[Sequence["_DhcpGenericOption"]]
    DhcpOption121: Optional[Sequence["_DhcpOption121"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AttachedLogicalPortId=json_data.get("AttachedLogicalPortId"),
            Description=json_data.get("Description"),
            DhcpProfileId=json_data.get("DhcpProfileId"),
            DhcpServerIp=json_data.get("DhcpServerIp"),
            DisplayName=json_data.get("DisplayName"),
            DnsNameServers=json_data.get("DnsNameServers"),
            DomainName=json_data.get("DomainName"),
            GatewayIp=json_data.get("GatewayIp"),
            Revision=json_data.get("Revision"),
            DhcpGenericOption=json_data.get("DhcpGenericOption"),
            DhcpOption121=json_data.get("DhcpOption121"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpGenericOption:
    Code: Optional[float]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpGenericOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpGenericOption"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpGenericOption = DhcpGenericOption


@dataclass
class DhcpOption121:
    Network: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOption121"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOption121"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOption121 = DhcpOption121


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


