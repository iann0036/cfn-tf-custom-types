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
    BuiltIn: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdated: Optional[str]
    Name: Optional[str]
    PostWebhookId: Optional[float]
    PreWebhookId: Optional[float]
    AwsCloudformationTemplates: Optional[Sequence["_AwsCloudformationTemplatesDefinition"]]
    AwsIamPolicies: Optional[Sequence["_AwsIamPoliciesDefinition"]]
    AzureArmTemplateDefinitions: Optional[Sequence["_AzureArmTemplateDefinitionsDefinition"]]
    AzurePolicyDefinitions: Optional[Sequence["_AzurePolicyDefinitionsDefinition"]]
    AzureRoleDefinitions: Optional[Sequence["_AzureRoleDefinitionsDefinition"]]
    ComplianceStandards: Optional[Sequence["_ComplianceStandardsDefinition"]]
    InternalAwsAmis: Optional[Sequence["_InternalAwsAmisDefinition"]]
    InternalAwsServiceCatalogPortfolios: Optional[Sequence["_InternalAwsServiceCatalogPortfoliosDefinition"]]
    Ous: Optional[Sequence["_OusDefinition"]]
    OwnerUserGroups: Optional[Sequence["_OwnerUserGroupsDefinition"]]
    OwnerUsers: Optional[Sequence["_OwnerUsersDefinition"]]
    Projects: Optional[Sequence["_ProjectsDefinition"]]
    ServiceControlPolicies: Optional[Sequence["_ServiceControlPoliciesDefinition"]]

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
            BuiltIn=json_data.get("BuiltIn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdated=json_data.get("LastUpdated"),
            Name=json_data.get("Name"),
            PostWebhookId=json_data.get("PostWebhookId"),
            PreWebhookId=json_data.get("PreWebhookId"),
            AwsCloudformationTemplates=deserialize_list(json_data.get("AwsCloudformationTemplates"), AwsCloudformationTemplatesDefinition),
            AwsIamPolicies=deserialize_list(json_data.get("AwsIamPolicies"), AwsIamPoliciesDefinition),
            AzureArmTemplateDefinitions=deserialize_list(json_data.get("AzureArmTemplateDefinitions"), AzureArmTemplateDefinitionsDefinition),
            AzurePolicyDefinitions=deserialize_list(json_data.get("AzurePolicyDefinitions"), AzurePolicyDefinitionsDefinition),
            AzureRoleDefinitions=deserialize_list(json_data.get("AzureRoleDefinitions"), AzureRoleDefinitionsDefinition),
            ComplianceStandards=deserialize_list(json_data.get("ComplianceStandards"), ComplianceStandardsDefinition),
            InternalAwsAmis=deserialize_list(json_data.get("InternalAwsAmis"), InternalAwsAmisDefinition),
            InternalAwsServiceCatalogPortfolios=deserialize_list(json_data.get("InternalAwsServiceCatalogPortfolios"), InternalAwsServiceCatalogPortfoliosDefinition),
            Ous=deserialize_list(json_data.get("Ous"), OusDefinition),
            OwnerUserGroups=deserialize_list(json_data.get("OwnerUserGroups"), OwnerUserGroupsDefinition),
            OwnerUsers=deserialize_list(json_data.get("OwnerUsers"), OwnerUsersDefinition),
            Projects=deserialize_list(json_data.get("Projects"), ProjectsDefinition),
            ServiceControlPolicies=deserialize_list(json_data.get("ServiceControlPolicies"), ServiceControlPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AwsCloudformationTemplatesDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationTemplatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationTemplatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationTemplatesDefinition = AwsCloudformationTemplatesDefinition


@dataclass
class AwsIamPoliciesDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamPoliciesDefinition = AwsIamPoliciesDefinition


@dataclass
class AzureArmTemplateDefinitionsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureArmTemplateDefinitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureArmTemplateDefinitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureArmTemplateDefinitionsDefinition = AzureArmTemplateDefinitionsDefinition


@dataclass
class AzurePolicyDefinitionsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzurePolicyDefinitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzurePolicyDefinitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzurePolicyDefinitionsDefinition = AzurePolicyDefinitionsDefinition


@dataclass
class AzureRoleDefinitionsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureRoleDefinitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureRoleDefinitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureRoleDefinitionsDefinition = AzureRoleDefinitionsDefinition


@dataclass
class ComplianceStandardsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ComplianceStandardsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComplianceStandardsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComplianceStandardsDefinition = ComplianceStandardsDefinition


@dataclass
class InternalAwsAmisDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternalAwsAmisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalAwsAmisDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalAwsAmisDefinition = InternalAwsAmisDefinition


@dataclass
class InternalAwsServiceCatalogPortfoliosDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternalAwsServiceCatalogPortfoliosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternalAwsServiceCatalogPortfoliosDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternalAwsServiceCatalogPortfoliosDefinition = InternalAwsServiceCatalogPortfoliosDefinition


@dataclass
class OusDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OusDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OusDefinition = OusDefinition


@dataclass
class OwnerUserGroupsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUserGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUserGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUserGroupsDefinition = OwnerUserGroupsDefinition


@dataclass
class OwnerUsersDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerUsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerUsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerUsersDefinition = OwnerUsersDefinition


@dataclass
class ProjectsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectsDefinition = ProjectsDefinition


@dataclass
class ServiceControlPoliciesDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceControlPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceControlPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceControlPoliciesDefinition = ServiceControlPoliciesDefinition


