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
    Capabilities: Optional[Sequence["_Capabilities"]]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Description: Optional[str]
    Email: Optional[str]
    ExternalIdentifier: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    IdentityProviderId: Optional[str]
    InactiveState: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
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
            Capabilities=json_data.get("Capabilities"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            ExternalIdentifier=json_data.get("ExternalIdentifier"),
            FreeformTags=json_data.get("FreeformTags"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
            InactiveState=json_data.get("InactiveState"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Capabilities:
    CanUseApiKeys: Optional[bool]
    CanUseAuthTokens: Optional[bool]
    CanUseConsolePassword: Optional[bool]
    CanUseCustomerSecretKeys: Optional[bool]
    CanUseOauth2clientCredentials: Optional[bool]
    CanUseSmtpCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Capabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capabilities"]:
        if not json_data:
            return None
        return cls(
            CanUseApiKeys=json_data.get("CanUseApiKeys"),
            CanUseAuthTokens=json_data.get("CanUseAuthTokens"),
            CanUseConsolePassword=json_data.get("CanUseConsolePassword"),
            CanUseCustomerSecretKeys=json_data.get("CanUseCustomerSecretKeys"),
            CanUseOauth2clientCredentials=json_data.get("CanUseOauth2clientCredentials"),
            CanUseSmtpCredentials=json_data.get("CanUseSmtpCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capabilities = Capabilities


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


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


