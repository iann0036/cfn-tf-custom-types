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
    CdcStartTime: Optional[str]
    Id: Optional[str]
    MigrationType: Optional[str]
    ReplicationInstanceArn: Optional[str]
    ReplicationTaskArn: Optional[str]
    ReplicationTaskId: Optional[str]
    ReplicationTaskSettings: Optional[str]
    SourceEndpointArn: Optional[str]
    TableMappings: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetEndpointArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CdcStartTime=json_data.get("CdcStartTime"),
            Id=json_data.get("Id"),
            MigrationType=json_data.get("MigrationType"),
            ReplicationInstanceArn=json_data.get("ReplicationInstanceArn"),
            ReplicationTaskArn=json_data.get("ReplicationTaskArn"),
            ReplicationTaskId=json_data.get("ReplicationTaskId"),
            ReplicationTaskSettings=json_data.get("ReplicationTaskSettings"),
            SourceEndpointArn=json_data.get("SourceEndpointArn"),
            TableMappings=json_data.get("TableMappings"),
            Tags=json_data.get("Tags"),
            TargetEndpointArn=json_data.get("TargetEndpointArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


