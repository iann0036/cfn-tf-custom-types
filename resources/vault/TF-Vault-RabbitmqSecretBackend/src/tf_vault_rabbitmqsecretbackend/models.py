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
    ConnectionUri: Optional[str]
    DefaultLeaseTtlSeconds: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    MaxLeaseTtlSeconds: Optional[float]
    Password: Optional[str]
    Path: Optional[str]
    Username: Optional[str]
    VerifyConnection: Optional[bool]

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
            ConnectionUri=json_data.get("ConnectionUri"),
            DefaultLeaseTtlSeconds=json_data.get("DefaultLeaseTtlSeconds"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxLeaseTtlSeconds=json_data.get("MaxLeaseTtlSeconds"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Username=json_data.get("Username"),
            VerifyConnection=json_data.get("VerifyConnection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


