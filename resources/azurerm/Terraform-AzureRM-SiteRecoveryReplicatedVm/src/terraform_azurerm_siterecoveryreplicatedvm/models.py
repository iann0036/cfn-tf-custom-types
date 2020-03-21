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
    Id: Optional[str]
    ManagedDisk: Optional[Sequence["_ManagedDisk"]]
    Name: Optional[str]
    RecoveryReplicationPolicyId: Optional[str]
    RecoveryVaultName: Optional[str]
    ResourceGroupName: Optional[str]
    SourceRecoveryFabricName: Optional[str]
    SourceRecoveryProtectionContainerName: Optional[str]
    SourceVmId: Optional[str]
    TargetAvailabilitySetId: Optional[str]
    TargetRecoveryFabricId: Optional[str]
    TargetRecoveryProtectionContainerId: Optional[str]
    TargetResourceGroupId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            ManagedDisk=json_data.get("ManagedDisk"),
            Name=json_data.get("Name"),
            RecoveryReplicationPolicyId=json_data.get("RecoveryReplicationPolicyId"),
            RecoveryVaultName=json_data.get("RecoveryVaultName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SourceRecoveryFabricName=json_data.get("SourceRecoveryFabricName"),
            SourceRecoveryProtectionContainerName=json_data.get("SourceRecoveryProtectionContainerName"),
            SourceVmId=json_data.get("SourceVmId"),
            TargetAvailabilitySetId=json_data.get("TargetAvailabilitySetId"),
            TargetRecoveryFabricId=json_data.get("TargetRecoveryFabricId"),
            TargetRecoveryProtectionContainerId=json_data.get("TargetRecoveryProtectionContainerId"),
            TargetResourceGroupId=json_data.get("TargetResourceGroupId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ManagedDisk:
    DiskId: Optional[str]
    StagingStorageAccountId: Optional[str]
    TargetDiskType: Optional[str]
    TargetReplicaDiskType: Optional[str]
    TargetResourceGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedDisk"]:
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
_ManagedDisk = ManagedDisk


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


