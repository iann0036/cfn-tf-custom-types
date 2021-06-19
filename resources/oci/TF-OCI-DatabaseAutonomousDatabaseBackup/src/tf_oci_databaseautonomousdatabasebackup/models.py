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
    AutonomousDatabaseId: Optional[str]
    CompartmentId: Optional[str]
    DatabaseSizeInTbs: Optional[float]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsAutomatic: Optional[bool]
    IsRestorable: Optional[bool]
    KeyStoreId: Optional[str]
    KeyStoreWalletName: Optional[str]
    KmsKeyId: Optional[str]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    TimeEnded: Optional[str]
    TimeStarted: Optional[str]
    Type: Optional[str]
    VaultId: Optional[str]
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
            AutonomousDatabaseId=json_data.get("AutonomousDatabaseId"),
            CompartmentId=json_data.get("CompartmentId"),
            DatabaseSizeInTbs=json_data.get("DatabaseSizeInTbs"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsAutomatic=json_data.get("IsAutomatic"),
            IsRestorable=json_data.get("IsRestorable"),
            KeyStoreId=json_data.get("KeyStoreId"),
            KeyStoreWalletName=json_data.get("KeyStoreWalletName"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            TimeEnded=json_data.get("TimeEnded"),
            TimeStarted=json_data.get("TimeStarted"),
            Type=json_data.get("Type"),
            VaultId=json_data.get("VaultId"),
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


