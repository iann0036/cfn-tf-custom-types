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
    AlwaysSend: Optional[str]
    AppService: Optional[str]
    CookieEncryption: Optional[str]
    CookieEncryptionPassphrase: Optional[str]
    CookieName: Optional[str]
    DefaultsFrom: Optional[str]
    Expiration: Optional[str]
    HashLength: Optional[float]
    HashOffset: Optional[float]
    Httponly: Optional[str]
    Id: Optional[str]
    MatchAcrossPools: Optional[str]
    MatchAcrossServices: Optional[str]
    MatchAcrossVirtuals: Optional[str]
    Method: Optional[str]
    Mirror: Optional[str]
    Name: Optional[str]
    OverrideConnLimit: Optional[str]
    Timeout: Optional[float]

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
            AlwaysSend=json_data.get("AlwaysSend"),
            AppService=json_data.get("AppService"),
            CookieEncryption=json_data.get("CookieEncryption"),
            CookieEncryptionPassphrase=json_data.get("CookieEncryptionPassphrase"),
            CookieName=json_data.get("CookieName"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            Expiration=json_data.get("Expiration"),
            HashLength=json_data.get("HashLength"),
            HashOffset=json_data.get("HashOffset"),
            Httponly=json_data.get("Httponly"),
            Id=json_data.get("Id"),
            MatchAcrossPools=json_data.get("MatchAcrossPools"),
            MatchAcrossServices=json_data.get("MatchAcrossServices"),
            MatchAcrossVirtuals=json_data.get("MatchAcrossVirtuals"),
            Method=json_data.get("Method"),
            Mirror=json_data.get("Mirror"),
            Name=json_data.get("Name"),
            OverrideConnLimit=json_data.get("OverrideConnLimit"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

