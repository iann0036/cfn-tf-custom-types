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
    Address: Optional[str]
    Datacenter: Optional[str]
    External: Optional[bool]
    Id: Optional[str]
    Meta: Optional[Sequence["_Meta"]]
    Name: Optional[str]
    Node: Optional[str]
    Port: Optional[float]
    ServiceId: Optional[str]
    Tags: Optional[Sequence[str]]
    Check: Optional[Sequence["_Check"]]
    Header: Optional[Sequence["_Header"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Address=json_data.get("Address"),
            Datacenter=json_data.get("Datacenter"),
            External=json_data.get("External"),
            Id=json_data.get("Id"),
            Meta=json_data.get("Meta"),
            Name=json_data.get("Name"),
            Node=json_data.get("Node"),
            Port=json_data.get("Port"),
            ServiceId=json_data.get("ServiceId"),
            Tags=json_data.get("Tags"),
            Check=json_data.get("Check"),
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Meta:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta = Meta


@dataclass
class Check:
    CheckId: Optional[str]
    DeregisterCriticalServiceAfter: Optional[str]
    Http: Optional[str]
    Interval: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Status: Optional[str]
    Tcp: Optional[str]
    Timeout: Optional[str]
    TlsSkipVerify: Optional[bool]
    Header: Optional[Sequence["_Header"]]

    @classmethod
    def _deserialize(
        cls: Type["_Check"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Check"]:
        if not json_data:
            return None
        return cls(
            CheckId=json_data.get("CheckId"),
            DeregisterCriticalServiceAfter=json_data.get("DeregisterCriticalServiceAfter"),
            Http=json_data.get("Http"),
            Interval=json_data.get("Interval"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Status=json_data.get("Status"),
            Tcp=json_data.get("Tcp"),
            Timeout=json_data.get("Timeout"),
            TlsSkipVerify=json_data.get("TlsSkipVerify"),
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Check = Check


@dataclass
class Header:
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


