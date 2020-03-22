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
    Action: Optional[str]
    AzureFirewallName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ResourceGroupName: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            AzureFirewallName=json_data.get("AzureFirewallName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Rule=json_data.get("Rule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Description: Optional[str]
    DestinationAddresses: Optional[Sequence[str]]
    DestinationPorts: Optional[Sequence[str]]
    Name: Optional[str]
    Protocols: Optional[Sequence[str]]
    SourceAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationPorts=json_data.get("DestinationPorts"),
            Name=json_data.get("Name"),
            Protocols=json_data.get("Protocols"),
            SourceAddresses=json_data.get("SourceAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


