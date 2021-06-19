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
    Comment: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    LastModifyTime: Optional[str]
    LifeCycle: Optional[float]
    Name: Optional[str]
    ProjectName: Optional[str]
    RecordSchema: Optional[Sequence["_RecordSchemaDefinition"]]
    RecordType: Optional[str]
    ShardCount: Optional[float]

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
            Comment=json_data.get("Comment"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            LastModifyTime=json_data.get("LastModifyTime"),
            LifeCycle=json_data.get("LifeCycle"),
            Name=json_data.get("Name"),
            ProjectName=json_data.get("ProjectName"),
            RecordSchema=deserialize_list(json_data.get("RecordSchema"), RecordSchemaDefinition),
            RecordType=json_data.get("RecordType"),
            ShardCount=json_data.get("ShardCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RecordSchemaDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSchemaDefinition = RecordSchemaDefinition


