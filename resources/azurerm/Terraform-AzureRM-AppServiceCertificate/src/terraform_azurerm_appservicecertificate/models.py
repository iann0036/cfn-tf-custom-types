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
    ExpirationDate: Optional[str]
    FriendlyName: Optional[str]
    HostNames: Optional[Sequence[str]]
    Id: Optional[str]
    IssueDate: Optional[str]
    Issuer: Optional[str]
    KeyVaultSecretId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PfxBlob: Optional[str]
    ResourceGroupName: Optional[str]
    SubjectName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Thumbprint: Optional[str]
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
            ExpirationDate=json_data.get("ExpirationDate"),
            FriendlyName=json_data.get("FriendlyName"),
            HostNames=json_data.get("HostNames"),
            Id=json_data.get("Id"),
            IssueDate=json_data.get("IssueDate"),
            Issuer=json_data.get("Issuer"),
            KeyVaultSecretId=json_data.get("KeyVaultSecretId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PfxBlob=json_data.get("PfxBlob"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SubjectName=json_data.get("SubjectName"),
            Tags=json_data.get("Tags"),
            Thumbprint=json_data.get("Thumbprint"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


