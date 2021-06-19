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
    Action: Optional[str]
    DefaultResponsePlatforms: Optional[Sequence[str]]
    DisplayName: Optional[str]
    Events: Optional[Sequence[str]]
    FollowupIntentInfo: Optional[Sequence["_FollowupIntentInfoDefinition"]]
    Id: Optional[str]
    InputContextNames: Optional[Sequence[str]]
    IsFallback: Optional[bool]
    MlDisabled: Optional[bool]
    Name: Optional[str]
    ParentFollowupIntentName: Optional[str]
    Priority: Optional[float]
    Project: Optional[str]
    ResetContexts: Optional[bool]
    RootFollowupIntentName: Optional[str]
    WebhookState: Optional[str]
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
            Action=json_data.get("Action"),
            DefaultResponsePlatforms=json_data.get("DefaultResponsePlatforms"),
            DisplayName=json_data.get("DisplayName"),
            Events=json_data.get("Events"),
            FollowupIntentInfo=deserialize_list(json_data.get("FollowupIntentInfo"), FollowupIntentInfoDefinition),
            Id=json_data.get("Id"),
            InputContextNames=json_data.get("InputContextNames"),
            IsFallback=json_data.get("IsFallback"),
            MlDisabled=json_data.get("MlDisabled"),
            Name=json_data.get("Name"),
            ParentFollowupIntentName=json_data.get("ParentFollowupIntentName"),
            Priority=json_data.get("Priority"),
            Project=json_data.get("Project"),
            ResetContexts=json_data.get("ResetContexts"),
            RootFollowupIntentName=json_data.get("RootFollowupIntentName"),
            WebhookState=json_data.get("WebhookState"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FollowupIntentInfoDefinition(BaseModel):
    FollowupIntentName: Optional[str]
    ParentFollowupIntentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FollowupIntentInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FollowupIntentInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            FollowupIntentName=json_data.get("FollowupIntentName"),
            ParentFollowupIntentName=json_data.get("ParentFollowupIntentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FollowupIntentInfoDefinition = FollowupIntentInfoDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


