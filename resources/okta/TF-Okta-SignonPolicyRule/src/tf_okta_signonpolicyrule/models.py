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
    Access: Optional[str]
    Authtype: Optional[str]
    Id: Optional[str]
    MfaLifetime: Optional[float]
    MfaPrompt: Optional[str]
    MfaRememberDevice: Optional[bool]
    MfaRequired: Optional[bool]
    Name: Optional[str]
    NetworkConnection: Optional[str]
    NetworkExcludes: Optional[Sequence[str]]
    NetworkIncludes: Optional[Sequence[str]]
    Policyid: Optional[str]
    Priority: Optional[float]
    SessionIdle: Optional[float]
    SessionLifetime: Optional[float]
    SessionPersistent: Optional[bool]
    Status: Optional[str]
    UsersExcluded: Optional[Sequence[str]]

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
            Access=json_data.get("Access"),
            Authtype=json_data.get("Authtype"),
            Id=json_data.get("Id"),
            MfaLifetime=json_data.get("MfaLifetime"),
            MfaPrompt=json_data.get("MfaPrompt"),
            MfaRememberDevice=json_data.get("MfaRememberDevice"),
            MfaRequired=json_data.get("MfaRequired"),
            Name=json_data.get("Name"),
            NetworkConnection=json_data.get("NetworkConnection"),
            NetworkExcludes=json_data.get("NetworkExcludes"),
            NetworkIncludes=json_data.get("NetworkIncludes"),
            Policyid=json_data.get("Policyid"),
            Priority=json_data.get("Priority"),
            SessionIdle=json_data.get("SessionIdle"),
            SessionLifetime=json_data.get("SessionLifetime"),
            SessionPersistent=json_data.get("SessionPersistent"),
            Status=json_data.get("Status"),
            UsersExcluded=json_data.get("UsersExcluded"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


