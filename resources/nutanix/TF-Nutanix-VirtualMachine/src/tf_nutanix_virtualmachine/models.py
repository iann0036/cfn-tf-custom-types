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
    ApiVersion: Optional[str]
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReferenceDefinition"]]
    BootDeviceDiskAddress: Optional[Sequence["_BootDeviceDiskAddressDefinition"]]
    BootDeviceMacAddress: Optional[str]
    BootDeviceOrderList: Optional[Sequence[str]]
    BootType: Optional[str]
    CloudInitCdromUuid: Optional[str]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    Description: Optional[str]
    EnableScriptExec: Optional[bool]
    GuestCustomizationCloudInitCustomKeyValues: Optional[Sequence["_GuestCustomizationCloudInitCustomKeyValuesDefinition"]]
    GuestCustomizationCloudInitMetaData: Optional[str]
    GuestCustomizationCloudInitUserData: Optional[str]
    GuestCustomizationIsOverridable: Optional[bool]
    GuestCustomizationSysprep: Optional[Sequence["_GuestCustomizationSysprepDefinition"]]
    GuestCustomizationSysprepCustomKeyValues: Optional[Sequence["_GuestCustomizationSysprepCustomKeyValuesDefinition"]]
    GuestOsId: Optional[str]
    HardwareClockTimezone: Optional[str]
    HostReference: Optional[Sequence["_HostReferenceDefinition"]]
    HypervisorType: Optional[str]
    Id: Optional[str]
    MachineType: Optional[str]
    MemorySizeMib: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NgtCredentials: Optional[Sequence["_NgtCredentialsDefinition"]]
    NgtEnabledCapabilityList: Optional[Sequence[str]]
    NicListStatus: Optional[Sequence["_NicListStatusDefinition3"]]
    NumSockets: Optional[float]
    NumVcpusPerSocket: Optional[float]
    NumVnumaNodes: Optional[float]
    NutanixGuestTools: Optional[Sequence["_NutanixGuestToolsDefinition"]]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ParentReference: Optional[Sequence["_ParentReferenceDefinition"]]
    PowerState: Optional[str]
    PowerStateMechanism: Optional[str]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    ShouldFailOnScriptFailure: Optional[bool]
    State: Optional[str]
    UseHotAdd: Optional[bool]
    VgaConsoleEnabled: Optional[bool]
    Categories: Optional[Sequence["_CategoriesDefinition"]]
    DiskList: Optional[Sequence["_DiskListDefinition"]]
    GpuList: Optional[Sequence["_GpuListDefinition"]]
    NicList: Optional[Sequence["_NicListDefinition"]]
    SerialPortList: Optional[Sequence["_SerialPortListDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            AvailabilityZoneReference=deserialize_list(json_data.get("AvailabilityZoneReference"), AvailabilityZoneReferenceDefinition),
            BootDeviceDiskAddress=deserialize_list(json_data.get("BootDeviceDiskAddress"), BootDeviceDiskAddressDefinition),
            BootDeviceMacAddress=json_data.get("BootDeviceMacAddress"),
            BootDeviceOrderList=json_data.get("BootDeviceOrderList"),
            BootType=json_data.get("BootType"),
            CloudInitCdromUuid=json_data.get("CloudInitCdromUuid"),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Description=json_data.get("Description"),
            EnableScriptExec=json_data.get("EnableScriptExec"),
            GuestCustomizationCloudInitCustomKeyValues=deserialize_list(json_data.get("GuestCustomizationCloudInitCustomKeyValues"), GuestCustomizationCloudInitCustomKeyValuesDefinition),
            GuestCustomizationCloudInitMetaData=json_data.get("GuestCustomizationCloudInitMetaData"),
            GuestCustomizationCloudInitUserData=json_data.get("GuestCustomizationCloudInitUserData"),
            GuestCustomizationIsOverridable=json_data.get("GuestCustomizationIsOverridable"),
            GuestCustomizationSysprep=deserialize_list(json_data.get("GuestCustomizationSysprep"), GuestCustomizationSysprepDefinition),
            GuestCustomizationSysprepCustomKeyValues=deserialize_list(json_data.get("GuestCustomizationSysprepCustomKeyValues"), GuestCustomizationSysprepCustomKeyValuesDefinition),
            GuestOsId=json_data.get("GuestOsId"),
            HardwareClockTimezone=json_data.get("HardwareClockTimezone"),
            HostReference=deserialize_list(json_data.get("HostReference"), HostReferenceDefinition),
            HypervisorType=json_data.get("HypervisorType"),
            Id=json_data.get("Id"),
            MachineType=json_data.get("MachineType"),
            MemorySizeMib=json_data.get("MemorySizeMib"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NgtCredentials=deserialize_list(json_data.get("NgtCredentials"), NgtCredentialsDefinition),
            NgtEnabledCapabilityList=json_data.get("NgtEnabledCapabilityList"),
            NicListStatus=deserialize_list(json_data.get("NicListStatus"), NicListStatusDefinition3),
            NumSockets=json_data.get("NumSockets"),
            NumVcpusPerSocket=json_data.get("NumVcpusPerSocket"),
            NumVnumaNodes=json_data.get("NumVnumaNodes"),
            NutanixGuestTools=deserialize_list(json_data.get("NutanixGuestTools"), NutanixGuestToolsDefinition),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ParentReference=deserialize_list(json_data.get("ParentReference"), ParentReferenceDefinition),
            PowerState=json_data.get("PowerState"),
            PowerStateMechanism=json_data.get("PowerStateMechanism"),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            ShouldFailOnScriptFailure=json_data.get("ShouldFailOnScriptFailure"),
            State=json_data.get("State"),
            UseHotAdd=json_data.get("UseHotAdd"),
            VgaConsoleEnabled=json_data.get("VgaConsoleEnabled"),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
            DiskList=deserialize_list(json_data.get("DiskList"), DiskListDefinition),
            GpuList=deserialize_list(json_data.get("GpuList"), GpuListDefinition),
            NicList=deserialize_list(json_data.get("NicList"), NicListDefinition),
            SerialPortList=deserialize_list(json_data.get("SerialPortList"), SerialPortListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReferenceDefinition = AvailabilityZoneReferenceDefinition


@dataclass
class BootDeviceDiskAddressDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDeviceDiskAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDeviceDiskAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDeviceDiskAddressDefinition = BootDeviceDiskAddressDefinition


@dataclass
class GuestCustomizationCloudInitCustomKeyValuesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationCloudInitCustomKeyValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationCloudInitCustomKeyValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationCloudInitCustomKeyValuesDefinition = GuestCustomizationCloudInitCustomKeyValuesDefinition


@dataclass
class GuestCustomizationSysprepDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationSysprepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationSysprepDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationSysprepDefinition = GuestCustomizationSysprepDefinition


@dataclass
class GuestCustomizationSysprepCustomKeyValuesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationSysprepCustomKeyValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationSysprepCustomKeyValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationSysprepCustomKeyValuesDefinition = GuestCustomizationSysprepCustomKeyValuesDefinition


@dataclass
class HostReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostReferenceDefinition = HostReferenceDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class NgtCredentialsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NgtCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NgtCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NgtCredentialsDefinition = NgtCredentialsDefinition


@dataclass
class NicListStatusDefinition3(BaseModel):
    FloatingIp: Optional[str]
    IpEndpointList: Optional[Sequence["_NicListStatusDefinition"]]
    IsConnected: Optional[str]
    MacAddress: Optional[str]
    Model: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NicListStatusDefinition2"]]
    NetworkFunctionNicType: Optional[str]
    NicType: Optional[str]
    SubnetName: Optional[str]
    SubnetUuid: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicListStatusDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicListStatusDefinition3"]:
        if not json_data:
            return None
        return cls(
            FloatingIp=json_data.get("FloatingIp"),
            IpEndpointList=deserialize_list(json_data.get("IpEndpointList"), NicListStatusDefinition),
            IsConnected=json_data.get("IsConnected"),
            MacAddress=json_data.get("MacAddress"),
            Model=json_data.get("Model"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NicListStatusDefinition2),
            NetworkFunctionNicType=json_data.get("NetworkFunctionNicType"),
            NicType=json_data.get("NicType"),
            SubnetName=json_data.get("SubnetName"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicListStatusDefinition3 = NicListStatusDefinition3


@dataclass
class NicListStatusDefinition(BaseModel):
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicListStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicListStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicListStatusDefinition = NicListStatusDefinition


@dataclass
class NicListStatusDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicListStatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicListStatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicListStatusDefinition2 = NicListStatusDefinition2


@dataclass
class NutanixGuestToolsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NutanixGuestToolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NutanixGuestToolsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NutanixGuestToolsDefinition = NutanixGuestToolsDefinition


@dataclass
class OwnerReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ParentReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentReferenceDefinition = ParentReferenceDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


@dataclass
class DiskListDefinition(BaseModel):
    DataSourceReference: Optional[Sequence["_DataSourceReferenceDefinition"]]
    DiskSizeBytes: Optional[float]
    DiskSizeMib: Optional[float]
    Uuid: Optional[str]
    VolumeGroupReference: Optional[Sequence["_VolumeGroupReferenceDefinition"]]
    DeviceProperties: Optional[Sequence["_DevicePropertiesDefinition"]]
    StorageConfig: Optional[Sequence["_StorageConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiskListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskListDefinition"]:
        if not json_data:
            return None
        return cls(
            DataSourceReference=deserialize_list(json_data.get("DataSourceReference"), DataSourceReferenceDefinition),
            DiskSizeBytes=json_data.get("DiskSizeBytes"),
            DiskSizeMib=json_data.get("DiskSizeMib"),
            Uuid=json_data.get("Uuid"),
            VolumeGroupReference=deserialize_list(json_data.get("VolumeGroupReference"), VolumeGroupReferenceDefinition),
            DeviceProperties=deserialize_list(json_data.get("DeviceProperties"), DevicePropertiesDefinition),
            StorageConfig=deserialize_list(json_data.get("StorageConfig"), StorageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskListDefinition = DiskListDefinition


@dataclass
class DataSourceReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceReferenceDefinition = DataSourceReferenceDefinition


@dataclass
class VolumeGroupReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeGroupReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeGroupReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeGroupReferenceDefinition = VolumeGroupReferenceDefinition


@dataclass
class DevicePropertiesDefinition(BaseModel):
    DeviceType: Optional[str]
    DiskAddress: Optional[Sequence["_DiskAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DevicePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceType=json_data.get("DeviceType"),
            DiskAddress=deserialize_list(json_data.get("DiskAddress"), DiskAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicePropertiesDefinition = DevicePropertiesDefinition


@dataclass
class DiskAddressDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskAddressDefinition = DiskAddressDefinition


@dataclass
class StorageConfigDefinition(BaseModel):
    FlashMode: Optional[str]
    StorageContainerReference: Optional[Sequence["_StorageContainerReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FlashMode=json_data.get("FlashMode"),
            StorageContainerReference=deserialize_list(json_data.get("StorageContainerReference"), StorageContainerReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageConfigDefinition = StorageConfigDefinition


@dataclass
class StorageContainerReferenceDefinition(BaseModel):
    Kind: Optional[str]
    Url: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageContainerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageContainerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            Url=json_data.get("Url"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageContainerReferenceDefinition = StorageContainerReferenceDefinition


@dataclass
class GpuListDefinition(BaseModel):
    DeviceId: Optional[float]
    Mode: Optional[str]
    Vendor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GpuListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GpuListDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceId=json_data.get("DeviceId"),
            Mode=json_data.get("Mode"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GpuListDefinition = GpuListDefinition


@dataclass
class NicListDefinition(BaseModel):
    IsConnected: Optional[str]
    MacAddress: Optional[str]
    Model: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReferenceDefinition"]]
    NetworkFunctionNicType: Optional[str]
    NicType: Optional[str]
    SubnetName: Optional[str]
    SubnetUuid: Optional[str]
    Uuid: Optional[str]
    IpEndpointList: Optional[Sequence["_IpEndpointListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NicListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicListDefinition"]:
        if not json_data:
            return None
        return cls(
            IsConnected=json_data.get("IsConnected"),
            MacAddress=json_data.get("MacAddress"),
            Model=json_data.get("Model"),
            NetworkFunctionChainReference=deserialize_list(json_data.get("NetworkFunctionChainReference"), NetworkFunctionChainReferenceDefinition),
            NetworkFunctionNicType=json_data.get("NetworkFunctionNicType"),
            NicType=json_data.get("NicType"),
            SubnetName=json_data.get("SubnetName"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Uuid=json_data.get("Uuid"),
            IpEndpointList=deserialize_list(json_data.get("IpEndpointList"), IpEndpointListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicListDefinition = NicListDefinition


@dataclass
class NetworkFunctionChainReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReferenceDefinition = NetworkFunctionChainReferenceDefinition


@dataclass
class IpEndpointListDefinition(BaseModel):
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpEndpointListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpEndpointListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpEndpointListDefinition = IpEndpointListDefinition


@dataclass
class SerialPortListDefinition(BaseModel):
    Index: Optional[float]
    IsConnected: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SerialPortListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerialPortListDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            IsConnected=json_data.get("IsConnected"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerialPortListDefinition = SerialPortListDefinition


