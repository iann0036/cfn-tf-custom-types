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
    Cancelled: Optional[bool]
    ClusterName: Optional[str]
    CreatedAt: Optional[str]
    DeliveryType: Optional[Sequence["_DeliveryTypeDefinition"]]
    DeliveryUrl: Optional[Sequence[str]]
    Expired: Optional[bool]
    ExpiresAt: Optional[str]
    FinishedAt: Optional[str]
    Id: Optional[str]
    ProjectId: Optional[str]
    SnapshotId: Optional[str]
    SnapshotRestoreJobId: Optional[str]
    Timestamp: Optional[str]

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
            Cancelled=json_data.get("Cancelled"),
            ClusterName=json_data.get("ClusterName"),
            CreatedAt=json_data.get("CreatedAt"),
            DeliveryType=deserialize_list(json_data.get("DeliveryType"), DeliveryTypeDefinition),
            DeliveryUrl=json_data.get("DeliveryUrl"),
            Expired=json_data.get("Expired"),
            ExpiresAt=json_data.get("ExpiresAt"),
            FinishedAt=json_data.get("FinishedAt"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            SnapshotId=json_data.get("SnapshotId"),
            SnapshotRestoreJobId=json_data.get("SnapshotRestoreJobId"),
            Timestamp=json_data.get("Timestamp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeliveryTypeDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryTypeDefinition = DeliveryTypeDefinition


