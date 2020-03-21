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
    AutomaticAttributesJson: Optional[str]
    DefaultAttributesJson: Optional[str]
    EnvironmentName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NormalAttributesJson: Optional[str]
    OverrideAttributesJson: Optional[str]
    RunList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutomaticAttributesJson=json_data.get("AutomaticAttributesJson"),
            DefaultAttributesJson=json_data.get("DefaultAttributesJson"),
            EnvironmentName=json_data.get("EnvironmentName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NormalAttributesJson=json_data.get("NormalAttributesJson"),
            OverrideAttributesJson=json_data.get("OverrideAttributesJson"),
            RunList=json_data.get("RunList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


