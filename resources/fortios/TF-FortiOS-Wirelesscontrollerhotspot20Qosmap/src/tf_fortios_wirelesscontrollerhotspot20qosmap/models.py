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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    DscpExcept: Optional[Sequence["_DscpExceptDefinition"]]
    DscpRange: Optional[Sequence["_DscpRangeDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            DscpExcept=deserialize_list(json_data.get("DscpExcept"), DscpExceptDefinition),
            DscpRange=deserialize_list(json_data.get("DscpRange"), DscpRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DscpExceptDefinition(BaseModel):
    Dscp: Optional[float]
    Index: Optional[float]
    Up: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpExceptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpExceptDefinition"]:
        if not json_data:
            return None
        return cls(
            Dscp=json_data.get("Dscp"),
            Index=json_data.get("Index"),
            Up=json_data.get("Up"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpExceptDefinition = DscpExceptDefinition


@dataclass
class DscpRangeDefinition(BaseModel):
    High: Optional[float]
    Index: Optional[float]
    Low: Optional[float]
    Up: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            High=json_data.get("High"),
            Index=json_data.get("Index"),
            Low=json_data.get("Low"),
            Up=json_data.get("Up"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpRangeDefinition = DscpRangeDefinition


