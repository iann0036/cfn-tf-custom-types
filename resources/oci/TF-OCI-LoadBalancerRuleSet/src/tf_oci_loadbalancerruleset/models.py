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
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    Items: Optional[Sequence["_ItemsDefinition"]]
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
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ItemsDefinition(BaseModel):
    Action: Optional[str]
    AllowedMethods: Optional[Sequence[str]]
    AreInvalidCharactersAllowed: Optional[bool]
    Description: Optional[str]
    Header: Optional[str]
    HttpLargeHeaderSizeInKb: Optional[float]
    Prefix: Optional[str]
    ResponseCode: Optional[float]
    StatusCode: Optional[float]
    Suffix: Optional[str]
    Value: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    RedirectUri: Optional[Sequence["_RedirectUriDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AreInvalidCharactersAllowed=json_data.get("AreInvalidCharactersAllowed"),
            Description=json_data.get("Description"),
            Header=json_data.get("Header"),
            HttpLargeHeaderSizeInKb=json_data.get("HttpLargeHeaderSizeInKb"),
            Prefix=json_data.get("Prefix"),
            ResponseCode=json_data.get("ResponseCode"),
            StatusCode=json_data.get("StatusCode"),
            Suffix=json_data.get("Suffix"),
            Value=json_data.get("Value"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            RedirectUri=deserialize_list(json_data.get("RedirectUri"), RedirectUriDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsDefinition = ItemsDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    AttributeName: Optional[str]
    AttributeValue: Optional[str]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValue=json_data.get("AttributeValue"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class RedirectUriDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectUriDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectUriDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectUriDefinition = RedirectUriDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


