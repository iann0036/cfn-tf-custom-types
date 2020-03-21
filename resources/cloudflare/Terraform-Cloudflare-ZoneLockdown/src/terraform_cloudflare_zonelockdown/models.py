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
    Paused: Optional[bool]
    Priority: Optional[float]
    Urls: Optional[Sequence[str]]
    ZoneId: Optional[str]
    Configurations: Optional[Sequence["_Configurations"]]

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
            Paused=json_data.get("Paused"),
            Priority=json_data.get("Priority"),
            Urls=json_data.get("Urls"),
            ZoneId=json_data.get("ZoneId"),
            Configurations=json_data.get("Configurations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Configurations:
    Target: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configurations"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configurations = Configurations


