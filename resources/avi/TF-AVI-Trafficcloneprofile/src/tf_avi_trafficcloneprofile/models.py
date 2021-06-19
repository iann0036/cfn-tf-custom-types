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
    Id: Optional[str]
    Name: Optional[str]
    PreserveClientIp: Optional[bool]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    CloneServers: Optional[Sequence["_CloneServersDefinition"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PreserveClientIp=json_data.get("PreserveClientIp"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            CloneServers=deserialize_list(json_data.get("CloneServers"), CloneServersDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloneServersDefinition(BaseModel):
    Mac: Optional[str]
    NetworkRef: Optional[str]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloneServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloneServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Mac=json_data.get("Mac"),
            NetworkRef=json_data.get("NetworkRef"),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloneServersDefinition = CloneServersDefinition


@dataclass
class IpAddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


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


