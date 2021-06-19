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
    Connect: Optional[bool]
    Datacenter: Optional[str]
    Id: Optional[str]
    IgnoreCheckIds: Optional[Sequence[str]]
    Name: Optional[str]
    Near: Optional[str]
    NodeMeta: Optional[Sequence["_NodeMetaDefinition"]]
    OnlyPassing: Optional[bool]
    Service: Optional[str]
    ServiceMeta: Optional[Sequence["_ServiceMetaDefinition"]]
    Session: Optional[str]
    StoredToken: Optional[str]
    Tags: Optional[Sequence[str]]
    Token: Optional[str]
    Dns: Optional[Sequence["_DnsDefinition"]]
    Failover: Optional[Sequence["_FailoverDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

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
            Connect=json_data.get("Connect"),
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            IgnoreCheckIds=json_data.get("IgnoreCheckIds"),
            Name=json_data.get("Name"),
            Near=json_data.get("Near"),
            NodeMeta=deserialize_list(json_data.get("NodeMeta"), NodeMetaDefinition),
            OnlyPassing=json_data.get("OnlyPassing"),
            Service=json_data.get("Service"),
            ServiceMeta=deserialize_list(json_data.get("ServiceMeta"), ServiceMetaDefinition),
            Session=json_data.get("Session"),
            StoredToken=json_data.get("StoredToken"),
            Tags=json_data.get("Tags"),
            Token=json_data.get("Token"),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            Failover=deserialize_list(json_data.get("Failover"), FailoverDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeMetaDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeMetaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeMetaDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeMetaDefinition = NodeMetaDefinition


@dataclass
class ServiceMetaDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceMetaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceMetaDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceMetaDefinition = ServiceMetaDefinition


@dataclass
class DnsDefinition(BaseModel):
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class FailoverDefinition(BaseModel):
    Datacenters: Optional[Sequence[str]]
    NearestN: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverDefinition"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            NearestN=json_data.get("NearestN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverDefinition = FailoverDefinition


@dataclass
class TemplateDefinition(BaseModel):
    Regexp: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Regexp=json_data.get("Regexp"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


