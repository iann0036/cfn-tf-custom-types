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
    AllowWriteAccess: Optional[bool]
    ApiKey: Optional[str]
    Enabled: Optional[bool]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Id: Optional[str]
    IgnoreRespondersFromPayload: Optional[bool]
    Name: Optional[str]
    OwnerTeamId: Optional[str]
    SuppressNotifications: Optional[bool]
    Type: Optional[str]
    WebhookUrl: Optional[str]
    Responders: Optional[Sequence["_RespondersDefinition"]]

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
            AllowWriteAccess=json_data.get("AllowWriteAccess"),
            ApiKey=json_data.get("ApiKey"),
            Enabled=json_data.get("Enabled"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Id=json_data.get("Id"),
            IgnoreRespondersFromPayload=json_data.get("IgnoreRespondersFromPayload"),
            Name=json_data.get("Name"),
            OwnerTeamId=json_data.get("OwnerTeamId"),
            SuppressNotifications=json_data.get("SuppressNotifications"),
            Type=json_data.get("Type"),
            WebhookUrl=json_data.get("WebhookUrl"),
            Responders=deserialize_list(json_data.get("Responders"), RespondersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


