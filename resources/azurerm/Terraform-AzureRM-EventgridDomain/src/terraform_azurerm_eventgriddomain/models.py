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
    Endpoint: Optional[str]
    Id: Optional[str]
    InputSchema: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    InputMappingDefaultValues: Optional[Sequence["_InputMappingDefaultValues"]]
    InputMappingFields: Optional[Sequence["_InputMappingFields"]]
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
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            InputSchema=json_data.get("InputSchema"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            Tags=json_data.get("Tags"),
            InputMappingDefaultValues=json_data.get("InputMappingDefaultValues"),
            InputMappingFields=json_data.get("InputMappingFields"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class InputMappingDefaultValues:
    DataVersion: Optional[str]
    EventType: Optional[str]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputMappingDefaultValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputMappingDefaultValues"]:
        if not json_data:
            return None
        return cls(
            DataVersion=json_data.get("DataVersion"),
            EventType=json_data.get("EventType"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputMappingDefaultValues = InputMappingDefaultValues


@dataclass
class InputMappingFields:
    DataVersion: Optional[str]
    EventTime: Optional[str]
    EventType: Optional[str]
    Id: Optional[str]
    Subject: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputMappingFields"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputMappingFields"]:
        if not json_data:
            return None
        return cls(
            DataVersion=json_data.get("DataVersion"),
            EventTime=json_data.get("EventTime"),
            EventType=json_data.get("EventType"),
            Id=json_data.get("Id"),
            Subject=json_data.get("Subject"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputMappingFields = InputMappingFields


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


