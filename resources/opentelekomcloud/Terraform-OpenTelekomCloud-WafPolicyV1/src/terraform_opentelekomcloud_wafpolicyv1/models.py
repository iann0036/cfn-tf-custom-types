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
    FullDetection: Optional[bool]
    Hosts: Optional[Sequence[str]]
    Id: Optional[str]
    Level: Optional[float]
    Name: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Options: Optional[Sequence["_Options"]]
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
            FullDetection=json_data.get("FullDetection"),
            Hosts=json_data.get("Hosts"),
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
            Name=json_data.get("Name"),
            Action=json_data.get("Action"),
            Options=json_data.get("Options"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Action:
    Category: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Options:
    Antitamper: Optional[bool]
    Cc: Optional[bool]
    Common: Optional[bool]
    Crawler: Optional[bool]
    CrawlerEngine: Optional[bool]
    CrawlerOther: Optional[bool]
    CrawlerScanner: Optional[bool]
    CrawlerScript: Optional[bool]
    Custom: Optional[bool]
    Ignore: Optional[bool]
    Privacy: Optional[bool]
    Webattack: Optional[bool]
    Webshell: Optional[bool]
    Whiteblackip: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Antitamper=json_data.get("Antitamper"),
            Cc=json_data.get("Cc"),
            Common=json_data.get("Common"),
            Crawler=json_data.get("Crawler"),
            CrawlerEngine=json_data.get("CrawlerEngine"),
            CrawlerOther=json_data.get("CrawlerOther"),
            CrawlerScanner=json_data.get("CrawlerScanner"),
            CrawlerScript=json_data.get("CrawlerScript"),
            Custom=json_data.get("Custom"),
            Ignore=json_data.get("Ignore"),
            Privacy=json_data.get("Privacy"),
            Webattack=json_data.get("Webattack"),
            Webshell=json_data.get("Webshell"),
            Whiteblackip=json_data.get("Whiteblackip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


