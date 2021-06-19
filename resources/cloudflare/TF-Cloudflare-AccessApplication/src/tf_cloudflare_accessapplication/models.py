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
    AccountId: Optional[str]
    AllowedIdps: Optional[Sequence[str]]
    Aud: Optional[str]
    AutoRedirectToIdentity: Optional[bool]
    CustomDenyMessage: Optional[str]
    CustomDenyUrl: Optional[str]
    Domain: Optional[str]
    EnableBindingCookie: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    SessionDuration: Optional[str]
    ZoneId: Optional[str]
    CorsHeaders: Optional[Sequence["_CorsHeadersDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            AllowedIdps=json_data.get("AllowedIdps"),
            Aud=json_data.get("Aud"),
            AutoRedirectToIdentity=json_data.get("AutoRedirectToIdentity"),
            CustomDenyMessage=json_data.get("CustomDenyMessage"),
            CustomDenyUrl=json_data.get("CustomDenyUrl"),
            Domain=json_data.get("Domain"),
            EnableBindingCookie=json_data.get("EnableBindingCookie"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SessionDuration=json_data.get("SessionDuration"),
            ZoneId=json_data.get("ZoneId"),
            CorsHeaders=deserialize_list(json_data.get("CorsHeaders"), CorsHeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CorsHeadersDefinition(BaseModel):
    AllowAllHeaders: Optional[bool]
    AllowAllMethods: Optional[bool]
    AllowAllOrigins: Optional[bool]
    AllowCredentials: Optional[bool]
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    MaxAge: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowAllHeaders=json_data.get("AllowAllHeaders"),
            AllowAllMethods=json_data.get("AllowAllMethods"),
            AllowAllOrigins=json_data.get("AllowAllOrigins"),
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            MaxAge=json_data.get("MaxAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsHeadersDefinition = CorsHeadersDefinition


