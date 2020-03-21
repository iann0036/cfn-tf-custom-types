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
    Catalog: Optional[str]
    Description: Optional[str]
    DisplayLayer: Optional[str]
    DisplayName: Optional[str]
    DomainId: Optional[str]
    Name: Optional[str]
    Statement: Optional[Sequence["_Statement"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Catalog=json_data.get("Catalog"),
            Description=json_data.get("Description"),
            DisplayLayer=json_data.get("DisplayLayer"),
            DisplayName=json_data.get("DisplayName"),
            DomainId=json_data.get("DomainId"),
            Name=json_data.get("Name"),
            Statement=json_data.get("Statement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Statement:
    Action: Optional[Sequence[str]]
    Effect: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Statement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Statement"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Effect=json_data.get("Effect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Statement = Statement


