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
    AllVars: Optional[Sequence["_AllVarsDefinition"]]
    Id: Optional[str]
    PipelineId: Optional[str]
    PipelineStage: Optional[str]
    SensitiveVars: Optional[Sequence["_SensitiveVarsDefinition"]]
    Vars: Optional[Sequence["_VarsDefinition"]]

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
            AllVars=deserialize_list(json_data.get("AllVars"), AllVarsDefinition),
            Id=json_data.get("Id"),
            PipelineId=json_data.get("PipelineId"),
            PipelineStage=json_data.get("PipelineStage"),
            SensitiveVars=deserialize_list(json_data.get("SensitiveVars"), SensitiveVarsDefinition),
            Vars=deserialize_list(json_data.get("Vars"), VarsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllVarsDefinition = AllVarsDefinition


@dataclass
class SensitiveVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveVarsDefinition = SensitiveVarsDefinition


@dataclass
class VarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VarsDefinition = VarsDefinition

