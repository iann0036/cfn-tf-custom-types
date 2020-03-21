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
    ApplyLag: Optional[str]
    ApplyRate: Optional[str]
    AvailabilityDomain: Optional[str]
    BackupNetworkNsgIds: Optional[Sequence[str]]
    CreationType: Optional[str]
    DatabaseAdminPassword: Optional[str]
    DatabaseId: Optional[str]
    DeleteStandbyDbHomeOnDelete: Optional[str]
    DisplayName: Optional[str]
    Hostname: Optional[str]
    LifecycleDetails: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PeerDataGuardAssociationId: Optional[str]
    PeerDatabaseId: Optional[str]
    PeerDbHomeId: Optional[str]
    PeerDbSystemId: Optional[str]
    PeerRole: Optional[str]
    ProtectionMode: Optional[str]
    Role: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TransportType: Optional[str]
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
            ApplyLag=json_data.get("ApplyLag"),
            ApplyRate=json_data.get("ApplyRate"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupNetworkNsgIds=json_data.get("BackupNetworkNsgIds"),
            CreationType=json_data.get("CreationType"),
            DatabaseAdminPassword=json_data.get("DatabaseAdminPassword"),
            DatabaseId=json_data.get("DatabaseId"),
            DeleteStandbyDbHomeOnDelete=json_data.get("DeleteStandbyDbHomeOnDelete"),
            DisplayName=json_data.get("DisplayName"),
            Hostname=json_data.get("Hostname"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NsgIds=json_data.get("NsgIds"),
            PeerDataGuardAssociationId=json_data.get("PeerDataGuardAssociationId"),
            PeerDatabaseId=json_data.get("PeerDatabaseId"),
            PeerDbHomeId=json_data.get("PeerDbHomeId"),
            PeerDbSystemId=json_data.get("PeerDbSystemId"),
            PeerRole=json_data.get("PeerRole"),
            ProtectionMode=json_data.get("ProtectionMode"),
            Role=json_data.get("Role"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TransportType=json_data.get("TransportType"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


