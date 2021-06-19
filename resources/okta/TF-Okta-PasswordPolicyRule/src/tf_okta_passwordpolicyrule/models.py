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
    NetworkConnection: Optional[str]
    NetworkExcludes: Optional[Sequence[str]]
    NetworkIncludes: Optional[Sequence[str]]
    PasswordChange: Optional[str]
    PasswordReset: Optional[str]
    PasswordUnlock: Optional[str]
    Policyid: Optional[str]
    Priority: Optional[float]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkConnection=json_data.get("NetworkConnection"),
            NetworkExcludes=json_data.get("NetworkExcludes"),
            NetworkIncludes=json_data.get("NetworkIncludes"),
            PasswordChange=json_data.get("PasswordChange"),
            PasswordReset=json_data.get("PasswordReset"),
            PasswordUnlock=json_data.get("PasswordUnlock"),
            Policyid=json_data.get("Policyid"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            UsersExcluded=json_data.get("UsersExcluded"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


