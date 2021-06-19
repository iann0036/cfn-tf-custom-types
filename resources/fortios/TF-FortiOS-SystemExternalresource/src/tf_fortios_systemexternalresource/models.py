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
    Category: Optional[float]
    Comments: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    RefreshRate: Optional[float]
    Resource: Optional[str]
    SourceIp: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    UserAgent: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]

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
            Category=json_data.get("Category"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            RefreshRate=json_data.get("RefreshRate"),
            Resource=json_data.get("Resource"),
            SourceIp=json_data.get("SourceIp"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            UserAgent=json_data.get("UserAgent"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


