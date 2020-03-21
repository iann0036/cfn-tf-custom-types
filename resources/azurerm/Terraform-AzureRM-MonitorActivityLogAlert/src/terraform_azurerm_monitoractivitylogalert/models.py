# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Scopes: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    Action: Optional[Sequence["_Action"]]
    Criteria: Optional[Sequence["_Criteria"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Scopes=json_data.get("Scopes"),
            Tags=json_data.get("Tags"),
            Action=json_data.get("Action"),
            Criteria=json_data.get("Criteria"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Action:
    ActionGroupId: Optional[str]
    WebhookProperties: Optional[Sequence["_WebhookProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ActionGroupId=json_data.get("ActionGroupId"),
            WebhookProperties=json_data.get("WebhookProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class WebhookProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookProperties = WebhookProperties


@dataclass
class Criteria:
    Caller: Optional[str]
    Category: Optional[str]
    Level: Optional[str]
    OperationName: Optional[str]
    ResourceGroup: Optional[str]
    ResourceId: Optional[str]
    ResourceProvider: Optional[str]
    ResourceType: Optional[str]
    Status: Optional[str]
    SubStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            Caller=json_data.get("Caller"),
            Category=json_data.get("Category"),
            Level=json_data.get("Level"),
            OperationName=json_data.get("OperationName"),
            ResourceGroup=json_data.get("ResourceGroup"),
            ResourceId=json_data.get("ResourceId"),
            ResourceProvider=json_data.get("ResourceProvider"),
            ResourceType=json_data.get("ResourceType"),
            Status=json_data.get("Status"),
            SubStatus=json_data.get("SubStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


