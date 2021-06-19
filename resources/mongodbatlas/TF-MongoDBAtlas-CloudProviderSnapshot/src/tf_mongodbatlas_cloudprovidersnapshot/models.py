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
    ClusterName: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    ExpiresAt: Optional[str]
    Id: Optional[str]
    MasterKeyUuid: Optional[str]
    MongodVersion: Optional[str]
    ProjectId: Optional[str]
    RetentionInDays: Optional[float]
    SnapshotId: Optional[str]
    SnapshotType: Optional[str]
    Status: Optional[str]
    StorageSizeBytes: Optional[float]
    Type: Optional[str]

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
            ClusterName=json_data.get("ClusterName"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            ExpiresAt=json_data.get("ExpiresAt"),
            Id=json_data.get("Id"),
            MasterKeyUuid=json_data.get("MasterKeyUuid"),
            MongodVersion=json_data.get("MongodVersion"),
            ProjectId=json_data.get("ProjectId"),
            RetentionInDays=json_data.get("RetentionInDays"),
            SnapshotId=json_data.get("SnapshotId"),
            SnapshotType=json_data.get("SnapshotType"),
            Status=json_data.get("Status"),
            StorageSizeBytes=json_data.get("StorageSizeBytes"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


