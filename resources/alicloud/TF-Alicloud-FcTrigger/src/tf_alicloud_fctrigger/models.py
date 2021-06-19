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
    Config: Optional[str]
    ConfigMns: Optional[str]
    Function: Optional[str]
    Id: Optional[str]
    LastModified: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Role: Optional[str]
    Service: Optional[str]
    SourceArn: Optional[str]
    TriggerId: Optional[str]
    Type: Optional[str]

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
            Config=json_data.get("Config"),
            ConfigMns=json_data.get("ConfigMns"),
            Function=json_data.get("Function"),
            Id=json_data.get("Id"),
            LastModified=json_data.get("LastModified"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Role=json_data.get("Role"),
            Service=json_data.get("Service"),
            SourceArn=json_data.get("SourceArn"),
            TriggerId=json_data.get("TriggerId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


