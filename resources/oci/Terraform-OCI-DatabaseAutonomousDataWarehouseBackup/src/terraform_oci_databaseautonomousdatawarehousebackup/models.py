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
    AutonomousDataWarehouseId: Optional[str]
    CompartmentId: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IsAutomatic: Optional[bool]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    TimeEnded: Optional[str]
    TimeStarted: Optional[str]
    Type: Optional[str]
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
            AutonomousDataWarehouseId=json_data.get("AutonomousDataWarehouseId"),
            CompartmentId=json_data.get("CompartmentId"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsAutomatic=json_data.get("IsAutomatic"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            TimeEnded=json_data.get("TimeEnded"),
            TimeStarted=json_data.get("TimeStarted"),
            Type=json_data.get("Type"),
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


