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
    CookieName: Optional[str]
    Domain: Optional[str]
    DontHonorConnRules: Optional[float]
    EncryptLevel: Optional[float]
    Encrypted: Optional[str]
    Expire: Optional[float]
    Httponly: Optional[float]
    Id: Optional[str]
    InsertAlways: Optional[float]
    MatchType: Optional[float]
    Name: Optional[str]
    PassPhrase: Optional[str]
    PassThru: Optional[float]
    Path: Optional[str]
    ScanAllMembers: Optional[float]
    Secure: Optional[float]
    Server: Optional[float]
    ServerServiceGroup: Optional[float]
    ServiceGroup: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]

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
            CookieName=json_data.get("CookieName"),
            Domain=json_data.get("Domain"),
            DontHonorConnRules=json_data.get("DontHonorConnRules"),
            EncryptLevel=json_data.get("EncryptLevel"),
            Encrypted=json_data.get("Encrypted"),
            Expire=json_data.get("Expire"),
            Httponly=json_data.get("Httponly"),
            Id=json_data.get("Id"),
            InsertAlways=json_data.get("InsertAlways"),
            MatchType=json_data.get("MatchType"),
            Name=json_data.get("Name"),
            PassPhrase=json_data.get("PassPhrase"),
            PassThru=json_data.get("PassThru"),
            Path=json_data.get("Path"),
            ScanAllMembers=json_data.get("ScanAllMembers"),
            Secure=json_data.get("Secure"),
            Server=json_data.get("Server"),
            ServerServiceGroup=json_data.get("ServerServiceGroup"),
            ServiceGroup=json_data.get("ServiceGroup"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


