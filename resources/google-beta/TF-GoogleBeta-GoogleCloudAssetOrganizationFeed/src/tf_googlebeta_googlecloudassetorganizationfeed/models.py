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
    AssetNames: Optional[Sequence[str]]
    AssetTypes: Optional[Sequence[str]]
    BillingProject: Optional[str]
    ContentType: Optional[str]
    FeedId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    FeedOutputConfig: Optional[Sequence["_FeedOutputConfigDefinition"]]
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
            AssetNames=json_data.get("AssetNames"),
            AssetTypes=json_data.get("AssetTypes"),
            BillingProject=json_data.get("BillingProject"),
            ContentType=json_data.get("ContentType"),
            FeedId=json_data.get("FeedId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            FeedOutputConfig=deserialize_list(json_data.get("FeedOutputConfig"), FeedOutputConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConditionDefinition(BaseModel):
    Description: Optional[str]
    Expression: Optional[str]
    Location: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Expression=json_data.get("Expression"),
            Location=json_data.get("Location"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class FeedOutputConfigDefinition(BaseModel):
    PubsubDestination: Optional[Sequence["_PubsubDestinationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FeedOutputConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeedOutputConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PubsubDestination=deserialize_list(json_data.get("PubsubDestination"), PubsubDestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeedOutputConfigDefinition = FeedOutputConfigDefinition


@dataclass
class PubsubDestinationDefinition(BaseModel):
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PubsubDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PubsubDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PubsubDestinationDefinition = PubsubDestinationDefinition


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


