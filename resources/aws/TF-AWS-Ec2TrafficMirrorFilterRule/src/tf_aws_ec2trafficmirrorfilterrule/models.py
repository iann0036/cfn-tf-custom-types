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
    DestinationCidrBlock: Optional[str]
    Id: Optional[str]
    Protocol: Optional[float]
    RuleAction: Optional[str]
    RuleNumber: Optional[float]
    SourceCidrBlock: Optional[str]
    TrafficDirection: Optional[str]
    TrafficMirrorFilterId: Optional[str]
    DestinationPortRange: Optional[Sequence["_DestinationPortRangeDefinition"]]
    SourcePortRange: Optional[Sequence["_SourcePortRangeDefinition"]]

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
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
            RuleAction=json_data.get("RuleAction"),
            RuleNumber=json_data.get("RuleNumber"),
            SourceCidrBlock=json_data.get("SourceCidrBlock"),
            TrafficDirection=json_data.get("TrafficDirection"),
            TrafficMirrorFilterId=json_data.get("TrafficMirrorFilterId"),
            DestinationPortRange=deserialize_list(json_data.get("DestinationPortRange"), DestinationPortRangeDefinition),
            SourcePortRange=deserialize_list(json_data.get("SourcePortRange"), SourcePortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationPortRangeDefinition(BaseModel):
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationPortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationPortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationPortRangeDefinition = DestinationPortRangeDefinition


@dataclass
class SourcePortRangeDefinition(BaseModel):
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortRangeDefinition = SourcePortRangeDefinition


