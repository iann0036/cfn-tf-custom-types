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
    Capabilities: Optional[Sequence["_CapabilitiesDefinition"]]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    Email: Optional[str]
    EmailVerified: Optional[bool]
    ExternalIdentifier: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    IdentityProviderId: Optional[str]
    InactiveState: Optional[str]
    LastSuccessfulLoginTime: Optional[str]
    Name: Optional[str]
    PreviousSuccessfulLoginTime: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
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
            Capabilities=deserialize_list(json_data.get("Capabilities"), CapabilitiesDefinition),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            EmailVerified=json_data.get("EmailVerified"),
            ExternalIdentifier=json_data.get("ExternalIdentifier"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
            InactiveState=json_data.get("InactiveState"),
            LastSuccessfulLoginTime=json_data.get("LastSuccessfulLoginTime"),
            Name=json_data.get("Name"),
            PreviousSuccessfulLoginTime=json_data.get("PreviousSuccessfulLoginTime"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CapabilitiesDefinition(BaseModel):
    CanUseApiKeys: Optional[bool]
    CanUseAuthTokens: Optional[bool]
    CanUseConsolePassword: Optional[bool]
    CanUseCustomerSecretKeys: Optional[bool]
    CanUseOauth2clientCredentials: Optional[bool]
    CanUseSmtpCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapabilitiesDefinition"]:
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
_CapabilitiesDefinition = CapabilitiesDefinition


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


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


