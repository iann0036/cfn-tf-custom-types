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
    AggregationType: Optional[str]
    ConstrainedProperty: Optional[str]
    DecayRate: Optional[float]
    Description: Optional[str]
    Domain: Optional[str]
    HostHeader: Optional[str]
    Id: Optional[str]
    LeaderString: Optional[str]
    LeastSquaresDecay: Optional[float]
    LoadImbalancePercentage: Optional[float]
    MaxUMultiplicativeIncrement: Optional[float]
    Name: Optional[str]
    Type: Optional[str]
    UpperBound: Optional[float]
    WaitOnComplete: Optional[bool]
    ResourceInstance: Optional[Sequence["_ResourceInstanceDefinition"]]

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
            AggregationType=json_data.get("AggregationType"),
            ConstrainedProperty=json_data.get("ConstrainedProperty"),
            DecayRate=json_data.get("DecayRate"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            HostHeader=json_data.get("HostHeader"),
            Id=json_data.get("Id"),
            LeaderString=json_data.get("LeaderString"),
            LeastSquaresDecay=json_data.get("LeastSquaresDecay"),
            LoadImbalancePercentage=json_data.get("LoadImbalancePercentage"),
            MaxUMultiplicativeIncrement=json_data.get("MaxUMultiplicativeIncrement"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            UpperBound=json_data.get("UpperBound"),
            WaitOnComplete=json_data.get("WaitOnComplete"),
            ResourceInstance=deserialize_list(json_data.get("ResourceInstance"), ResourceInstanceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceInstanceDefinition(BaseModel):
    DatacenterId: Optional[float]
    LoadObject: Optional[str]
    LoadObjectPort: Optional[float]
    LoadServers: Optional[Sequence[str]]
    UseDefaultLoadObject: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceInstanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceInstanceDefinition"]:
        if not json_data:
            return None
        return cls(
            DatacenterId=json_data.get("DatacenterId"),
            LoadObject=json_data.get("LoadObject"),
            LoadObjectPort=json_data.get("LoadObjectPort"),
            LoadServers=json_data.get("LoadServers"),
            UseDefaultLoadObject=json_data.get("UseDefaultLoadObject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceInstanceDefinition = ResourceInstanceDefinition


