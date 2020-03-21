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
    EventDeliverySchema: Optional[str]
    IncludedEventTypes: Optional[Sequence[str]]
    Labels: Optional[Sequence[str]]
    Name: Optional[str]
    Scope: Optional[str]
    TopicName: Optional[str]
    EventhubEndpoint: Optional[Sequence["_EventhubEndpoint"]]
    HybridConnectionEndpoint: Optional[Sequence["_HybridConnectionEndpoint"]]
    RetryPolicy: Optional[Sequence["_RetryPolicy"]]
    StorageBlobDeadLetterDestination: Optional[Sequence["_StorageBlobDeadLetterDestination"]]
    StorageQueueEndpoint: Optional[Sequence["_StorageQueueEndpoint"]]
    SubjectFilter: Optional[Sequence["_SubjectFilter"]]
    Timeouts: Optional["_Timeouts"]
    WebhookEndpoint: Optional[Sequence["_WebhookEndpoint"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EventDeliverySchema=json_data.get("EventDeliverySchema"),
            IncludedEventTypes=json_data.get("IncludedEventTypes"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Scope=json_data.get("Scope"),
            TopicName=json_data.get("TopicName"),
            EventhubEndpoint=json_data.get("EventhubEndpoint"),
            HybridConnectionEndpoint=json_data.get("HybridConnectionEndpoint"),
            RetryPolicy=json_data.get("RetryPolicy"),
            StorageBlobDeadLetterDestination=json_data.get("StorageBlobDeadLetterDestination"),
            StorageQueueEndpoint=json_data.get("StorageQueueEndpoint"),
            SubjectFilter=json_data.get("SubjectFilter"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WebhookEndpoint=json_data.get("WebhookEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventhubEndpoint:
    EventhubId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventhubEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventhubEndpoint"]:
        if not json_data:
            return None
        return cls(
            EventhubId=json_data.get("EventhubId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventhubEndpoint = EventhubEndpoint


@dataclass
class HybridConnectionEndpoint:
    HybridConnectionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HybridConnectionEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HybridConnectionEndpoint"]:
        if not json_data:
            return None
        return cls(
            HybridConnectionId=json_data.get("HybridConnectionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HybridConnectionEndpoint = HybridConnectionEndpoint


@dataclass
class RetryPolicy:
    EventTimeToLive: Optional[float]
    MaxDeliveryAttempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicy"]:
        if not json_data:
            return None
        return cls(
            EventTimeToLive=json_data.get("EventTimeToLive"),
            MaxDeliveryAttempts=json_data.get("MaxDeliveryAttempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicy = RetryPolicy


@dataclass
class StorageBlobDeadLetterDestination:
    StorageAccountId: Optional[str]
    StorageBlobContainerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageBlobDeadLetterDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageBlobDeadLetterDestination"]:
        if not json_data:
            return None
        return cls(
            StorageAccountId=json_data.get("StorageAccountId"),
            StorageBlobContainerName=json_data.get("StorageBlobContainerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageBlobDeadLetterDestination = StorageBlobDeadLetterDestination


@dataclass
class StorageQueueEndpoint:
    QueueName: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageQueueEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageQueueEndpoint"]:
        if not json_data:
            return None
        return cls(
            QueueName=json_data.get("QueueName"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageQueueEndpoint = StorageQueueEndpoint


@dataclass
class SubjectFilter:
    CaseSensitive: Optional[bool]
    SubjectBeginsWith: Optional[str]
    SubjectEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectFilter"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            SubjectBeginsWith=json_data.get("SubjectBeginsWith"),
            SubjectEndsWith=json_data.get("SubjectEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectFilter = SubjectFilter


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


@dataclass
class WebhookEndpoint:
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookEndpoint"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookEndpoint = WebhookEndpoint


