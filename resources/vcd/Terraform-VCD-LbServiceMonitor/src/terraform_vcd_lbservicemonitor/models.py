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
    EdgeGateway: Optional[str]
    Expected: Optional[str]
    Extension: Optional[Sequence["_Extension"]]
    Interval: Optional[float]
    MaxRetries: Optional[float]
    Method: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Receive: Optional[str]
    Send: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    Url: Optional[str]
    Vdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Expected=json_data.get("Expected"),
            Extension=json_data.get("Extension"),
            Interval=json_data.get("Interval"),
            MaxRetries=json_data.get("MaxRetries"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Receive=json_data.get("Receive"),
            Send=json_data.get("Send"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Extension:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Extension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Extension"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Extension = Extension


