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
    EnableFirewall: Optional[bool]
    FailoverMode: Optional[str]
    ForceWhitelisting: Optional[bool]
    HaMode: Optional[str]
    Id: Optional[str]
    InternalTransitSubnets: Optional[Sequence[str]]
    Ipv6DadProfilePath: Optional[str]
    Ipv6NdraProfilePath: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    RdAdminAddress: Optional[str]
    RedistributionSet: Optional[bool]
    Revision: Optional[float]
    TransitSubnets: Optional[Sequence[str]]
    BgpConfig: Optional[Sequence["_BgpConfigDefinition"]]
    IntersiteConfig: Optional[Sequence["_IntersiteConfigDefinition"]]
    LocaleService: Optional[Sequence["_LocaleServiceDefinition"]]
    RedistributionConfig: Optional[Sequence["_RedistributionConfigDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    VrfConfig: Optional[Sequence["_VrfConfigDefinition"]]

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
            EnableFirewall=json_data.get("EnableFirewall"),
            FailoverMode=json_data.get("FailoverMode"),
            ForceWhitelisting=json_data.get("ForceWhitelisting"),
            HaMode=json_data.get("HaMode"),
            Id=json_data.get("Id"),
            InternalTransitSubnets=json_data.get("InternalTransitSubnets"),
            Ipv6DadProfilePath=json_data.get("Ipv6DadProfilePath"),
            Ipv6NdraProfilePath=json_data.get("Ipv6NdraProfilePath"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            RdAdminAddress=json_data.get("RdAdminAddress"),
            RedistributionSet=json_data.get("RedistributionSet"),
            Revision=json_data.get("Revision"),
            TransitSubnets=json_data.get("TransitSubnets"),
            BgpConfig=deserialize_list(json_data.get("BgpConfig"), BgpConfigDefinition),
            IntersiteConfig=deserialize_list(json_data.get("IntersiteConfig"), IntersiteConfigDefinition),
            LocaleService=deserialize_list(json_data.get("LocaleService"), LocaleServiceDefinition),
            RedistributionConfig=deserialize_list(json_data.get("RedistributionConfig"), RedistributionConfigDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            VrfConfig=deserialize_list(json_data.get("VrfConfig"), VrfConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpConfigDefinition(BaseModel):
    Ecmp: Optional[bool]
    Enabled: Optional[bool]
    GracefulRestartMode: Optional[str]
    GracefulRestartStaleRouteTimer: Optional[float]
    GracefulRestartTimer: Optional[float]
    InterSrIbgp: Optional[bool]
    LocalAsNum: Optional[str]
    MultipathRelax: Optional[bool]
    RouteAggregation: Optional[Sequence["_RouteAggregationDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ecmp=json_data.get("Ecmp"),
            Enabled=json_data.get("Enabled"),
            GracefulRestartMode=json_data.get("GracefulRestartMode"),
            GracefulRestartStaleRouteTimer=json_data.get("GracefulRestartStaleRouteTimer"),
            GracefulRestartTimer=json_data.get("GracefulRestartTimer"),
            InterSrIbgp=json_data.get("InterSrIbgp"),
            LocalAsNum=json_data.get("LocalAsNum"),
            MultipathRelax=json_data.get("MultipathRelax"),
            RouteAggregation=deserialize_list(json_data.get("RouteAggregation"), RouteAggregationDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpConfigDefinition = BgpConfigDefinition


@dataclass
class RouteAggregationDefinition(BaseModel):
    Prefix: Optional[str]
    SummaryOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RouteAggregationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteAggregationDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            SummaryOnly=json_data.get("SummaryOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteAggregationDefinition = RouteAggregationDefinition


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
    RedistributionConfig: Optional[Sequence["_RedistributionConfigDefinition"]]

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
            RedistributionConfig=deserialize_list(json_data.get("RedistributionConfig"), RedistributionConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocaleServiceDefinition = LocaleServiceDefinition


@dataclass
class RedistributionConfigDefinition(BaseModel):
    Enabled: Optional[bool]
    OspfEnabled: Optional[bool]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            OspfEnabled=json_data.get("OspfEnabled"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributionConfigDefinition = RedistributionConfigDefinition


@dataclass
class RuleDefinition(BaseModel):
    Name: Optional[str]
    RouteMapPath: Optional[str]
    Types: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RouteMapPath=json_data.get("RouteMapPath"),
            Types=json_data.get("Types"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class VrfConfigDefinition(BaseModel):
    EvpnTransitVni: Optional[float]
    GatewayPath: Optional[str]
    RouteDistinguisher: Optional[str]
    RouteTarget: Optional[Sequence["_RouteTargetDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VrfConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VrfConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EvpnTransitVni=json_data.get("EvpnTransitVni"),
            GatewayPath=json_data.get("GatewayPath"),
            RouteDistinguisher=json_data.get("RouteDistinguisher"),
            RouteTarget=deserialize_list(json_data.get("RouteTarget"), RouteTargetDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VrfConfigDefinition = VrfConfigDefinition


@dataclass
class RouteTargetDefinition(BaseModel):
    AddressFamily: Optional[str]
    AutoMode: Optional[bool]
    ExportTargets: Optional[Sequence[str]]
    ImportTargets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressFamily=json_data.get("AddressFamily"),
            AutoMode=json_data.get("AutoMode"),
            ExportTargets=json_data.get("ExportTargets"),
            ImportTargets=json_data.get("ImportTargets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteTargetDefinition = RouteTargetDefinition


