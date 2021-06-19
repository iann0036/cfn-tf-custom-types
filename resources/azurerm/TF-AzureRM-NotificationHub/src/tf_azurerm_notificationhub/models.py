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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NamespaceName: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ApnsCredential: Optional[Sequence["_ApnsCredentialDefinition"]]
    GcmCredential: Optional[Sequence["_GcmCredentialDefinition"]]
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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ApnsCredential=deserialize_list(json_data.get("ApnsCredential"), ApnsCredentialDefinition),
            GcmCredential=deserialize_list(json_data.get("GcmCredential"), GcmCredentialDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ApnsCredentialDefinition(BaseModel):
    ApplicationMode: Optional[str]
    BundleId: Optional[str]
    KeyId: Optional[str]
    TeamId: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApnsCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApnsCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationMode=json_data.get("ApplicationMode"),
            BundleId=json_data.get("BundleId"),
            KeyId=json_data.get("KeyId"),
            TeamId=json_data.get("TeamId"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApnsCredentialDefinition = ApnsCredentialDefinition


@dataclass
class GcmCredentialDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcmCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcmCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcmCredentialDefinition = GcmCredentialDefinition


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


