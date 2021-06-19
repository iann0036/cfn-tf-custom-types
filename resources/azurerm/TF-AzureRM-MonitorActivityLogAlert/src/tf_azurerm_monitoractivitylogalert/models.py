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
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Scopes: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Action: Optional[Sequence["_ActionDefinition"]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Scopes=json_data.get("Scopes"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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


@dataclass
class ActionDefinition(BaseModel):
    ActionGroupId: Optional[str]
    WebhookProperties: Optional[Sequence["_WebhookPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionGroupId=json_data.get("ActionGroupId"),
            WebhookProperties=deserialize_list(json_data.get("WebhookProperties"), WebhookPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class WebhookPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookPropertiesDefinition = WebhookPropertiesDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    Caller: Optional[str]
    Category: Optional[str]
    Level: Optional[str]
    OperationName: Optional[str]
    RecommendationCategory: Optional[str]
    RecommendationImpact: Optional[str]
    RecommendationType: Optional[str]
    ResourceGroup: Optional[str]
    ResourceId: Optional[str]
    ResourceProvider: Optional[str]
    ResourceType: Optional[str]
    Status: Optional[str]
    SubStatus: Optional[str]
    ServiceHealth: Optional[Sequence["_ServiceHealthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Caller=json_data.get("Caller"),
            Category=json_data.get("Category"),
            Level=json_data.get("Level"),
            OperationName=json_data.get("OperationName"),
            RecommendationCategory=json_data.get("RecommendationCategory"),
            RecommendationImpact=json_data.get("RecommendationImpact"),
            RecommendationType=json_data.get("RecommendationType"),
            ResourceGroup=json_data.get("ResourceGroup"),
            ResourceId=json_data.get("ResourceId"),
            ResourceProvider=json_data.get("ResourceProvider"),
            ResourceType=json_data.get("ResourceType"),
            Status=json_data.get("Status"),
            SubStatus=json_data.get("SubStatus"),
            ServiceHealth=deserialize_list(json_data.get("ServiceHealth"), ServiceHealthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class ServiceHealthDefinition(BaseModel):
    Events: Optional[Sequence[str]]
    Locations: Optional[Sequence[str]]
    Services: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceHealthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceHealthDefinition"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            Locations=json_data.get("Locations"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceHealthDefinition = ServiceHealthDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


