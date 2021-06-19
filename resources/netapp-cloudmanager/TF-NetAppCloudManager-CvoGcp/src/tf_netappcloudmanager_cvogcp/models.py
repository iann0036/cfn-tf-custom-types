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
    CapacityTier: Optional[str]
    ClientId: Optional[str]
    DataEncryptionType: Optional[str]
    FirewallRule: Optional[str]
    GcpEncryptionParameters: Optional[str]
    GcpServiceAccount: Optional[str]
    GcpVolumeSize: Optional[float]
    GcpVolumeSizeUnit: Optional[str]
    GcpVolumeType: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    IsHa: Optional[bool]
    LicenseType: Optional[str]
    MediatorZone: Optional[str]
    Name: Optional[str]
    NetworkProjectId: Optional[str]
    Node1Zone: Optional[str]
    Node2Zone: Optional[str]
    NssAccount: Optional[str]
    OntapVersion: Optional[str]
    PlatformSerialNumberNode1: Optional[str]
    PlatformSerialNumberNode2: Optional[str]
    ProjectId: Optional[str]
    SerialNumber: Optional[str]
    Subnet0NodeAndDataConnectivity: Optional[str]
    Subnet1ClusterConnectivity: Optional[str]
    Subnet2HaConnectivity: Optional[str]
    Subnet3DataReplication: Optional[str]
    SubnetId: Optional[str]
    SvmPassword: Optional[str]
    TierLevel: Optional[str]
    UseLatestVersion: Optional[bool]
    Vpc0FirewallRuleName: Optional[str]
    Vpc0NodeAndDataConnectivity: Optional[str]
    Vpc1ClusterConnectivity: Optional[str]
    Vpc1FirewallRuleName: Optional[str]
    Vpc2FirewallRuleName: Optional[str]
    Vpc2HaConnectivity: Optional[str]
    Vpc3DataReplication: Optional[str]
    Vpc3FirewallRuleName: Optional[str]
    VpcId: Optional[str]
    WorkspaceId: Optional[str]
    WritingSpeedState: Optional[str]
    Zone: Optional[str]
    GcpLabel: Optional[Sequence["_GcpLabelDefinition"]]

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
            CapacityTier=json_data.get("CapacityTier"),
            ClientId=json_data.get("ClientId"),
            DataEncryptionType=json_data.get("DataEncryptionType"),
            FirewallRule=json_data.get("FirewallRule"),
            GcpEncryptionParameters=json_data.get("GcpEncryptionParameters"),
            GcpServiceAccount=json_data.get("GcpServiceAccount"),
            GcpVolumeSize=json_data.get("GcpVolumeSize"),
            GcpVolumeSizeUnit=json_data.get("GcpVolumeSizeUnit"),
            GcpVolumeType=json_data.get("GcpVolumeType"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            IsHa=json_data.get("IsHa"),
            LicenseType=json_data.get("LicenseType"),
            MediatorZone=json_data.get("MediatorZone"),
            Name=json_data.get("Name"),
            NetworkProjectId=json_data.get("NetworkProjectId"),
            Node1Zone=json_data.get("Node1Zone"),
            Node2Zone=json_data.get("Node2Zone"),
            NssAccount=json_data.get("NssAccount"),
            OntapVersion=json_data.get("OntapVersion"),
            PlatformSerialNumberNode1=json_data.get("PlatformSerialNumberNode1"),
            PlatformSerialNumberNode2=json_data.get("PlatformSerialNumberNode2"),
            ProjectId=json_data.get("ProjectId"),
            SerialNumber=json_data.get("SerialNumber"),
            Subnet0NodeAndDataConnectivity=json_data.get("Subnet0NodeAndDataConnectivity"),
            Subnet1ClusterConnectivity=json_data.get("Subnet1ClusterConnectivity"),
            Subnet2HaConnectivity=json_data.get("Subnet2HaConnectivity"),
            Subnet3DataReplication=json_data.get("Subnet3DataReplication"),
            SubnetId=json_data.get("SubnetId"),
            SvmPassword=json_data.get("SvmPassword"),
            TierLevel=json_data.get("TierLevel"),
            UseLatestVersion=json_data.get("UseLatestVersion"),
            Vpc0FirewallRuleName=json_data.get("Vpc0FirewallRuleName"),
            Vpc0NodeAndDataConnectivity=json_data.get("Vpc0NodeAndDataConnectivity"),
            Vpc1ClusterConnectivity=json_data.get("Vpc1ClusterConnectivity"),
            Vpc1FirewallRuleName=json_data.get("Vpc1FirewallRuleName"),
            Vpc2FirewallRuleName=json_data.get("Vpc2FirewallRuleName"),
            Vpc2HaConnectivity=json_data.get("Vpc2HaConnectivity"),
            Vpc3DataReplication=json_data.get("Vpc3DataReplication"),
            Vpc3FirewallRuleName=json_data.get("Vpc3FirewallRuleName"),
            VpcId=json_data.get("VpcId"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WritingSpeedState=json_data.get("WritingSpeedState"),
            Zone=json_data.get("Zone"),
            GcpLabel=deserialize_list(json_data.get("GcpLabel"), GcpLabelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GcpLabelDefinition(BaseModel):
    LabelKey: Optional[str]
    LabelValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpLabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpLabelDefinition"]:
        if not json_data:
            return None
        return cls(
            LabelKey=json_data.get("LabelKey"),
            LabelValue=json_data.get("LabelValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpLabelDefinition = GcpLabelDefinition


