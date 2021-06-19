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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Description: Optional[str]
    Disable: Optional[bool]
    EndpointSelection: Optional[str]
    HealthCheckPort: Optional[float]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LoadbalancerAlgorithm: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    NoTls: Optional[bool]
    Port: Optional[float]
    SameAsEndpointPort: Optional[bool]
    AdvancedOptions: Optional[Sequence["_AdvancedOptionsDefinition"]]
    Healthcheck: Optional[Sequence["_HealthcheckDefinition"]]
    OriginServers: Optional[Sequence["_OriginServersDefinition"]]
    UseTls: Optional[Sequence["_UseTlsDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            EndpointSelection=json_data.get("EndpointSelection"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LoadbalancerAlgorithm=json_data.get("LoadbalancerAlgorithm"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoTls=json_data.get("NoTls"),
            Port=json_data.get("Port"),
            SameAsEndpointPort=json_data.get("SameAsEndpointPort"),
            AdvancedOptions=deserialize_list(json_data.get("AdvancedOptions"), AdvancedOptionsDefinition),
            Healthcheck=deserialize_list(json_data.get("Healthcheck"), HealthcheckDefinition),
            OriginServers=deserialize_list(json_data.get("OriginServers"), OriginServersDefinition),
            UseTls=deserialize_list(json_data.get("UseTls"), UseTlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AdvancedOptionsDefinition(BaseModel):
    ConnectionTimeout: Optional[float]
    DisableCircuitBreaker: Optional[bool]
    DisableOutlierDetection: Optional[bool]
    DisableSubsets: Optional[bool]
    HttpIdleTimeout: Optional[float]
    NoPanicThreshold: Optional[bool]
    PanicThreshold: Optional[float]
    CircuitBreaker: Optional[Sequence["_CircuitBreakerDefinition"]]
    EnableSubsets: Optional[Sequence["_EnableSubsetsDefinition"]]
    Http2Options: Optional[Sequence["_Http2OptionsDefinition"]]
    OutlierDetection: Optional[Sequence["_OutlierDetectionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            DisableCircuitBreaker=json_data.get("DisableCircuitBreaker"),
            DisableOutlierDetection=json_data.get("DisableOutlierDetection"),
            DisableSubsets=json_data.get("DisableSubsets"),
            HttpIdleTimeout=json_data.get("HttpIdleTimeout"),
            NoPanicThreshold=json_data.get("NoPanicThreshold"),
            PanicThreshold=json_data.get("PanicThreshold"),
            CircuitBreaker=deserialize_list(json_data.get("CircuitBreaker"), CircuitBreakerDefinition),
            EnableSubsets=deserialize_list(json_data.get("EnableSubsets"), EnableSubsetsDefinition),
            Http2Options=deserialize_list(json_data.get("Http2Options"), Http2OptionsDefinition),
            OutlierDetection=deserialize_list(json_data.get("OutlierDetection"), OutlierDetectionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedOptionsDefinition = AdvancedOptionsDefinition


@dataclass
class CircuitBreakerDefinition(BaseModel):
    ConnectionLimit: Optional[float]
    MaxRequests: Optional[float]
    PendingRequests: Optional[float]
    Priority: Optional[str]
    Retries: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CircuitBreakerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CircuitBreakerDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionLimit=json_data.get("ConnectionLimit"),
            MaxRequests=json_data.get("MaxRequests"),
            PendingRequests=json_data.get("PendingRequests"),
            Priority=json_data.get("Priority"),
            Retries=json_data.get("Retries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CircuitBreakerDefinition = CircuitBreakerDefinition


@dataclass
class EnableSubsetsDefinition(BaseModel):
    AnyEndpoint: Optional[bool]
    FailRequest: Optional[bool]
    DefaultSubset: Optional[Sequence["_DefaultSubsetDefinition"]]
    EndpointSubsets: Optional[Sequence["_EndpointSubsetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnableSubsetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableSubsetsDefinition"]:
        if not json_data:
            return None
        return cls(
            AnyEndpoint=json_data.get("AnyEndpoint"),
            FailRequest=json_data.get("FailRequest"),
            DefaultSubset=deserialize_list(json_data.get("DefaultSubset"), DefaultSubsetDefinition),
            EndpointSubsets=deserialize_list(json_data.get("EndpointSubsets"), EndpointSubsetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableSubsetsDefinition = EnableSubsetsDefinition


@dataclass
class DefaultSubsetDefinition(BaseModel):
    DefaultSubset: Optional[Sequence["_DefaultSubsetDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSubsetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSubsetDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultSubset=deserialize_list(json_data.get("DefaultSubset"), DefaultSubsetDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSubsetDefinition = DefaultSubsetDefinition


@dataclass
class DefaultSubsetDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSubsetDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSubsetDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSubsetDefinition2 = DefaultSubsetDefinition2


@dataclass
class EndpointSubsetsDefinition(BaseModel):
    Keys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSubsetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSubsetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSubsetsDefinition = EndpointSubsetsDefinition


@dataclass
class Http2OptionsDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Http2OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2OptionsDefinition = Http2OptionsDefinition


@dataclass
class OutlierDetectionDefinition(BaseModel):
    BaseEjectionTime: Optional[float]
    Consecutive5xx: Optional[float]
    ConsecutiveGatewayFailure: Optional[float]
    Interval: Optional[float]
    MaxEjectionPercent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OutlierDetectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutlierDetectionDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseEjectionTime=json_data.get("BaseEjectionTime"),
            Consecutive5xx=json_data.get("Consecutive5xx"),
            ConsecutiveGatewayFailure=json_data.get("ConsecutiveGatewayFailure"),
            Interval=json_data.get("Interval"),
            MaxEjectionPercent=json_data.get("MaxEjectionPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutlierDetectionDefinition = OutlierDetectionDefinition


@dataclass
class HealthcheckDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthcheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthcheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthcheckDefinition = HealthcheckDefinition


@dataclass
class OriginServersDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    ConsulService: Optional[Sequence["_ConsulServiceDefinition"]]
    CustomEndpointObject: Optional[Sequence["_CustomEndpointObjectDefinition"]]
    K8sService: Optional[Sequence["_K8sServiceDefinition"]]
    PrivateIp: Optional[Sequence["_PrivateIpDefinition"]]
    PrivateName: Optional[Sequence["_PrivateNameDefinition"]]
    PublicIp: Optional[Sequence["_PublicIpDefinition"]]
    PublicName: Optional[Sequence["_PublicNameDefinition"]]
    VnPrivateIp: Optional[Sequence["_VnPrivateIpDefinition"]]
    VnPrivateName: Optional[Sequence["_VnPrivateNameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            ConsulService=deserialize_list(json_data.get("ConsulService"), ConsulServiceDefinition),
            CustomEndpointObject=deserialize_list(json_data.get("CustomEndpointObject"), CustomEndpointObjectDefinition),
            K8sService=deserialize_list(json_data.get("K8sService"), K8sServiceDefinition),
            PrivateIp=deserialize_list(json_data.get("PrivateIp"), PrivateIpDefinition),
            PrivateName=deserialize_list(json_data.get("PrivateName"), PrivateNameDefinition),
            PublicIp=deserialize_list(json_data.get("PublicIp"), PublicIpDefinition),
            PublicName=deserialize_list(json_data.get("PublicName"), PublicNameDefinition),
            VnPrivateIp=deserialize_list(json_data.get("VnPrivateIp"), VnPrivateIpDefinition),
            VnPrivateName=deserialize_list(json_data.get("VnPrivateName"), VnPrivateNameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginServersDefinition = OriginServersDefinition


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class ConsulServiceDefinition(BaseModel):
    InsideNetwork: Optional[bool]
    OutsideNetwork: Optional[bool]
    ServiceName: Optional[str]
    SiteLocator: Optional[Sequence["_SiteLocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConsulServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsulServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            InsideNetwork=json_data.get("InsideNetwork"),
            OutsideNetwork=json_data.get("OutsideNetwork"),
            ServiceName=json_data.get("ServiceName"),
            SiteLocator=deserialize_list(json_data.get("SiteLocator"), SiteLocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsulServiceDefinition = ConsulServiceDefinition


@dataclass
class SiteLocatorDefinition(BaseModel):
    Site: Optional[Sequence["_SiteDefinition"]]
    VirtualSite: Optional[Sequence["_VirtualSiteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteLocatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteLocatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Site=deserialize_list(json_data.get("Site"), SiteDefinition),
            VirtualSite=deserialize_list(json_data.get("VirtualSite"), VirtualSiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteLocatorDefinition = SiteLocatorDefinition


@dataclass
class SiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteDefinition = SiteDefinition


@dataclass
class VirtualSiteDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualSiteDefinition = VirtualSiteDefinition


@dataclass
class CustomEndpointObjectDefinition(BaseModel):
    Endpoint: Optional[Sequence["_EndpointDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEndpointObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEndpointObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEndpointObjectDefinition = CustomEndpointObjectDefinition


@dataclass
class EndpointDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class K8sServiceDefinition(BaseModel):
    InsideNetwork: Optional[bool]
    OutsideNetwork: Optional[bool]
    ServiceName: Optional[str]
    Vk8sNetworks: Optional[bool]
    SiteLocator: Optional[Sequence["_SiteLocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_K8sServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_K8sServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            InsideNetwork=json_data.get("InsideNetwork"),
            OutsideNetwork=json_data.get("OutsideNetwork"),
            ServiceName=json_data.get("ServiceName"),
            Vk8sNetworks=json_data.get("Vk8sNetworks"),
            SiteLocator=deserialize_list(json_data.get("SiteLocator"), SiteLocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_K8sServiceDefinition = K8sServiceDefinition


@dataclass
class PrivateIpDefinition(BaseModel):
    InsideNetwork: Optional[bool]
    Ip: Optional[str]
    OutsideNetwork: Optional[bool]
    SiteLocator: Optional[Sequence["_SiteLocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateIpDefinition"]:
        if not json_data:
            return None
        return cls(
            InsideNetwork=json_data.get("InsideNetwork"),
            Ip=json_data.get("Ip"),
            OutsideNetwork=json_data.get("OutsideNetwork"),
            SiteLocator=deserialize_list(json_data.get("SiteLocator"), SiteLocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateIpDefinition = PrivateIpDefinition


@dataclass
class PrivateNameDefinition(BaseModel):
    DnsName: Optional[str]
    InsideNetwork: Optional[bool]
    OutsideNetwork: Optional[bool]
    SiteLocator: Optional[Sequence["_SiteLocatorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateNameDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            InsideNetwork=json_data.get("InsideNetwork"),
            OutsideNetwork=json_data.get("OutsideNetwork"),
            SiteLocator=deserialize_list(json_data.get("SiteLocator"), SiteLocatorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateNameDefinition = PrivateNameDefinition


@dataclass
class PublicIpDefinition(BaseModel):
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIpDefinition = PublicIpDefinition


@dataclass
class PublicNameDefinition(BaseModel):
    DnsName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicNameDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicNameDefinition = PublicNameDefinition


@dataclass
class VnPrivateIpDefinition(BaseModel):
    Ip: Optional[str]
    VirtualNetwork: Optional[Sequence["_VirtualNetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VnPrivateIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnPrivateIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), VirtualNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnPrivateIpDefinition = VnPrivateIpDefinition


@dataclass
class VirtualNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkDefinition = VirtualNetworkDefinition


@dataclass
class VnPrivateNameDefinition(BaseModel):
    DnsName: Optional[str]
    PrivateNetwork: Optional[Sequence["_PrivateNetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VnPrivateNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VnPrivateNameDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            PrivateNetwork=deserialize_list(json_data.get("PrivateNetwork"), PrivateNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VnPrivateNameDefinition = VnPrivateNameDefinition


@dataclass
class PrivateNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateNetworkDefinition = PrivateNetworkDefinition


@dataclass
class UseTlsDefinition(BaseModel):
    DisableSni: Optional[bool]
    NoMtls: Optional[bool]
    SkipServerVerification: Optional[bool]
    Sni: Optional[str]
    UseHostHeaderAsSni: Optional[bool]
    VolterraTrustedCa: Optional[bool]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]
    UseMtls: Optional[Sequence["_UseMtlsDefinition"]]
    UseServerVerification: Optional[Sequence["_UseServerVerificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseTlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseTlsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableSni=json_data.get("DisableSni"),
            NoMtls=json_data.get("NoMtls"),
            SkipServerVerification=json_data.get("SkipServerVerification"),
            Sni=json_data.get("Sni"),
            UseHostHeaderAsSni=json_data.get("UseHostHeaderAsSni"),
            VolterraTrustedCa=json_data.get("VolterraTrustedCa"),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
            UseMtls=deserialize_list(json_data.get("UseMtls"), UseMtlsDefinition),
            UseServerVerification=deserialize_list(json_data.get("UseServerVerification"), UseServerVerificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseTlsDefinition = UseTlsDefinition


@dataclass
class TlsConfigDefinition(BaseModel):
    DefaultSecurity: Optional[bool]
    LowSecurity: Optional[bool]
    MediumSecurity: Optional[bool]
    CustomSecurity: Optional[Sequence["_CustomSecurityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultSecurity=json_data.get("DefaultSecurity"),
            LowSecurity=json_data.get("LowSecurity"),
            MediumSecurity=json_data.get("MediumSecurity"),
            CustomSecurity=deserialize_list(json_data.get("CustomSecurity"), CustomSecurityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


@dataclass
class CustomSecurityDefinition(BaseModel):
    CipherSuites: Optional[Sequence[str]]
    MaxVersion: Optional[str]
    MinVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSecurityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSecurityDefinition"]:
        if not json_data:
            return None
        return cls(
            CipherSuites=json_data.get("CipherSuites"),
            MaxVersion=json_data.get("MaxVersion"),
            MinVersion=json_data.get("MinVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSecurityDefinition = CustomSecurityDefinition


@dataclass
class UseMtlsDefinition(BaseModel):
    TlsCertificates: Optional[Sequence["_TlsCertificatesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseMtlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseMtlsDefinition"]:
        if not json_data:
            return None
        return cls(
            TlsCertificates=deserialize_list(json_data.get("TlsCertificates"), TlsCertificatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseMtlsDefinition = UseMtlsDefinition


@dataclass
class TlsCertificatesDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Description: Optional[str]
    PrivateKey: Optional[Sequence["_PrivateKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Description=json_data.get("Description"),
            PrivateKey=deserialize_list(json_data.get("PrivateKey"), PrivateKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsCertificatesDefinition = TlsCertificatesDefinition


@dataclass
class PrivateKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretEncodingType=json_data.get("SecretEncodingType"),
            BlindfoldSecretInfo=deserialize_list(json_data.get("BlindfoldSecretInfo"), BlindfoldSecretInfoDefinition),
            BlindfoldSecretInfoInternal=deserialize_list(json_data.get("BlindfoldSecretInfoInternal"), BlindfoldSecretInfoInternalDefinition),
            ClearSecretInfo=deserialize_list(json_data.get("ClearSecretInfo"), ClearSecretInfoDefinition),
            VaultSecretInfo=deserialize_list(json_data.get("VaultSecretInfo"), VaultSecretInfoDefinition),
            WingmanSecretInfo=deserialize_list(json_data.get("WingmanSecretInfo"), WingmanSecretInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyDefinition = PrivateKeyDefinition


@dataclass
class BlindfoldSecretInfoDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoDefinition = BlindfoldSecretInfoDefinition


@dataclass
class BlindfoldSecretInfoInternalDefinition(BaseModel):
    DecryptionProvider: Optional[str]
    Location: Optional[str]
    StoreProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlindfoldSecretInfoInternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlindfoldSecretInfoInternalDefinition"]:
        if not json_data:
            return None
        return cls(
            DecryptionProvider=json_data.get("DecryptionProvider"),
            Location=json_data.get("Location"),
            StoreProvider=json_data.get("StoreProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlindfoldSecretInfoInternalDefinition = BlindfoldSecretInfoInternalDefinition


@dataclass
class ClearSecretInfoDefinition(BaseModel):
    Provider: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Provider=json_data.get("Provider"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearSecretInfoDefinition = ClearSecretInfoDefinition


@dataclass
class VaultSecretInfoDefinition(BaseModel):
    Key: Optional[str]
    Location: Optional[str]
    Provider: Optional[str]
    SecretEncoding: Optional[str]
    Version: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VaultSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VaultSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Location=json_data.get("Location"),
            Provider=json_data.get("Provider"),
            SecretEncoding=json_data.get("SecretEncoding"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VaultSecretInfoDefinition = VaultSecretInfoDefinition


@dataclass
class WingmanSecretInfoDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WingmanSecretInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WingmanSecretInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WingmanSecretInfoDefinition = WingmanSecretInfoDefinition


@dataclass
class UseServerVerificationDefinition(BaseModel):
    TrustedCaUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UseServerVerificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseServerVerificationDefinition"]:
        if not json_data:
            return None
        return cls(
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseServerVerificationDefinition = UseServerVerificationDefinition


