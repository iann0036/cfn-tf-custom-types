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
    AddOnFeatures: Optional[Sequence[str]]
    ClusterCodeVersion: Optional[str]
    ClusterEndpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    ManagementEndpoint: Optional[str]
    Name: Optional[str]
    ReliabilityLevel: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UpgradeMode: Optional[str]
    VmImage: Optional[str]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectoryDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    CertificateCommonNames: Optional[Sequence["_CertificateCommonNamesDefinition"]]
    ClientCertificateCommonName: Optional[Sequence["_ClientCertificateCommonNameDefinition"]]
    ClientCertificateThumbprint: Optional[Sequence["_ClientCertificateThumbprintDefinition"]]
    DiagnosticsConfig: Optional[Sequence["_DiagnosticsConfigDefinition"]]
    FabricSettings: Optional[Sequence["_FabricSettingsDefinition"]]
    NodeType: Optional[Sequence["_NodeTypeDefinition"]]
    ReverseProxyCertificate: Optional[Sequence["_ReverseProxyCertificateDefinition"]]
    ReverseProxyCertificateCommonNames: Optional[Sequence["_ReverseProxyCertificateCommonNamesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradePolicy: Optional[Sequence["_UpgradePolicyDefinition"]]

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
            AddOnFeatures=json_data.get("AddOnFeatures"),
            ClusterCodeVersion=json_data.get("ClusterCodeVersion"),
            ClusterEndpoint=json_data.get("ClusterEndpoint"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            ManagementEndpoint=json_data.get("ManagementEndpoint"),
            Name=json_data.get("Name"),
            ReliabilityLevel=json_data.get("ReliabilityLevel"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UpgradeMode=json_data.get("UpgradeMode"),
            VmImage=json_data.get("VmImage"),
            AzureActiveDirectory=deserialize_list(json_data.get("AzureActiveDirectory"), AzureActiveDirectoryDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            CertificateCommonNames=deserialize_list(json_data.get("CertificateCommonNames"), CertificateCommonNamesDefinition),
            ClientCertificateCommonName=deserialize_list(json_data.get("ClientCertificateCommonName"), ClientCertificateCommonNameDefinition),
            ClientCertificateThumbprint=deserialize_list(json_data.get("ClientCertificateThumbprint"), ClientCertificateThumbprintDefinition),
            DiagnosticsConfig=deserialize_list(json_data.get("DiagnosticsConfig"), DiagnosticsConfigDefinition),
            FabricSettings=deserialize_list(json_data.get("FabricSettings"), FabricSettingsDefinition),
            NodeType=deserialize_list(json_data.get("NodeType"), NodeTypeDefinition),
            ReverseProxyCertificate=deserialize_list(json_data.get("ReverseProxyCertificate"), ReverseProxyCertificateDefinition),
            ReverseProxyCertificateCommonNames=deserialize_list(json_data.get("ReverseProxyCertificateCommonNames"), ReverseProxyCertificateCommonNamesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradePolicy=deserialize_list(json_data.get("UpgradePolicy"), UpgradePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AzureActiveDirectoryDefinition(BaseModel):
    ClientApplicationId: Optional[str]
    ClusterApplicationId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientApplicationId=json_data.get("ClientApplicationId"),
            ClusterApplicationId=json_data.get("ClusterApplicationId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectoryDefinition = AzureActiveDirectoryDefinition


@dataclass
class CertificateDefinition(BaseModel):
    Thumbprint: Optional[str]
    ThumbprintSecondary: Optional[str]
    X509StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Thumbprint=json_data.get("Thumbprint"),
            ThumbprintSecondary=json_data.get("ThumbprintSecondary"),
            X509StoreName=json_data.get("X509StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class CertificateCommonNamesDefinition(BaseModel):
    X509StoreName: Optional[str]
    CommonNames: Optional[Sequence["_CommonNamesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateCommonNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateCommonNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            X509StoreName=json_data.get("X509StoreName"),
            CommonNames=deserialize_list(json_data.get("CommonNames"), CommonNamesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateCommonNamesDefinition = CertificateCommonNamesDefinition


@dataclass
class CommonNamesDefinition(BaseModel):
    CertificateCommonName: Optional[str]
    CertificateIssuerThumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommonNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateCommonName=json_data.get("CertificateCommonName"),
            CertificateIssuerThumbprint=json_data.get("CertificateIssuerThumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonNamesDefinition = CommonNamesDefinition


@dataclass
class ClientCertificateCommonNameDefinition(BaseModel):
    CommonName: Optional[str]
    IsAdmin: Optional[bool]
    IssuerThumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateCommonNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateCommonNameDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            IsAdmin=json_data.get("IsAdmin"),
            IssuerThumbprint=json_data.get("IssuerThumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateCommonNameDefinition = ClientCertificateCommonNameDefinition


@dataclass
class ClientCertificateThumbprintDefinition(BaseModel):
    IsAdmin: Optional[bool]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateThumbprintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateThumbprintDefinition"]:
        if not json_data:
            return None
        return cls(
            IsAdmin=json_data.get("IsAdmin"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateThumbprintDefinition = ClientCertificateThumbprintDefinition


@dataclass
class DiagnosticsConfigDefinition(BaseModel):
    BlobEndpoint: Optional[str]
    ProtectedAccountKeyName: Optional[str]
    QueueEndpoint: Optional[str]
    StorageAccountName: Optional[str]
    TableEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiagnosticsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiagnosticsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BlobEndpoint=json_data.get("BlobEndpoint"),
            ProtectedAccountKeyName=json_data.get("ProtectedAccountKeyName"),
            QueueEndpoint=json_data.get("QueueEndpoint"),
            StorageAccountName=json_data.get("StorageAccountName"),
            TableEndpoint=json_data.get("TableEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiagnosticsConfigDefinition = DiagnosticsConfigDefinition


@dataclass
class FabricSettingsDefinition(BaseModel):
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FabricSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FabricSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FabricSettingsDefinition = FabricSettingsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class NodeTypeDefinition(BaseModel):
    Capacities: Optional[Sequence["_CapacitiesDefinition"]]
    ClientEndpointPort: Optional[float]
    DurabilityLevel: Optional[str]
    HttpEndpointPort: Optional[float]
    InstanceCount: Optional[float]
    IsPrimary: Optional[bool]
    Name: Optional[str]
    PlacementProperties: Optional[Sequence["_PlacementPropertiesDefinition"]]
    ReverseProxyEndpointPort: Optional[float]
    ApplicationPorts: Optional[Sequence["_ApplicationPortsDefinition"]]
    EphemeralPorts: Optional[Sequence["_EphemeralPortsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacities=deserialize_list(json_data.get("Capacities"), CapacitiesDefinition),
            ClientEndpointPort=json_data.get("ClientEndpointPort"),
            DurabilityLevel=json_data.get("DurabilityLevel"),
            HttpEndpointPort=json_data.get("HttpEndpointPort"),
            InstanceCount=json_data.get("InstanceCount"),
            IsPrimary=json_data.get("IsPrimary"),
            Name=json_data.get("Name"),
            PlacementProperties=deserialize_list(json_data.get("PlacementProperties"), PlacementPropertiesDefinition),
            ReverseProxyEndpointPort=json_data.get("ReverseProxyEndpointPort"),
            ApplicationPorts=deserialize_list(json_data.get("ApplicationPorts"), ApplicationPortsDefinition),
            EphemeralPorts=deserialize_list(json_data.get("EphemeralPorts"), EphemeralPortsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeTypeDefinition = NodeTypeDefinition


@dataclass
class CapacitiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacitiesDefinition = CapacitiesDefinition


@dataclass
class PlacementPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementPropertiesDefinition = PlacementPropertiesDefinition


@dataclass
class ApplicationPortsDefinition(BaseModel):
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationPortsDefinition = ApplicationPortsDefinition


@dataclass
class EphemeralPortsDefinition(BaseModel):
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralPortsDefinition = EphemeralPortsDefinition


@dataclass
class ReverseProxyCertificateDefinition(BaseModel):
    Thumbprint: Optional[str]
    ThumbprintSecondary: Optional[str]
    X509StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReverseProxyCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReverseProxyCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Thumbprint=json_data.get("Thumbprint"),
            ThumbprintSecondary=json_data.get("ThumbprintSecondary"),
            X509StoreName=json_data.get("X509StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReverseProxyCertificateDefinition = ReverseProxyCertificateDefinition


@dataclass
class ReverseProxyCertificateCommonNamesDefinition(BaseModel):
    X509StoreName: Optional[str]
    CommonNames: Optional[Sequence["_CommonNamesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReverseProxyCertificateCommonNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReverseProxyCertificateCommonNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            X509StoreName=json_data.get("X509StoreName"),
            CommonNames=deserialize_list(json_data.get("CommonNames"), CommonNamesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReverseProxyCertificateCommonNamesDefinition = ReverseProxyCertificateCommonNamesDefinition


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


@dataclass
class UpgradePolicyDefinition(BaseModel):
    ForceRestartEnabled: Optional[bool]
    HealthCheckRetryTimeout: Optional[str]
    HealthCheckStableDuration: Optional[str]
    HealthCheckWaitDuration: Optional[str]
    UpgradeDomainTimeout: Optional[str]
    UpgradeReplicaSetCheckTimeout: Optional[str]
    UpgradeTimeout: Optional[str]
    DeltaHealthPolicy: Optional[Sequence["_DeltaHealthPolicyDefinition"]]
    HealthPolicy: Optional[Sequence["_HealthPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ForceRestartEnabled=json_data.get("ForceRestartEnabled"),
            HealthCheckRetryTimeout=json_data.get("HealthCheckRetryTimeout"),
            HealthCheckStableDuration=json_data.get("HealthCheckStableDuration"),
            HealthCheckWaitDuration=json_data.get("HealthCheckWaitDuration"),
            UpgradeDomainTimeout=json_data.get("UpgradeDomainTimeout"),
            UpgradeReplicaSetCheckTimeout=json_data.get("UpgradeReplicaSetCheckTimeout"),
            UpgradeTimeout=json_data.get("UpgradeTimeout"),
            DeltaHealthPolicy=deserialize_list(json_data.get("DeltaHealthPolicy"), DeltaHealthPolicyDefinition),
            HealthPolicy=deserialize_list(json_data.get("HealthPolicy"), HealthPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradePolicyDefinition = UpgradePolicyDefinition


@dataclass
class DeltaHealthPolicyDefinition(BaseModel):
    MaxDeltaUnhealthyApplicationsPercent: Optional[float]
    MaxDeltaUnhealthyNodesPercent: Optional[float]
    MaxUpgradeDomainDeltaUnhealthyNodesPercent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeltaHealthPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeltaHealthPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxDeltaUnhealthyApplicationsPercent=json_data.get("MaxDeltaUnhealthyApplicationsPercent"),
            MaxDeltaUnhealthyNodesPercent=json_data.get("MaxDeltaUnhealthyNodesPercent"),
            MaxUpgradeDomainDeltaUnhealthyNodesPercent=json_data.get("MaxUpgradeDomainDeltaUnhealthyNodesPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeltaHealthPolicyDefinition = DeltaHealthPolicyDefinition


@dataclass
class HealthPolicyDefinition(BaseModel):
    MaxUnhealthyApplicationsPercent: Optional[float]
    MaxUnhealthyNodesPercent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxUnhealthyApplicationsPercent=json_data.get("MaxUnhealthyApplicationsPercent"),
            MaxUnhealthyNodesPercent=json_data.get("MaxUnhealthyNodesPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthPolicyDefinition = HealthPolicyDefinition


