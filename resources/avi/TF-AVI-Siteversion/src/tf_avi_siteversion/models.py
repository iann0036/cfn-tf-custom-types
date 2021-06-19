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
    Datetime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrevTargetVersion: Optional[float]
    ReplicationState: Optional[str]
    SiteId: Optional[str]
    TargetTimeline: Optional[str]
    TargetVersion: Optional[float]
    TenantRef: Optional[str]
    Timeline: Optional[str]
    Uuid: Optional[str]
    Version: Optional[float]
    VersionType: Optional[str]

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
            Datetime=json_data.get("Datetime"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrevTargetVersion=json_data.get("PrevTargetVersion"),
            ReplicationState=json_data.get("ReplicationState"),
            SiteId=json_data.get("SiteId"),
            TargetTimeline=json_data.get("TargetTimeline"),
            TargetVersion=json_data.get("TargetVersion"),
            TenantRef=json_data.get("TenantRef"),
            Timeline=json_data.get("Timeline"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


