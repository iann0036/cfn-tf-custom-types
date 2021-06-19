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
    Action: Optional[str]
    ActionInfo: Optional[Sequence["_ActionInfoDefinition"]]
    AdditionalProperties: Optional[str]
    AffinitySelectors: Optional[Sequence["_AffinitySelectorsDefinition"]]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    AntiAffinitySelectors: Optional[Sequence["_AntiAffinitySelectorsDefinition"]]
    ClassId: Optional[str]
    CloudInitConfig: Optional[Sequence["_CloudInitConfigDefinition"]]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    ClusterEsxi: Optional[str]
    Cpu: Optional[float]
    CreateTime: Optional[str]
    Discovered: Optional[bool]
    Disk: Optional[Sequence["_DiskDefinition2"]]
    DomainGroupMoid: Optional[str]
    ForceDelete: Optional[bool]
    GuestOs: Optional[str]
    Host: Optional[Sequence["_HostDefinition"]]
    HostEsxi: Optional[str]
    HypervisorType: Optional[str]
    Id: Optional[str]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]
    Inventory: Optional[Sequence["_InventoryDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Memory: Optional[float]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    PowerState: Optional[str]
    ProvisionType: Optional[str]
    RegisteredDevice: Optional[Sequence["_RegisteredDeviceDefinition"]]
    SharedScope: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    VmConfig: Optional[Sequence["_VmConfigDefinition"]]
    WaitForCompletion: Optional[bool]
    WorkflowInfo: Optional[Sequence["_WorkflowInfoDefinition"]]

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
            Action=json_data.get("Action"),
            ActionInfo=deserialize_list(json_data.get("ActionInfo"), ActionInfoDefinition),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AffinitySelectors=deserialize_list(json_data.get("AffinitySelectors"), AffinitySelectorsDefinition),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            AntiAffinitySelectors=deserialize_list(json_data.get("AntiAffinitySelectors"), AntiAffinitySelectorsDefinition),
            ClassId=json_data.get("ClassId"),
            CloudInitConfig=deserialize_list(json_data.get("CloudInitConfig"), CloudInitConfigDefinition),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            ClusterEsxi=json_data.get("ClusterEsxi"),
            Cpu=json_data.get("Cpu"),
            CreateTime=json_data.get("CreateTime"),
            Discovered=json_data.get("Discovered"),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition2),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            ForceDelete=json_data.get("ForceDelete"),
            GuestOs=json_data.get("GuestOs"),
            Host=deserialize_list(json_data.get("Host"), HostDefinition),
            HostEsxi=json_data.get("HostEsxi"),
            HypervisorType=json_data.get("HypervisorType"),
            Id=json_data.get("Id"),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
            Inventory=deserialize_list(json_data.get("Inventory"), InventoryDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Memory=json_data.get("Memory"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            PowerState=json_data.get("PowerState"),
            ProvisionType=json_data.get("ProvisionType"),
            RegisteredDevice=deserialize_list(json_data.get("RegisteredDevice"), RegisteredDeviceDefinition),
            SharedScope=json_data.get("SharedScope"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            VmConfig=deserialize_list(json_data.get("VmConfig"), VmConfigDefinition),
            WaitForCompletion=json_data.get("WaitForCompletion"),
            WorkflowInfo=deserialize_list(json_data.get("WorkflowInfo"), WorkflowInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    FailureReason: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            FailureReason=json_data.get("FailureReason"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionInfoDefinition = ActionInfoDefinition


@dataclass
class AffinitySelectorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AffinitySelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AffinitySelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AffinitySelectorsDefinition = AffinitySelectorsDefinition


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
class AntiAffinitySelectorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AntiAffinitySelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntiAffinitySelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntiAffinitySelectorsDefinition = AntiAffinitySelectorsDefinition


@dataclass
class CloudInitConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ConfigType: Optional[str]
    NetworkData: Optional[str]
    NetworkDataBase64Encoded: Optional[bool]
    ObjectType: Optional[str]
    UserData: Optional[str]
    UserDataBase64Encoded: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudInitConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudInitConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ConfigType=json_data.get("ConfigType"),
            NetworkData=json_data.get("NetworkData"),
            NetworkDataBase64Encoded=json_data.get("NetworkDataBase64Encoded"),
            ObjectType=json_data.get("ObjectType"),
            UserData=json_data.get("UserData"),
            UserDataBase64Encoded=json_data.get("UserDataBase64Encoded"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudInitConfigDefinition = CloudInitConfigDefinition


@dataclass
class ClusterDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDefinition"]:
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
_ClusterDefinition = ClusterDefinition


@dataclass
class DiskDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    Bus: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Order: Optional[float]
    Type: Optional[str]
    VirtualDisk: Optional[Sequence["_DiskDefinition"]]
    VirtualDiskReference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Bus=json_data.get("Bus"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Order=json_data.get("Order"),
            Type=json_data.get("Type"),
            VirtualDisk=deserialize_list(json_data.get("VirtualDisk"), DiskDefinition),
            VirtualDiskReference=json_data.get("VirtualDiskReference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition2 = DiskDefinition2


@dataclass
class DiskDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Capacity: Optional[str]
    ClassId: Optional[str]
    Mode: Optional[str]
    ObjectType: Optional[str]
    SourceCerts: Optional[str]
    SourceDiskToClone: Optional[str]
    SourceFilePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Capacity=json_data.get("Capacity"),
            ClassId=json_data.get("ClassId"),
            Mode=json_data.get("Mode"),
            ObjectType=json_data.get("ObjectType"),
            SourceCerts=json_data.get("SourceCerts"),
            SourceDiskToClone=json_data.get("SourceDiskToClone"),
            SourceFilePath=json_data.get("SourceFilePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


@dataclass
class HostDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostDefinition"]:
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
_HostDefinition = HostDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    AdaptorType: Optional[str]
    AdditionalProperties: Optional[str]
    Bridge: Optional[str]
    ClassId: Optional[str]
    ConnectAtPowerOn: Optional[bool]
    DirectPathIo: Optional[bool]
    MacAddress: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdaptorType=json_data.get("AdaptorType"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Bridge=json_data.get("Bridge"),
            ClassId=json_data.get("ClassId"),
            ConnectAtPowerOn=json_data.get("ConnectAtPowerOn"),
            DirectPathIo=json_data.get("DirectPathIo"),
            MacAddress=json_data.get("MacAddress"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class InventoryDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InventoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InventoryDefinition"]:
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
_InventoryDefinition = InventoryDefinition


@dataclass
class LabelsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


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
class RegisteredDeviceDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegisteredDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegisteredDeviceDefinition"]:
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
_RegisteredDeviceDefinition = RegisteredDeviceDefinition


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


@dataclass
class VmConfigDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmConfigDefinition = VmConfigDefinition


@dataclass
class WorkflowInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowInfoDefinition"]:
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
_WorkflowInfoDefinition = WorkflowInfoDefinition


