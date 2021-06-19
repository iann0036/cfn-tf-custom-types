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
    Arn: Optional[str]
    Description: Optional[str]
    FunctionName: Optional[str]
    FunctionVersion: Optional[str]
    Id: Optional[str]
    InvokeArn: Optional[str]
    Name: Optional[str]
    RoutingConfig: Optional[Sequence["_RoutingConfigDefinition"]]

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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            FunctionName=json_data.get("FunctionName"),
            FunctionVersion=json_data.get("FunctionVersion"),
            Id=json_data.get("Id"),
            InvokeArn=json_data.get("InvokeArn"),
            Name=json_data.get("Name"),
            RoutingConfig=deserialize_list(json_data.get("RoutingConfig"), RoutingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoutingConfigDefinition(BaseModel):
    AdditionalVersionWeights: Optional[Sequence["_AdditionalVersionWeightsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalVersionWeights=deserialize_list(json_data.get("AdditionalVersionWeights"), AdditionalVersionWeightsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingConfigDefinition = RoutingConfigDefinition


@dataclass
class AdditionalVersionWeightsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalVersionWeightsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalVersionWeightsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalVersionWeightsDefinition = AdditionalVersionWeightsDefinition


