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
    BucketId: Optional[str]
    Id: Optional[str]
    InitialVariables: Optional[Sequence["_InitialVariables"]]
    Integrations: Optional[Sequence[str]]
    Name: Optional[str]
    PreserveCookies: Optional[bool]
    Regions: Optional[Sequence[str]]
    RetryOnFailure: Optional[bool]
    Script: Optional[str]
    TestId: Optional[str]
    VerifySsl: Optional[bool]
    Webhooks: Optional[Sequence[str]]
    Emails: Optional[Sequence["_Emails"]]
    RemoteAgents: Optional[Sequence["_RemoteAgents"]]
    Recipients: Optional[Sequence["_Recipients"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BucketId=json_data.get("BucketId"),
            Id=json_data.get("Id"),
            InitialVariables=json_data.get("InitialVariables"),
            Integrations=json_data.get("Integrations"),
            Name=json_data.get("Name"),
            PreserveCookies=json_data.get("PreserveCookies"),
            Regions=json_data.get("Regions"),
            RetryOnFailure=json_data.get("RetryOnFailure"),
            Script=json_data.get("Script"),
            TestId=json_data.get("TestId"),
            VerifySsl=json_data.get("VerifySsl"),
            Webhooks=json_data.get("Webhooks"),
            Emails=json_data.get("Emails"),
            RemoteAgents=json_data.get("RemoteAgents"),
            Recipients=json_data.get("Recipients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InitialVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialVariables = InitialVariables


@dataclass
class Emails:
    NotifyAll: Optional[bool]
    NotifyOn: Optional[str]
    NotifyThreshold: Optional[float]
    Recipients: Optional[Sequence["_Recipients"]]

    @classmethod
    def _deserialize(
        cls: Type["_Emails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Emails"]:
        if not json_data:
            return None
        return cls(
            NotifyAll=json_data.get("NotifyAll"),
            NotifyOn=json_data.get("NotifyOn"),
            NotifyThreshold=json_data.get("NotifyThreshold"),
            Recipients=json_data.get("Recipients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Emails = Emails


@dataclass
class Recipients:
    Email: Optional[str]
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Recipients"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recipients"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recipients = Recipients


@dataclass
class RemoteAgents:
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteAgents"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteAgents"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteAgents = RemoteAgents


