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
    AggregateConfigRuleName: Optional[str]
    AggregatorId: Optional[str]
    ConfigRuleTriggerTypes: Optional[str]
    Description: Optional[str]
    ExcludeResourceIdsScope: Optional[str]
    Id: Optional[str]
    InputParameters: Optional[Sequence["_InputParametersDefinition"]]
    MaximumExecutionFrequency: Optional[str]
    RegionIdsScope: Optional[str]
    ResourceGroupIdsScope: Optional[str]
    ResourceTypesScope: Optional[Sequence[str]]
    RiskLevel: Optional[float]
    SourceIdentifier: Optional[str]
    SourceOwner: Optional[str]
    Status: Optional[str]
    TagKeyScope: Optional[str]
    TagValueScope: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AggregateConfigRuleName=json_data.get("AggregateConfigRuleName"),
            AggregatorId=json_data.get("AggregatorId"),
            ConfigRuleTriggerTypes=json_data.get("ConfigRuleTriggerTypes"),
            Description=json_data.get("Description"),
            ExcludeResourceIdsScope=json_data.get("ExcludeResourceIdsScope"),
            Id=json_data.get("Id"),
            InputParameters=deserialize_list(json_data.get("InputParameters"), InputParametersDefinition),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            RegionIdsScope=json_data.get("RegionIdsScope"),
            ResourceGroupIdsScope=json_data.get("ResourceGroupIdsScope"),
            ResourceTypesScope=json_data.get("ResourceTypesScope"),
            RiskLevel=json_data.get("RiskLevel"),
            SourceIdentifier=json_data.get("SourceIdentifier"),
            SourceOwner=json_data.get("SourceOwner"),
            Status=json_data.get("Status"),
            TagKeyScope=json_data.get("TagKeyScope"),
            TagValueScope=json_data.get("TagValueScope"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InputParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParametersDefinition = InputParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


