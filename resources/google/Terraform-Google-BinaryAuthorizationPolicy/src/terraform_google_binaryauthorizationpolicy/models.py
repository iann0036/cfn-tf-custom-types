# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    GlobalPolicyEvaluationMode: Optional[str]
    Project: Optional[str]
    AdmissionWhitelistPatterns: Optional[Sequence["_AdmissionWhitelistPatterns"]]
    ClusterAdmissionRules: Optional[Sequence["_ClusterAdmissionRules"]]
    DefaultAdmissionRule: Optional[Sequence["_DefaultAdmissionRule"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            GlobalPolicyEvaluationMode=json_data.get("GlobalPolicyEvaluationMode"),
            Project=json_data.get("Project"),
            AdmissionWhitelistPatterns=json_data.get("AdmissionWhitelistPatterns"),
            ClusterAdmissionRules=json_data.get("ClusterAdmissionRules"),
            DefaultAdmissionRule=json_data.get("DefaultAdmissionRule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdmissionWhitelistPatterns:
    NamePattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdmissionWhitelistPatterns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdmissionWhitelistPatterns"]:
        if not json_data:
            return None
        return cls(
            NamePattern=json_data.get("NamePattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdmissionWhitelistPatterns = AdmissionWhitelistPatterns


@dataclass
class ClusterAdmissionRules:
    Cluster: Optional[str]
    EnforcementMode: Optional[str]
    EvaluationMode: Optional[str]
    RequireAttestationsBy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterAdmissionRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterAdmissionRules"]:
        if not json_data:
            return None
        return cls(
            Cluster=json_data.get("Cluster"),
            EnforcementMode=json_data.get("EnforcementMode"),
            EvaluationMode=json_data.get("EvaluationMode"),
            RequireAttestationsBy=json_data.get("RequireAttestationsBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterAdmissionRules = ClusterAdmissionRules


@dataclass
class DefaultAdmissionRule:
    EnforcementMode: Optional[str]
    EvaluationMode: Optional[str]
    RequireAttestationsBy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAdmissionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAdmissionRule"]:
        if not json_data:
            return None
        return cls(
            EnforcementMode=json_data.get("EnforcementMode"),
            EvaluationMode=json_data.get("EvaluationMode"),
            RequireAttestationsBy=json_data.get("RequireAttestationsBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAdmissionRule = DefaultAdmissionRule


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


