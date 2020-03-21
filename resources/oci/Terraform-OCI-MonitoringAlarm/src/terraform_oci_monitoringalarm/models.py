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
    Body: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Destinations: Optional[Sequence[str]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    IsEnabled: Optional[bool]
    MetricCompartmentId: Optional[str]
    MetricCompartmentIdInSubtree: Optional[bool]
    Namespace: Optional[str]
    PendingDuration: Optional[str]
    Query: Optional[str]
    RepeatNotificationDuration: Optional[str]
    Resolution: Optional[str]
    ResourceGroup: Optional[str]
    Severity: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Suppression: Optional[Sequence["_Suppression"]]
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
            Body=json_data.get("Body"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            Destinations=json_data.get("Destinations"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            IsEnabled=json_data.get("IsEnabled"),
            MetricCompartmentId=json_data.get("MetricCompartmentId"),
            MetricCompartmentIdInSubtree=json_data.get("MetricCompartmentIdInSubtree"),
            Namespace=json_data.get("Namespace"),
            PendingDuration=json_data.get("PendingDuration"),
            Query=json_data.get("Query"),
            RepeatNotificationDuration=json_data.get("RepeatNotificationDuration"),
            Resolution=json_data.get("Resolution"),
            ResourceGroup=json_data.get("ResourceGroup"),
            Severity=json_data.get("Severity"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Suppression=json_data.get("Suppression"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Suppression:
    Description: Optional[str]
    TimeSuppressFrom: Optional[str]
    TimeSuppressUntil: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Suppression"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Suppression"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            TimeSuppressFrom=json_data.get("TimeSuppressFrom"),
            TimeSuppressUntil=json_data.get("TimeSuppressUntil"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Suppression = Suppression


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


