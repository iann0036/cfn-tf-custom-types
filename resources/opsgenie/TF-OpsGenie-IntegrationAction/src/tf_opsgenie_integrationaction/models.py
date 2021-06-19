# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Id: Optional[str]
    IntegrationId: Optional[str]
    Acknowledge: Optional[Sequence["_AcknowledgeDefinition"]]
    AddNote: Optional[Sequence["_AddNoteDefinition"]]
    Close: Optional[Sequence["_CloseDefinition"]]
    Create: Optional[Sequence["_CreateDefinition"]]
    Ignore: Optional[Sequence["_IgnoreDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            IntegrationId=json_data.get("IntegrationId"),
            Acknowledge=deserialize_list(json_data.get("Acknowledge"), AcknowledgeDefinition),
            AddNote=deserialize_list(json_data.get("AddNote"), AddNoteDefinition),
            Close=deserialize_list(json_data.get("Close"), CloseDefinition),
            Create=deserialize_list(json_data.get("Create"), CreateDefinition),
            Ignore=deserialize_list(json_data.get("Ignore"), IgnoreDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AcknowledgeDefinition(BaseModel):
    Alias: Optional[str]
    Name: Optional[str]
    Note: Optional[str]
    Order: Optional[float]
    Type: Optional[str]
    User: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AcknowledgeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcknowledgeDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            Name=json_data.get("Name"),
            Note=json_data.get("Note"),
            Order=json_data.get("Order"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcknowledgeDefinition = AcknowledgeDefinition


@dataclass
class FilterDefinition(BaseModel):
    Type: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    ExpectedValue: Optional[str]
    Field: Optional[str]
    Key: Optional[str]
    Not: Optional[bool]
    Operation: Optional[str]
    Order: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedValue=json_data.get("ExpectedValue"),
            Field=json_data.get("Field"),
            Key=json_data.get("Key"),
            Not=json_data.get("Not"),
            Operation=json_data.get("Operation"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class AddNoteDefinition(BaseModel):
    Alias: Optional[str]
    Name: Optional[str]
    Note: Optional[str]
    Order: Optional[float]
    Type: Optional[str]
    User: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AddNoteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddNoteDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            Name=json_data.get("Name"),
            Note=json_data.get("Note"),
            Order=json_data.get("Order"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddNoteDefinition = AddNoteDefinition


@dataclass
class CloseDefinition(BaseModel):
    Alias: Optional[str]
    Name: Optional[str]
    Note: Optional[str]
    Order: Optional[float]
    Type: Optional[str]
    User: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloseDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            Name=json_data.get("Name"),
            Note=json_data.get("Note"),
            Order=json_data.get("Order"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloseDefinition = CloseDefinition


@dataclass
class CreateDefinition(BaseModel):
    AlertActions: Optional[Sequence[str]]
    Alias: Optional[str]
    AppendAttachments: Optional[bool]
    CustomPriority: Optional[str]
    Description: Optional[str]
    Entity: Optional[str]
    ExtraProperties: Optional[Sequence["_ExtraPropertiesDefinition"]]
    IgnoreAlertActionsFromPayload: Optional[bool]
    IgnoreExtraPropertiesFromPayload: Optional[bool]
    IgnoreRespondersFromPayload: Optional[bool]
    IgnoreTagsFromPayload: Optional[bool]
    IgnoreTeamsFromPayload: Optional[bool]
    Message: Optional[str]
    Name: Optional[str]
    Note: Optional[str]
    Order: Optional[float]
    Priority: Optional[str]
    Source: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    User: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Responders: Optional[Sequence["_RespondersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertActions=json_data.get("AlertActions"),
            Alias=json_data.get("Alias"),
            AppendAttachments=json_data.get("AppendAttachments"),
            CustomPriority=json_data.get("CustomPriority"),
            Description=json_data.get("Description"),
            Entity=json_data.get("Entity"),
            ExtraProperties=deserialize_list(json_data.get("ExtraProperties"), ExtraPropertiesDefinition),
            IgnoreAlertActionsFromPayload=json_data.get("IgnoreAlertActionsFromPayload"),
            IgnoreExtraPropertiesFromPayload=json_data.get("IgnoreExtraPropertiesFromPayload"),
            IgnoreRespondersFromPayload=json_data.get("IgnoreRespondersFromPayload"),
            IgnoreTagsFromPayload=json_data.get("IgnoreTagsFromPayload"),
            IgnoreTeamsFromPayload=json_data.get("IgnoreTeamsFromPayload"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Note=json_data.get("Note"),
            Order=json_data.get("Order"),
            Priority=json_data.get("Priority"),
            Source=json_data.get("Source"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Responders=deserialize_list(json_data.get("Responders"), RespondersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateDefinition = CreateDefinition


@dataclass
class ExtraPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraPropertiesDefinition = ExtraPropertiesDefinition


@dataclass
class RespondersDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RespondersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RespondersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RespondersDefinition = RespondersDefinition


@dataclass
class IgnoreDefinition(BaseModel):
    Name: Optional[str]
    Order: Optional[float]
    Type: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IgnoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IgnoreDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            Type=json_data.get("Type"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IgnoreDefinition = IgnoreDefinition


