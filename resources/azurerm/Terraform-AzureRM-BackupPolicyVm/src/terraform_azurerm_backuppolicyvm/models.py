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
    Tags: Optional[Sequence["_Tags"]]
    Timezone: Optional[str]
    Backup: Optional[Sequence["_Backup"]]
    RetentionDaily: Optional[Sequence["_RetentionDaily"]]
    RetentionMonthly: Optional[Sequence["_RetentionMonthly"]]
    RetentionWeekly: Optional[Sequence["_RetentionWeekly"]]
    RetentionYearly: Optional[Sequence["_RetentionYearly"]]
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
            Tags=json_data.get("Tags"),
            Timezone=json_data.get("Timezone"),
            Backup=json_data.get("Backup"),
            RetentionDaily=json_data.get("RetentionDaily"),
            RetentionMonthly=json_data.get("RetentionMonthly"),
            RetentionWeekly=json_data.get("RetentionWeekly"),
            RetentionYearly=json_data.get("RetentionYearly"),
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
class Backup:
    Frequency: Optional[str]
    Time: Optional[str]
    Weekdays: Optional[Sequence[str]]

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
            Weekdays=json_data.get("Weekdays"),
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
class RetentionMonthly:
    Count: Optional[float]
    Weekdays: Optional[Sequence[str]]
    Weeks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionMonthly"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionMonthly"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Weekdays=json_data.get("Weekdays"),
            Weeks=json_data.get("Weeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionMonthly = RetentionMonthly


@dataclass
class RetentionWeekly:
    Count: Optional[float]
    Weekdays: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionWeekly"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionWeekly"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Weekdays=json_data.get("Weekdays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionWeekly = RetentionWeekly


@dataclass
class RetentionYearly:
    Count: Optional[float]
    Months: Optional[Sequence[str]]
    Weekdays: Optional[Sequence[str]]
    Weeks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionYearly"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionYearly"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Months=json_data.get("Months"),
            Weekdays=json_data.get("Weekdays"),
            Weeks=json_data.get("Weeks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionYearly = RetentionYearly


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


