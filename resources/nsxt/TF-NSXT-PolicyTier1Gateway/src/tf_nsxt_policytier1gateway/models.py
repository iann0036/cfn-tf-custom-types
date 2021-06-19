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
    DefaultRuleLogging: Optional[bool]
    Description: Optional[str]
    DhcpConfigPath: Optional[str]
    DisplayName: Optional[str]
    EdgeClusterPath: Optional[str]
    EgressQosProfilePath: Optional[str]
    EnableFirewall: Optional[bool]
    EnableStandbyRelocation: Optional[bool]
    FailoverMode: Optional[str]
    ForceWhitelisting: Optional[bool]
    Id: Optional[str]
    IngressQosProfilePath: Optional[str]
    Ipv6DadProfilePath: Optional[str]
    Ipv6NdraProfilePath: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    PoolAllocation: Optional[str]
    Revision: Optional[float]
    RouteAdvertisementTypes: Optional[Sequence[str]]
    Tier0Path: Optional[str]
    IntersiteConfig: Optional[Sequence["_IntersiteConfigDefinition"]]
    LocaleService: Optional[Sequence["_LocaleServiceDefinition"]]
    RouteAdvertisementRule: Optional[Sequence["_RouteAdvertisementRuleDefinition"]]
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
            DefaultRuleLogging=json_data.get("DefaultRuleLogging"),
            Description=json_data.get("Description"),
            DhcpConfigPath=json_data.get("DhcpConfigPath"),
            DisplayName=json_data.get("DisplayName"),
            EdgeClusterPath=json_data.get("EdgeClusterPath"),
            EgressQosProfilePath=json_data.get("EgressQosProfilePath"),
            EnableFirewall=json_data.get("EnableFirewall"),
            EnableStandbyRelocation=json_data.get("EnableStandbyRelocation"),
            FailoverMode=json_data.get("FailoverMode"),
            ForceWhitelisting=json_data.get("ForceWhitelisting"),
            Id=json_data.get("Id"),
            IngressQosProfilePath=json_data.get("IngressQosProfilePath"),
            Ipv6DadProfilePath=json_data.get("Ipv6DadProfilePath"),
            Ipv6NdraProfilePath=json_data.get("Ipv6NdraProfilePath"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            PoolAllocation=json_data.get("PoolAllocation"),
            Revision=json_data.get("Revision"),
            RouteAdvertisementTypes=json_data.get("RouteAdvertisementTypes"),
            Tier0Path=json_data.get("Tier0Path"),
            IntersiteConfig=deserialize_list(json_data.get("IntersiteConfig"), IntersiteConfigDefinition),
            LocaleService=deserialize_list(json_data.get("LocaleService"), LocaleServiceDefinition),
            RouteAdvertisementRule=deserialize_list(json_data.get("RouteAdvertisementRule"), RouteAdvertisementRuleDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IntersiteConfigDefinition(BaseModel):
    FallbackSitePaths: Optional[Sequence[str]]
    PrimarySitePath: Optional[str]
    TransitSubnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntersiteConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntersiteConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FallbackSitePaths=json_data.get("FallbackSitePaths"),
            PrimarySitePath=json_data.get("PrimarySitePath"),
            TransitSubnet=json_data.get("TransitSubnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntersiteConfigDefinition = IntersiteConfigDefinition


@dataclass
class LocaleServiceDefinition(BaseModel):
    EdgeClusterPath: Optional[str]
    PreferredEdgePaths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LocaleServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocaleServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            EdgeClusterPath=json_data.get("EdgeClusterPath"),
            PreferredEdgePaths=json_data.get("PreferredEdgePaths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocaleServiceDefinition = LocaleServiceDefinition


@dataclass
class RouteAdvertisementRuleDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    PrefixOperator: Optional[str]
    RouteAdvertisementTypes: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteAdvertisementRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteAdvertisementRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            PrefixOperator=json_data.get("PrefixOperator"),
            RouteAdvertisementTypes=json_data.get("RouteAdvertisementTypes"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteAdvertisementRuleDefinition = RouteAdvertisementRuleDefinition


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


