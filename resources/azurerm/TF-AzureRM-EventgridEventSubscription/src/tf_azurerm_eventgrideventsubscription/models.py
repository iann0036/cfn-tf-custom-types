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
    EventDeliverySchema: Optional[str]
    EventhubEndpointId: Optional[str]
    ExpirationTimeUtc: Optional[str]
    HybridConnectionEndpointId: Optional[str]
    Id: Optional[str]
    IncludedEventTypes: Optional[Sequence[str]]
    Labels: Optional[Sequence[str]]
    Name: Optional[str]
    Scope: Optional[str]
    ServiceBusQueueEndpointId: Optional[str]
    ServiceBusTopicEndpointId: Optional[str]
    TopicName: Optional[str]
    AdvancedFilter: Optional[Sequence["_AdvancedFilterDefinition"]]
    AzureFunctionEndpoint: Optional[Sequence["_AzureFunctionEndpointDefinition"]]
    EventhubEndpoint: Optional[Sequence["_EventhubEndpointDefinition"]]
    HybridConnectionEndpoint: Optional[Sequence["_HybridConnectionEndpointDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
    StorageBlobDeadLetterDestination: Optional[Sequence["_StorageBlobDeadLetterDestinationDefinition"]]
    StorageQueueEndpoint: Optional[Sequence["_StorageQueueEndpointDefinition"]]
    SubjectFilter: Optional[Sequence["_SubjectFilterDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WebhookEndpoint: Optional[Sequence["_WebhookEndpointDefinition"]]

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
            EventDeliverySchema=json_data.get("EventDeliverySchema"),
            EventhubEndpointId=json_data.get("EventhubEndpointId"),
            ExpirationTimeUtc=json_data.get("ExpirationTimeUtc"),
            HybridConnectionEndpointId=json_data.get("HybridConnectionEndpointId"),
            Id=json_data.get("Id"),
            IncludedEventTypes=json_data.get("IncludedEventTypes"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Scope=json_data.get("Scope"),
            ServiceBusQueueEndpointId=json_data.get("ServiceBusQueueEndpointId"),
            ServiceBusTopicEndpointId=json_data.get("ServiceBusTopicEndpointId"),
            TopicName=json_data.get("TopicName"),
            AdvancedFilter=deserialize_list(json_data.get("AdvancedFilter"), AdvancedFilterDefinition),
            AzureFunctionEndpoint=deserialize_list(json_data.get("AzureFunctionEndpoint"), AzureFunctionEndpointDefinition),
            EventhubEndpoint=deserialize_list(json_data.get("EventhubEndpoint"), EventhubEndpointDefinition),
            HybridConnectionEndpoint=deserialize_list(json_data.get("HybridConnectionEndpoint"), HybridConnectionEndpointDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            StorageBlobDeadLetterDestination=deserialize_list(json_data.get("StorageBlobDeadLetterDestination"), StorageBlobDeadLetterDestinationDefinition),
            StorageQueueEndpoint=deserialize_list(json_data.get("StorageQueueEndpoint"), StorageQueueEndpointDefinition),
            SubjectFilter=deserialize_list(json_data.get("SubjectFilter"), SubjectFilterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WebhookEndpoint=deserialize_list(json_data.get("WebhookEndpoint"), WebhookEndpointDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdvancedFilterDefinition(BaseModel):
    BoolEquals: Optional[Sequence["_BoolEqualsDefinition"]]
    NumberGreaterThan: Optional[Sequence["_NumberGreaterThanDefinition"]]
    NumberGreaterThanOrEquals: Optional[Sequence["_NumberGreaterThanOrEqualsDefinition"]]
    NumberIn: Optional[Sequence["_NumberInDefinition"]]
    NumberLessThan: Optional[Sequence["_NumberLessThanDefinition"]]
    NumberLessThanOrEquals: Optional[Sequence["_NumberLessThanOrEqualsDefinition"]]
    NumberNotIn: Optional[Sequence["_NumberNotInDefinition"]]
    StringBeginsWith: Optional[Sequence["_StringBeginsWithDefinition"]]
    StringContains: Optional[Sequence["_StringContainsDefinition"]]
    StringEndsWith: Optional[Sequence["_StringEndsWithDefinition"]]
    StringIn: Optional[Sequence["_StringInDefinition"]]
    StringNotIn: Optional[Sequence["_StringNotInDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            BoolEquals=deserialize_list(json_data.get("BoolEquals"), BoolEqualsDefinition),
            NumberGreaterThan=deserialize_list(json_data.get("NumberGreaterThan"), NumberGreaterThanDefinition),
            NumberGreaterThanOrEquals=deserialize_list(json_data.get("NumberGreaterThanOrEquals"), NumberGreaterThanOrEqualsDefinition),
            NumberIn=deserialize_list(json_data.get("NumberIn"), NumberInDefinition),
            NumberLessThan=deserialize_list(json_data.get("NumberLessThan"), NumberLessThanDefinition),
            NumberLessThanOrEquals=deserialize_list(json_data.get("NumberLessThanOrEquals"), NumberLessThanOrEqualsDefinition),
            NumberNotIn=deserialize_list(json_data.get("NumberNotIn"), NumberNotInDefinition),
            StringBeginsWith=deserialize_list(json_data.get("StringBeginsWith"), StringBeginsWithDefinition),
            StringContains=deserialize_list(json_data.get("StringContains"), StringContainsDefinition),
            StringEndsWith=deserialize_list(json_data.get("StringEndsWith"), StringEndsWithDefinition),
            StringIn=deserialize_list(json_data.get("StringIn"), StringInDefinition),
            StringNotIn=deserialize_list(json_data.get("StringNotIn"), StringNotInDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedFilterDefinition = AdvancedFilterDefinition


@dataclass
class BoolEqualsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BoolEqualsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoolEqualsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoolEqualsDefinition = BoolEqualsDefinition


@dataclass
class NumberGreaterThanDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberGreaterThanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberGreaterThanDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberGreaterThanDefinition = NumberGreaterThanDefinition


@dataclass
class NumberGreaterThanOrEqualsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberGreaterThanOrEqualsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberGreaterThanOrEqualsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberGreaterThanOrEqualsDefinition = NumberGreaterThanOrEqualsDefinition


@dataclass
class NumberInDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_NumberInDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberInDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberInDefinition = NumberInDefinition


@dataclass
class NumberLessThanDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberLessThanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberLessThanDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberLessThanDefinition = NumberLessThanDefinition


@dataclass
class NumberLessThanOrEqualsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberLessThanOrEqualsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberLessThanOrEqualsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberLessThanOrEqualsDefinition = NumberLessThanOrEqualsDefinition


@dataclass
class NumberNotInDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_NumberNotInDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberNotInDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberNotInDefinition = NumberNotInDefinition


@dataclass
class StringBeginsWithDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringBeginsWithDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringBeginsWithDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringBeginsWithDefinition = StringBeginsWithDefinition


@dataclass
class StringContainsDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringContainsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringContainsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringContainsDefinition = StringContainsDefinition


@dataclass
class StringEndsWithDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringEndsWithDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringEndsWithDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringEndsWithDefinition = StringEndsWithDefinition


@dataclass
class StringInDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringInDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringInDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringInDefinition = StringInDefinition


@dataclass
class StringNotInDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringNotInDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringNotInDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringNotInDefinition = StringNotInDefinition


@dataclass
class AzureFunctionEndpointDefinition(BaseModel):
    FunctionId: Optional[str]
    MaxEventsPerBatch: Optional[float]
    PreferredBatchSizeInKilobytes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFunctionEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFunctionEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionId=json_data.get("FunctionId"),
            MaxEventsPerBatch=json_data.get("MaxEventsPerBatch"),
            PreferredBatchSizeInKilobytes=json_data.get("PreferredBatchSizeInKilobytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFunctionEndpointDefinition = AzureFunctionEndpointDefinition


@dataclass
class EventhubEndpointDefinition(BaseModel):
    EventhubId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventhubEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventhubEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            EventhubId=json_data.get("EventhubId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventhubEndpointDefinition = EventhubEndpointDefinition


@dataclass
class HybridConnectionEndpointDefinition(BaseModel):
    HybridConnectionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HybridConnectionEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HybridConnectionEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            HybridConnectionId=json_data.get("HybridConnectionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HybridConnectionEndpointDefinition = HybridConnectionEndpointDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    EventTimeToLive: Optional[float]
    MaxDeliveryAttempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            EventTimeToLive=json_data.get("EventTimeToLive"),
            MaxDeliveryAttempts=json_data.get("MaxDeliveryAttempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


@dataclass
class StorageBlobDeadLetterDestinationDefinition(BaseModel):
    StorageAccountId: Optional[str]
    StorageBlobContainerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageBlobDeadLetterDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageBlobDeadLetterDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageAccountId=json_data.get("StorageAccountId"),
            StorageBlobContainerName=json_data.get("StorageBlobContainerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageBlobDeadLetterDestinationDefinition = StorageBlobDeadLetterDestinationDefinition


@dataclass
class StorageQueueEndpointDefinition(BaseModel):
    QueueName: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageQueueEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageQueueEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            QueueName=json_data.get("QueueName"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageQueueEndpointDefinition = StorageQueueEndpointDefinition


@dataclass
class SubjectFilterDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    SubjectBeginsWith: Optional[str]
    SubjectEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            SubjectBeginsWith=json_data.get("SubjectBeginsWith"),
            SubjectEndsWith=json_data.get("SubjectEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectFilterDefinition = SubjectFilterDefinition


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


@dataclass
class WebhookEndpointDefinition(BaseModel):
    ActiveDirectoryAppIdOrUri: Optional[str]
    ActiveDirectoryTenantId: Optional[str]
    MaxEventsPerBatch: Optional[float]
    PreferredBatchSizeInKilobytes: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveDirectoryAppIdOrUri=json_data.get("ActiveDirectoryAppIdOrUri"),
            ActiveDirectoryTenantId=json_data.get("ActiveDirectoryTenantId"),
            MaxEventsPerBatch=json_data.get("MaxEventsPerBatch"),
            PreferredBatchSizeInKilobytes=json_data.get("PreferredBatchSizeInKilobytes"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookEndpointDefinition = WebhookEndpointDefinition


