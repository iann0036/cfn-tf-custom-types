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
    CloudType: Optional[str]
    CreatedBy: Optional[str]
    CreatedOn: Optional[float]
    Deleted: Optional[bool]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    LastModifiedBy: Optional[str]
    LastModifiedOn: Optional[float]
    Name: Optional[str]
    OpenAlertsCount: Optional[float]
    Overridden: Optional[bool]
    Owner: Optional[str]
    PolicyId: Optional[str]
    PolicyMode: Optional[str]
    PolicyType: Optional[str]
    Recommendation: Optional[str]
    Remediable: Optional[bool]
    RestrictAlertDismissal: Optional[bool]
    RuleLastModifiedOn: Optional[float]
    Severity: Optional[str]
    SystemDefault: Optional[bool]
    ComplianceMetadata: Optional[Sequence["_ComplianceMetadataDefinition"]]
    Remediation: Optional[Sequence["_RemediationDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
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
            CloudType=json_data.get("CloudType"),
            CreatedBy=json_data.get("CreatedBy"),
            CreatedOn=json_data.get("CreatedOn"),
            Deleted=json_data.get("Deleted"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LastModifiedOn=json_data.get("LastModifiedOn"),
            Name=json_data.get("Name"),
            OpenAlertsCount=json_data.get("OpenAlertsCount"),
            Overridden=json_data.get("Overridden"),
            Owner=json_data.get("Owner"),
            PolicyId=json_data.get("PolicyId"),
            PolicyMode=json_data.get("PolicyMode"),
            PolicyType=json_data.get("PolicyType"),
            Recommendation=json_data.get("Recommendation"),
            Remediable=json_data.get("Remediable"),
            RestrictAlertDismissal=json_data.get("RestrictAlertDismissal"),
            RuleLastModifiedOn=json_data.get("RuleLastModifiedOn"),
            Severity=json_data.get("Severity"),
            SystemDefault=json_data.get("SystemDefault"),
            ComplianceMetadata=deserialize_list(json_data.get("ComplianceMetadata"), ComplianceMetadataDefinition),
            Remediation=deserialize_list(json_data.get("Remediation"), RemediationDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComplianceMetadataDefinition(BaseModel):
    ComplianceId: Optional[str]
    CustomAssigned: Optional[bool]
    RequirementDescription: Optional[str]
    RequirementId: Optional[str]
    RequirementName: Optional[str]
    SectionDescription: Optional[str]
    SectionId: Optional[str]
    SectionLabel: Optional[str]
    StandardDescription: Optional[str]
    StandardName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComplianceMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComplianceMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            ComplianceId=json_data.get("ComplianceId"),
            CustomAssigned=json_data.get("CustomAssigned"),
            RequirementDescription=json_data.get("RequirementDescription"),
            RequirementId=json_data.get("RequirementId"),
            RequirementName=json_data.get("RequirementName"),
            SectionDescription=json_data.get("SectionDescription"),
            SectionId=json_data.get("SectionId"),
            SectionLabel=json_data.get("SectionLabel"),
            StandardDescription=json_data.get("StandardDescription"),
            StandardName=json_data.get("StandardName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComplianceMetadataDefinition = ComplianceMetadataDefinition


@dataclass
class RemediationDefinition(BaseModel):
    CliScriptJsonSchemaString: Optional[str]
    CliScriptTemplate: Optional[str]
    Description: Optional[str]
    TemplateType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemediationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemediationDefinition"]:
        if not json_data:
            return None
        return cls(
            CliScriptJsonSchemaString=json_data.get("CliScriptJsonSchemaString"),
            CliScriptTemplate=json_data.get("CliScriptTemplate"),
            Description=json_data.get("Description"),
            TemplateType=json_data.get("TemplateType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemediationDefinition = RemediationDefinition


@dataclass
class RuleDefinition(BaseModel):
    ApiName: Optional[str]
    CloudAccount: Optional[str]
    CloudType: Optional[str]
    Criteria: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    ResourceIdPath: Optional[str]
    ResourceType: Optional[str]
    RuleType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiName=json_data.get("ApiName"),
            CloudAccount=json_data.get("CloudAccount"),
            CloudType=json_data.get("CloudType"),
            Criteria=json_data.get("Criteria"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            ResourceIdPath=json_data.get("ResourceIdPath"),
            ResourceType=json_data.get("ResourceType"),
            RuleType=json_data.get("RuleType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


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


