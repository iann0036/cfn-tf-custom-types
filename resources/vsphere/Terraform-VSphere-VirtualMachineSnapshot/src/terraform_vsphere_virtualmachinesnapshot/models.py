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
    Consolidate: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    Memory: Optional[bool]
    Quiesce: Optional[bool]
    RemoveChildren: Optional[bool]
    SnapshotName: Optional[str]
    VirtualMachineUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Consolidate=json_data.get("Consolidate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Memory=json_data.get("Memory"),
            Quiesce=json_data.get("Quiesce"),
            RemoveChildren=json_data.get("RemoveChildren"),
            SnapshotName=json_data.get("SnapshotName"),
            VirtualMachineUuid=json_data.get("VirtualMachineUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


