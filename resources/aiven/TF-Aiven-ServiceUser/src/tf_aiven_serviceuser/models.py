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
    AccessCert: Optional[str]
    AccessKey: Optional[str]
    Authentication: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    Project: Optional[str]
    RedisAclCategories: Optional[Sequence[str]]
    RedisAclCommands: Optional[Sequence[str]]
    RedisAclKeys: Optional[Sequence[str]]
    ServiceName: Optional[str]
    Type: Optional[str]
    Username: Optional[str]

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
            AccessCert=json_data.get("AccessCert"),
            AccessKey=json_data.get("AccessKey"),
            Authentication=json_data.get("Authentication"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Project=json_data.get("Project"),
            RedisAclCategories=json_data.get("RedisAclCategories"),
            RedisAclCommands=json_data.get("RedisAclCommands"),
            RedisAclKeys=json_data.get("RedisAclKeys"),
            ServiceName=json_data.get("ServiceName"),
            Type=json_data.get("Type"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


