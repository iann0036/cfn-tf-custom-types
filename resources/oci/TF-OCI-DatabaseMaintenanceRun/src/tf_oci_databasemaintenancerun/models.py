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
    CompartmentId: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    IsPatchNowEnabled: Optional[bool]
    LifecycleDetails: Optional[str]
    MaintenanceRunId: Optional[str]
    MaintenanceSubtype: Optional[str]
    MaintenanceType: Optional[str]
    PatchFailureCount: Optional[float]
    PatchId: Optional[str]
    PatchingMode: Optional[str]
    PeerMaintenanceRunId: Optional[str]
    State: Optional[str]
    TargetResourceId: Optional[str]
    TargetResourceType: Optional[str]
    TimeEnded: Optional[str]
    TimeScheduled: Optional[str]
    TimeStarted: Optional[str]
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
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            IsPatchNowEnabled=json_data.get("IsPatchNowEnabled"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MaintenanceRunId=json_data.get("MaintenanceRunId"),
            MaintenanceSubtype=json_data.get("MaintenanceSubtype"),
            MaintenanceType=json_data.get("MaintenanceType"),
            PatchFailureCount=json_data.get("PatchFailureCount"),
            PatchId=json_data.get("PatchId"),
            PatchingMode=json_data.get("PatchingMode"),
            PeerMaintenanceRunId=json_data.get("PeerMaintenanceRunId"),
            State=json_data.get("State"),
            TargetResourceId=json_data.get("TargetResourceId"),
            TargetResourceType=json_data.get("TargetResourceType"),
            TimeEnded=json_data.get("TimeEnded"),
            TimeScheduled=json_data.get("TimeScheduled"),
            TimeStarted=json_data.get("TimeStarted"),
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


