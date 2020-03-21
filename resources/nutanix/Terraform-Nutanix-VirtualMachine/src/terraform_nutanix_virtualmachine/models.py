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
    ApiVersion: Optional[str]
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReference"]]
    BootDeviceDiskAddress: Optional[Sequence["_BootDeviceDiskAddress"]]
    BootDeviceMacAddress: Optional[str]
    BootDeviceOrderList: Optional[Sequence[str]]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    Description: Optional[str]
    EnableScriptExec: Optional[bool]
    GuestCustomizationCloudInitCustomKeyValues: Optional[Sequence["_GuestCustomizationCloudInitCustomKeyValues"]]
    GuestCustomizationCloudInitMetaData: Optional[str]
    GuestCustomizationCloudInitUserData: Optional[str]
    GuestCustomizationIsOverridable: Optional[bool]
    GuestCustomizationSysprep: Optional[Sequence["_GuestCustomizationSysprep"]]
    GuestCustomizationSysprepCustomKeyValues: Optional[Sequence["_GuestCustomizationSysprepCustomKeyValues"]]
    GuestOsId: Optional[str]
    HardwareClockTimezone: Optional[str]
    HostReference: Optional[Sequence["_HostReference"]]
    HypervisorType: Optional[str]
    MemorySizeMib: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NgtCredentials: Optional[Sequence["_NgtCredentials"]]
    NgtEnabledCapabilityList: Optional[Sequence[str]]
    NicListStatus: Optional[Sequence["_NicListStatus"]]
    NumSockets: Optional[float]
    NumVcpusPerSocket: Optional[float]
    NumVnumaNodes: Optional[float]
    NutanixGuestTools: Optional[Sequence["_NutanixGuestTools"]]
    OwnerReference: Optional[Sequence["_OwnerReference"]]
    ParentReference: Optional[Sequence["_ParentReference"]]
    PowerState: Optional[str]
    PowerStateMechanism: Optional[str]
    ProjectReference: Optional[Sequence["_ProjectReference"]]
    ShouldFailOnScriptFailure: Optional[bool]
    State: Optional[str]
    VgaConsoleEnabled: Optional[bool]
    Categories: Optional[Sequence["_Categories"]]
    DiskList: Optional[Sequence["_DiskList"]]
    GpuList: Optional[Sequence["_GpuList"]]
    NicList: Optional[Sequence["_NicList"]]
    SerialPortList: Optional[Sequence["_SerialPortList"]]
    DeviceProperties: Optional[Sequence["_DeviceProperties"]]
    IpEndpointList: Optional[Sequence["_IpEndpointList2"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiVersion=json_data.get("ApiVersion"),
            AvailabilityZoneReference=json_data.get("AvailabilityZoneReference"),
            BootDeviceDiskAddress=json_data.get("BootDeviceDiskAddress"),
            BootDeviceMacAddress=json_data.get("BootDeviceMacAddress"),
            BootDeviceOrderList=json_data.get("BootDeviceOrderList"),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Description=json_data.get("Description"),
            EnableScriptExec=json_data.get("EnableScriptExec"),
            GuestCustomizationCloudInitCustomKeyValues=json_data.get("GuestCustomizationCloudInitCustomKeyValues"),
            GuestCustomizationCloudInitMetaData=json_data.get("GuestCustomizationCloudInitMetaData"),
            GuestCustomizationCloudInitUserData=json_data.get("GuestCustomizationCloudInitUserData"),
            GuestCustomizationIsOverridable=json_data.get("GuestCustomizationIsOverridable"),
            GuestCustomizationSysprep=json_data.get("GuestCustomizationSysprep"),
            GuestCustomizationSysprepCustomKeyValues=json_data.get("GuestCustomizationSysprepCustomKeyValues"),
            GuestOsId=json_data.get("GuestOsId"),
            HardwareClockTimezone=json_data.get("HardwareClockTimezone"),
            HostReference=json_data.get("HostReference"),
            HypervisorType=json_data.get("HypervisorType"),
            MemorySizeMib=json_data.get("MemorySizeMib"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NgtCredentials=json_data.get("NgtCredentials"),
            NgtEnabledCapabilityList=json_data.get("NgtEnabledCapabilityList"),
            NicListStatus=json_data.get("NicListStatus"),
            NumSockets=json_data.get("NumSockets"),
            NumVcpusPerSocket=json_data.get("NumVcpusPerSocket"),
            NumVnumaNodes=json_data.get("NumVnumaNodes"),
            NutanixGuestTools=json_data.get("NutanixGuestTools"),
            OwnerReference=json_data.get("OwnerReference"),
            ParentReference=json_data.get("ParentReference"),
            PowerState=json_data.get("PowerState"),
            PowerStateMechanism=json_data.get("PowerStateMechanism"),
            ProjectReference=json_data.get("ProjectReference"),
            ShouldFailOnScriptFailure=json_data.get("ShouldFailOnScriptFailure"),
            State=json_data.get("State"),
            VgaConsoleEnabled=json_data.get("VgaConsoleEnabled"),
            Categories=json_data.get("Categories"),
            DiskList=json_data.get("DiskList"),
            GpuList=json_data.get("GpuList"),
            NicList=json_data.get("NicList"),
            SerialPortList=json_data.get("SerialPortList"),
            DeviceProperties=json_data.get("DeviceProperties"),
            IpEndpointList=json_data.get("IpEndpointList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReference = AvailabilityZoneReference


@dataclass
class BootDeviceDiskAddress:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootDeviceDiskAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDeviceDiskAddress"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDeviceDiskAddress = BootDeviceDiskAddress


@dataclass
class GuestCustomizationCloudInitCustomKeyValues:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationCloudInitCustomKeyValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationCloudInitCustomKeyValues"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationCloudInitCustomKeyValues = GuestCustomizationCloudInitCustomKeyValues


@dataclass
class GuestCustomizationSysprep:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationSysprep"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationSysprep"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationSysprep = GuestCustomizationSysprep


@dataclass
class GuestCustomizationSysprepCustomKeyValues:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestCustomizationSysprepCustomKeyValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestCustomizationSysprepCustomKeyValues"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestCustomizationSysprepCustomKeyValues = GuestCustomizationSysprepCustomKeyValues


@dataclass
class HostReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostReference = HostReference


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class NgtCredentials:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NgtCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NgtCredentials"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NgtCredentials = NgtCredentials


@dataclass
class NicListStatus:
    FloatingIp: Optional[str]
    IpEndpointList: Optional[Sequence["_IpEndpointList"]]
    IsConnected: Optional[str]
    MacAddress: Optional[str]
    Model: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReference"]]
    NetworkFunctionNicType: Optional[str]
    NicType: Optional[str]
    SubnetName: Optional[str]
    SubnetUuid: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NicListStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicListStatus"]:
        if not json_data:
            return None
        return cls(
            FloatingIp=json_data.get("FloatingIp"),
            IpEndpointList=json_data.get("IpEndpointList"),
            IsConnected=json_data.get("IsConnected"),
            MacAddress=json_data.get("MacAddress"),
            Model=json_data.get("Model"),
            NetworkFunctionChainReference=json_data.get("NetworkFunctionChainReference"),
            NetworkFunctionNicType=json_data.get("NetworkFunctionNicType"),
            NicType=json_data.get("NicType"),
            SubnetName=json_data.get("SubnetName"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicListStatus = NicListStatus


@dataclass
class IpEndpointList:
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpEndpointList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpEndpointList"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpEndpointList = IpEndpointList


@dataclass
class NetworkFunctionChainReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReference = NetworkFunctionChainReference


@dataclass
class NutanixGuestTools:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NutanixGuestTools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NutanixGuestTools"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NutanixGuestTools = NutanixGuestTools


@dataclass
class OwnerReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReference = OwnerReference


@dataclass
class ParentReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentReference = ParentReference


@dataclass
class ProjectReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReference = ProjectReference


@dataclass
class Categories:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Categories"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Categories"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Categories = Categories


@dataclass
class DiskList:
    DataSourceReference: Optional[Sequence["_DataSourceReference"]]
    DiskSizeBytes: Optional[float]
    DiskSizeMib: Optional[float]
    Uuid: Optional[str]
    VolumeGroupReference: Optional[Sequence["_VolumeGroupReference"]]
    DeviceProperties: Optional[Sequence["_DeviceProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiskList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskList"]:
        if not json_data:
            return None
        return cls(
            DataSourceReference=json_data.get("DataSourceReference"),
            DiskSizeBytes=json_data.get("DiskSizeBytes"),
            DiskSizeMib=json_data.get("DiskSizeMib"),
            Uuid=json_data.get("Uuid"),
            VolumeGroupReference=json_data.get("VolumeGroupReference"),
            DeviceProperties=json_data.get("DeviceProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskList = DiskList


@dataclass
class DataSourceReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceReference = DataSourceReference


@dataclass
class VolumeGroupReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeGroupReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeGroupReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeGroupReference = VolumeGroupReference


@dataclass
class DeviceProperties:
    DeviceType: Optional[str]
    DiskAddress: Optional[Sequence["_DiskAddress"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceProperties"]:
        if not json_data:
            return None
        return cls(
            DeviceType=json_data.get("DeviceType"),
            DiskAddress=json_data.get("DiskAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceProperties = DeviceProperties


@dataclass
class DiskAddress:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskAddress"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskAddress = DiskAddress


@dataclass
class GpuList:
    DeviceId: Optional[float]
    Mode: Optional[str]
    Vendor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GpuList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GpuList"]:
        if not json_data:
            return None
        return cls(
            DeviceId=json_data.get("DeviceId"),
            Mode=json_data.get("Mode"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GpuList = GpuList


@dataclass
class NicList:
    IsConnected: Optional[str]
    MacAddress: Optional[str]
    Model: Optional[str]
    NetworkFunctionChainReference: Optional[Sequence["_NetworkFunctionChainReference2"]]
    NetworkFunctionNicType: Optional[str]
    NicType: Optional[str]
    SubnetName: Optional[str]
    SubnetUuid: Optional[str]
    Uuid: Optional[str]
    IpEndpointList: Optional[Sequence["_IpEndpointList2"]]

    @classmethod
    def _deserialize(
        cls: Type["_NicList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicList"]:
        if not json_data:
            return None
        return cls(
            IsConnected=json_data.get("IsConnected"),
            MacAddress=json_data.get("MacAddress"),
            Model=json_data.get("Model"),
            NetworkFunctionChainReference=json_data.get("NetworkFunctionChainReference"),
            NetworkFunctionNicType=json_data.get("NetworkFunctionNicType"),
            NicType=json_data.get("NicType"),
            SubnetName=json_data.get("SubnetName"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Uuid=json_data.get("Uuid"),
            IpEndpointList=json_data.get("IpEndpointList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicList = NicList


@dataclass
class NetworkFunctionChainReference2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFunctionChainReference2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFunctionChainReference2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFunctionChainReference2 = NetworkFunctionChainReference2


@dataclass
class IpEndpointList2:
    Ip: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpEndpointList2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpEndpointList2"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpEndpointList2 = IpEndpointList2


@dataclass
class SerialPortList:
    Index: Optional[float]
    IsConnected: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SerialPortList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerialPortList"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            IsConnected=json_data.get("IsConnected"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerialPortList = SerialPortList


