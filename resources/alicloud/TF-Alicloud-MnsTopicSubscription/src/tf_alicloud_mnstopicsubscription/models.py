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
    Endpoint: Optional[str]
    FilterTag: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NotifyContentFormat: Optional[str]
    NotifyStrategy: Optional[str]
    TopicName: Optional[str]

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
            Endpoint=json_data.get("Endpoint"),
            FilterTag=json_data.get("FilterTag"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NotifyContentFormat=json_data.get("NotifyContentFormat"),
            NotifyStrategy=json_data.get("NotifyStrategy"),
            TopicName=json_data.get("TopicName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


