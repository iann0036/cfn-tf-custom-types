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
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdatedAt: Optional[str]
    LastUpdatedBy: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    ProjectId: Optional[str]
    SyncEnabled: Optional[bool]
    TypeId: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            LastUpdatedBy=json_data.get("LastUpdatedBy"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            ProjectId=json_data.get("ProjectId"),
            SyncEnabled=json_data.get("SyncEnabled"),
            TypeId=json_data.get("TypeId"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    Branch: Optional[str]
    ContentType: Optional[str]
    IntegrationId: Optional[str]
    Path: Optional[str]
    ProjectName: Optional[str]
    Repository: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            ContentType=json_data.get("ContentType"),
            IntegrationId=json_data.get("IntegrationId"),
            Path=json_data.get("Path"),
            ProjectName=json_data.get("ProjectName"),
            Repository=json_data.get("Repository"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


