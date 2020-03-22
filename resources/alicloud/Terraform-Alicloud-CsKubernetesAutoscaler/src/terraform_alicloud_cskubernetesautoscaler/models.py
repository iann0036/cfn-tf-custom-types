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
    ClusterId: Optional[str]
    CoolDownDuration: Optional[str]
    DeferScaleInDuration: Optional[str]
    Id: Optional[str]
    Utilization: Optional[str]
    Nodepools: Optional[Sequence["_Nodepools"]]
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
            ClusterId=json_data.get("ClusterId"),
            CoolDownDuration=json_data.get("CoolDownDuration"),
            DeferScaleInDuration=json_data.get("DeferScaleInDuration"),
            Id=json_data.get("Id"),
            Utilization=json_data.get("Utilization"),
            Nodepools=json_data.get("Nodepools"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nodepools:
    Id: Optional[str]
    Labels: Optional[str]
    Taints: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodepools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodepools"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Taints=json_data.get("Taints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodepools = Nodepools


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


