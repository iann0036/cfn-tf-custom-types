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
    Id: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    NamespaceName: Optional[str]
    RepoName: Optional[str]
    RuleId: Optional[str]
    SyncDirection: Optional[str]
    SyncScope: Optional[str]
    TagFilter: Optional[str]
    TargetInstanceId: Optional[str]
    TargetNamespaceName: Optional[str]
    TargetRegionId: Optional[str]
    TargetRepoName: Optional[str]

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
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            RepoName=json_data.get("RepoName"),
            RuleId=json_data.get("RuleId"),
            SyncDirection=json_data.get("SyncDirection"),
            SyncScope=json_data.get("SyncScope"),
            TagFilter=json_data.get("TagFilter"),
            TargetInstanceId=json_data.get("TargetInstanceId"),
            TargetNamespaceName=json_data.get("TargetNamespaceName"),
            TargetRegionId=json_data.get("TargetRegionId"),
            TargetRepoName=json_data.get("TargetRepoName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


