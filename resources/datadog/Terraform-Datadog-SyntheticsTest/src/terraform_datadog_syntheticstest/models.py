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
    Assertions: Optional[Sequence[Sequence["_Assertions"]]]
    DeviceIds: Optional[Sequence[str]]
    Locations: Optional[Sequence[str]]
    Message: Optional[str]
    MonitorId: Optional[float]
    Name: Optional[str]
    Options: Optional[Sequence["_Options"]]
    Request: Optional[Sequence["_Request"]]
    RequestHeaders: Optional[Sequence["_RequestHeaders"]]
    Status: Optional[str]
    Subtype: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Assertions=json_data.get("Assertions"),
            DeviceIds=json_data.get("DeviceIds"),
            Locations=json_data.get("Locations"),
            Message=json_data.get("Message"),
            MonitorId=json_data.get("MonitorId"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            Request=json_data.get("Request"),
            RequestHeaders=json_data.get("RequestHeaders"),
            Status=json_data.get("Status"),
            Subtype=json_data.get("Subtype"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Assertions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Assertions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Assertions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Assertions = Assertions


@dataclass
class Options:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Request:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Request"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Request"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Request = Request


@dataclass
class RequestHeaders:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaders"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaders = RequestHeaders


