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
    Convention: Optional[str]
    Id: Optional[str]
    MaxLength: Optional[float]
    Name: Optional[str]
    Postfix: Optional[str]
    Prefix: Optional[str]
    Prefixes: Optional[Sequence[str]]
    ResourceType: Optional[str]
    Result: Optional[str]
    Suffixes: Optional[Sequence[str]]

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
            Convention=json_data.get("Convention"),
            Id=json_data.get("Id"),
            MaxLength=json_data.get("MaxLength"),
            Name=json_data.get("Name"),
            Postfix=json_data.get("Postfix"),
            Prefix=json_data.get("Prefix"),
            Prefixes=json_data.get("Prefixes"),
            ResourceType=json_data.get("ResourceType"),
            Result=json_data.get("Result"),
            Suffixes=json_data.get("Suffixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


