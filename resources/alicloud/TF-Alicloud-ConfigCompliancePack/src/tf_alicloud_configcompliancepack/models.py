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
    CompliancePackName: Optional[str]
    CompliancePackTemplateId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    RiskLevel: Optional[float]
    Status: Optional[str]
    ConfigRules: Optional[Sequence["_ConfigRulesDefinition"]]
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
            CompliancePackName=json_data.get("CompliancePackName"),
            CompliancePackTemplateId=json_data.get("CompliancePackTemplateId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            RiskLevel=json_data.get("RiskLevel"),
            Status=json_data.get("Status"),
            ConfigRules=deserialize_list(json_data.get("ConfigRules"), ConfigRulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigRulesDefinition(BaseModel):
    ManagedRuleIdentifier: Optional[str]
    ConfigRuleParameters: Optional[Sequence["_ConfigRuleParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            ManagedRuleIdentifier=json_data.get("ManagedRuleIdentifier"),
            ConfigRuleParameters=deserialize_list(json_data.get("ConfigRuleParameters"), ConfigRuleParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigRulesDefinition = ConfigRulesDefinition


@dataclass
class ConfigRuleParametersDefinition(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigRuleParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigRuleParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigRuleParametersDefinition = ConfigRuleParametersDefinition


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


