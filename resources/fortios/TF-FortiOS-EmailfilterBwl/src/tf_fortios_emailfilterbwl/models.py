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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Entries: Optional[Sequence["_EntriesDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    AddrType: Optional[str]
    EmailPattern: Optional[str]
    Id: Optional[float]
    Ip4Subnet: Optional[str]
    Ip6Subnet: Optional[str]
    PatternType: Optional[str]
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AddrType=json_data.get("AddrType"),
            EmailPattern=json_data.get("EmailPattern"),
            Id=json_data.get("Id"),
            Ip4Subnet=json_data.get("Ip4Subnet"),
            Ip6Subnet=json_data.get("Ip6Subnet"),
            PatternType=json_data.get("PatternType"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition

