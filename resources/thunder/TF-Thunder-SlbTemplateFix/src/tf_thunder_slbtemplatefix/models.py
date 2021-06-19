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
    Id: Optional[str]
    InsertClientIp: Optional[float]
    Logging: Optional[str]
    Name: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    TagSwitching: Optional[Sequence["_TagSwitchingDefinition"]]

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
            Id=json_data.get("Id"),
            InsertClientIp=json_data.get("InsertClientIp"),
            Logging=json_data.get("Logging"),
            Name=json_data.get("Name"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            TagSwitching=deserialize_list(json_data.get("TagSwitching"), TagSwitchingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagSwitchingDefinition(BaseModel):
    Equals: Optional[str]
    ServiceGroup: Optional[str]
    SwitchingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagSwitchingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSwitchingDefinition"]:
        if not json_data:
            return None
        return cls(
            Equals=json_data.get("Equals"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SwitchingType=json_data.get("SwitchingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSwitchingDefinition = TagSwitchingDefinition


