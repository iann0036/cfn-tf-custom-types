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
    ContextVersion: Optional[str]
    CreatedAt: Optional[str]
    Disabled: Optional[bool]
    EnvVars: Optional[Sequence[str]]
    Function: Optional[str]
    Id: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]
    Packages: Optional[Sequence["_PackagesDefinition"]]
    Retries: Optional[float]
    Runtime: Optional[str]
    Status: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    UpdatedAt: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

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
            ContextVersion=json_data.get("ContextVersion"),
            CreatedAt=json_data.get("CreatedAt"),
            Disabled=json_data.get("Disabled"),
            EnvVars=json_data.get("EnvVars"),
            Function=json_data.get("Function"),
            Id=json_data.get("Id"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            Packages=deserialize_list(json_data.get("Packages"), PackagesDefinition),
            Retries=json_data.get("Retries"),
            Runtime=json_data.get("Runtime"),
            Status=json_data.get("Status"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class PackagesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PackagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackagesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackagesDefinition = PackagesDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    Operator: Optional[str]
    Source: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Source=json_data.get("Source"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


