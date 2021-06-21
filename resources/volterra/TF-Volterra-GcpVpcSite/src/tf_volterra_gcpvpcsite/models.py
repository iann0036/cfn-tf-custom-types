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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Assisted: Optional[bool]
    Description: Optional[str]
    Disable: Optional[bool]
    DiskSize: Optional[float]
    GcpRegion: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LogsStreamingDisabled: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    NodesPerAz: Optional[float]
    SshKey: Optional[str]
    CloudCredentials: Optional[Sequence["_CloudCredentialsDefinition"]]
    Coordinates: Optional[Sequence["_CoordinatesDefinition"]]
    IngressEgressGw: Optional[Sequence["_IngressEgressGwDefinition"]]
    IngressGw: Optional[Sequence["_IngressGwDefinition"]]
    LogReceiver: Optional[Sequence["_LogReceiverDefinition"]]
    Os: Optional[Sequence["_OsDefinition"]]
    Sw: Optional[Sequence["_SwDefinition"]]
    VoltstackCluster: Optional[Sequence["_VoltstackClusterDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Assisted=json_data.get("Assisted"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DiskSize=json_data.get("DiskSize"),
            GcpRegion=json_data.get("GcpRegion"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LogsStreamingDisabled=json_data.get("LogsStreamingDisabled"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NodesPerAz=json_data.get("NodesPerAz"),
            SshKey=json_data.get("SshKey"),
            CloudCredentials=deserialize_list(json_data.get("CloudCredentials"), CloudCredentialsDefinition),
            Coordinates=deserialize_list(json_data.get("Coordinates"), CoordinatesDefinition),
            IngressEgressGw=deserialize_list(json_data.get("IngressEgressGw"), IngressEgressGwDefinition),
            IngressGw=deserialize_list(json_data.get("IngressGw"), IngressGwDefinition),
            LogReceiver=deserialize_list(json_data.get("LogReceiver"), LogReceiverDefinition),
            Os=deserialize_list(json_data.get("Os"), OsDefinition),
            Sw=deserialize_list(json_data.get("Sw"), SwDefinition),
            VoltstackCluster=deserialize_list(json_data.get("VoltstackCluster"), VoltstackClusterDefinition),
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
class CloudCredentialsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudCredentialsDefinition = CloudCredentialsDefinition


@dataclass
class CoordinatesDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CoordinatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoordinatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoordinatesDefinition = CoordinatesDefinition


@dataclass
class IngressEgressGwDefinition(BaseModel):
    ForwardProxyAllowAll: Optional[bool]
    GcpCertifiedHw: Optional[str]
    GcpZoneNames: Optional[Sequence[str]]
    NoForwardProxy: Optional[bool]
    NoGlobalNetwork: Optional[bool]
    NoInsideStaticRoutes: Optional[bool]
    NoNetworkPolicy: Optional[bool]
    NoOutsideStaticRoutes: Optional[bool]
    NodeNumber: Optional[float]
    ActiveForwardProxyPolicies: Optional[Sequence["_ActiveForwardProxyPoliciesDefinition"]]
    ActiveNetworkPolicies: Optional[Sequence["_ActiveNetworkPoliciesDefinition"]]
    GlobalNetworkList: Optional[Sequence["_GlobalNetworkListDefinition"]]
    InsideNetwork: Optional[Sequence["_InsideNetworkDefinition"]]
    InsideStaticRoutes: Optional[Sequence["_InsideStaticRoutesDefinition"]]
    InsideSubnet: Optional[Sequence["_InsideSubnetDefinition"]]
    OutsideNetwork: Optional[Sequence["_OutsideNetworkDefinition"]]
    OutsideStaticRoutes: Optional[Sequence["_OutsideStaticRoutesDefinition"]]
    OutsideSubnet: Optional[Sequence["_OutsideSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressEgressGwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressEgressGwDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyAllowAll=json_data.get("ForwardProxyAllowAll"),
            GcpCertifiedHw=json_data.get("GcpCertifiedHw"),
            GcpZoneNames=json_data.get("GcpZoneNames"),
            NoForwardProxy=json_data.get("NoForwardProxy"),
            NoGlobalNetwork=json_data.get("NoGlobalNetwork"),
            NoInsideStaticRoutes=json_data.get("NoInsideStaticRoutes"),
            NoNetworkPolicy=json_data.get("NoNetworkPolicy"),
            NoOutsideStaticRoutes=json_data.get("NoOutsideStaticRoutes"),
            NodeNumber=json_data.get("NodeNumber"),
            ActiveForwardProxyPolicies=deserialize_list(json_data.get("ActiveForwardProxyPolicies"), ActiveForwardProxyPoliciesDefinition),
            ActiveNetworkPolicies=deserialize_list(json_data.get("ActiveNetworkPolicies"), ActiveNetworkPoliciesDefinition),
            GlobalNetworkList=deserialize_list(json_data.get("GlobalNetworkList"), GlobalNetworkListDefinition),
            InsideNetwork=deserialize_list(json_data.get("InsideNetwork"), InsideNetworkDefinition),
            InsideStaticRoutes=deserialize_list(json_data.get("InsideStaticRoutes"), InsideStaticRoutesDefinition),
            InsideSubnet=deserialize_list(json_data.get("InsideSubnet"), InsideSubnetDefinition),
            OutsideNetwork=deserialize_list(json_data.get("OutsideNetwork"), OutsideNetworkDefinition),
            OutsideStaticRoutes=deserialize_list(json_data.get("OutsideStaticRoutes"), OutsideStaticRoutesDefinition),
            OutsideSubnet=deserialize_list(json_data.get("OutsideSubnet"), OutsideSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressEgressGwDefinition = IngressEgressGwDefinition


@dataclass
class ActiveForwardProxyPoliciesDefinition(BaseModel):
    ForwardProxyPolicies: Optional[Sequence["_ForwardProxyPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyPolicies=deserialize_list(json_data.get("ForwardProxyPolicies"), ForwardProxyPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveForwardProxyPoliciesDefinition = ActiveForwardProxyPoliciesDefinition


@dataclass
class ForwardProxyPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardProxyPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardProxyPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardProxyPoliciesDefinition = ForwardProxyPoliciesDefinition


@dataclass
class ActiveNetworkPoliciesDefinition(BaseModel):
    NetworkPolicies: Optional[Sequence["_NetworkPoliciesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveNetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveNetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkPolicies=deserialize_list(json_data.get("NetworkPolicies"), NetworkPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveNetworkPoliciesDefinition = ActiveNetworkPoliciesDefinition


@dataclass
class NetworkPoliciesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkPoliciesDefinition = NetworkPoliciesDefinition


@dataclass
class GlobalNetworkListDefinition(BaseModel):
    GlobalNetworkConnections: Optional[Sequence["_GlobalNetworkConnectionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalNetworkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalNetworkListDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalNetworkConnections=deserialize_list(json_data.get("GlobalNetworkConnections"), GlobalNetworkConnectionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalNetworkListDefinition = GlobalNetworkListDefinition


@dataclass
class GlobalNetworkConnectionsDefinition(BaseModel):
    DisableForwardProxy: Optional[bool]
    EnableForwardProxy: Optional[Sequence["_EnableForwardProxyDefinition"]]
    SliToGlobalDr: Optional[Sequence["_SliToGlobalDrDefinition"]]
    SloToGlobalDr: Optional[Sequence["_SloToGlobalDrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalNetworkConnectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalNetworkConnectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableForwardProxy=json_data.get("DisableForwardProxy"),
            EnableForwardProxy=deserialize_list(json_data.get("EnableForwardProxy"), EnableForwardProxyDefinition),
            SliToGlobalDr=deserialize_list(json_data.get("SliToGlobalDr"), SliToGlobalDrDefinition),
            SloToGlobalDr=deserialize_list(json_data.get("SloToGlobalDr"), SloToGlobalDrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalNetworkConnectionsDefinition = GlobalNetworkConnectionsDefinition


@dataclass
class EnableForwardProxyDefinition(BaseModel):
    ConnectionTimeout: Optional[float]
    MaxConnectAttempts: Optional[float]
    NoInterception: Optional[bool]
    WhiteListedPorts: Optional[Sequence[float]]
    WhiteListedPrefixes: Optional[Sequence[str]]
    TlsIntercept: Optional[Sequence["_TlsInterceptDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnableForwardProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableForwardProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            MaxConnectAttempts=json_data.get("MaxConnectAttempts"),
            NoInterception=json_data.get("NoInterception"),
            WhiteListedPorts=json_data.get("WhiteListedPorts"),
            WhiteListedPrefixes=json_data.get("WhiteListedPrefixes"),
            TlsIntercept=deserialize_list(json_data.get("TlsIntercept"), TlsInterceptDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableForwardProxyDefinition = EnableForwardProxyDefinition


@dataclass
class TlsInterceptDefinition(BaseModel):
    EnableForAllDomains: Optional[bool]
    TrustedCaUrl: Optional[str]
    VolterraCertificate: Optional[bool]
    VolterraTrustedCa: Optional[bool]
    CustomCertificate: Optional[Sequence["_CustomCertificateDefinition"]]
    Policy: Optional[Sequence["_PolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsInterceptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsInterceptDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableForAllDomains=json_data.get("EnableForAllDomains"),
            TrustedCaUrl=json_data.get("TrustedCaUrl"),
            VolterraCertificate=json_data.get("VolterraCertificate"),
            VolterraTrustedCa=json_data.get("VolterraTrustedCa"),
            CustomCertificate=deserialize_list(json_data.get("CustomCertificate"), CustomCertificateDefinition),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsInterceptDefinition = TlsInterceptDefinition


@dataclass
class CustomCertificateDefinition(BaseModel):
    CertificateUrl: Optional[str]
    Description: Optional[str]
    PrivateKey: Optional[Sequence["_PrivateKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateUrl=json_data.get("CertificateUrl"),
            Description=json_data.get("Description"),
            PrivateKey=deserialize_list(json_data.get("PrivateKey"), PrivateKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCertificateDefinition = CustomCertificateDefinition


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
class PolicyDefinition(BaseModel):
    InterceptionRules: Optional[Sequence["_InterceptionRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InterceptionRules=deserialize_list(json_data.get("InterceptionRules"), InterceptionRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


@dataclass
class InterceptionRulesDefinition(BaseModel):
    DisableInterception: Optional[bool]
    EnableInterception: Optional[bool]
    DomainMatch: Optional[Sequence["_DomainMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterceptionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterceptionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableInterception=json_data.get("DisableInterception"),
            EnableInterception=json_data.get("EnableInterception"),
            DomainMatch=deserialize_list(json_data.get("DomainMatch"), DomainMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterceptionRulesDefinition = InterceptionRulesDefinition


@dataclass
class DomainMatchDefinition(BaseModel):
    ExactValue: Optional[str]
    RegexValue: Optional[str]
    SuffixValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactValue=json_data.get("ExactValue"),
            RegexValue=json_data.get("RegexValue"),
            SuffixValue=json_data.get("SuffixValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainMatchDefinition = DomainMatchDefinition


@dataclass
class SliToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SliToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliToGlobalDrDefinition = SliToGlobalDrDefinition


@dataclass
class GlobalVnDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalVnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalVnDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalVnDefinition = GlobalVnDefinition


@dataclass
class SloToGlobalDrDefinition(BaseModel):
    GlobalVn: Optional[Sequence["_GlobalVnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SloToGlobalDrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SloToGlobalDrDefinition"]:
        if not json_data:
            return None
        return cls(
            GlobalVn=deserialize_list(json_data.get("GlobalVn"), GlobalVnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SloToGlobalDrDefinition = SloToGlobalDrDefinition


@dataclass
class InsideNetworkDefinition(BaseModel):
    ExistingNetwork: Optional[Sequence["_ExistingNetworkDefinition"]]
    NewNetwork: Optional[Sequence["_NewNetworkDefinition"]]
    NewNetworkAutogenerate: Optional[Sequence["_NewNetworkAutogenerateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InsideNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingNetwork=deserialize_list(json_data.get("ExistingNetwork"), ExistingNetworkDefinition),
            NewNetwork=deserialize_list(json_data.get("NewNetwork"), NewNetworkDefinition),
            NewNetworkAutogenerate=deserialize_list(json_data.get("NewNetworkAutogenerate"), NewNetworkAutogenerateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideNetworkDefinition = InsideNetworkDefinition


@dataclass
class ExistingNetworkDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExistingNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExistingNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExistingNetworkDefinition = ExistingNetworkDefinition


@dataclass
class NewNetworkDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NewNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewNetworkDefinition = NewNetworkDefinition


@dataclass
class NewNetworkAutogenerateDefinition(BaseModel):
    Autogenerate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NewNetworkAutogenerateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewNetworkAutogenerateDefinition"]:
        if not json_data:
            return None
        return cls(
            Autogenerate=json_data.get("Autogenerate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewNetworkAutogenerateDefinition = NewNetworkAutogenerateDefinition


@dataclass
class InsideStaticRoutesDefinition(BaseModel):
    StaticRouteList: Optional[Sequence["_StaticRouteListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InsideStaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideStaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            StaticRouteList=deserialize_list(json_data.get("StaticRouteList"), StaticRouteListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideStaticRoutesDefinition = InsideStaticRoutesDefinition


@dataclass
class StaticRouteListDefinition(BaseModel):
    SimpleStaticRoute: Optional[str]
    CustomStaticRoute: Optional[Sequence["_CustomStaticRouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticRouteListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticRouteListDefinition"]:
        if not json_data:
            return None
        return cls(
            SimpleStaticRoute=json_data.get("SimpleStaticRoute"),
            CustomStaticRoute=deserialize_list(json_data.get("CustomStaticRoute"), CustomStaticRouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticRouteListDefinition = StaticRouteListDefinition


@dataclass
class CustomStaticRouteDefinition(BaseModel):
    Attrs: Optional[Sequence[str]]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Nexthop: Optional[Sequence["_NexthopDefinition"]]
    Subnets: Optional[Sequence["_SubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomStaticRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomStaticRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Attrs=json_data.get("Attrs"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Nexthop=deserialize_list(json_data.get("Nexthop"), NexthopDefinition),
            Subnets=deserialize_list(json_data.get("Subnets"), SubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomStaticRouteDefinition = CustomStaticRouteDefinition


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
class NexthopDefinition(BaseModel):
    Type: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    NexthopAddress: Optional[Sequence["_NexthopAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NexthopDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NexthopDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            NexthopAddress=deserialize_list(json_data.get("NexthopAddress"), NexthopAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NexthopDefinition = NexthopDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class NexthopAddressDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NexthopAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NexthopAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NexthopAddressDefinition = NexthopAddressDefinition


@dataclass
class Ipv4Definition(BaseModel):
    Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4Definition = Ipv4Definition


@dataclass
class Ipv6Definition(BaseModel):
    Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class SubnetsDefinition(BaseModel):
    Ipv4: Optional[Sequence["_Ipv4Definition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=deserialize_list(json_data.get("Ipv4"), Ipv4Definition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetsDefinition = SubnetsDefinition


@dataclass
class InsideSubnetDefinition(BaseModel):
    ExistingSubnet: Optional[Sequence["_ExistingSubnetDefinition"]]
    NewSubnet: Optional[Sequence["_NewSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InsideSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnet=deserialize_list(json_data.get("ExistingSubnet"), ExistingSubnetDefinition),
            NewSubnet=deserialize_list(json_data.get("NewSubnet"), NewSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideSubnetDefinition = InsideSubnetDefinition


@dataclass
class ExistingSubnetDefinition(BaseModel):
    SubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExistingSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExistingSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetName=json_data.get("SubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExistingSubnetDefinition = ExistingSubnetDefinition


@dataclass
class NewSubnetDefinition(BaseModel):
    PrimaryIpv4: Optional[str]
    SubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NewSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            PrimaryIpv4=json_data.get("PrimaryIpv4"),
            SubnetName=json_data.get("SubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewSubnetDefinition = NewSubnetDefinition


@dataclass
class OutsideNetworkDefinition(BaseModel):
    ExistingNetwork: Optional[Sequence["_ExistingNetworkDefinition"]]
    NewNetwork: Optional[Sequence["_NewNetworkDefinition"]]
    NewNetworkAutogenerate: Optional[Sequence["_NewNetworkAutogenerateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingNetwork=deserialize_list(json_data.get("ExistingNetwork"), ExistingNetworkDefinition),
            NewNetwork=deserialize_list(json_data.get("NewNetwork"), NewNetworkDefinition),
            NewNetworkAutogenerate=deserialize_list(json_data.get("NewNetworkAutogenerate"), NewNetworkAutogenerateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideNetworkDefinition = OutsideNetworkDefinition


@dataclass
class OutsideStaticRoutesDefinition(BaseModel):
    StaticRouteList: Optional[Sequence["_StaticRouteListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideStaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideStaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            StaticRouteList=deserialize_list(json_data.get("StaticRouteList"), StaticRouteListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideStaticRoutesDefinition = OutsideStaticRoutesDefinition


@dataclass
class OutsideSubnetDefinition(BaseModel):
    ExistingSubnet: Optional[Sequence["_ExistingSubnetDefinition"]]
    NewSubnet: Optional[Sequence["_NewSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnet=deserialize_list(json_data.get("ExistingSubnet"), ExistingSubnetDefinition),
            NewSubnet=deserialize_list(json_data.get("NewSubnet"), NewSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideSubnetDefinition = OutsideSubnetDefinition


@dataclass
class IngressGwDefinition(BaseModel):
    GcpCertifiedHw: Optional[str]
    GcpZoneNames: Optional[Sequence[str]]
    NodeNumber: Optional[float]
    LocalNetwork: Optional[Sequence["_LocalNetworkDefinition"]]
    LocalSubnet: Optional[Sequence["_LocalSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressGwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressGwDefinition"]:
        if not json_data:
            return None
        return cls(
            GcpCertifiedHw=json_data.get("GcpCertifiedHw"),
            GcpZoneNames=json_data.get("GcpZoneNames"),
            NodeNumber=json_data.get("NodeNumber"),
            LocalNetwork=deserialize_list(json_data.get("LocalNetwork"), LocalNetworkDefinition),
            LocalSubnet=deserialize_list(json_data.get("LocalSubnet"), LocalSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressGwDefinition = IngressGwDefinition


@dataclass
class LocalNetworkDefinition(BaseModel):
    ExistingNetwork: Optional[Sequence["_ExistingNetworkDefinition"]]
    NewNetwork: Optional[Sequence["_NewNetworkDefinition"]]
    NewNetworkAutogenerate: Optional[Sequence["_NewNetworkAutogenerateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingNetwork=deserialize_list(json_data.get("ExistingNetwork"), ExistingNetworkDefinition),
            NewNetwork=deserialize_list(json_data.get("NewNetwork"), NewNetworkDefinition),
            NewNetworkAutogenerate=deserialize_list(json_data.get("NewNetworkAutogenerate"), NewNetworkAutogenerateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalNetworkDefinition = LocalNetworkDefinition


@dataclass
class LocalSubnetDefinition(BaseModel):
    ExistingSubnet: Optional[Sequence["_ExistingSubnetDefinition"]]
    NewSubnet: Optional[Sequence["_NewSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnet=deserialize_list(json_data.get("ExistingSubnet"), ExistingSubnetDefinition),
            NewSubnet=deserialize_list(json_data.get("NewSubnet"), NewSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSubnetDefinition = LocalSubnetDefinition


@dataclass
class LogReceiverDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogReceiverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogReceiverDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogReceiverDefinition = LogReceiverDefinition


@dataclass
class OsDefinition(BaseModel):
    DefaultOsVersion: Optional[bool]
    OperatingSystemVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultOsVersion=json_data.get("DefaultOsVersion"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDefinition = OsDefinition


@dataclass
class SwDefinition(BaseModel):
    DefaultSwVersion: Optional[bool]
    VolterraSoftwareVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultSwVersion=json_data.get("DefaultSwVersion"),
            VolterraSoftwareVersion=json_data.get("VolterraSoftwareVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwDefinition = SwDefinition


@dataclass
class VoltstackClusterDefinition(BaseModel):
    ForwardProxyAllowAll: Optional[bool]
    GcpCertifiedHw: Optional[str]
    GcpZoneNames: Optional[Sequence[str]]
    NoForwardProxy: Optional[bool]
    NoGlobalNetwork: Optional[bool]
    NoK8sCluster: Optional[bool]
    NoNetworkPolicy: Optional[bool]
    NoOutsideStaticRoutes: Optional[bool]
    NodeNumber: Optional[float]
    ActiveForwardProxyPolicies: Optional[Sequence["_ActiveForwardProxyPoliciesDefinition"]]
    ActiveNetworkPolicies: Optional[Sequence["_ActiveNetworkPoliciesDefinition"]]
    GlobalNetworkList: Optional[Sequence["_GlobalNetworkListDefinition"]]
    K8sCluster: Optional[Sequence["_K8sClusterDefinition"]]
    OutsideStaticRoutes: Optional[Sequence["_OutsideStaticRoutesDefinition"]]
    SiteLocalNetwork: Optional[Sequence["_SiteLocalNetworkDefinition"]]
    SiteLocalSubnet: Optional[Sequence["_SiteLocalSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VoltstackClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoltstackClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyAllowAll=json_data.get("ForwardProxyAllowAll"),
            GcpCertifiedHw=json_data.get("GcpCertifiedHw"),
            GcpZoneNames=json_data.get("GcpZoneNames"),
            NoForwardProxy=json_data.get("NoForwardProxy"),
            NoGlobalNetwork=json_data.get("NoGlobalNetwork"),
            NoK8sCluster=json_data.get("NoK8sCluster"),
            NoNetworkPolicy=json_data.get("NoNetworkPolicy"),
            NoOutsideStaticRoutes=json_data.get("NoOutsideStaticRoutes"),
            NodeNumber=json_data.get("NodeNumber"),
            ActiveForwardProxyPolicies=deserialize_list(json_data.get("ActiveForwardProxyPolicies"), ActiveForwardProxyPoliciesDefinition),
            ActiveNetworkPolicies=deserialize_list(json_data.get("ActiveNetworkPolicies"), ActiveNetworkPoliciesDefinition),
            GlobalNetworkList=deserialize_list(json_data.get("GlobalNetworkList"), GlobalNetworkListDefinition),
            K8sCluster=deserialize_list(json_data.get("K8sCluster"), K8sClusterDefinition),
            OutsideStaticRoutes=deserialize_list(json_data.get("OutsideStaticRoutes"), OutsideStaticRoutesDefinition),
            SiteLocalNetwork=deserialize_list(json_data.get("SiteLocalNetwork"), SiteLocalNetworkDefinition),
            SiteLocalSubnet=deserialize_list(json_data.get("SiteLocalSubnet"), SiteLocalSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoltstackClusterDefinition = VoltstackClusterDefinition


@dataclass
class K8sClusterDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_K8sClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_K8sClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_K8sClusterDefinition = K8sClusterDefinition


@dataclass
class SiteLocalNetworkDefinition(BaseModel):
    ExistingNetwork: Optional[Sequence["_ExistingNetworkDefinition"]]
    NewNetwork: Optional[Sequence["_NewNetworkDefinition"]]
    NewNetworkAutogenerate: Optional[Sequence["_NewNetworkAutogenerateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteLocalNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteLocalNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingNetwork=deserialize_list(json_data.get("ExistingNetwork"), ExistingNetworkDefinition),
            NewNetwork=deserialize_list(json_data.get("NewNetwork"), NewNetworkDefinition),
            NewNetworkAutogenerate=deserialize_list(json_data.get("NewNetworkAutogenerate"), NewNetworkAutogenerateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteLocalNetworkDefinition = SiteLocalNetworkDefinition


@dataclass
class SiteLocalSubnetDefinition(BaseModel):
    ExistingSubnet: Optional[Sequence["_ExistingSubnetDefinition"]]
    NewSubnet: Optional[Sequence["_NewSubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteLocalSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteLocalSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            ExistingSubnet=deserialize_list(json_data.get("ExistingSubnet"), ExistingSubnetDefinition),
            NewSubnet=deserialize_list(json_data.get("NewSubnet"), NewSubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteLocalSubnetDefinition = SiteLocalSubnetDefinition

