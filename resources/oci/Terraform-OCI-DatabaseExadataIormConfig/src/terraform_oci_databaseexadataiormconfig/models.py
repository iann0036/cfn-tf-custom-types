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
    DbSystemId: Optional[str]
    LifecycleDetails: Optional[str]
    Objective: Optional[str]
    State: Optional[str]
    DbPlans: Optional[Sequence["_DbPlans"]]
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
            DbSystemId=json_data.get("DbSystemId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Objective=json_data.get("Objective"),
            State=json_data.get("State"),
            DbPlans=json_data.get("DbPlans"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DbPlans:
    DbName: Optional[str]
    Share: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DbPlans"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbPlans"]:
        if not json_data:
            return None
        return cls(
            DbName=json_data.get("DbName"),
            Share=json_data.get("Share"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbPlans = DbPlans


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


