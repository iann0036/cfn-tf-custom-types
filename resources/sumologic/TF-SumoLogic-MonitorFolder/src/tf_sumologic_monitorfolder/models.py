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
    ContentType: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsLocked: Optional[bool]
    IsMutable: Optional[bool]
    IsSystem: Optional[bool]
    ModifiedAt: Optional[str]
    ModifiedBy: Optional[str]
    Name: Optional[str]
    ParentId: Optional[str]
    PostRequestMap: Optional[Sequence["_PostRequestMapDefinition"]]
    Type: Optional[str]
    Version: Optional[float]

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
            ContentType=json_data.get("ContentType"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsLocked=json_data.get("IsLocked"),
            IsMutable=json_data.get("IsMutable"),
            IsSystem=json_data.get("IsSystem"),
            ModifiedAt=json_data.get("ModifiedAt"),
            ModifiedBy=json_data.get("ModifiedBy"),
            Name=json_data.get("Name"),
            ParentId=json_data.get("ParentId"),
            PostRequestMap=deserialize_list(json_data.get("PostRequestMap"), PostRequestMapDefinition),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PostRequestMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostRequestMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostRequestMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostRequestMapDefinition = PostRequestMapDefinition


