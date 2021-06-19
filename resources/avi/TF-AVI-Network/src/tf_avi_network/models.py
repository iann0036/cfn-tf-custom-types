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
    CloudRef: Optional[str]
    DhcpEnabled: Optional[bool]
    ExcludeDiscoveredSubnets: Optional[bool]
    Id: Optional[str]
    Ip6AutocfgEnabled: Optional[bool]
    Name: Optional[str]
    SyncedFromSe: Optional[bool]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    VcenterDvs: Optional[bool]
    VrfContextRef: Optional[str]
    Attrs: Optional[Sequence["_AttrsDefinition"]]
    ConfiguredSubnets: Optional[Sequence["_ConfiguredSubnetsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            CloudRef=json_data.get("CloudRef"),
            DhcpEnabled=json_data.get("DhcpEnabled"),
            ExcludeDiscoveredSubnets=json_data.get("ExcludeDiscoveredSubnets"),
            Id=json_data.get("Id"),
            Ip6AutocfgEnabled=json_data.get("Ip6AutocfgEnabled"),
            Name=json_data.get("Name"),
            SyncedFromSe=json_data.get("SyncedFromSe"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            VcenterDvs=json_data.get("VcenterDvs"),
            VrfContextRef=json_data.get("VrfContextRef"),
            Attrs=deserialize_list(json_data.get("Attrs"), AttrsDefinition),
            ConfiguredSubnets=deserialize_list(json_data.get("ConfiguredSubnets"), ConfiguredSubnetsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttrsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttrsDefinition = AttrsDefinition


@dataclass
class ConfiguredSubnetsDefinition(BaseModel):
    Prefix: Optional[Sequence["_PrefixDefinition"]]
    StaticIpRanges: Optional[Sequence["_StaticIpRangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfiguredSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfiguredSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=deserialize_list(json_data.get("Prefix"), PrefixDefinition),
            StaticIpRanges=deserialize_list(json_data.get("StaticIpRanges"), StaticIpRangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfiguredSubnetsDefinition = ConfiguredSubnetsDefinition


@dataclass
class PrefixDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixDefinition = PrefixDefinition


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
class StaticIpRangesDefinition(BaseModel):
    Type: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIpRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIpRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIpRangesDefinition = StaticIpRangesDefinition


@dataclass
class RangeDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


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


