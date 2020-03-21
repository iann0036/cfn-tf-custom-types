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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DestinationRanges: Optional[Sequence[str]]
    Direction: Optional[str]
    Disabled: Optional[bool]
    EnableLogging: Optional[bool]
    Name: Optional[str]
    Network: Optional[str]
    Priority: Optional[float]
    Project: Optional[str]
    SelfLink: Optional[str]
    SourceRanges: Optional[Sequence[str]]
    SourceServiceAccounts: Optional[Sequence[str]]
    SourceTags: Optional[Sequence[str]]
    TargetServiceAccounts: Optional[Sequence[str]]
    TargetTags: Optional[Sequence[str]]
    Allow: Optional[Sequence["_Allow"]]
    Deny: Optional[Sequence["_Deny"]]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DestinationRanges=json_data.get("DestinationRanges"),
            Direction=json_data.get("Direction"),
            Disabled=json_data.get("Disabled"),
            EnableLogging=json_data.get("EnableLogging"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            Priority=json_data.get("Priority"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SourceRanges=json_data.get("SourceRanges"),
            SourceServiceAccounts=json_data.get("SourceServiceAccounts"),
            SourceTags=json_data.get("SourceTags"),
            TargetServiceAccounts=json_data.get("TargetServiceAccounts"),
            TargetTags=json_data.get("TargetTags"),
            Allow=json_data.get("Allow"),
            Deny=json_data.get("Deny"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Allow:
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Allow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Allow"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Allow = Allow


@dataclass
class Deny:
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Deny"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deny"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deny = Deny


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


