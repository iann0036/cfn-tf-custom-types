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
    CreateTime: Optional[str]
    DiskType: Optional[str]
    Id: Optional[str]
    Percent: Optional[float]
    SnapshotName: Optional[str]
    SnapshotStatus: Optional[str]
    StorageId: Optional[str]
    StorageSize: Optional[float]

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
            CreateTime=json_data.get("CreateTime"),
            DiskType=json_data.get("DiskType"),
            Id=json_data.get("Id"),
            Percent=json_data.get("Percent"),
            SnapshotName=json_data.get("SnapshotName"),
            SnapshotStatus=json_data.get("SnapshotStatus"),
            StorageId=json_data.get("StorageId"),
            StorageSize=json_data.get("StorageSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


