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
    Comment: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    LastModifyTime: Optional[str]
    LifeCycle: Optional[float]
    Name: Optional[str]
    ProjectName: Optional[str]
    RecordSchema: Optional[Sequence["_RecordSchema"]]
    RecordType: Optional[str]
    ShardCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comment=json_data.get("Comment"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            LastModifyTime=json_data.get("LastModifyTime"),
            LifeCycle=json_data.get("LifeCycle"),
            Name=json_data.get("Name"),
            ProjectName=json_data.get("ProjectName"),
            RecordSchema=json_data.get("RecordSchema"),
            RecordType=json_data.get("RecordType"),
            ShardCount=json_data.get("ShardCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RecordSchema:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordSchema"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordSchema = RecordSchema


