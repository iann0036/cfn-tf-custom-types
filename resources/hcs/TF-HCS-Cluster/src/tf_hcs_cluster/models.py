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
    AuditLogStorageContainerUrl: Optional[str]
    AuditLoggingEnabled: Optional[bool]
    BlobContainerName: Optional[str]
    ClusterMode: Optional[str]
    ClusterName: Optional[str]
    ConsulAutomaticUpgrades: Optional[bool]
    ConsulCaFile: Optional[str]
    ConsulClusterId: Optional[str]
    ConsulConfigFile: Optional[str]
    ConsulConnect: Optional[bool]
    ConsulDatacenter: Optional[str]
    ConsulExternalEndpoint: Optional[bool]
    ConsulExternalEndpointUrl: Optional[str]
    ConsulFederationToken: Optional[str]
    ConsulPrivateEndpointUrl: Optional[str]
    ConsulRootTokenAccessorId: Optional[str]
    ConsulRootTokenSecretId: Optional[str]
    ConsulSnapshotInterval: Optional[str]
    ConsulSnapshotRetention: Optional[str]
    ConsulVersion: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    ManagedApplicationId: Optional[str]
    ManagedApplicationName: Optional[str]
    ManagedIdentityName: Optional[str]
    ManagedResourceGroupName: Optional[str]
    MinConsulVersion: Optional[str]
    PlanName: Optional[str]
    ResourceGroupName: Optional[str]
    State: Optional[str]
    StorageAccountName: Optional[str]
    StorageAccountResourceGroup: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VnetCidr: Optional[str]
    VnetId: Optional[str]
    VnetName: Optional[str]
    VnetResourceGroupName: Optional[str]
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
            AuditLogStorageContainerUrl=json_data.get("AuditLogStorageContainerUrl"),
            AuditLoggingEnabled=json_data.get("AuditLoggingEnabled"),
            BlobContainerName=json_data.get("BlobContainerName"),
            ClusterMode=json_data.get("ClusterMode"),
            ClusterName=json_data.get("ClusterName"),
            ConsulAutomaticUpgrades=json_data.get("ConsulAutomaticUpgrades"),
            ConsulCaFile=json_data.get("ConsulCaFile"),
            ConsulClusterId=json_data.get("ConsulClusterId"),
            ConsulConfigFile=json_data.get("ConsulConfigFile"),
            ConsulConnect=json_data.get("ConsulConnect"),
            ConsulDatacenter=json_data.get("ConsulDatacenter"),
            ConsulExternalEndpoint=json_data.get("ConsulExternalEndpoint"),
            ConsulExternalEndpointUrl=json_data.get("ConsulExternalEndpointUrl"),
            ConsulFederationToken=json_data.get("ConsulFederationToken"),
            ConsulPrivateEndpointUrl=json_data.get("ConsulPrivateEndpointUrl"),
            ConsulRootTokenAccessorId=json_data.get("ConsulRootTokenAccessorId"),
            ConsulRootTokenSecretId=json_data.get("ConsulRootTokenSecretId"),
            ConsulSnapshotInterval=json_data.get("ConsulSnapshotInterval"),
            ConsulSnapshotRetention=json_data.get("ConsulSnapshotRetention"),
            ConsulVersion=json_data.get("ConsulVersion"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            ManagedApplicationId=json_data.get("ManagedApplicationId"),
            ManagedApplicationName=json_data.get("ManagedApplicationName"),
            ManagedIdentityName=json_data.get("ManagedIdentityName"),
            ManagedResourceGroupName=json_data.get("ManagedResourceGroupName"),
            MinConsulVersion=json_data.get("MinConsulVersion"),
            PlanName=json_data.get("PlanName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            State=json_data.get("State"),
            StorageAccountName=json_data.get("StorageAccountName"),
            StorageAccountResourceGroup=json_data.get("StorageAccountResourceGroup"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VnetCidr=json_data.get("VnetCidr"),
            VnetId=json_data.get("VnetId"),
            VnetName=json_data.get("VnetName"),
            VnetResourceGroupName=json_data.get("VnetResourceGroupName"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
    Delete: Optional[str]
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
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


