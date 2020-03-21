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
    Configuration: Optional[Sequence["_Configuration"]]
    Name: Optional[str]
    Type: Optional[str]
    Config: Optional[Sequence["_Config"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Configuration=json_data.get("Configuration"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Config=json_data.get("Config"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Configuration:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


@dataclass
class Config:
    ApiKey: Optional[str]
    AuthPassword: Optional[str]
    AuthType: Optional[str]
    AuthUsername: Optional[str]
    BaseUrl: Optional[str]
    Channel: Optional[str]
    Headers: Optional[Sequence["_Headers"]]
    HeadersString: Optional[str]
    IncludeJsonAttachment: Optional[str]
    Key: Optional[str]
    Payload: Optional[Sequence["_Payload"]]
    PayloadString: Optional[str]
    PayloadType: Optional[str]
    Recipients: Optional[str]
    Region: Optional[str]
    RouteKey: Optional[str]
    ServiceKey: Optional[str]
    Tags: Optional[str]
    Teams: Optional[str]
    Url: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthType=json_data.get("AuthType"),
            AuthUsername=json_data.get("AuthUsername"),
            BaseUrl=json_data.get("BaseUrl"),
            Channel=json_data.get("Channel"),
            Headers=json_data.get("Headers"),
            HeadersString=json_data.get("HeadersString"),
            IncludeJsonAttachment=json_data.get("IncludeJsonAttachment"),
            Key=json_data.get("Key"),
            Payload=json_data.get("Payload"),
            PayloadString=json_data.get("PayloadString"),
            PayloadType=json_data.get("PayloadType"),
            Recipients=json_data.get("Recipients"),
            Region=json_data.get("Region"),
            RouteKey=json_data.get("RouteKey"),
            ServiceKey=json_data.get("ServiceKey"),
            Tags=json_data.get("Tags"),
            Teams=json_data.get("Teams"),
            Url=json_data.get("Url"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Headers:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class Payload:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Payload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Payload"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Payload = Payload


