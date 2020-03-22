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
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    Items: Optional[Sequence["_Items"]]
    Timeouts: Optional["_Timeouts"]
    Conditions: Optional[Sequence["_Conditions"]]
    RedirectUri: Optional[Sequence["_RedirectUri"]]

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
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Items=json_data.get("Items"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Conditions=json_data.get("Conditions"),
            RedirectUri=json_data.get("RedirectUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Items:
    Action: Optional[str]
    AllowedMethods: Optional[Sequence[str]]
    Description: Optional[str]
    Header: Optional[str]
    Prefix: Optional[str]
    ResponseCode: Optional[float]
    StatusCode: Optional[float]
    Suffix: Optional[str]
    Value: Optional[str]
    Conditions: Optional[Sequence["_Conditions"]]
    RedirectUri: Optional[Sequence["_RedirectUri"]]

    @classmethod
    def _deserialize(
        cls: Type["_Items"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Items"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AllowedMethods=json_data.get("AllowedMethods"),
            Description=json_data.get("Description"),
            Header=json_data.get("Header"),
            Prefix=json_data.get("Prefix"),
            ResponseCode=json_data.get("ResponseCode"),
            StatusCode=json_data.get("StatusCode"),
            Suffix=json_data.get("Suffix"),
            Value=json_data.get("Value"),
            Conditions=json_data.get("Conditions"),
            RedirectUri=json_data.get("RedirectUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Items = Items


@dataclass
class Conditions:
    AttributeName: Optional[str]
    AttributeValue: Optional[str]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValue=json_data.get("AttributeValue"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class RedirectUri:
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectUri"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectUri"]:
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
_RedirectUri = RedirectUri


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


