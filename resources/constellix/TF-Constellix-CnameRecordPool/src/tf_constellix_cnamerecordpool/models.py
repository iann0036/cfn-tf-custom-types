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
    DisableFlag: Optional[str]
    FailedFlag: Optional[str]
    Id: Optional[str]
    MinAvailableFailover: Optional[float]
    Name: Optional[str]
    Note: Optional[str]
    NumReturn: Optional[float]
    Version: Optional[float]
    Values: Optional[Sequence["_ValuesDefinition"]]

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
            DisableFlag=json_data.get("DisableFlag"),
            FailedFlag=json_data.get("FailedFlag"),
            Id=json_data.get("Id"),
            MinAvailableFailover=json_data.get("MinAvailableFailover"),
            Name=json_data.get("Name"),
            Note=json_data.get("Note"),
            NumReturn=json_data.get("NumReturn"),
            Version=json_data.get("Version"),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValuesDefinition(BaseModel):
    CheckId: Optional[float]
    DisableFlag: Optional[str]
    Policy: Optional[str]
    Value: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckId=json_data.get("CheckId"),
            DisableFlag=json_data.get("DisableFlag"),
            Policy=json_data.get("Policy"),
            Value=json_data.get("Value"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


