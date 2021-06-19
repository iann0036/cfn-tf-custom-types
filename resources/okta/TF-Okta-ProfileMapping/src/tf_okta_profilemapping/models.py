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
    DeleteWhenAbsent: Optional[bool]
    Id: Optional[str]
    SourceId: Optional[str]
    SourceName: Optional[str]
    SourceType: Optional[str]
    TargetId: Optional[str]
    TargetName: Optional[str]
    TargetType: Optional[str]
    Mappings: Optional[Sequence["_MappingsDefinition"]]

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
            DeleteWhenAbsent=json_data.get("DeleteWhenAbsent"),
            Id=json_data.get("Id"),
            SourceId=json_data.get("SourceId"),
            SourceName=json_data.get("SourceName"),
            SourceType=json_data.get("SourceType"),
            TargetId=json_data.get("TargetId"),
            TargetName=json_data.get("TargetName"),
            TargetType=json_data.get("TargetType"),
            Mappings=deserialize_list(json_data.get("Mappings"), MappingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MappingsDefinition(BaseModel):
    Expression: Optional[str]
    Id: Optional[str]
    PushStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Id=json_data.get("Id"),
            PushStatus=json_data.get("PushStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingsDefinition = MappingsDefinition


