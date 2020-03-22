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
    Algorithm: Optional[str]
    AllMetadata: Optional[Sequence["_AllMetadata"]]
    BitLength: Optional[float]
    ContentTypes: Optional[Sequence["_ContentTypes"]]
    CreatedAt: Optional[str]
    CreatorId: Optional[str]
    Expiration: Optional[str]
    Id: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Mode: Optional[str]
    Name: Optional[str]
    Payload: Optional[str]
    PayloadContentEncoding: Optional[str]
    PayloadContentType: Optional[str]
    Region: Optional[str]
    SecretRef: Optional[str]
    SecretType: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]
    Acl: Optional[Sequence["_Acl"]]
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
            Algorithm=json_data.get("Algorithm"),
            AllMetadata=json_data.get("AllMetadata"),
            BitLength=json_data.get("BitLength"),
            ContentTypes=json_data.get("ContentTypes"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatorId=json_data.get("CreatorId"),
            Expiration=json_data.get("Expiration"),
            Id=json_data.get("Id"),
            Metadata=json_data.get("Metadata"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Payload=json_data.get("Payload"),
            PayloadContentEncoding=json_data.get("PayloadContentEncoding"),
            PayloadContentType=json_data.get("PayloadContentType"),
            Region=json_data.get("Region"),
            SecretRef=json_data.get("SecretRef"),
            SecretType=json_data.get("SecretType"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Acl=json_data.get("Acl"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllMetadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllMetadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllMetadata = AllMetadata


@dataclass
class ContentTypes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentTypes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentTypes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentTypes = ContentTypes


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


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


