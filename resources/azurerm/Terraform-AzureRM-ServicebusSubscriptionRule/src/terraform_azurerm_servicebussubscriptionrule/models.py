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
    Action: Optional[str]
    FilterType: Optional[str]
    Name: Optional[str]
    NamespaceName: Optional[str]
    ResourceGroupName: Optional[str]
    SqlFilter: Optional[str]
    SubscriptionName: Optional[str]
    TopicName: Optional[str]
    CorrelationFilter: Optional[Sequence["_CorrelationFilter"]]
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
            Action=json_data.get("Action"),
            FilterType=json_data.get("FilterType"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SqlFilter=json_data.get("SqlFilter"),
            SubscriptionName=json_data.get("SubscriptionName"),
            TopicName=json_data.get("TopicName"),
            CorrelationFilter=json_data.get("CorrelationFilter"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CorrelationFilter:
    ContentType: Optional[str]
    CorrelationId: Optional[str]
    Label: Optional[str]
    MessageId: Optional[str]
    ReplyTo: Optional[str]
    ReplyToSessionId: Optional[str]
    SessionId: Optional[str]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CorrelationFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorrelationFilter"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            CorrelationId=json_data.get("CorrelationId"),
            Label=json_data.get("Label"),
            MessageId=json_data.get("MessageId"),
            ReplyTo=json_data.get("ReplyTo"),
            ReplyToSessionId=json_data.get("ReplyToSessionId"),
            SessionId=json_data.get("SessionId"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorrelationFilter = CorrelationFilter


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


