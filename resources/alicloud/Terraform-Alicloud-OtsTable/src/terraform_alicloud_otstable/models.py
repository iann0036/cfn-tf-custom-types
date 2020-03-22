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
    DeviationCellVersionInSec: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    MaxVersion: Optional[float]
    TableName: Optional[str]
    TimeToLive: Optional[float]
    PrimaryKey: Optional[Sequence["_PrimaryKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeviationCellVersionInSec=json_data.get("DeviationCellVersionInSec"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            MaxVersion=json_data.get("MaxVersion"),
            TableName=json_data.get("TableName"),
            TimeToLive=json_data.get("TimeToLive"),
            PrimaryKey=json_data.get("PrimaryKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrimaryKey:
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryKey"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryKey = PrimaryKey


