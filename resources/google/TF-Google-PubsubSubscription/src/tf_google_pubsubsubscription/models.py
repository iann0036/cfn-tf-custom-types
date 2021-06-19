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
    AckDeadlineSeconds: Optional[float]
    EnableMessageOrdering: Optional[bool]
    Filter: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MessageRetentionDuration: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Project: Optional[str]
    RetainAckedMessages: Optional[bool]
    Topic: Optional[str]
    DeadLetterPolicy: Optional[Sequence["_DeadLetterPolicyDefinition"]]
    ExpirationPolicy: Optional[Sequence["_ExpirationPolicyDefinition"]]
    PushConfig: Optional[Sequence["_PushConfigDefinition"]]
    RetryPolicy: Optional[Sequence["_RetryPolicyDefinition"]]
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
            AckDeadlineSeconds=json_data.get("AckDeadlineSeconds"),
            EnableMessageOrdering=json_data.get("EnableMessageOrdering"),
            Filter=json_data.get("Filter"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MessageRetentionDuration=json_data.get("MessageRetentionDuration"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Project=json_data.get("Project"),
            RetainAckedMessages=json_data.get("RetainAckedMessages"),
            Topic=json_data.get("Topic"),
            DeadLetterPolicy=deserialize_list(json_data.get("DeadLetterPolicy"), DeadLetterPolicyDefinition),
            ExpirationPolicy=deserialize_list(json_data.get("ExpirationPolicy"), ExpirationPolicyDefinition),
            PushConfig=deserialize_list(json_data.get("PushConfig"), PushConfigDefinition),
            RetryPolicy=deserialize_list(json_data.get("RetryPolicy"), RetryPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class DeadLetterPolicyDefinition(BaseModel):
    DeadLetterTopic: Optional[str]
    MaxDeliveryAttempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DeadLetterTopic=json_data.get("DeadLetterTopic"),
            MaxDeliveryAttempts=json_data.get("MaxDeliveryAttempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterPolicyDefinition = DeadLetterPolicyDefinition


@dataclass
class ExpirationPolicyDefinition(BaseModel):
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExpirationPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpirationPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpirationPolicyDefinition = ExpirationPolicyDefinition


@dataclass
class PushConfigDefinition(BaseModel):
    Attributes: Optional[Sequence["_AttributesDefinition"]]
    PushEndpoint: Optional[str]
    OidcToken: Optional[Sequence["_OidcTokenDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PushConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PushConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Attributes=deserialize_list(json_data.get("Attributes"), AttributesDefinition),
            PushEndpoint=json_data.get("PushEndpoint"),
            OidcToken=deserialize_list(json_data.get("OidcToken"), OidcTokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PushConfigDefinition = PushConfigDefinition


@dataclass
class AttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributesDefinition = AttributesDefinition


@dataclass
class OidcTokenDefinition(BaseModel):
    Audience: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcTokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcTokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcTokenDefinition = OidcTokenDefinition


@dataclass
class RetryPolicyDefinition(BaseModel):
    MaximumBackoff: Optional[str]
    MinimumBackoff: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaximumBackoff=json_data.get("MaximumBackoff"),
            MinimumBackoff=json_data.get("MinimumBackoff"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicyDefinition = RetryPolicyDefinition


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


