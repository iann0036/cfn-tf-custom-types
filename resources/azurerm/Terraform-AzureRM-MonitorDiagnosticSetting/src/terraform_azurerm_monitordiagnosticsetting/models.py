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
    EventhubAuthorizationRuleId: Optional[str]
    EventhubName: Optional[str]
    Id: Optional[str]
    LogAnalyticsDestinationType: Optional[str]
    LogAnalyticsWorkspaceId: Optional[str]
    Name: Optional[str]
    StorageAccountId: Optional[str]
    TargetResourceId: Optional[str]
    Log: Optional[Sequence["_Log"]]
    Metric: Optional[Sequence["_Metric"]]
    Timeouts: Optional["_Timeouts"]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EventhubAuthorizationRuleId=json_data.get("EventhubAuthorizationRuleId"),
            EventhubName=json_data.get("EventhubName"),
            Id=json_data.get("Id"),
            LogAnalyticsDestinationType=json_data.get("LogAnalyticsDestinationType"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
            Name=json_data.get("Name"),
            StorageAccountId=json_data.get("StorageAccountId"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Log=json_data.get("Log"),
            Metric=json_data.get("Metric"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            RetentionPolicy=json_data.get("RetentionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Log:
    Category: Optional[str]
    Enabled: Optional[bool]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_Log"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Log"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Enabled=json_data.get("Enabled"),
            RetentionPolicy=json_data.get("RetentionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Log = Log


@dataclass
class RetentionPolicy:
    Days: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicy"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicy = RetentionPolicy


@dataclass
class Metric:
    Category: Optional[str]
    Enabled: Optional[bool]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Enabled=json_data.get("Enabled"),
            RetentionPolicy=json_data.get("RetentionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


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


