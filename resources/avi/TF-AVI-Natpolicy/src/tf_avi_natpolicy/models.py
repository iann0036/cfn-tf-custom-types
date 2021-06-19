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
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
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
class RulesDefinition(BaseModel):
    CreatedBy: Optional[str]
    Enable: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatedBy=json_data.get("CreatedBy"),
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    Type: Optional[str]
    NatInfo: Optional[Sequence["_NatInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            NatInfo=deserialize_list(json_data.get("NatInfo"), NatInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class NatInfoDefinition(BaseModel):
    NatIp: Optional[Sequence["_NatIpDefinition"]]
    NatIpRange: Optional[Sequence["_NatIpRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NatInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            NatIp=deserialize_list(json_data.get("NatIp"), NatIpDefinition),
            NatIpRange=deserialize_list(json_data.get("NatIpRange"), NatIpRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatInfoDefinition = NatInfoDefinition


@dataclass
class NatIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatIpDefinition = NatIpDefinition


@dataclass
class NatIpRangeDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NatIpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatIpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatIpRangeDefinition = NatIpRangeDefinition


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
class MatchDefinition(BaseModel):
    DestinationIp: Optional[Sequence["_DestinationIpDefinition"]]
    Services: Optional[Sequence["_ServicesDefinition"]]
    SourceIp: Optional[Sequence["_SourceIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationIp=deserialize_list(json_data.get("DestinationIp"), DestinationIpDefinition),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
            SourceIp=deserialize_list(json_data.get("SourceIp"), SourceIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class DestinationIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationIpDefinition"]:
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
_DestinationIpDefinition = DestinationIpDefinition


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
class ServicesDefinition(BaseModel):
    DestinationPort: Optional[Sequence["_DestinationPortDefinition"]]
    Protocol: Optional[Sequence["_ProtocolDefinition"]]
    SourcePort: Optional[Sequence["_SourcePortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationPort=deserialize_list(json_data.get("DestinationPort"), DestinationPortDefinition),
            Protocol=deserialize_list(json_data.get("Protocol"), ProtocolDefinition),
            SourcePort=deserialize_list(json_data.get("SourcePort"), SourcePortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesDefinition = ServicesDefinition


@dataclass
class DestinationPortDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Ports: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortDefinition = DestinationPortDefinition


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
class SourcePortDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Ports: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortDefinition = SourcePortDefinition


@dataclass
class SourceIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceIpDefinition"]:
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
_SourceIpDefinition = SourceIpDefinition


