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
    ColumnFamily: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    Mode: Optional[str]
    Project: Optional[str]
    Table: Optional[str]
    MaxAge: Optional[Sequence["_MaxAgeDefinition"]]
    MaxVersion: Optional[Sequence["_MaxVersionDefinition"]]

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
            ColumnFamily=json_data.get("ColumnFamily"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            Mode=json_data.get("Mode"),
            Project=json_data.get("Project"),
            Table=json_data.get("Table"),
            MaxAge=deserialize_list(json_data.get("MaxAge"), MaxAgeDefinition),
            MaxVersion=deserialize_list(json_data.get("MaxVersion"), MaxVersionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MaxAgeDefinition(BaseModel):
    Days: Optional[float]
    Duration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaxAgeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxAgeDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Duration=json_data.get("Duration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxAgeDefinition = MaxAgeDefinition


@dataclass
class MaxVersionDefinition(BaseModel):
    Number: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaxVersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaxVersionDefinition"]:
        if not json_data:
            return None
        return cls(
            Number=json_data.get("Number"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaxVersionDefinition = MaxVersionDefinition


