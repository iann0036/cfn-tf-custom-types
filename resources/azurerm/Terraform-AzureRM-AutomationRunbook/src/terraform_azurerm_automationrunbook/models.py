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
    AutomationAccountName: Optional[str]
    Content: Optional[str]
    Description: Optional[str]
    Location: Optional[str]
    LogProgress: Optional[bool]
    LogVerbose: Optional[bool]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    RunbookType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    PublishContentLink: Optional[Sequence["_PublishContentLink"]]
    Timeouts: Optional["_Timeouts"]
    Hash: Optional[Sequence["_Hash"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutomationAccountName=json_data.get("AutomationAccountName"),
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            Location=json_data.get("Location"),
            LogProgress=json_data.get("LogProgress"),
            LogVerbose=json_data.get("LogVerbose"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RunbookType=json_data.get("RunbookType"),
            Tags=json_data.get("Tags"),
            PublishContentLink=json_data.get("PublishContentLink"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Hash=json_data.get("Hash"),
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
class PublishContentLink:
    Uri: Optional[str]
    Version: Optional[str]
    Hash: Optional[Sequence["_Hash"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishContentLink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishContentLink"]:
        if not json_data:
            return None
        return cls(
            Uri=json_data.get("Uri"),
            Version=json_data.get("Version"),
            Hash=json_data.get("Hash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishContentLink = PublishContentLink


@dataclass
class Hash:
    Algorithm: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Hash"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hash"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hash = Hash


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


