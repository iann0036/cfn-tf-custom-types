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
    AllowAllUsb: Optional[bool]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    DefaultConfig: Optional[bool]
    DefaultStorageClass: Optional[bool]
    DenyAllUsb: Optional[bool]
    Description: Optional[str]
    Disable: Optional[bool]
    DisableGpu: Optional[bool]
    EnableDefaultFleetConfigDownload: Optional[bool]
    EnableGpu: Optional[bool]
    FleetLabel: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LogsStreamingDisabled: Optional[bool]
    Name: Optional[str]
    Namespace: Optional[str]
    NoBondDevices: Optional[bool]
    NoDcClusterGroup: Optional[bool]
    NoStorageDevice: Optional[bool]
    NoStorageInterfaces: Optional[bool]
    NoStorageStaticRoutes: Optional[bool]
    OperatingSystemVersion: Optional[str]
    VolterraSoftwareVersion: Optional[str]
    BondDeviceList: Optional[Sequence["_BondDeviceListDefinition"]]
    DcClusterGroup: Optional[Sequence["_DcClusterGroupDefinition"]]
    DcClusterGroupInside: Optional[Sequence["_DcClusterGroupInsideDefinition"]]
    DeviceList: Optional[Sequence["_DeviceListDefinition"]]
    InsideVirtualNetwork: Optional[Sequence["_InsideVirtualNetworkDefinition"]]
    InterfaceList: Optional[Sequence["_InterfaceListDefinition"]]
    LogReceiver: Optional[Sequence["_LogReceiverDefinition"]]
    NetworkConnectors: Optional[Sequence["_NetworkConnectorsDefinition"]]
    NetworkFirewall: Optional[Sequence["_NetworkFirewallDefinition"]]
    OutsideVirtualNetwork: Optional[Sequence["_OutsideVirtualNetworkDefinition"]]
    StorageClassList: Optional[Sequence["_StorageClassListDefinition"]]
    StorageDeviceList: Optional[Sequence["_StorageDeviceListDefinition"]]
    StorageInterfaceList: Optional[Sequence["_StorageInterfaceListDefinition"]]
    StorageStaticRoutes: Optional[Sequence["_StorageStaticRoutesDefinition"]]
    UsbPolicy: Optional[Sequence["_UsbPolicyDefinition"]]

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
            AllowAllUsb=json_data.get("AllowAllUsb"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            DefaultConfig=json_data.get("DefaultConfig"),
            DefaultStorageClass=json_data.get("DefaultStorageClass"),
            DenyAllUsb=json_data.get("DenyAllUsb"),
            Description=json_data.get("Description"),
            Disable=json_data.get("Disable"),
            DisableGpu=json_data.get("DisableGpu"),
            EnableDefaultFleetConfigDownload=json_data.get("EnableDefaultFleetConfigDownload"),
            EnableGpu=json_data.get("EnableGpu"),
            FleetLabel=json_data.get("FleetLabel"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LogsStreamingDisabled=json_data.get("LogsStreamingDisabled"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            NoBondDevices=json_data.get("NoBondDevices"),
            NoDcClusterGroup=json_data.get("NoDcClusterGroup"),
            NoStorageDevice=json_data.get("NoStorageDevice"),
            NoStorageInterfaces=json_data.get("NoStorageInterfaces"),
            NoStorageStaticRoutes=json_data.get("NoStorageStaticRoutes"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
            VolterraSoftwareVersion=json_data.get("VolterraSoftwareVersion"),
            BondDeviceList=deserialize_list(json_data.get("BondDeviceList"), BondDeviceListDefinition),
            DcClusterGroup=deserialize_list(json_data.get("DcClusterGroup"), DcClusterGroupDefinition),
            DcClusterGroupInside=deserialize_list(json_data.get("DcClusterGroupInside"), DcClusterGroupInsideDefinition),
            DeviceList=deserialize_list(json_data.get("DeviceList"), DeviceListDefinition),
            InsideVirtualNetwork=deserialize_list(json_data.get("InsideVirtualNetwork"), InsideVirtualNetworkDefinition),
            InterfaceList=deserialize_list(json_data.get("InterfaceList"), InterfaceListDefinition),
            LogReceiver=deserialize_list(json_data.get("LogReceiver"), LogReceiverDefinition),
            NetworkConnectors=deserialize_list(json_data.get("NetworkConnectors"), NetworkConnectorsDefinition),
            NetworkFirewall=deserialize_list(json_data.get("NetworkFirewall"), NetworkFirewallDefinition),
            OutsideVirtualNetwork=deserialize_list(json_data.get("OutsideVirtualNetwork"), OutsideVirtualNetworkDefinition),
            StorageClassList=deserialize_list(json_data.get("StorageClassList"), StorageClassListDefinition),
            StorageDeviceList=deserialize_list(json_data.get("StorageDeviceList"), StorageDeviceListDefinition),
            StorageInterfaceList=deserialize_list(json_data.get("StorageInterfaceList"), StorageInterfaceListDefinition),
            StorageStaticRoutes=deserialize_list(json_data.get("StorageStaticRoutes"), StorageStaticRoutesDefinition),
            UsbPolicy=deserialize_list(json_data.get("UsbPolicy"), UsbPolicyDefinition),
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
class BondDeviceListDefinition(BaseModel):
    BondDevices: Optional[Sequence["_BondDevicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BondDeviceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BondDeviceListDefinition"]:
        if not json_data:
            return None
        return cls(
            BondDevices=deserialize_list(json_data.get("BondDevices"), BondDevicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BondDeviceListDefinition = BondDeviceListDefinition


@dataclass
class BondDevicesDefinition(BaseModel):
    ActiveBackup: Optional[bool]
    Devices: Optional[Sequence[str]]
    LinkPollingInterval: Optional[float]
    LinkUpDelay: Optional[float]
    Name: Optional[str]
    Lacp: Optional[Sequence["_LacpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BondDevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BondDevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveBackup=json_data.get("ActiveBackup"),
            Devices=json_data.get("Devices"),
            LinkPollingInterval=json_data.get("LinkPollingInterval"),
            LinkUpDelay=json_data.get("LinkUpDelay"),
            Name=json_data.get("Name"),
            Lacp=deserialize_list(json_data.get("Lacp"), LacpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BondDevicesDefinition = BondDevicesDefinition


@dataclass
class LacpDefinition(BaseModel):
    Rate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LacpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LacpDefinition"]:
        if not json_data:
            return None
        return cls(
            Rate=json_data.get("Rate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LacpDefinition = LacpDefinition


@dataclass
class DcClusterGroupDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DcClusterGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DcClusterGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DcClusterGroupDefinition = DcClusterGroupDefinition


@dataclass
class DcClusterGroupInsideDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DcClusterGroupInsideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DcClusterGroupInsideDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DcClusterGroupInsideDefinition = DcClusterGroupInsideDefinition


@dataclass
class DeviceListDefinition(BaseModel):
    Devices: Optional[Sequence["_DevicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Devices=deserialize_list(json_data.get("Devices"), DevicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceListDefinition = DeviceListDefinition


@dataclass
class DevicesDefinition(BaseModel):
    Name: Optional[str]
    Owner: Optional[str]
    NetworkDevice: Optional[Sequence["_NetworkDeviceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            NetworkDevice=deserialize_list(json_data.get("NetworkDevice"), NetworkDeviceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicesDefinition = DevicesDefinition


@dataclass
class NetworkDeviceDefinition(BaseModel):
    Use: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Use=json_data.get("Use"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDeviceDefinition = NetworkDeviceDefinition


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
class InsideVirtualNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsideVirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsideVirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsideVirtualNetworkDefinition = InsideVirtualNetworkDefinition


@dataclass
class InterfaceListDefinition(BaseModel):
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceListDefinition = InterfaceListDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


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
class NetworkConnectorsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConnectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConnectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConnectorsDefinition = NetworkConnectorsDefinition


@dataclass
class NetworkFirewallDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFirewallDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFirewallDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFirewallDefinition = NetworkFirewallDefinition


@dataclass
class OutsideVirtualNetworkDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutsideVirtualNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutsideVirtualNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutsideVirtualNetworkDefinition = OutsideVirtualNetworkDefinition


@dataclass
class StorageClassListDefinition(BaseModel):
    StorageClasses: Optional[Sequence["_StorageClassesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageClasses=deserialize_list(json_data.get("StorageClasses"), StorageClassesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassListDefinition = StorageClassListDefinition


@dataclass
class StorageClassesDefinition(BaseModel):
    AdvancedStorageParameters: Optional[Sequence["_AdvancedStorageParametersDefinition"]]
    AllowVolumeExpansion: Optional[bool]
    DefaultStorageClass: Optional[bool]
    Description: Optional[str]
    ReclaimPolicy: Optional[str]
    StorageClassName: Optional[str]
    StorageDevice: Optional[str]
    NetappTrident: Optional[Sequence["_NetappTridentDefinition"]]
    OpenebsEnterprise: Optional[Sequence["_OpenebsEnterpriseDefinition"]]
    PureServiceOrchestrator: Optional[Sequence["_PureServiceOrchestratorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvancedStorageParameters=deserialize_list(json_data.get("AdvancedStorageParameters"), AdvancedStorageParametersDefinition),
            AllowVolumeExpansion=json_data.get("AllowVolumeExpansion"),
            DefaultStorageClass=json_data.get("DefaultStorageClass"),
            Description=json_data.get("Description"),
            ReclaimPolicy=json_data.get("ReclaimPolicy"),
            StorageClassName=json_data.get("StorageClassName"),
            StorageDevice=json_data.get("StorageDevice"),
            NetappTrident=deserialize_list(json_data.get("NetappTrident"), NetappTridentDefinition),
            OpenebsEnterprise=deserialize_list(json_data.get("OpenebsEnterprise"), OpenebsEnterpriseDefinition),
            PureServiceOrchestrator=deserialize_list(json_data.get("PureServiceOrchestrator"), PureServiceOrchestratorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassesDefinition = StorageClassesDefinition


@dataclass
class AdvancedStorageParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedStorageParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedStorageParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedStorageParametersDefinition = AdvancedStorageParametersDefinition


@dataclass
class NetappTridentDefinition(BaseModel):
    NetappBackendOntapNas: Optional[Sequence["_NetappBackendOntapNasDefinition"]]
    NetappBackendOntapSan: Optional[Sequence["_NetappBackendOntapSanDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetappTridentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetappTridentDefinition"]:
        if not json_data:
            return None
        return cls(
            NetappBackendOntapNas=deserialize_list(json_data.get("NetappBackendOntapNas"), NetappBackendOntapNasDefinition),
            NetappBackendOntapSan=deserialize_list(json_data.get("NetappBackendOntapSan"), NetappBackendOntapSanDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetappTridentDefinition = NetappTridentDefinition


@dataclass
class NetappBackendOntapNasDefinition(BaseModel):
    AutoExportPolicy: Optional[bool]
    BackendName: Optional[str]
    ClientCertificate: Optional[str]
    DataLifDnsName: Optional[str]
    DataLifIp: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition3"]]
    LimitAggregateUsage: Optional[str]
    LimitVolumeSize: Optional[str]
    ManagementLifDnsName: Optional[str]
    ManagementLifIp: Optional[str]
    NfsMountOptions: Optional[str]
    Region: Optional[str]
    StorageDriverName: Optional[str]
    StoragePrefix: Optional[str]
    Svm: Optional[str]
    TrustedCaCertificate: Optional[str]
    Username: Optional[str]
    AutoExportCidrs: Optional[Sequence["_AutoExportCidrsDefinition"]]
    ClientPrivateKey: Optional[Sequence["_ClientPrivateKeyDefinition"]]
    Password: Optional[Sequence["_PasswordDefinition"]]
    Storage: Optional[Sequence["_StorageDefinition"]]
    VolumeDefaults: Optional[Sequence["_VolumeDefaultsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetappBackendOntapNasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetappBackendOntapNasDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoExportPolicy=json_data.get("AutoExportPolicy"),
            BackendName=json_data.get("BackendName"),
            ClientCertificate=json_data.get("ClientCertificate"),
            DataLifDnsName=json_data.get("DataLifDnsName"),
            DataLifIp=json_data.get("DataLifIp"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition3),
            LimitAggregateUsage=json_data.get("LimitAggregateUsage"),
            LimitVolumeSize=json_data.get("LimitVolumeSize"),
            ManagementLifDnsName=json_data.get("ManagementLifDnsName"),
            ManagementLifIp=json_data.get("ManagementLifIp"),
            NfsMountOptions=json_data.get("NfsMountOptions"),
            Region=json_data.get("Region"),
            StorageDriverName=json_data.get("StorageDriverName"),
            StoragePrefix=json_data.get("StoragePrefix"),
            Svm=json_data.get("Svm"),
            TrustedCaCertificate=json_data.get("TrustedCaCertificate"),
            Username=json_data.get("Username"),
            AutoExportCidrs=deserialize_list(json_data.get("AutoExportCidrs"), AutoExportCidrsDefinition),
            ClientPrivateKey=deserialize_list(json_data.get("ClientPrivateKey"), ClientPrivateKeyDefinition),
            Password=deserialize_list(json_data.get("Password"), PasswordDefinition),
            Storage=deserialize_list(json_data.get("Storage"), StorageDefinition),
            VolumeDefaults=deserialize_list(json_data.get("VolumeDefaults"), VolumeDefaultsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetappBackendOntapNasDefinition = NetappBackendOntapNasDefinition


@dataclass
class LabelsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition3 = LabelsDefinition3


@dataclass
class AutoExportCidrsDefinition(BaseModel):
    Prefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoExportCidrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoExportCidrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Prefixes=json_data.get("Prefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoExportCidrsDefinition = AutoExportCidrsDefinition


@dataclass
class ClientPrivateKeyDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientPrivateKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientPrivateKeyDefinition"]:
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
_ClientPrivateKeyDefinition = ClientPrivateKeyDefinition


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
class PasswordDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordDefinition"]:
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
_PasswordDefinition = PasswordDefinition


@dataclass
class StorageDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition5"]]
    Zone: Optional[str]
    VolumeDefaults: Optional[Sequence["_VolumeDefaultsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition5),
            Zone=json_data.get("Zone"),
            VolumeDefaults=deserialize_list(json_data.get("VolumeDefaults"), VolumeDefaultsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDefinition = StorageDefinition


@dataclass
class LabelsDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition5 = LabelsDefinition5


@dataclass
class VolumeDefaultsDefinition(BaseModel):
    AdaptiveQosPolicy: Optional[str]
    Encryption: Optional[bool]
    ExportPolicy: Optional[str]
    NoQos: Optional[bool]
    QosPolicy: Optional[str]
    SecurityStyle: Optional[str]
    SnapshotDir: Optional[bool]
    SnapshotPolicy: Optional[str]
    SnapshotReserve: Optional[str]
    SpaceReserve: Optional[str]
    SplitOnClone: Optional[bool]
    TieringPolicy: Optional[str]
    UnixPermissions: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdaptiveQosPolicy=json_data.get("AdaptiveQosPolicy"),
            Encryption=json_data.get("Encryption"),
            ExportPolicy=json_data.get("ExportPolicy"),
            NoQos=json_data.get("NoQos"),
            QosPolicy=json_data.get("QosPolicy"),
            SecurityStyle=json_data.get("SecurityStyle"),
            SnapshotDir=json_data.get("SnapshotDir"),
            SnapshotPolicy=json_data.get("SnapshotPolicy"),
            SnapshotReserve=json_data.get("SnapshotReserve"),
            SpaceReserve=json_data.get("SpaceReserve"),
            SplitOnClone=json_data.get("SplitOnClone"),
            TieringPolicy=json_data.get("TieringPolicy"),
            UnixPermissions=json_data.get("UnixPermissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefaultsDefinition = VolumeDefaultsDefinition


@dataclass
class NetappBackendOntapSanDefinition(BaseModel):
    ClientCertificate: Optional[str]
    DataLifDnsName: Optional[str]
    DataLifIp: Optional[str]
    IgroupName: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition4"]]
    LimitAggregateUsage: Optional[float]
    LimitVolumeSize: Optional[float]
    ManagementLifDnsName: Optional[str]
    ManagementLifIp: Optional[str]
    NoChap: Optional[bool]
    Region: Optional[str]
    StorageDriverName: Optional[str]
    StoragePrefix: Optional[str]
    Svm: Optional[str]
    TrustedCaCertificate: Optional[str]
    Username: Optional[str]
    ClientPrivateKey: Optional[Sequence["_ClientPrivateKeyDefinition"]]
    Password: Optional[Sequence["_PasswordDefinition"]]
    Storage: Optional[Sequence["_StorageDefinition"]]
    UseChap: Optional[Sequence["_UseChapDefinition"]]
    VolumeDefaults: Optional[Sequence["_VolumeDefaultsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetappBackendOntapSanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetappBackendOntapSanDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientCertificate=json_data.get("ClientCertificate"),
            DataLifDnsName=json_data.get("DataLifDnsName"),
            DataLifIp=json_data.get("DataLifIp"),
            IgroupName=json_data.get("IgroupName"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition4),
            LimitAggregateUsage=json_data.get("LimitAggregateUsage"),
            LimitVolumeSize=json_data.get("LimitVolumeSize"),
            ManagementLifDnsName=json_data.get("ManagementLifDnsName"),
            ManagementLifIp=json_data.get("ManagementLifIp"),
            NoChap=json_data.get("NoChap"),
            Region=json_data.get("Region"),
            StorageDriverName=json_data.get("StorageDriverName"),
            StoragePrefix=json_data.get("StoragePrefix"),
            Svm=json_data.get("Svm"),
            TrustedCaCertificate=json_data.get("TrustedCaCertificate"),
            Username=json_data.get("Username"),
            ClientPrivateKey=deserialize_list(json_data.get("ClientPrivateKey"), ClientPrivateKeyDefinition),
            Password=deserialize_list(json_data.get("Password"), PasswordDefinition),
            Storage=deserialize_list(json_data.get("Storage"), StorageDefinition),
            UseChap=deserialize_list(json_data.get("UseChap"), UseChapDefinition),
            VolumeDefaults=deserialize_list(json_data.get("VolumeDefaults"), VolumeDefaultsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetappBackendOntapSanDefinition = NetappBackendOntapSanDefinition


@dataclass
class LabelsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition4 = LabelsDefinition4


@dataclass
class UseChapDefinition(BaseModel):
    ChapTargetUsername: Optional[str]
    ChapUsername: Optional[str]
    ChapInitiatorSecret: Optional[Sequence["_ChapInitiatorSecretDefinition"]]
    ChapTargetInitiatorSecret: Optional[Sequence["_ChapTargetInitiatorSecretDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UseChapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UseChapDefinition"]:
        if not json_data:
            return None
        return cls(
            ChapTargetUsername=json_data.get("ChapTargetUsername"),
            ChapUsername=json_data.get("ChapUsername"),
            ChapInitiatorSecret=deserialize_list(json_data.get("ChapInitiatorSecret"), ChapInitiatorSecretDefinition),
            ChapTargetInitiatorSecret=deserialize_list(json_data.get("ChapTargetInitiatorSecret"), ChapTargetInitiatorSecretDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UseChapDefinition = UseChapDefinition


@dataclass
class ChapInitiatorSecretDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChapInitiatorSecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChapInitiatorSecretDefinition"]:
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
_ChapInitiatorSecretDefinition = ChapInitiatorSecretDefinition


@dataclass
class ChapTargetInitiatorSecretDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChapTargetInitiatorSecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChapTargetInitiatorSecretDefinition"]:
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
_ChapTargetInitiatorSecretDefinition = ChapTargetInitiatorSecretDefinition


@dataclass
class OpenebsEnterpriseDefinition(BaseModel):
    MayastorPools: Optional[Sequence["_MayastorPoolsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenebsEnterpriseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenebsEnterpriseDefinition"]:
        if not json_data:
            return None
        return cls(
            MayastorPools=deserialize_list(json_data.get("MayastorPools"), MayastorPoolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenebsEnterpriseDefinition = OpenebsEnterpriseDefinition


@dataclass
class MayastorPoolsDefinition(BaseModel):
    Node: Optional[str]
    PoolDiskDevices: Optional[Sequence[str]]
    PoolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MayastorPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MayastorPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Node=json_data.get("Node"),
            PoolDiskDevices=json_data.get("PoolDiskDevices"),
            PoolName=json_data.get("PoolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MayastorPoolsDefinition = MayastorPoolsDefinition


@dataclass
class PureServiceOrchestratorDefinition(BaseModel):
    ClusterId: Optional[str]
    EnableStorageTopology: Optional[bool]
    EnableStrictTopology: Optional[bool]
    Arrays: Optional[Sequence["_ArraysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PureServiceOrchestratorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PureServiceOrchestratorDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            EnableStorageTopology=json_data.get("EnableStorageTopology"),
            EnableStrictTopology=json_data.get("EnableStrictTopology"),
            Arrays=deserialize_list(json_data.get("Arrays"), ArraysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PureServiceOrchestratorDefinition = PureServiceOrchestratorDefinition


@dataclass
class ArraysDefinition(BaseModel):
    FlashArray: Optional[Sequence["_FlashArrayDefinition"]]
    FlashBlade: Optional[Sequence["_FlashBladeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArraysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArraysDefinition"]:
        if not json_data:
            return None
        return cls(
            FlashArray=deserialize_list(json_data.get("FlashArray"), FlashArrayDefinition),
            FlashBlade=deserialize_list(json_data.get("FlashBlade"), FlashBladeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArraysDefinition = ArraysDefinition


@dataclass
class FlashArrayDefinition(BaseModel):
    DefaultFsOpt: Optional[str]
    DefaultFsType: Optional[str]
    DefaultMountOpts: Optional[Sequence[str]]
    DisablePreemptAttachments: Optional[bool]
    IscsiLoginTimeout: Optional[float]
    SanType: Optional[str]
    FlashArrays: Optional[Sequence["_FlashArraysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlashArrayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlashArrayDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultFsOpt=json_data.get("DefaultFsOpt"),
            DefaultFsType=json_data.get("DefaultFsType"),
            DefaultMountOpts=json_data.get("DefaultMountOpts"),
            DisablePreemptAttachments=json_data.get("DisablePreemptAttachments"),
            IscsiLoginTimeout=json_data.get("IscsiLoginTimeout"),
            SanType=json_data.get("SanType"),
            FlashArrays=deserialize_list(json_data.get("FlashArrays"), FlashArraysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlashArrayDefinition = FlashArrayDefinition


@dataclass
class FlashArraysDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition6"]]
    MgmtDnsName: Optional[str]
    MgmtIp: Optional[str]
    ApiToken: Optional[Sequence["_ApiTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlashArraysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlashArraysDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition6),
            MgmtDnsName=json_data.get("MgmtDnsName"),
            MgmtIp=json_data.get("MgmtIp"),
            ApiToken=deserialize_list(json_data.get("ApiToken"), ApiTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlashArraysDefinition = FlashArraysDefinition


@dataclass
class LabelsDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition6 = LabelsDefinition6


@dataclass
class ApiTokenDefinition(BaseModel):
    SecretEncodingType: Optional[str]
    BlindfoldSecretInfo: Optional[Sequence["_BlindfoldSecretInfoDefinition"]]
    BlindfoldSecretInfoInternal: Optional[Sequence["_BlindfoldSecretInfoInternalDefinition"]]
    ClearSecretInfo: Optional[Sequence["_ClearSecretInfoDefinition"]]
    VaultSecretInfo: Optional[Sequence["_VaultSecretInfoDefinition"]]
    WingmanSecretInfo: Optional[Sequence["_WingmanSecretInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiTokenDefinition"]:
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
_ApiTokenDefinition = ApiTokenDefinition


@dataclass
class FlashBladeDefinition(BaseModel):
    EnableSnapshotDirectory: Optional[bool]
    ExportRules: Optional[str]
    FlashBlades: Optional[Sequence["_FlashBladesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlashBladeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlashBladeDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableSnapshotDirectory=json_data.get("EnableSnapshotDirectory"),
            ExportRules=json_data.get("ExportRules"),
            FlashBlades=deserialize_list(json_data.get("FlashBlades"), FlashBladesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlashBladeDefinition = FlashBladeDefinition


@dataclass
class FlashBladesDefinition(BaseModel):
    Lables: Optional[Sequence["_LablesDefinition"]]
    MgmtDnsName: Optional[str]
    MgmtIp: Optional[str]
    NfsEndpointDnsName: Optional[str]
    NfsEndpointIp: Optional[str]
    ApiToken: Optional[Sequence["_ApiTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlashBladesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlashBladesDefinition"]:
        if not json_data:
            return None
        return cls(
            Lables=deserialize_list(json_data.get("Lables"), LablesDefinition),
            MgmtDnsName=json_data.get("MgmtDnsName"),
            MgmtIp=json_data.get("MgmtIp"),
            NfsEndpointDnsName=json_data.get("NfsEndpointDnsName"),
            NfsEndpointIp=json_data.get("NfsEndpointIp"),
            ApiToken=deserialize_list(json_data.get("ApiToken"), ApiTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlashBladesDefinition = FlashBladesDefinition


@dataclass
class LablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LablesDefinition = LablesDefinition


@dataclass
class StorageDeviceListDefinition(BaseModel):
    StorageDevices: Optional[Sequence["_StorageDevicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDeviceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDeviceListDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageDevices=deserialize_list(json_data.get("StorageDevices"), StorageDevicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDeviceListDefinition = StorageDeviceListDefinition


@dataclass
class StorageDevicesDefinition(BaseModel):
    AdvancedAdvancedParameters: Optional[Sequence["_AdvancedAdvancedParametersDefinition"]]
    StorageDevice: Optional[str]
    NetappTrident: Optional[Sequence["_NetappTridentDefinition"]]
    OpenebsEnterprise: Optional[Sequence["_OpenebsEnterpriseDefinition"]]
    PureServiceOrchestrator: Optional[Sequence["_PureServiceOrchestratorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvancedAdvancedParameters=deserialize_list(json_data.get("AdvancedAdvancedParameters"), AdvancedAdvancedParametersDefinition),
            StorageDevice=json_data.get("StorageDevice"),
            NetappTrident=deserialize_list(json_data.get("NetappTrident"), NetappTridentDefinition),
            OpenebsEnterprise=deserialize_list(json_data.get("OpenebsEnterprise"), OpenebsEnterpriseDefinition),
            PureServiceOrchestrator=deserialize_list(json_data.get("PureServiceOrchestrator"), PureServiceOrchestratorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDevicesDefinition = StorageDevicesDefinition


@dataclass
class AdvancedAdvancedParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedAdvancedParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedAdvancedParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedAdvancedParametersDefinition = AdvancedAdvancedParametersDefinition


@dataclass
class StorageInterfaceListDefinition(BaseModel):
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageInterfaceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageInterfaceListDefinition"]:
        if not json_data:
            return None
        return cls(
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageInterfaceListDefinition = StorageInterfaceListDefinition


@dataclass
class StorageStaticRoutesDefinition(BaseModel):
    StorageRoutes: Optional[Sequence["_StorageRoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageStaticRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageStaticRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageRoutes=deserialize_list(json_data.get("StorageRoutes"), StorageRoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageStaticRoutesDefinition = StorageStaticRoutesDefinition


@dataclass
class StorageRoutesDefinition(BaseModel):
    Attrs: Optional[Sequence[str]]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Nexthop: Optional[Sequence["_NexthopDefinition"]]
    Subnets: Optional[Sequence["_SubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attrs=json_data.get("Attrs"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Nexthop=deserialize_list(json_data.get("Nexthop"), NexthopDefinition),
            Subnets=deserialize_list(json_data.get("Subnets"), SubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageRoutesDefinition = StorageRoutesDefinition


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
class UsbPolicyDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsbPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsbPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsbPolicyDefinition = UsbPolicyDefinition


