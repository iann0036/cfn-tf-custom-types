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
    CreatedAt: Optional[str]
    Description: Optional[str]
    FailureDetail: Optional[str]
    FaultLevel: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PriorityStation: Optional[str]
    Progress: Optional[str]
    RecordMetadata: Optional[str]
    ReplicationConsistencyGroupId: Optional[str]
    ReplicationModel: Optional[str]
    ReplicationStatus: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]
    VolumeIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            FailureDetail=json_data.get("FailureDetail"),
            FaultLevel=json_data.get("FaultLevel"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PriorityStation=json_data.get("PriorityStation"),
            Progress=json_data.get("Progress"),
            RecordMetadata=json_data.get("RecordMetadata"),
            ReplicationConsistencyGroupId=json_data.get("ReplicationConsistencyGroupId"),
            ReplicationModel=json_data.get("ReplicationModel"),
            ReplicationStatus=json_data.get("ReplicationStatus"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
            VolumeIds=json_data.get("VolumeIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


