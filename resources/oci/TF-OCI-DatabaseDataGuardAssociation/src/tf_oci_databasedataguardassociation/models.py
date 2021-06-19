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
    ApplyLag: Optional[str]
    ApplyRate: Optional[str]
    AvailabilityDomain: Optional[str]
    BackupNetworkNsgIds: Optional[Sequence[str]]
    CreateAsync: Optional[bool]
    CreationType: Optional[str]
    DatabaseAdminPassword: Optional[str]
    DatabaseId: Optional[str]
    DatabaseSoftwareImageId: Optional[str]
    DeleteStandbyDbHomeOnDelete: Optional[str]
    DisplayName: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PeerDataGuardAssociationId: Optional[str]
    PeerDatabaseId: Optional[str]
    PeerDbHomeId: Optional[str]
    PeerDbSystemId: Optional[str]
    PeerRole: Optional[str]
    PeerVmClusterId: Optional[str]
    ProtectionMode: Optional[str]
    Role: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TransportType: Optional[str]
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
            ApplyLag=json_data.get("ApplyLag"),
            ApplyRate=json_data.get("ApplyRate"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupNetworkNsgIds=json_data.get("BackupNetworkNsgIds"),
            CreateAsync=json_data.get("CreateAsync"),
            CreationType=json_data.get("CreationType"),
            DatabaseAdminPassword=json_data.get("DatabaseAdminPassword"),
            DatabaseId=json_data.get("DatabaseId"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DeleteStandbyDbHomeOnDelete=json_data.get("DeleteStandbyDbHomeOnDelete"),
            DisplayName=json_data.get("DisplayName"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NsgIds=json_data.get("NsgIds"),
            PeerDataGuardAssociationId=json_data.get("PeerDataGuardAssociationId"),
            PeerDatabaseId=json_data.get("PeerDatabaseId"),
            PeerDbHomeId=json_data.get("PeerDbHomeId"),
            PeerDbSystemId=json_data.get("PeerDbSystemId"),
            PeerRole=json_data.get("PeerRole"),
            PeerVmClusterId=json_data.get("PeerVmClusterId"),
            ProtectionMode=json_data.get("ProtectionMode"),
            Role=json_data.get("Role"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TransportType=json_data.get("TransportType"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


