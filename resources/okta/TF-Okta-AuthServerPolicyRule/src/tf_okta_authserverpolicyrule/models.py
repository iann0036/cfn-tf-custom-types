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
    AccessTokenLifetimeMinutes: Optional[float]
    AuthServerId: Optional[str]
    GrantTypeWhitelist: Optional[Sequence[str]]
    GroupBlacklist: Optional[Sequence[str]]
    GroupWhitelist: Optional[Sequence[str]]
    Id: Optional[str]
    InlineHookId: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    Priority: Optional[float]
    RefreshTokenLifetimeMinutes: Optional[float]
    RefreshTokenWindowMinutes: Optional[float]
    ScopeWhitelist: Optional[Sequence[str]]
    Status: Optional[str]
    Type: Optional[str]
    UserBlacklist: Optional[Sequence[str]]
    UserWhitelist: Optional[Sequence[str]]

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
            AccessTokenLifetimeMinutes=json_data.get("AccessTokenLifetimeMinutes"),
            AuthServerId=json_data.get("AuthServerId"),
            GrantTypeWhitelist=json_data.get("GrantTypeWhitelist"),
            GroupBlacklist=json_data.get("GroupBlacklist"),
            GroupWhitelist=json_data.get("GroupWhitelist"),
            Id=json_data.get("Id"),
            InlineHookId=json_data.get("InlineHookId"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            Priority=json_data.get("Priority"),
            RefreshTokenLifetimeMinutes=json_data.get("RefreshTokenLifetimeMinutes"),
            RefreshTokenWindowMinutes=json_data.get("RefreshTokenWindowMinutes"),
            ScopeWhitelist=json_data.get("ScopeWhitelist"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            UserBlacklist=json_data.get("UserBlacklist"),
            UserWhitelist=json_data.get("UserWhitelist"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


