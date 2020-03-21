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
    IpVersion: Optional[str]
    Name: Optional[str]
    ResourceGroupId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    EntryList: Optional[Sequence["_EntryList"]]

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
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Tags=json_data.get("Tags"),
            EntryList=json_data.get("EntryList"),
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
class EntryList:
    Comment: Optional[str]
    Entry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntryList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntryList"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Entry=json_data.get("Entry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntryList = EntryList


