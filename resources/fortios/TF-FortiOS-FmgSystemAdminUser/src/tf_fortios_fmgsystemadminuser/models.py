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
    Description: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    Profileid: Optional[str]
    RadiusServer: Optional[str]
    RpcPermit: Optional[str]
    Trusthost1: Optional[str]
    Trusthost2: Optional[str]
    Trusthost3: Optional[str]
    UserType: Optional[str]
    Userid: Optional[str]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Profileid=json_data.get("Profileid"),
            RadiusServer=json_data.get("RadiusServer"),
            RpcPermit=json_data.get("RpcPermit"),
            Trusthost1=json_data.get("Trusthost1"),
            Trusthost2=json_data.get("Trusthost2"),
            Trusthost3=json_data.get("Trusthost3"),
            UserType=json_data.get("UserType"),
            Userid=json_data.get("Userid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


