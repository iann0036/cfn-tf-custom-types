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
    ClonedFromTenantId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SpaceId: Optional[str]
    TenantTags: Optional[Sequence[str]]
    ProjectEnvironment: Optional[Sequence["_ProjectEnvironmentDefinition"]]

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
            ClonedFromTenantId=json_data.get("ClonedFromTenantId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SpaceId=json_data.get("SpaceId"),
            TenantTags=json_data.get("TenantTags"),
            ProjectEnvironment=deserialize_list(json_data.get("ProjectEnvironment"), ProjectEnvironmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProjectEnvironmentDefinition(BaseModel):
    Environments: Optional[Sequence[str]]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectEnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectEnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Environments=json_data.get("Environments"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectEnvironmentDefinition = ProjectEnvironmentDefinition


