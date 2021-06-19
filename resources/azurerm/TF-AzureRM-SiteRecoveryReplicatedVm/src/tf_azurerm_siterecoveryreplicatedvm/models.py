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
    Id: Optional[str]
    ManagedDisk: Optional[Sequence["_ManagedDiskDefinition"]]
    Name: Optional[str]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    RecoveryReplicationPolicyId: Optional[str]
    RecoveryVaultName: Optional[str]
    ResourceGroupName: Optional[str]
    SourceRecoveryFabricName: Optional[str]
    SourceRecoveryProtectionContainerName: Optional[str]
    SourceVmId: Optional[str]
    TargetAvailabilitySetId: Optional[str]
    TargetNetworkId: Optional[str]
    TargetRecoveryFabricId: Optional[str]
    TargetRecoveryProtectionContainerId: Optional[str]
    TargetResourceGroupId: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            ManagedDisk=deserialize_list(json_data.get("ManagedDisk"), ManagedDiskDefinition),
            Name=json_data.get("Name"),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            RecoveryReplicationPolicyId=json_data.get("RecoveryReplicationPolicyId"),
            RecoveryVaultName=json_data.get("RecoveryVaultName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceRecoveryFabricName=json_data.get("SourceRecoveryFabricName"),
            SourceRecoveryProtectionContainerName=json_data.get("SourceRecoveryProtectionContainerName"),
            SourceVmId=json_data.get("SourceVmId"),
            TargetAvailabilitySetId=json_data.get("TargetAvailabilitySetId"),
            TargetNetworkId=json_data.get("TargetNetworkId"),
            TargetRecoveryFabricId=json_data.get("TargetRecoveryFabricId"),
            TargetRecoveryProtectionContainerId=json_data.get("TargetRecoveryProtectionContainerId"),
            TargetResourceGroupId=json_data.get("TargetResourceGroupId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ManagedDiskDefinition(BaseModel):
    DiskId: Optional[str]
    StagingStorageAccountId: Optional[str]
    TargetDiskType: Optional[str]
    TargetReplicaDiskType: Optional[str]
    TargetResourceGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskId=json_data.get("DiskId"),
            StagingStorageAccountId=json_data.get("StagingStorageAccountId"),
            TargetDiskType=json_data.get("TargetDiskType"),
            TargetReplicaDiskType=json_data.get("TargetReplicaDiskType"),
            TargetResourceGroupId=json_data.get("TargetResourceGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedDiskDefinition = ManagedDiskDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    RecoveryPublicIpAddressId: Optional[str]
    SourceNetworkInterfaceId: Optional[str]
    TargetStaticIp: Optional[str]
    TargetSubnetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryPublicIpAddressId=json_data.get("RecoveryPublicIpAddressId"),
            SourceNetworkInterfaceId=json_data.get("SourceNetworkInterfaceId"),
            TargetStaticIp=json_data.get("TargetStaticIp"),
            TargetSubnetName=json_data.get("TargetSubnetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


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


