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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MacChangeAllowed: Optional[bool]
    Revision: Optional[float]
    MacLearning: Optional[Sequence["_MacLearning"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MacChangeAllowed=json_data.get("MacChangeAllowed"),
            Revision=json_data.get("Revision"),
            MacLearning=json_data.get("MacLearning"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MacLearning:
    Enabled: Optional[bool]
    Limit: Optional[float]
    LimitPolicy: Optional[str]
    UnicastFloodingAllowed: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MacLearning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacLearning"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Limit=json_data.get("Limit"),
            LimitPolicy=json_data.get("LimitPolicy"),
            UnicastFloodingAllowed=json_data.get("UnicastFloodingAllowed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacLearning = MacLearning


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


