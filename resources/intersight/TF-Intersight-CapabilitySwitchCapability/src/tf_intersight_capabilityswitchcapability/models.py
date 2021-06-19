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
    AccountMoid: Optional[str]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    DefaultFcoeVlan: Optional[float]
    DomainGroupMoid: Optional[str]
    DynamicVifsSupported: Optional[bool]
    FanModulesSupported: Optional[bool]
    FcEndHostModeReservedVsans: Optional[Sequence["_FcEndHostModeReservedVsansDefinition"]]
    FcUplinkPortsAutoNegotiationSupported: Optional[bool]
    Id: Optional[str]
    LocatorBeaconSupported: Optional[bool]
    MaxPorts: Optional[float]
    MaxSlots: Optional[float]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NetworkLimits: Optional[Sequence["_NetworkLimitsDefinition"]]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Pid: Optional[str]
    PortsSupporting100gSpeed: Optional[Sequence["_PortsSupporting100gSpeedDefinition"]]
    PortsSupporting10gSpeed: Optional[Sequence["_PortsSupporting10gSpeedDefinition"]]
    PortsSupporting1gSpeed: Optional[Sequence["_PortsSupporting1gSpeedDefinition"]]
    PortsSupporting25gSpeed: Optional[Sequence["_PortsSupporting25gSpeedDefinition"]]
    PortsSupporting40gSpeed: Optional[Sequence["_PortsSupporting40gSpeedDefinition"]]
    PortsSupportingBreakout: Optional[Sequence["_PortsSupportingBreakoutDefinition"]]
    PortsSupportingFcoe: Optional[Sequence["_PortsSupportingFcoeDefinition"]]
    PortsSupportingServerRole: Optional[Sequence["_PortsSupportingServerRoleDefinition"]]
    ReservedVsans: Optional[Sequence["_ReservedVsansDefinition"]]
    SerenoNetflowSupported: Optional[bool]
    SharedScope: Optional[str]
    Sku: Optional[str]
    StorageLimits: Optional[Sequence["_StorageLimitsDefinition"]]
    SwitchingModeCapabilities: Optional[Sequence["_SwitchingModeCapabilitiesDefinition"]]
    SystemLimits: Optional[Sequence["_SystemLimitsDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UnifiedPorts: Optional[Sequence["_UnifiedPortsDefinition"]]
    UnifiedRule: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    Vid: Optional[str]

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
            AccountMoid=json_data.get("AccountMoid"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            DefaultFcoeVlan=json_data.get("DefaultFcoeVlan"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            DynamicVifsSupported=json_data.get("DynamicVifsSupported"),
            FanModulesSupported=json_data.get("FanModulesSupported"),
            FcEndHostModeReservedVsans=deserialize_list(json_data.get("FcEndHostModeReservedVsans"), FcEndHostModeReservedVsansDefinition),
            FcUplinkPortsAutoNegotiationSupported=json_data.get("FcUplinkPortsAutoNegotiationSupported"),
            Id=json_data.get("Id"),
            LocatorBeaconSupported=json_data.get("LocatorBeaconSupported"),
            MaxPorts=json_data.get("MaxPorts"),
            MaxSlots=json_data.get("MaxSlots"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NetworkLimits=deserialize_list(json_data.get("NetworkLimits"), NetworkLimitsDefinition),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Pid=json_data.get("Pid"),
            PortsSupporting100gSpeed=deserialize_list(json_data.get("PortsSupporting100gSpeed"), PortsSupporting100gSpeedDefinition),
            PortsSupporting10gSpeed=deserialize_list(json_data.get("PortsSupporting10gSpeed"), PortsSupporting10gSpeedDefinition),
            PortsSupporting1gSpeed=deserialize_list(json_data.get("PortsSupporting1gSpeed"), PortsSupporting1gSpeedDefinition),
            PortsSupporting25gSpeed=deserialize_list(json_data.get("PortsSupporting25gSpeed"), PortsSupporting25gSpeedDefinition),
            PortsSupporting40gSpeed=deserialize_list(json_data.get("PortsSupporting40gSpeed"), PortsSupporting40gSpeedDefinition),
            PortsSupportingBreakout=deserialize_list(json_data.get("PortsSupportingBreakout"), PortsSupportingBreakoutDefinition),
            PortsSupportingFcoe=deserialize_list(json_data.get("PortsSupportingFcoe"), PortsSupportingFcoeDefinition),
            PortsSupportingServerRole=deserialize_list(json_data.get("PortsSupportingServerRole"), PortsSupportingServerRoleDefinition),
            ReservedVsans=deserialize_list(json_data.get("ReservedVsans"), ReservedVsansDefinition),
            SerenoNetflowSupported=json_data.get("SerenoNetflowSupported"),
            SharedScope=json_data.get("SharedScope"),
            Sku=json_data.get("Sku"),
            StorageLimits=deserialize_list(json_data.get("StorageLimits"), StorageLimitsDefinition),
            SwitchingModeCapabilities=deserialize_list(json_data.get("SwitchingModeCapabilities"), SwitchingModeCapabilitiesDefinition),
            SystemLimits=deserialize_list(json_data.get("SystemLimits"), SystemLimitsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UnifiedPorts=deserialize_list(json_data.get("UnifiedPorts"), UnifiedPortsDefinition),
            UnifiedRule=json_data.get("UnifiedRule"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            Vid=json_data.get("Vid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class FcEndHostModeReservedVsansDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FcEndHostModeReservedVsansDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FcEndHostModeReservedVsansDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FcEndHostModeReservedVsansDefinition = FcEndHostModeReservedVsansDefinition


@dataclass
class NetworkLimitsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    MaxCompressedPortVlanCount: Optional[float]
    MaxUncompressedPortVlanCount: Optional[float]
    MaximumActiveTrafficMonitoringSessions: Optional[float]
    MaximumEthernetPortChannels: Optional[float]
    MaximumEthernetUplinkPorts: Optional[float]
    MaximumFcPortChannelMembers: Optional[float]
    MaximumFcPortChannels: Optional[float]
    MaximumIgmpGroups: Optional[float]
    MaximumPortChannelMembers: Optional[float]
    MaximumPrimaryVlan: Optional[float]
    MaximumSecondaryVlan: Optional[float]
    MaximumSecondaryVlanPerPrimary: Optional[float]
    MaximumVifs: Optional[float]
    MaximumVlans: Optional[float]
    MinimumActiveFans: Optional[float]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            MaxCompressedPortVlanCount=json_data.get("MaxCompressedPortVlanCount"),
            MaxUncompressedPortVlanCount=json_data.get("MaxUncompressedPortVlanCount"),
            MaximumActiveTrafficMonitoringSessions=json_data.get("MaximumActiveTrafficMonitoringSessions"),
            MaximumEthernetPortChannels=json_data.get("MaximumEthernetPortChannels"),
            MaximumEthernetUplinkPorts=json_data.get("MaximumEthernetUplinkPorts"),
            MaximumFcPortChannelMembers=json_data.get("MaximumFcPortChannelMembers"),
            MaximumFcPortChannels=json_data.get("MaximumFcPortChannels"),
            MaximumIgmpGroups=json_data.get("MaximumIgmpGroups"),
            MaximumPortChannelMembers=json_data.get("MaximumPortChannelMembers"),
            MaximumPrimaryVlan=json_data.get("MaximumPrimaryVlan"),
            MaximumSecondaryVlan=json_data.get("MaximumSecondaryVlan"),
            MaximumSecondaryVlanPerPrimary=json_data.get("MaximumSecondaryVlanPerPrimary"),
            MaximumVifs=json_data.get("MaximumVifs"),
            MaximumVlans=json_data.get("MaximumVlans"),
            MinimumActiveFans=json_data.get("MinimumActiveFans"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkLimitsDefinition = NetworkLimitsDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class PortsSupporting100gSpeedDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupporting100gSpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupporting100gSpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupporting100gSpeedDefinition = PortsSupporting100gSpeedDefinition


@dataclass
class PortsSupporting10gSpeedDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupporting10gSpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupporting10gSpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupporting10gSpeedDefinition = PortsSupporting10gSpeedDefinition


@dataclass
class PortsSupporting1gSpeedDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupporting1gSpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupporting1gSpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupporting1gSpeedDefinition = PortsSupporting1gSpeedDefinition


@dataclass
class PortsSupporting25gSpeedDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupporting25gSpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupporting25gSpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupporting25gSpeedDefinition = PortsSupporting25gSpeedDefinition


@dataclass
class PortsSupporting40gSpeedDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupporting40gSpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupporting40gSpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupporting40gSpeedDefinition = PortsSupporting40gSpeedDefinition


@dataclass
class PortsSupportingBreakoutDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupportingBreakoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupportingBreakoutDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupportingBreakoutDefinition = PortsSupportingBreakoutDefinition


@dataclass
class PortsSupportingFcoeDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupportingFcoeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupportingFcoeDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupportingFcoeDefinition = PortsSupportingFcoeDefinition


@dataclass
class PortsSupportingServerRoleDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortsSupportingServerRoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsSupportingServerRoleDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsSupportingServerRoleDefinition = PortsSupportingServerRoleDefinition


@dataclass
class ReservedVsansDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReservedVsansDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReservedVsansDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReservedVsansDefinition = ReservedVsansDefinition


@dataclass
class StorageLimitsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    MaximumUserZoneCount: Optional[float]
    MaximumVirtualFcInterfaces: Optional[float]
    MaximumVirtualFcInterfacesPerBladeServer: Optional[float]
    MaximumVsans: Optional[float]
    MaximumZoneCount: Optional[float]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            MaximumUserZoneCount=json_data.get("MaximumUserZoneCount"),
            MaximumVirtualFcInterfaces=json_data.get("MaximumVirtualFcInterfaces"),
            MaximumVirtualFcInterfacesPerBladeServer=json_data.get("MaximumVirtualFcInterfacesPerBladeServer"),
            MaximumVsans=json_data.get("MaximumVsans"),
            MaximumZoneCount=json_data.get("MaximumZoneCount"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLimitsDefinition = StorageLimitsDefinition


@dataclass
class SwitchingModeCapabilitiesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    SwitchingMode: Optional[str]
    VpCompressionSupported: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchingModeCapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchingModeCapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            SwitchingMode=json_data.get("SwitchingMode"),
            VpCompressionSupported=json_data.get("VpCompressionSupported"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchingModeCapabilitiesDefinition = SwitchingModeCapabilitiesDefinition


@dataclass
class SystemLimitsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    MaximumChassisCount: Optional[float]
    MaximumFexPerDomain: Optional[float]
    MaximumServersPerDomain: Optional[float]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            MaximumChassisCount=json_data.get("MaximumChassisCount"),
            MaximumFexPerDomain=json_data.get("MaximumFexPerDomain"),
            MaximumServersPerDomain=json_data.get("MaximumServersPerDomain"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemLimitsDefinition = SystemLimitsDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class UnifiedPortsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    EndPortId: Optional[float]
    EndSlotId: Optional[float]
    ObjectType: Optional[str]
    StartPortId: Optional[float]
    StartSlotId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UnifiedPortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UnifiedPortsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            EndPortId=json_data.get("EndPortId"),
            EndSlotId=json_data.get("EndSlotId"),
            ObjectType=json_data.get("ObjectType"),
            StartPortId=json_data.get("StartPortId"),
            StartSlotId=json_data.get("StartSlotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UnifiedPortsDefinition = UnifiedPortsDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


