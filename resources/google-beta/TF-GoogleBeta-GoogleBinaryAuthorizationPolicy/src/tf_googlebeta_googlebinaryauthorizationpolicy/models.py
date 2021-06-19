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
    Description: Optional[str]
    GlobalPolicyEvaluationMode: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    AdmissionWhitelistPatterns: Optional[Sequence["_AdmissionWhitelistPatternsDefinition"]]
    ClusterAdmissionRules: Optional[Sequence["_ClusterAdmissionRulesDefinition"]]
    DefaultAdmissionRule: Optional[Sequence["_DefaultAdmissionRuleDefinition"]]
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
            Description=json_data.get("Description"),
            GlobalPolicyEvaluationMode=json_data.get("GlobalPolicyEvaluationMode"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            AdmissionWhitelistPatterns=deserialize_list(json_data.get("AdmissionWhitelistPatterns"), AdmissionWhitelistPatternsDefinition),
            ClusterAdmissionRules=deserialize_list(json_data.get("ClusterAdmissionRules"), ClusterAdmissionRulesDefinition),
            DefaultAdmissionRule=deserialize_list(json_data.get("DefaultAdmissionRule"), DefaultAdmissionRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdmissionWhitelistPatternsDefinition(BaseModel):
    NamePattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdmissionWhitelistPatternsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdmissionWhitelistPatternsDefinition"]:
        if not json_data:
            return None
        return cls(
            NamePattern=json_data.get("NamePattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdmissionWhitelistPatternsDefinition = AdmissionWhitelistPatternsDefinition


@dataclass
class ClusterAdmissionRulesDefinition(BaseModel):
    Cluster: Optional[str]
    EnforcementMode: Optional[str]
    EvaluationMode: Optional[str]
    RequireAttestationsBy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterAdmissionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterAdmissionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cluster=json_data.get("Cluster"),
            EnforcementMode=json_data.get("EnforcementMode"),
            EvaluationMode=json_data.get("EvaluationMode"),
            RequireAttestationsBy=json_data.get("RequireAttestationsBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterAdmissionRulesDefinition = ClusterAdmissionRulesDefinition


@dataclass
class DefaultAdmissionRuleDefinition(BaseModel):
    EnforcementMode: Optional[str]
    EvaluationMode: Optional[str]
    RequireAttestationsBy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAdmissionRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAdmissionRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            EnforcementMode=json_data.get("EnforcementMode"),
            EvaluationMode=json_data.get("EvaluationMode"),
            RequireAttestationsBy=json_data.get("RequireAttestationsBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAdmissionRuleDefinition = DefaultAdmissionRuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


