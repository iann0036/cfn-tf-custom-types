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
    AppendMeta: Optional[bool]
    AutoSplit: Optional[bool]
    EnableWebTracking: Optional[bool]
    Id: Optional[str]
    MaxSplitShardCount: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    RetentionPeriod: Optional[float]
    ShardCount: Optional[float]
    Shards: Optional[Sequence["_Shards"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppendMeta=json_data.get("AppendMeta"),
            AutoSplit=json_data.get("AutoSplit"),
            EnableWebTracking=json_data.get("EnableWebTracking"),
            Id=json_data.get("Id"),
            MaxSplitShardCount=json_data.get("MaxSplitShardCount"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            ShardCount=json_data.get("ShardCount"),
            Shards=json_data.get("Shards"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Shards:
    BeginKey: Optional[str]
    EndKey: Optional[str]
    Id: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Shards"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Shards"]:
        if not json_data:
            return None
        return cls(
            BeginKey=json_data.get("BeginKey"),
            EndKey=json_data.get("EndKey"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Shards = Shards


