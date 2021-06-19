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
    Config: Optional[Sequence["_ConfigDefinition"]]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Global: Optional[bool]
    Id: Optional[str]
    ItemsFound: Optional[str]
    ItemsImported: Optional[str]
    LastImportCompletedAt: Optional[str]
    LastImportErrors: Optional[Sequence[str]]
    LastImportStartedAt: Optional[str]
    LastUpdatedBy: Optional[str]
    Name: Optional[str]
    ProjectId: Optional[str]
    TypeId: Optional[str]

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
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            ItemsFound=json_data.get("ItemsFound"),
            ItemsImported=json_data.get("ItemsImported"),
            LastImportCompletedAt=json_data.get("LastImportCompletedAt"),
            LastImportErrors=json_data.get("LastImportErrors"),
            LastImportStartedAt=json_data.get("LastImportStartedAt"),
            LastUpdatedBy=json_data.get("LastUpdatedBy"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            TypeId=json_data.get("TypeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


