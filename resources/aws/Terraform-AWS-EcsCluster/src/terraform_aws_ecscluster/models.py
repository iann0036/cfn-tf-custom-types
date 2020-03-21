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
    Arn: Optional[str]
    CapacityProviders: Optional[Sequence[str]]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    DefaultCapacityProviderStrategy: Optional[Sequence["_DefaultCapacityProviderStrategy"]]
    Setting: Optional[Sequence["_Setting"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CapacityProviders=json_data.get("CapacityProviders"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            DefaultCapacityProviderStrategy=json_data.get("DefaultCapacityProviderStrategy"),
            Setting=json_data.get("Setting"),
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
class DefaultCapacityProviderStrategy:
    Base: Optional[float]
    CapacityProvider: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCapacityProviderStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCapacityProviderStrategy"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCapacityProviderStrategy = DefaultCapacityProviderStrategy


@dataclass
class Setting:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Setting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Setting"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Setting = Setting


