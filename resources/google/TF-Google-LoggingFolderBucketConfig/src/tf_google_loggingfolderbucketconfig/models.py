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
    BucketId: Optional[str]
    Description: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    LifecycleState: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    RetentionDays: Optional[float]

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
            BucketId=json_data.get("BucketId"),
            Description=json_data.get("Description"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            LifecycleState=json_data.get("LifecycleState"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


