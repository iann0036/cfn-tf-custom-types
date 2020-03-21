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
    Endpoint: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryReadKey: Optional[Sequence["_PrimaryReadKey"]]
    PrimaryWriteKey: Optional[Sequence["_PrimaryWriteKey"]]
    ResourceGroupName: Optional[str]
    SecondaryReadKey: Optional[Sequence["_SecondaryReadKey"]]
    SecondaryWriteKey: Optional[Sequence["_SecondaryWriteKey"]]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
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
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryReadKey=json_data.get("PrimaryReadKey"),
            PrimaryWriteKey=json_data.get("PrimaryWriteKey"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryReadKey=json_data.get("SecondaryReadKey"),
            SecondaryWriteKey=json_data.get("SecondaryWriteKey"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrimaryReadKey:
    ConnectionString: Optional[str]
    Id: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryReadKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryReadKey"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Id=json_data.get("Id"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryReadKey = PrimaryReadKey


@dataclass
class PrimaryWriteKey:
    ConnectionString: Optional[str]
    Id: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryWriteKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryWriteKey"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Id=json_data.get("Id"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryWriteKey = PrimaryWriteKey


@dataclass
class SecondaryReadKey:
    ConnectionString: Optional[str]
    Id: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryReadKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryReadKey"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Id=json_data.get("Id"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryReadKey = SecondaryReadKey


@dataclass
class SecondaryWriteKey:
    ConnectionString: Optional[str]
    Id: Optional[str]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryWriteKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryWriteKey"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Id=json_data.get("Id"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryWriteKey = SecondaryWriteKey


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


