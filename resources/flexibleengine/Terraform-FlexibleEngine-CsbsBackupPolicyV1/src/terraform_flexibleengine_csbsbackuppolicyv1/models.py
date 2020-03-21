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
    Common: Optional[Sequence["_Common"]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProviderId: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Resource: Optional[Sequence["_Resource"]]
    ScheduledOperation: Optional[Sequence["_ScheduledOperation"]]
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
            Common=json_data.get("Common"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProviderId=json_data.get("ProviderId"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Resource=json_data.get("Resource"),
            ScheduledOperation=json_data.get("ScheduledOperation"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Common:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Common"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Common"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Common = Common


@dataclass
class Resource:
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Resource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resource"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resource = Resource


@dataclass
class ScheduledOperation:
    Description: Optional[str]
    Enabled: Optional[bool]
    MaxBackups: Optional[float]
    Name: Optional[str]
    OperationType: Optional[str]
    Permanent: Optional[bool]
    RetentionDurationDays: Optional[float]
    TriggerPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledOperation"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            MaxBackups=json_data.get("MaxBackups"),
            Name=json_data.get("Name"),
            OperationType=json_data.get("OperationType"),
            Permanent=json_data.get("Permanent"),
            RetentionDurationDays=json_data.get("RetentionDurationDays"),
            TriggerPattern=json_data.get("TriggerPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledOperation = ScheduledOperation


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


