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
    Backend: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[str]
    Vhost: Optional[Sequence["_VhostDefinition"]]

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
            Backend=json_data.get("Backend"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Vhost=deserialize_list(json_data.get("Vhost"), VhostDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VhostDefinition(BaseModel):
    Configure: Optional[str]
    Host: Optional[str]
    Read: Optional[str]
    Write: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VhostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VhostDefinition"]:
        if not json_data:
            return None
        return cls(
            Configure=json_data.get("Configure"),
            Host=json_data.get("Host"),
            Read=json_data.get("Read"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VhostDefinition = VhostDefinition


