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
    AutoDeleteExecutions: Optional[bool]
    Content: Optional[str]
    CreatedBy: Optional[str]
    CreatedDate: Optional[str]
    Description: Optional[str]
    HasTrigger: Optional[bool]
    Id: Optional[str]
    ShareType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TemplateFormat: Optional[str]
    TemplateId: Optional[str]
    TemplateName: Optional[str]
    TemplateType: Optional[str]
    TemplateVersion: Optional[str]
    UpdatedBy: Optional[str]
    UpdatedDate: Optional[str]
    VersionName: Optional[str]

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
            AutoDeleteExecutions=json_data.get("AutoDeleteExecutions"),
            Content=json_data.get("Content"),
            CreatedBy=json_data.get("CreatedBy"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            HasTrigger=json_data.get("HasTrigger"),
            Id=json_data.get("Id"),
            ShareType=json_data.get("ShareType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TemplateFormat=json_data.get("TemplateFormat"),
            TemplateId=json_data.get("TemplateId"),
            TemplateName=json_data.get("TemplateName"),
            TemplateType=json_data.get("TemplateType"),
            TemplateVersion=json_data.get("TemplateVersion"),
            UpdatedBy=json_data.get("UpdatedBy"),
            UpdatedDate=json_data.get("UpdatedDate"),
            VersionName=json_data.get("VersionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


