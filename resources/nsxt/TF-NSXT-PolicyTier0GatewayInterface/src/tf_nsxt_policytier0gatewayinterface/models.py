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
    AccessVlanId: Optional[float]
    Description: Optional[str]
    DisplayName: Optional[str]
    EdgeNodePath: Optional[str]
    EnablePim: Optional[bool]
    GatewayPath: Optional[str]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    Ipv6NdraProfilePath: Optional[str]
    LocaleServiceId: Optional[str]
    Mtu: Optional[float]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    SegmentPath: Optional[str]
    SitePath: Optional[str]
    Subnets: Optional[Sequence[str]]
    Type: Optional[str]
    UrpfMode: Optional[str]
    Ospf: Optional[Sequence["_OspfDefinition"]]
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
            AccessVlanId=json_data.get("AccessVlanId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EdgeNodePath=json_data.get("EdgeNodePath"),
            EnablePim=json_data.get("EnablePim"),
            GatewayPath=json_data.get("GatewayPath"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            Ipv6NdraProfilePath=json_data.get("Ipv6NdraProfilePath"),
            LocaleServiceId=json_data.get("LocaleServiceId"),
            Mtu=json_data.get("Mtu"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            SegmentPath=json_data.get("SegmentPath"),
            SitePath=json_data.get("SitePath"),
            Subnets=json_data.get("Subnets"),
            Type=json_data.get("Type"),
            UrpfMode=json_data.get("UrpfMode"),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OspfDefinition(BaseModel):
    AreaPath: Optional[str]
    BfdProfilePath: Optional[str]
    DeadInterval: Optional[float]
    EnableBfd: Optional[bool]
    Enabled: Optional[bool]
    HelloInterval: Optional[float]
    NetworkType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OspfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaPath=json_data.get("AreaPath"),
            BfdProfilePath=json_data.get("BfdProfilePath"),
            DeadInterval=json_data.get("DeadInterval"),
            EnableBfd=json_data.get("EnableBfd"),
            Enabled=json_data.get("Enabled"),
            HelloInterval=json_data.get("HelloInterval"),
            NetworkType=json_data.get("NetworkType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfDefinition = OspfDefinition


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


