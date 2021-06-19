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
    AttachedLogicalPortId: Optional[str]
    Description: Optional[str]
    DhcpProfileId: Optional[str]
    DhcpServerIp: Optional[str]
    DisplayName: Optional[str]
    DnsNameServers: Optional[Sequence[str]]
    DomainName: Optional[str]
    GatewayIp: Optional[str]
    Id: Optional[str]
    Revision: Optional[float]
    DhcpGenericOption: Optional[Sequence["_DhcpGenericOptionDefinition"]]
    DhcpOption121: Optional[Sequence["_DhcpOption121Definition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            AttachedLogicalPortId=json_data.get("AttachedLogicalPortId"),
            Description=json_data.get("Description"),
            DhcpProfileId=json_data.get("DhcpProfileId"),
            DhcpServerIp=json_data.get("DhcpServerIp"),
            DisplayName=json_data.get("DisplayName"),
            DnsNameServers=json_data.get("DnsNameServers"),
            DomainName=json_data.get("DomainName"),
            GatewayIp=json_data.get("GatewayIp"),
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
            DhcpGenericOption=deserialize_list(json_data.get("DhcpGenericOption"), DhcpGenericOptionDefinition),
            DhcpOption121=deserialize_list(json_data.get("DhcpOption121"), DhcpOption121Definition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DhcpGenericOptionDefinition(BaseModel):
    Code: Optional[float]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpGenericOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpGenericOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpGenericOptionDefinition = DhcpGenericOptionDefinition


@dataclass
class DhcpOption121Definition(BaseModel):
    Network: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOption121Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOption121Definition"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOption121Definition = DhcpOption121Definition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


