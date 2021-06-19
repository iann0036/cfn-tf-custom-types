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
    Endpoint: Optional[str]
    Id: Optional[str]
    InboundIpRule: Optional[Sequence["_InboundIpRuleDefinition"]]
    InputSchema: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    InputMappingDefaultValues: Optional[Sequence["_InputMappingDefaultValuesDefinition"]]
    InputMappingFields: Optional[Sequence["_InputMappingFieldsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            InboundIpRule=deserialize_list(json_data.get("InboundIpRule"), InboundIpRuleDefinition),
            InputSchema=json_data.get("InputSchema"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            InputMappingDefaultValues=deserialize_list(json_data.get("InputMappingDefaultValues"), InputMappingDefaultValuesDefinition),
            InputMappingFields=deserialize_list(json_data.get("InputMappingFields"), InputMappingFieldsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InboundIpRuleDefinition(BaseModel):
    Action: Optional[str]
    IpMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundIpRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundIpRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpMask=json_data.get("IpMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundIpRuleDefinition = InboundIpRuleDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class InputMappingDefaultValuesDefinition(BaseModel):
    DataVersion: Optional[str]
    EventType: Optional[str]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputMappingDefaultValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputMappingDefaultValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            DataVersion=json_data.get("DataVersion"),
            EventType=json_data.get("EventType"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputMappingDefaultValuesDefinition = InputMappingDefaultValuesDefinition


@dataclass
class InputMappingFieldsDefinition(BaseModel):
    DataVersion: Optional[str]
    EventTime: Optional[str]
    EventType: Optional[str]
    Id: Optional[str]
    Subject: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputMappingFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputMappingFieldsDefinition"]:
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
_InputMappingFieldsDefinition = InputMappingFieldsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


