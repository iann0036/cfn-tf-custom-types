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
    Adaptive: Optional[str]
    AdaptiveLimit: Optional[float]
    Compatibility: Optional[str]
    Database: Optional[str]
    DefaultsFrom: Optional[str]
    Destination: Optional[str]
    Filename: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    IpDscp: Optional[float]
    ManualResume: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    Password: Optional[str]
    Receive: Optional[str]
    ReceiveDisable: Optional[str]
    Reverse: Optional[str]
    Send: Optional[str]
    TimeUntilUp: Optional[float]
    Timeout: Optional[float]
    Transparent: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Adaptive=json_data.get("Adaptive"),
            AdaptiveLimit=json_data.get("AdaptiveLimit"),
            Compatibility=json_data.get("Compatibility"),
            Database=json_data.get("Database"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            Destination=json_data.get("Destination"),
            Filename=json_data.get("Filename"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            IpDscp=json_data.get("IpDscp"),
            ManualResume=json_data.get("ManualResume"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            Password=json_data.get("Password"),
            Receive=json_data.get("Receive"),
            ReceiveDisable=json_data.get("ReceiveDisable"),
            Reverse=json_data.get("Reverse"),
            Send=json_data.get("Send"),
            TimeUntilUp=json_data.get("TimeUntilUp"),
            Timeout=json_data.get("Timeout"),
            Transparent=json_data.get("Transparent"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


