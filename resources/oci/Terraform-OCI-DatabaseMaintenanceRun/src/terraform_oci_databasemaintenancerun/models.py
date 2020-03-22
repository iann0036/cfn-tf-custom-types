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
    CompartmentId: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    LifecycleDetails: Optional[str]
    MaintenanceRunId: Optional[str]
    MaintenanceSubtype: Optional[str]
    MaintenanceType: Optional[str]
    State: Optional[str]
    TargetResourceId: Optional[str]
    TargetResourceType: Optional[str]
    TimeEnded: Optional[str]
    TimeScheduled: Optional[str]
    TimeStarted: Optional[str]
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
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MaintenanceRunId=json_data.get("MaintenanceRunId"),
            MaintenanceSubtype=json_data.get("MaintenanceSubtype"),
            MaintenanceType=json_data.get("MaintenanceType"),
            State=json_data.get("State"),
            TargetResourceId=json_data.get("TargetResourceId"),
            TargetResourceType=json_data.get("TargetResourceType"),
            TimeEnded=json_data.get("TimeEnded"),
            TimeScheduled=json_data.get("TimeScheduled"),
            TimeStarted=json_data.get("TimeStarted"),
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


