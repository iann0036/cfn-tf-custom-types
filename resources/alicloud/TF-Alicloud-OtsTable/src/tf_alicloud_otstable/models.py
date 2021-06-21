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
    DeviationCellVersionInSec: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    MaxVersion: Optional[float]
    TableName: Optional[str]
    TimeToLive: Optional[float]
    PrimaryKey: Optional[Sequence["_PrimaryKeyDefinition"]]

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
            DeviationCellVersionInSec=json_data.get("DeviationCellVersionInSec"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            MaxVersion=json_data.get("MaxVersion"),
            TableName=json_data.get("TableName"),
            TimeToLive=json_data.get("TimeToLive"),
            PrimaryKey=deserialize_list(json_data.get("PrimaryKey"), PrimaryKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrimaryKeyDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryKeyDefinition = PrimaryKeyDefinition

