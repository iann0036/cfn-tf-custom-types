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
    Consumers: Optional[Sequence["_Consumers"]]
    ContainerRef: Optional[str]
    CreatedAt: Optional[str]
    CreatorId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    UpdatedAt: Optional[str]
    Acl: Optional[Sequence["_Acl"]]
    SecretRefs: Optional[Sequence["_SecretRefs"]]
    Timeouts: Optional["_Timeouts"]
    Read: Optional[Sequence["_Read"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Consumers=json_data.get("Consumers"),
            ContainerRef=json_data.get("ContainerRef"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatorId=json_data.get("CreatorId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Acl=json_data.get("Acl"),
            SecretRefs=json_data.get("SecretRefs"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Consumers:
    Name: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Consumers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Consumers"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Consumers = Consumers


@dataclass
class Acl:
    Read: Optional[Sequence["_Read"]]

    @classmethod
    def _deserialize(
        cls: Type["_Acl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Acl"]:
        if not json_data:
            return None
        return cls(
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Acl = Acl


@dataclass
class Read:
    ProjectAccess: Optional[bool]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Read"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Read"]:
        if not json_data:
            return None
        return cls(
            ProjectAccess=json_data.get("ProjectAccess"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Read = Read


@dataclass
class SecretRefs:
    Name: Optional[str]
    SecretRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRefs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRefs"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRefs = SecretRefs


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


