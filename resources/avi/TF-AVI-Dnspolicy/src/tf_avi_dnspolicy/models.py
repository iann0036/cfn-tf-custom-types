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
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class RuleDefinition(BaseModel):
    Enable: Optional[bool]
    Index: Optional[float]
    Log: Optional[bool]
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class MatchDefinition(BaseModel):
    ClientIpAddress: Optional[Sequence["_ClientIpAddressDefinition"]]
    GeoLocation: Optional[Sequence["_GeoLocationDefinition"]]
    Protocol: Optional[Sequence["_ProtocolDefinition"]]
    QueryName: Optional[Sequence["_QueryNameDefinition"]]
    QueryType: Optional[Sequence["_QueryTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIpAddress=deserialize_list(json_data.get("ClientIpAddress"), ClientIpAddressDefinition),
            GeoLocation=deserialize_list(json_data.get("GeoLocation"), GeoLocationDefinition),
            Protocol=deserialize_list(json_data.get("Protocol"), ProtocolDefinition),
            QueryName=deserialize_list(json_data.get("QueryName"), QueryNameDefinition),
            QueryType=deserialize_list(json_data.get("QueryType"), QueryTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class ClientIpAddressDefinition(BaseModel):
    UseEdnsClientSubnetIp: Optional[bool]
    ClientIp: Optional[Sequence["_ClientIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            UseEdnsClientSubnetIp=json_data.get("UseEdnsClientSubnetIp"),
            ClientIp=deserialize_list(json_data.get("ClientIp"), ClientIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpAddressDefinition = ClientIpAddressDefinition


@dataclass
class ClientIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpDefinition = ClientIpDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class RangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class BeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginDefinition = BeginDefinition


@dataclass
class EndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndDefinition = EndDefinition


@dataclass
class GeoLocationDefinition(BaseModel):
    GeolocationName: Optional[str]
    GeolocationTag: Optional[str]
    MatchCriteria: Optional[str]
    UseEdnsClientSubnetIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            GeolocationName=json_data.get("GeolocationName"),
            GeolocationTag=json_data.get("GeolocationTag"),
            MatchCriteria=json_data.get("MatchCriteria"),
            UseEdnsClientSubnetIp=json_data.get("UseEdnsClientSubnetIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocationDefinition = GeoLocationDefinition


@dataclass
class ProtocolDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolDefinition = ProtocolDefinition


@dataclass
class QueryNameDefinition(BaseModel):
    MatchCriteria: Optional[str]
    QueryDomainNames: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryNameDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            QueryDomainNames=json_data.get("QueryDomainNames"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryNameDefinition = QueryNameDefinition


@dataclass
class QueryTypeDefinition(BaseModel):
    MatchCriteria: Optional[str]
    QueryType: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            QueryType=json_data.get("QueryType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryTypeDefinition = QueryTypeDefinition


