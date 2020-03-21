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
    Curve: Optional[str]
    E: Optional[str]
    ExpirationDate: Optional[str]
    Id: Optional[str]
    KeyOpts: Optional[Sequence[str]]
    KeySize: Optional[float]
    KeyType: Optional[str]
    KeyVaultId: Optional[str]
    N: Optional[str]
    Name: Optional[str]
    NotBeforeDate: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    X: Optional[str]
    Y: Optional[str]
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
            Curve=json_data.get("Curve"),
            E=json_data.get("E"),
            ExpirationDate=json_data.get("ExpirationDate"),
            Id=json_data.get("Id"),
            KeyOpts=json_data.get("KeyOpts"),
            KeySize=json_data.get("KeySize"),
            KeyType=json_data.get("KeyType"),
            KeyVaultId=json_data.get("KeyVaultId"),
            N=json_data.get("N"),
            Name=json_data.get("Name"),
            NotBeforeDate=json_data.get("NotBeforeDate"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            X=json_data.get("X"),
            Y=json_data.get("Y"),
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


