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
    ApicEpgName: Optional[str]
    CountryCodes: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    MarathonAppName: Optional[str]
    MarathonServicePort: Optional[float]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    IpPorts: Optional[Sequence["_IpPortsDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

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
            ApicEpgName=json_data.get("ApicEpgName"),
            CountryCodes=json_data.get("CountryCodes"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MarathonAppName=json_data.get("MarathonAppName"),
            MarathonServicePort=json_data.get("MarathonServicePort"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            IpPorts=deserialize_list(json_data.get("IpPorts"), IpPortsDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class IpPortsDefinition(BaseModel):
    Hostname: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPortsDefinition = IpPortsDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


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


