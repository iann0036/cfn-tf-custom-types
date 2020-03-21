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
    ConfigurationId: Optional[str]
    RepositoryName: Optional[str]
    Trigger: Optional[Sequence["_Trigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConfigurationId=json_data.get("ConfigurationId"),
            RepositoryName=json_data.get("RepositoryName"),
            Trigger=json_data.get("Trigger"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Trigger:
    Branches: Optional[Sequence[str]]
    CustomData: Optional[str]
    DestinationArn: Optional[str]
    Events: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Trigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Trigger"]:
        if not json_data:
            return None
        return cls(
            Branches=json_data.get("Branches"),
            CustomData=json_data.get("CustomData"),
            DestinationArn=json_data.get("DestinationArn"),
            Events=json_data.get("Events"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Trigger = Trigger


