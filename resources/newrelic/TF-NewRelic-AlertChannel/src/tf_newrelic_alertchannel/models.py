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
    Name: Optional[str]
    Type: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]

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
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    ApiKey: Optional[str]
    AuthPassword: Optional[str]
    AuthType: Optional[str]
    AuthUsername: Optional[str]
    BaseUrl: Optional[str]
    Channel: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HeadersString: Optional[str]
    IncludeJsonAttachment: Optional[str]
    Key: Optional[str]
    Payload: Optional[Sequence["_PayloadDefinition"]]
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
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthType=json_data.get("AuthType"),
            AuthUsername=json_data.get("AuthUsername"),
            BaseUrl=json_data.get("BaseUrl"),
            Channel=json_data.get("Channel"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HeadersString=json_data.get("HeadersString"),
            IncludeJsonAttachment=json_data.get("IncludeJsonAttachment"),
            Key=json_data.get("Key"),
            Payload=deserialize_list(json_data.get("Payload"), PayloadDefinition),
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
_ConfigDefinition = ConfigDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class PayloadDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PayloadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PayloadDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PayloadDefinition = PayloadDefinition


