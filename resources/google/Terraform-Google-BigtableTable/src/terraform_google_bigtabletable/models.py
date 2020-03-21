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
    Id: Optional[str]
    InstanceName: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SplitKeys: Optional[Sequence[str]]
    ColumnFamily: Optional[Sequence["_ColumnFamily"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SplitKeys=json_data.get("SplitKeys"),
            ColumnFamily=json_data.get("ColumnFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ColumnFamily:
    Family: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnFamily"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnFamily"]:
        if not json_data:
            return None
        return cls(
            Family=json_data.get("Family"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnFamily = ColumnFamily


