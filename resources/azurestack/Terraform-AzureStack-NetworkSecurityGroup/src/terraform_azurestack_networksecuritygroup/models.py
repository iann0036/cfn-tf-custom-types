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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    SecurityRule: Optional[Sequence["_SecurityRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            SecurityRule=json_data.get("SecurityRule"),
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
class SecurityRule:
    Access: Optional[str]
    Description: Optional[str]
    DestinationAddressPrefix: Optional[str]
    DestinationPortRange: Optional[str]
    Direction: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[str]
    SourceAddressPrefix: Optional[str]
    SourcePortRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityRule"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Description=json_data.get("Description"),
            DestinationAddressPrefix=json_data.get("DestinationAddressPrefix"),
            DestinationPortRange=json_data.get("DestinationPortRange"),
            Direction=json_data.get("Direction"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            SourceAddressPrefix=json_data.get("SourceAddressPrefix"),
            SourcePortRange=json_data.get("SourcePortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityRule = SecurityRule


