# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
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
    Tags: Optional[Sequence["_Tags"]]
    UpgradeMode: Optional[str]
    VmImage: Optional[str]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectory"]]
    Certificate: Optional[Sequence["_Certificate"]]
    CertificateCommonNames: Optional[Sequence["_CertificateCommonNames"]]
    ClientCertificateThumbprint: Optional[Sequence["_ClientCertificateThumbprint"]]
    DiagnosticsConfig: Optional[Sequence["_DiagnosticsConfig"]]
    FabricSettings: Optional[Sequence["_FabricSettings"]]
    NodeType: Optional[Sequence["_NodeType"]]
    ReverseProxyCertificate: Optional[Sequence["_ReverseProxyCertificate"]]
    Timeouts: Optional["_Timeouts"]
    CommonNames: Optional[Sequence["_CommonNames"]]
    ApplicationPorts: Optional[Sequence["_ApplicationPorts"]]
    EphemeralPorts: Optional[Sequence["_EphemeralPorts"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            UpgradeMode=json_data.get("UpgradeMode"),
            VmImage=json_data.get("VmImage"),
            AzureActiveDirectory=json_data.get("AzureActiveDirectory"),
            Certificate=json_data.get("Certificate"),
            CertificateCommonNames=json_data.get("CertificateCommonNames"),
            ClientCertificateThumbprint=json_data.get("ClientCertificateThumbprint"),
            DiagnosticsConfig=json_data.get("DiagnosticsConfig"),
            FabricSettings=json_data.get("FabricSettings"),
            NodeType=json_data.get("NodeType"),
            ReverseProxyCertificate=json_data.get("ReverseProxyCertificate"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            CommonNames=json_data.get("CommonNames"),
            ApplicationPorts=json_data.get("ApplicationPorts"),
            EphemeralPorts=json_data.get("EphemeralPorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AzureActiveDirectory:
    ClientApplicationId: Optional[str]
    ClusterApplicationId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectory"]:
        if not json_data:
            return None
        return cls(
            ClientApplicationId=json_data.get("ClientApplicationId"),
            ClusterApplicationId=json_data.get("ClusterApplicationId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectory = AzureActiveDirectory


@dataclass
class Certificate:
    Thumbprint: Optional[str]
    ThumbprintSecondary: Optional[str]
    X509StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            Thumbprint=json_data.get("Thumbprint"),
            ThumbprintSecondary=json_data.get("ThumbprintSecondary"),
            X509StoreName=json_data.get("X509StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


@dataclass
class CertificateCommonNames:
    X509StoreName: Optional[str]
    CommonNames: Optional[Sequence["_CommonNames"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateCommonNames"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateCommonNames"]:
        if not json_data:
            return None
        return cls(
            X509StoreName=json_data.get("X509StoreName"),
            CommonNames=json_data.get("CommonNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateCommonNames = CertificateCommonNames


@dataclass
class CommonNames:
    CertificateCommonName: Optional[str]
    CertificateIssuerThumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommonNames"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonNames"]:
        if not json_data:
            return None
        return cls(
            CertificateCommonName=json_data.get("CertificateCommonName"),
            CertificateIssuerThumbprint=json_data.get("CertificateIssuerThumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonNames = CommonNames


@dataclass
class ClientCertificateThumbprint:
    IsAdmin: Optional[bool]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientCertificateThumbprint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientCertificateThumbprint"]:
        if not json_data:
            return None
        return cls(
            IsAdmin=json_data.get("IsAdmin"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientCertificateThumbprint = ClientCertificateThumbprint


@dataclass
class DiagnosticsConfig:
    BlobEndpoint: Optional[str]
    ProtectedAccountKeyName: Optional[str]
    QueueEndpoint: Optional[str]
    StorageAccountName: Optional[str]
    TableEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiagnosticsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiagnosticsConfig"]:
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
_DiagnosticsConfig = DiagnosticsConfig


@dataclass
class FabricSettings:
    Name: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]

    @classmethod
    def _deserialize(
        cls: Type["_FabricSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FabricSettings"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FabricSettings = FabricSettings


@dataclass
class Parameters:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class NodeType:
    Capacities: Optional[Sequence["_Capacities"]]
    ClientEndpointPort: Optional[float]
    DurabilityLevel: Optional[str]
    HttpEndpointPort: Optional[float]
    InstanceCount: Optional[float]
    IsPrimary: Optional[bool]
    Name: Optional[str]
    PlacementProperties: Optional[Sequence["_PlacementProperties"]]
    ReverseProxyEndpointPort: Optional[float]
    ApplicationPorts: Optional[Sequence["_ApplicationPorts"]]
    EphemeralPorts: Optional[Sequence["_EphemeralPorts"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeType"]:
        if not json_data:
            return None
        return cls(
            Capacities=json_data.get("Capacities"),
            ClientEndpointPort=json_data.get("ClientEndpointPort"),
            DurabilityLevel=json_data.get("DurabilityLevel"),
            HttpEndpointPort=json_data.get("HttpEndpointPort"),
            InstanceCount=json_data.get("InstanceCount"),
            IsPrimary=json_data.get("IsPrimary"),
            Name=json_data.get("Name"),
            PlacementProperties=json_data.get("PlacementProperties"),
            ReverseProxyEndpointPort=json_data.get("ReverseProxyEndpointPort"),
            ApplicationPorts=json_data.get("ApplicationPorts"),
            EphemeralPorts=json_data.get("EphemeralPorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeType = NodeType


@dataclass
class Capacities:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Capacities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capacities"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capacities = Capacities


@dataclass
class PlacementProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementProperties = PlacementProperties


@dataclass
class ApplicationPorts:
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationPorts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationPorts"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationPorts = ApplicationPorts


@dataclass
class EphemeralPorts:
    EndPort: Optional[float]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralPorts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralPorts"]:
        if not json_data:
            return None
        return cls(
            EndPort=json_data.get("EndPort"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralPorts = EphemeralPorts


@dataclass
class ReverseProxyCertificate:
    Thumbprint: Optional[str]
    ThumbprintSecondary: Optional[str]
    X509StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReverseProxyCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReverseProxyCertificate"]:
        if not json_data:
            return None
        return cls(
            Thumbprint=json_data.get("Thumbprint"),
            ThumbprintSecondary=json_data.get("ThumbprintSecondary"),
            X509StoreName=json_data.get("X509StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReverseProxyCertificate = ReverseProxyCertificate


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


