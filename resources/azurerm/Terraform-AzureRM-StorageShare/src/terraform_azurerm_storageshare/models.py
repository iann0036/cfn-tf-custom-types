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
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Quota: Optional[float]
    StorageAccountName: Optional[str]
    Url: Optional[str]
    Acl: Optional[Sequence["_Acl"]]
    Timeouts: Optional["_Timeouts"]
    AccessPolicy: Optional[Sequence["_AccessPolicy"]]

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
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Quota=json_data.get("Quota"),
            StorageAccountName=json_data.get("StorageAccountName"),
            Url=json_data.get("Url"),
            Acl=json_data.get("Acl"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AccessPolicy=json_data.get("AccessPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Acl:
    Id: Optional[str]
    AccessPolicy: Optional[Sequence["_AccessPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_Acl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Acl"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            AccessPolicy=json_data.get("AccessPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Acl = Acl


@dataclass
class AccessPolicy:
    Expiry: Optional[str]
    Permissions: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicy"]:
        if not json_data:
            return None
        return cls(
            Expiry=json_data.get("Expiry"),
            Permissions=json_data.get("Permissions"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPolicy = AccessPolicy


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


