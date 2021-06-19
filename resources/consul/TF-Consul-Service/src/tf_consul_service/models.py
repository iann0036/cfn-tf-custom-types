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
    Address: Optional[str]
    Datacenter: Optional[str]
    EnableTagOverride: Optional[bool]
    External: Optional[bool]
    Id: Optional[str]
    Meta: Optional[Sequence["_MetaDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    Node: Optional[str]
    Port: Optional[float]
    ServiceId: Optional[str]
    Tags: Optional[Sequence[str]]
    Check: Optional[Sequence["_CheckDefinition"]]

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
            Address=json_data.get("Address"),
            Datacenter=json_data.get("Datacenter"),
            EnableTagOverride=json_data.get("EnableTagOverride"),
            External=json_data.get("External"),
            Id=json_data.get("Id"),
            Meta=deserialize_list(json_data.get("Meta"), MetaDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Node=json_data.get("Node"),
            Port=json_data.get("Port"),
            ServiceId=json_data.get("ServiceId"),
            Tags=json_data.get("Tags"),
            Check=deserialize_list(json_data.get("Check"), CheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetaDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetaDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetaDefinition = MetaDefinition


@dataclass
class CheckDefinition(BaseModel):
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
    Header: Optional[Sequence["_HeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckDefinition"]:
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
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckDefinition = CheckDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


