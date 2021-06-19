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
    BlueprintDescription: Optional[str]
    BlueprintId: Optional[str]
    ChangeLog: Optional[str]
    Content: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    ProjectId: Optional[str]
    ProjectName: Optional[str]
    Release: Optional[bool]
    Status: Optional[str]
    UpdatedAt: Optional[str]
    UpdatedBy: Optional[str]
    Valid: Optional[str]
    Version: Optional[str]

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
            BlueprintDescription=json_data.get("BlueprintDescription"),
            BlueprintId=json_data.get("BlueprintId"),
            ChangeLog=json_data.get("ChangeLog"),
            Content=json_data.get("Content"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            ProjectId=json_data.get("ProjectId"),
            ProjectName=json_data.get("ProjectName"),
            Release=json_data.get("Release"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UpdatedBy=json_data.get("UpdatedBy"),
            Valid=json_data.get("Valid"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


