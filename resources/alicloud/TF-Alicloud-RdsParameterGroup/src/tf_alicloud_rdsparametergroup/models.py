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
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    ParameterGroupDesc: Optional[str]
    ParameterGroupName: Optional[str]
    ParamDetail: Optional[Sequence["_ParamDetailDefinition"]]

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
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            ParameterGroupDesc=json_data.get("ParameterGroupDesc"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            ParamDetail=deserialize_list(json_data.get("ParamDetail"), ParamDetailDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParamDetailDefinition(BaseModel):
    ParamName: Optional[str]
    ParamValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamDetailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamDetailDefinition"]:
        if not json_data:
            return None
        return cls(
            ParamName=json_data.get("ParamName"),
            ParamValue=json_data.get("ParamValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamDetailDefinition = ParamDetailDefinition


