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
    DynamicSortSubtable: Optional[str]
    Fortilink: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fortilink=json_data.get("Fortilink"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MembersDefinition(BaseModel):
    Name: Optional[str]
    SwitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SwitchId=json_data.get("SwitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


