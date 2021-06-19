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
    BackendPoolHealthProbes: Optional[Sequence["_BackendPoolHealthProbesDefinition"]]
    BackendPoolLoadBalancingSettings: Optional[Sequence["_BackendPoolLoadBalancingSettingsDefinition"]]
    BackendPools: Optional[Sequence["_BackendPoolsDefinition"]]
    BackendPoolsSendReceiveTimeoutSeconds: Optional[float]
    Cname: Optional[str]
    EnforceBackendPoolsCertificateNameCheck: Optional[bool]
    ExplicitResourceOrder: Optional[Sequence["_ExplicitResourceOrderDefinition"]]
    FriendlyName: Optional[str]
    FrontendEndpoints: Optional[Sequence["_FrontendEndpointsDefinition"]]
    HeaderFrontdoorId: Optional[str]
    Id: Optional[str]
    LoadBalancerEnabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    RoutingRules: Optional[Sequence["_RoutingRulesDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    BackendPool: Optional[Sequence["_BackendPoolDefinition"]]
    BackendPoolHealthProbe: Optional[Sequence["_BackendPoolHealthProbeDefinition"]]
    BackendPoolLoadBalancing: Optional[Sequence["_BackendPoolLoadBalancingDefinition"]]
    FrontendEndpoint: Optional[Sequence["_FrontendEndpointDefinition"]]
    RoutingRule: Optional[Sequence["_RoutingRuleDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            BackendPoolHealthProbes=deserialize_list(json_data.get("BackendPoolHealthProbes"), BackendPoolHealthProbesDefinition),
            BackendPoolLoadBalancingSettings=deserialize_list(json_data.get("BackendPoolLoadBalancingSettings"), BackendPoolLoadBalancingSettingsDefinition),
            BackendPools=deserialize_list(json_data.get("BackendPools"), BackendPoolsDefinition),
            BackendPoolsSendReceiveTimeoutSeconds=json_data.get("BackendPoolsSendReceiveTimeoutSeconds"),
            Cname=json_data.get("Cname"),
            EnforceBackendPoolsCertificateNameCheck=json_data.get("EnforceBackendPoolsCertificateNameCheck"),
            ExplicitResourceOrder=deserialize_list(json_data.get("ExplicitResourceOrder"), ExplicitResourceOrderDefinition),
            FriendlyName=json_data.get("FriendlyName"),
            FrontendEndpoints=deserialize_list(json_data.get("FrontendEndpoints"), FrontendEndpointsDefinition),
            HeaderFrontdoorId=json_data.get("HeaderFrontdoorId"),
            Id=json_data.get("Id"),
            LoadBalancerEnabled=json_data.get("LoadBalancerEnabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RoutingRules=deserialize_list(json_data.get("RoutingRules"), RoutingRulesDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            BackendPool=deserialize_list(json_data.get("BackendPool"), BackendPoolDefinition),
            BackendPoolHealthProbe=deserialize_list(json_data.get("BackendPoolHealthProbe"), BackendPoolHealthProbeDefinition),
            BackendPoolLoadBalancing=deserialize_list(json_data.get("BackendPoolLoadBalancing"), BackendPoolLoadBalancingDefinition),
            FrontendEndpoint=deserialize_list(json_data.get("FrontendEndpoint"), FrontendEndpointDefinition),
            RoutingRule=deserialize_list(json_data.get("RoutingRule"), RoutingRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendPoolHealthProbesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolHealthProbesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolHealthProbesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolHealthProbesDefinition = BackendPoolHealthProbesDefinition


@dataclass
class BackendPoolLoadBalancingSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolLoadBalancingSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolLoadBalancingSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolLoadBalancingSettingsDefinition = BackendPoolLoadBalancingSettingsDefinition


@dataclass
class BackendPoolsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolsDefinition = BackendPoolsDefinition


@dataclass
class ExplicitResourceOrderDefinition(BaseModel):
    BackendPoolHealthProbeIds: Optional[Sequence[str]]
    BackendPoolIds: Optional[Sequence[str]]
    BackendPoolLoadBalancingIds: Optional[Sequence[str]]
    FrontendEndpointIds: Optional[Sequence[str]]
    RoutingRuleIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ExplicitResourceOrderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExplicitResourceOrderDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPoolHealthProbeIds=json_data.get("BackendPoolHealthProbeIds"),
            BackendPoolIds=json_data.get("BackendPoolIds"),
            BackendPoolLoadBalancingIds=json_data.get("BackendPoolLoadBalancingIds"),
            FrontendEndpointIds=json_data.get("FrontendEndpointIds"),
            RoutingRuleIds=json_data.get("RoutingRuleIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExplicitResourceOrderDefinition = ExplicitResourceOrderDefinition


@dataclass
class FrontendEndpointsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendEndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendEndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendEndpointsDefinition = FrontendEndpointsDefinition


@dataclass
class RoutingRulesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRulesDefinition = RoutingRulesDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class BackendPoolDefinition(BaseModel):
    HealthProbeName: Optional[str]
    LoadBalancingName: Optional[str]
    Name: Optional[str]
    Backend: Optional[Sequence["_BackendDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthProbeName=json_data.get("HealthProbeName"),
            LoadBalancingName=json_data.get("LoadBalancingName"),
            Name=json_data.get("Name"),
            Backend=deserialize_list(json_data.get("Backend"), BackendDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolDefinition = BackendPoolDefinition


@dataclass
class BackendDefinition(BaseModel):
    Address: Optional[str]
    Enabled: Optional[bool]
    HostHeader: Optional[str]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Priority: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Enabled=json_data.get("Enabled"),
            HostHeader=json_data.get("HostHeader"),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Priority=json_data.get("Priority"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefinition = BackendDefinition


@dataclass
class BackendPoolHealthProbeDefinition(BaseModel):
    Enabled: Optional[bool]
    IntervalInSeconds: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    ProbeMethod: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolHealthProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolHealthProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            ProbeMethod=json_data.get("ProbeMethod"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolHealthProbeDefinition = BackendPoolHealthProbeDefinition


@dataclass
class BackendPoolLoadBalancingDefinition(BaseModel):
    AdditionalLatencyMilliseconds: Optional[float]
    Name: Optional[str]
    SampleSize: Optional[float]
    SuccessfulSamplesRequired: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendPoolLoadBalancingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendPoolLoadBalancingDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalLatencyMilliseconds=json_data.get("AdditionalLatencyMilliseconds"),
            Name=json_data.get("Name"),
            SampleSize=json_data.get("SampleSize"),
            SuccessfulSamplesRequired=json_data.get("SuccessfulSamplesRequired"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendPoolLoadBalancingDefinition = BackendPoolLoadBalancingDefinition


@dataclass
class FrontendEndpointDefinition(BaseModel):
    HostName: Optional[str]
    Name: Optional[str]
    SessionAffinityEnabled: Optional[bool]
    SessionAffinityTtlSeconds: Optional[float]
    WebApplicationFirewallPolicyLinkId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            HostName=json_data.get("HostName"),
            Name=json_data.get("Name"),
            SessionAffinityEnabled=json_data.get("SessionAffinityEnabled"),
            SessionAffinityTtlSeconds=json_data.get("SessionAffinityTtlSeconds"),
            WebApplicationFirewallPolicyLinkId=json_data.get("WebApplicationFirewallPolicyLinkId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendEndpointDefinition = FrontendEndpointDefinition


@dataclass
class RoutingRuleDefinition(BaseModel):
    AcceptedProtocols: Optional[Sequence[str]]
    Enabled: Optional[bool]
    FrontendEndpoints: Optional[Sequence[str]]
    Name: Optional[str]
    PatternsToMatch: Optional[Sequence[str]]
    ForwardingConfiguration: Optional[Sequence["_ForwardingConfigurationDefinition"]]
    RedirectConfiguration: Optional[Sequence["_RedirectConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptedProtocols=json_data.get("AcceptedProtocols"),
            Enabled=json_data.get("Enabled"),
            FrontendEndpoints=json_data.get("FrontendEndpoints"),
            Name=json_data.get("Name"),
            PatternsToMatch=json_data.get("PatternsToMatch"),
            ForwardingConfiguration=deserialize_list(json_data.get("ForwardingConfiguration"), ForwardingConfigurationDefinition),
            RedirectConfiguration=deserialize_list(json_data.get("RedirectConfiguration"), RedirectConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRuleDefinition = RoutingRuleDefinition


@dataclass
class ForwardingConfigurationDefinition(BaseModel):
    BackendPoolName: Optional[str]
    CacheEnabled: Optional[bool]
    CacheQueryParameterStripDirective: Optional[str]
    CacheUseDynamicCompression: Optional[bool]
    CustomForwardingPath: Optional[str]
    ForwardingProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPoolName=json_data.get("BackendPoolName"),
            CacheEnabled=json_data.get("CacheEnabled"),
            CacheQueryParameterStripDirective=json_data.get("CacheQueryParameterStripDirective"),
            CacheUseDynamicCompression=json_data.get("CacheUseDynamicCompression"),
            CustomForwardingPath=json_data.get("CustomForwardingPath"),
            ForwardingProtocol=json_data.get("ForwardingProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingConfigurationDefinition = ForwardingConfigurationDefinition


@dataclass
class RedirectConfigurationDefinition(BaseModel):
    CustomFragment: Optional[str]
    CustomHost: Optional[str]
    CustomPath: Optional[str]
    CustomQueryString: Optional[str]
    RedirectProtocol: Optional[str]
    RedirectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomFragment=json_data.get("CustomFragment"),
            CustomHost=json_data.get("CustomHost"),
            CustomPath=json_data.get("CustomPath"),
            CustomQueryString=json_data.get("CustomQueryString"),
            RedirectProtocol=json_data.get("RedirectProtocol"),
            RedirectType=json_data.get("RedirectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectConfigurationDefinition = RedirectConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


