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
    Id: Optional[str]
    OidVal: Optional[str]
    ReadUser: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Remote: Optional[Sequence["_RemoteDefinition"]]

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
            Id=json_data.get("Id"),
            OidVal=json_data.get("OidVal"),
            ReadUser=json_data.get("ReadUser"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Remote=deserialize_list(json_data.get("Remote"), RemoteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RemoteDefinition(BaseModel):
    HostList: Optional[Sequence["_HostListDefinition"]]
    Ipv4List: Optional[Sequence["_Ipv4ListDefinition"]]
    Ipv6List: Optional[Sequence["_Ipv6ListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteDefinition"]:
        if not json_data:
            return None
        return cls(
            HostList=deserialize_list(json_data.get("HostList"), HostListDefinition),
            Ipv4List=deserialize_list(json_data.get("Ipv4List"), Ipv4ListDefinition),
            Ipv6List=deserialize_list(json_data.get("Ipv6List"), Ipv6ListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteDefinition = RemoteDefinition


@dataclass
class HostListDefinition(BaseModel):
    DnsHost: Optional[str]
    Ipv4Mask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostListDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsHost=json_data.get("DnsHost"),
            Ipv4Mask=json_data.get("Ipv4Mask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostListDefinition = HostListDefinition


@dataclass
class Ipv4ListDefinition(BaseModel):
    Ipv4Host: Optional[str]
    Ipv4Mask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4ListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Host=json_data.get("Ipv4Host"),
            Ipv4Mask=json_data.get("Ipv4Mask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4ListDefinition = Ipv4ListDefinition


@dataclass
class Ipv6ListDefinition(BaseModel):
    Ipv6Host: Optional[str]
    Ipv6Mask: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6ListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6ListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv6Host=json_data.get("Ipv6Host"),
            Ipv6Mask=json_data.get("Ipv6Mask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6ListDefinition = Ipv6ListDefinition


