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
    Authentication: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetAction: Optional[str]
    TargetPipeline: Optional[str]
    Url: Optional[str]
    AuthenticationConfiguration: Optional[Sequence["_AuthenticationConfiguration"]]
    Filter: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Authentication=json_data.get("Authentication"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            TargetAction=json_data.get("TargetAction"),
            TargetPipeline=json_data.get("TargetPipeline"),
            Url=json_data.get("Url"),
            AuthenticationConfiguration=json_data.get("AuthenticationConfiguration"),
            Filter=json_data.get("Filter"),
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
class AuthenticationConfiguration:
    AllowedIpRange: Optional[str]
    SecretToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationConfiguration"]:
        if not json_data:
            return None
        return cls(
            AllowedIpRange=json_data.get("AllowedIpRange"),
            SecretToken=json_data.get("SecretToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationConfiguration = AuthenticationConfiguration


@dataclass
class Filter:
    JsonPath: Optional[str]
    MatchEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
            MatchEquals=json_data.get("MatchEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


