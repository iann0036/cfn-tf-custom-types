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
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DatabaseEdition: Optional[str]
    DatabaseId: Optional[str]
    DatabaseSizeInGbs: Optional[float]
    DisplayName: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    LifecycleDetails: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    TimeEnded: Optional[str]
    TimeStarted: Optional[str]
    Type: Optional[str]
    Version: Optional[str]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DatabaseEdition=json_data.get("DatabaseEdition"),
            DatabaseId=json_data.get("DatabaseId"),
            DatabaseSizeInGbs=json_data.get("DatabaseSizeInGbs"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            TimeEnded=json_data.get("TimeEnded"),
            TimeStarted=json_data.get("TimeStarted"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
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


