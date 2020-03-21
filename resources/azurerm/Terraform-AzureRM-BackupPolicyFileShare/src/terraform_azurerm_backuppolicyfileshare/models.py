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
    Name: Optional[str]
    RecoveryVaultName: Optional[str]
    ResourceGroupName: Optional[str]
    Timezone: Optional[str]
    Backup: Optional[Sequence["_Backup"]]
    RetentionDaily: Optional[Sequence["_RetentionDaily"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RecoveryVaultName=json_data.get("RecoveryVaultName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Timezone=json_data.get("Timezone"),
            Backup=json_data.get("Backup"),
            RetentionDaily=json_data.get("RetentionDaily"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backup:
    Frequency: Optional[str]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Backup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backup"]:
        if not json_data:
            return None
        return cls(
            Frequency=json_data.get("Frequency"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backup = Backup


@dataclass
class RetentionDaily:
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionDaily"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionDaily"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionDaily = RetentionDaily


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


