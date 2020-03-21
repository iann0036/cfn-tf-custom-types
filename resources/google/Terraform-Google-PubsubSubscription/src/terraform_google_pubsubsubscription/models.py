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
    AckDeadlineSeconds: Optional[float]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MessageRetentionDuration: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Project: Optional[str]
    RetainAckedMessages: Optional[bool]
    Topic: Optional[str]
    ExpirationPolicy: Optional[Sequence["_ExpirationPolicy"]]
    PushConfig: Optional[Sequence["_PushConfig"]]
    Timeouts: Optional["_Timeouts"]
    OidcToken: Optional[Sequence["_OidcToken"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AckDeadlineSeconds=json_data.get("AckDeadlineSeconds"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            MessageRetentionDuration=json_data.get("MessageRetentionDuration"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Project=json_data.get("Project"),
            RetainAckedMessages=json_data.get("RetainAckedMessages"),
            Topic=json_data.get("Topic"),
            ExpirationPolicy=json_data.get("ExpirationPolicy"),
            PushConfig=json_data.get("PushConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            OidcToken=json_data.get("OidcToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class ExpirationPolicy:
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExpirationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpirationPolicy"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpirationPolicy = ExpirationPolicy


@dataclass
class PushConfig:
    Attributes: Optional[Sequence["_Attributes"]]
    PushEndpoint: Optional[str]
    OidcToken: Optional[Sequence["_OidcToken"]]

    @classmethod
    def _deserialize(
        cls: Type["_PushConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PushConfig"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            PushEndpoint=json_data.get("PushEndpoint"),
            OidcToken=json_data.get("OidcToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PushConfig = PushConfig


@dataclass
class Attributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


@dataclass
class OidcToken:
    Audience: Optional[str]
    ServiceAccountEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcToken"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcToken"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcToken = OidcToken


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


