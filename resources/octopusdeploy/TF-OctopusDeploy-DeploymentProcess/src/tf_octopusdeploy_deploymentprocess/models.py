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
    Id: Optional[str]
    LastSnapshotId: Optional[str]
    ProjectId: Optional[str]
    SpaceId: Optional[str]
    Version: Optional[float]
    Step: Optional[Sequence["_StepDefinition"]]

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
            Id=json_data.get("Id"),
            LastSnapshotId=json_data.get("LastSnapshotId"),
            ProjectId=json_data.get("ProjectId"),
            SpaceId=json_data.get("SpaceId"),
            Version=json_data.get("Version"),
            Step=deserialize_list(json_data.get("Step"), StepDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepDefinition(BaseModel):
    Condition: Optional[str]
    ConditionExpression: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PackageRequirement: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    StartTrigger: Optional[str]
    TargetRoles: Optional[Sequence[str]]
    WindowSize: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    ApplyTerraformTemplateAction: Optional[Sequence["_ApplyTerraformTemplateActionDefinition"]]
    DeployKubernetesSecretAction: Optional[Sequence["_DeployKubernetesSecretActionDefinition"]]
    DeployPackageAction: Optional[Sequence["_DeployPackageActionDefinition"]]
    DeployWindowsServiceAction: Optional[Sequence["_DeployWindowsServiceActionDefinition"]]
    ManualInterventionAction: Optional[Sequence["_ManualInterventionActionDefinition"]]
    RunKubectlScriptAction: Optional[Sequence["_RunKubectlScriptActionDefinition"]]
    RunScriptAction: Optional[Sequence["_RunScriptActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            ConditionExpression=json_data.get("ConditionExpression"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PackageRequirement=json_data.get("PackageRequirement"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            StartTrigger=json_data.get("StartTrigger"),
            TargetRoles=json_data.get("TargetRoles"),
            WindowSize=json_data.get("WindowSize"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            ApplyTerraformTemplateAction=deserialize_list(json_data.get("ApplyTerraformTemplateAction"), ApplyTerraformTemplateActionDefinition),
            DeployKubernetesSecretAction=deserialize_list(json_data.get("DeployKubernetesSecretAction"), DeployKubernetesSecretActionDefinition),
            DeployPackageAction=deserialize_list(json_data.get("DeployPackageAction"), DeployPackageActionDefinition),
            DeployWindowsServiceAction=deserialize_list(json_data.get("DeployWindowsServiceAction"), DeployWindowsServiceActionDefinition),
            ManualInterventionAction=deserialize_list(json_data.get("ManualInterventionAction"), ManualInterventionActionDefinition),
            RunKubectlScriptAction=deserialize_list(json_data.get("RunKubectlScriptAction"), RunKubectlScriptActionDefinition),
            RunScriptAction=deserialize_list(json_data.get("RunScriptAction"), RunScriptActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition = StepDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class ActionDefinition(BaseModel):
    ActionType: Optional[str]
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition2"]]
    RunOnServer: Optional[bool]
    TenantTags: Optional[Sequence[str]]
    WorkerPoolId: Optional[str]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition2),
            RunOnServer=json_data.get("RunOnServer"),
            TenantTags=json_data.get("TenantTags"),
            WorkerPoolId=json_data.get("WorkerPoolId"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class PropertiesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition2 = PropertiesDefinition2


@dataclass
class ActionTemplateDefinition(BaseModel):
    CommunityActionTemplateId: Optional[str]
    Id: Optional[str]
    Version: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ActionTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            CommunityActionTemplateId=json_data.get("CommunityActionTemplateId"),
            Id=json_data.get("Id"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionTemplateDefinition = ActionTemplateDefinition


@dataclass
class ContainerDefinition(BaseModel):
    FeedId: Optional[str]
    Image: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            FeedId=json_data.get("FeedId"),
            Image=json_data.get("Image"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class PackageDefinition(BaseModel):
    AcquisitionLocation: Optional[str]
    ExtractDuringDeployment: Optional[bool]
    FeedId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PackageId: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition10"]]

    @classmethod
    def _deserialize(
        cls: Type["_PackageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageDefinition"]:
        if not json_data:
            return None
        return cls(
            AcquisitionLocation=json_data.get("AcquisitionLocation"),
            ExtractDuringDeployment=json_data.get("ExtractDuringDeployment"),
            FeedId=json_data.get("FeedId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PackageId=json_data.get("PackageId"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition10),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageDefinition = PackageDefinition


@dataclass
class PropertiesDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition10 = PropertiesDefinition10


@dataclass
class PrimaryPackageDefinition(BaseModel):
    AcquisitionLocation: Optional[str]
    FeedId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PackageId: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition11"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrimaryPackageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimaryPackageDefinition"]:
        if not json_data:
            return None
        return cls(
            AcquisitionLocation=json_data.get("AcquisitionLocation"),
            FeedId=json_data.get("FeedId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PackageId=json_data.get("PackageId"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition11),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimaryPackageDefinition = PrimaryPackageDefinition


@dataclass
class PropertiesDefinition11(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition11 = PropertiesDefinition11


@dataclass
class ApplyTerraformTemplateActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition3"]]
    RunOnServer: Optional[bool]
    TemplateParameters: Optional[str]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    AdvancedOptions: Optional[Sequence["_AdvancedOptionsDefinition"]]
    AwsAccount: Optional[Sequence["_AwsAccountDefinition"]]
    AzureAccount: Optional[Sequence["_AzureAccountDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplyTerraformTemplateActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplyTerraformTemplateActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition3),
            RunOnServer=json_data.get("RunOnServer"),
            TemplateParameters=json_data.get("TemplateParameters"),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            AdvancedOptions=deserialize_list(json_data.get("AdvancedOptions"), AdvancedOptionsDefinition),
            AwsAccount=deserialize_list(json_data.get("AwsAccount"), AwsAccountDefinition),
            AzureAccount=deserialize_list(json_data.get("AzureAccount"), AzureAccountDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplyTerraformTemplateActionDefinition = ApplyTerraformTemplateActionDefinition


@dataclass
class PropertiesDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition3 = PropertiesDefinition3


@dataclass
class AdvancedOptionsDefinition(BaseModel):
    AllowAdditionalPluginDownloads: Optional[bool]
    ApplyParameters: Optional[str]
    InitParameters: Optional[str]
    PluginCacheDirectory: Optional[str]
    Workspace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowAdditionalPluginDownloads=json_data.get("AllowAdditionalPluginDownloads"),
            ApplyParameters=json_data.get("ApplyParameters"),
            InitParameters=json_data.get("InitParameters"),
            PluginCacheDirectory=json_data.get("PluginCacheDirectory"),
            Workspace=json_data.get("Workspace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedOptionsDefinition = AdvancedOptionsDefinition


@dataclass
class AwsAccountDefinition(BaseModel):
    Region: Optional[str]
    UseInstanceRole: Optional[bool]
    Variable: Optional[str]
    Role: Optional[Sequence["_RoleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            UseInstanceRole=json_data.get("UseInstanceRole"),
            Variable=json_data.get("Variable"),
            Role=deserialize_list(json_data.get("Role"), RoleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAccountDefinition = AwsAccountDefinition


@dataclass
class RoleDefinition(BaseModel):
    Arn: Optional[str]
    ExternalId: Optional[str]
    RoleSessionName: Optional[str]
    SessionDuration: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            ExternalId=json_data.get("ExternalId"),
            RoleSessionName=json_data.get("RoleSessionName"),
            SessionDuration=json_data.get("SessionDuration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleDefinition = RoleDefinition


@dataclass
class AzureAccountDefinition(BaseModel):
    Variable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            Variable=json_data.get("Variable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureAccountDefinition = AzureAccountDefinition


@dataclass
class TemplateDefinition(BaseModel):
    AdditionalVariableFiles: Optional[str]
    Directory: Optional[str]
    RunAutomaticFileSubstitution: Optional[bool]
    TargetFiles: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalVariableFiles=json_data.get("AdditionalVariableFiles"),
            Directory=json_data.get("Directory"),
            RunAutomaticFileSubstitution=json_data.get("RunAutomaticFileSubstitution"),
            TargetFiles=json_data.get("TargetFiles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


@dataclass
class DeployKubernetesSecretActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition4"]]
    RunOnServer: Optional[bool]
    SecretName: Optional[str]
    SecretValues: Optional[Sequence["_SecretValuesDefinition"]]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeployKubernetesSecretActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployKubernetesSecretActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition4),
            RunOnServer=json_data.get("RunOnServer"),
            SecretName=json_data.get("SecretName"),
            SecretValues=deserialize_list(json_data.get("SecretValues"), SecretValuesDefinition),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployKubernetesSecretActionDefinition = DeployKubernetesSecretActionDefinition


@dataclass
class PropertiesDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition4 = PropertiesDefinition4


@dataclass
class SecretValuesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretValuesDefinition = SecretValuesDefinition


@dataclass
class DeployPackageActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition5"]]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]
    WindowsService: Optional[Sequence["_WindowsServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeployPackageActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployPackageActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition5),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
            WindowsService=deserialize_list(json_data.get("WindowsService"), WindowsServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployPackageActionDefinition = DeployPackageActionDefinition


@dataclass
class PropertiesDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition5 = PropertiesDefinition5


@dataclass
class WindowsServiceDefinition(BaseModel):
    Arguments: Optional[str]
    CreateOrUpdateService: Optional[bool]
    CustomAccountName: Optional[str]
    CustomAccountPassword: Optional[str]
    Dependencies: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    ExecutablePath: Optional[str]
    ServiceAccount: Optional[str]
    ServiceName: Optional[str]
    StartMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            CreateOrUpdateService=json_data.get("CreateOrUpdateService"),
            CustomAccountName=json_data.get("CustomAccountName"),
            CustomAccountPassword=json_data.get("CustomAccountPassword"),
            Dependencies=json_data.get("Dependencies"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            ExecutablePath=json_data.get("ExecutablePath"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceName=json_data.get("ServiceName"),
            StartMode=json_data.get("StartMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsServiceDefinition = WindowsServiceDefinition


@dataclass
class DeployWindowsServiceActionDefinition(BaseModel):
    Arguments: Optional[str]
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    CreateOrUpdateService: Optional[bool]
    CustomAccountName: Optional[str]
    CustomAccountPassword: Optional[str]
    Dependencies: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    ExecutablePath: Optional[str]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition6"]]
    ServiceAccount: Optional[str]
    ServiceName: Optional[str]
    StartMode: Optional[str]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeployWindowsServiceActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployWindowsServiceActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Arguments=json_data.get("Arguments"),
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            CreateOrUpdateService=json_data.get("CreateOrUpdateService"),
            CustomAccountName=json_data.get("CustomAccountName"),
            CustomAccountPassword=json_data.get("CustomAccountPassword"),
            Dependencies=json_data.get("Dependencies"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            ExecutablePath=json_data.get("ExecutablePath"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition6),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceName=json_data.get("ServiceName"),
            StartMode=json_data.get("StartMode"),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployWindowsServiceActionDefinition = DeployWindowsServiceActionDefinition


@dataclass
class PropertiesDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition6 = PropertiesDefinition6


@dataclass
class ManualInterventionActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    Instructions: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition7"]]
    ResponsibleTeams: Optional[str]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManualInterventionActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManualInterventionActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            Instructions=json_data.get("Instructions"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition7),
            ResponsibleTeams=json_data.get("ResponsibleTeams"),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManualInterventionActionDefinition = ManualInterventionActionDefinition


@dataclass
class PropertiesDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition7 = PropertiesDefinition7


@dataclass
class RunKubectlScriptActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition8"]]
    RunOnServer: Optional[bool]
    ScriptFileName: Optional[str]
    ScriptParameters: Optional[str]
    ScriptSource: Optional[str]
    TenantTags: Optional[Sequence[str]]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunKubectlScriptActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunKubectlScriptActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition8),
            RunOnServer=json_data.get("RunOnServer"),
            ScriptFileName=json_data.get("ScriptFileName"),
            ScriptParameters=json_data.get("ScriptParameters"),
            ScriptSource=json_data.get("ScriptSource"),
            TenantTags=json_data.get("TenantTags"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunKubectlScriptActionDefinition = RunKubectlScriptActionDefinition


@dataclass
class PropertiesDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition8 = PropertiesDefinition8


@dataclass
class RunScriptActionDefinition(BaseModel):
    CanBeUsedForProjectVersioning: Optional[bool]
    Channels: Optional[Sequence[str]]
    Condition: Optional[str]
    Environments: Optional[Sequence[str]]
    ExcludedEnvironments: Optional[Sequence[str]]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsRequired: Optional[bool]
    Name: Optional[str]
    Notes: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition9"]]
    RunOnServer: Optional[bool]
    ScriptBody: Optional[str]
    ScriptFileName: Optional[str]
    ScriptParameters: Optional[str]
    ScriptSource: Optional[str]
    ScriptSyntax: Optional[str]
    TenantTags: Optional[Sequence[str]]
    VariableSubstitutionInFiles: Optional[str]
    ActionTemplate: Optional[Sequence["_ActionTemplateDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Package: Optional[Sequence["_PackageDefinition"]]
    PrimaryPackage: Optional[Sequence["_PrimaryPackageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunScriptActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunScriptActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CanBeUsedForProjectVersioning=json_data.get("CanBeUsedForProjectVersioning"),
            Channels=json_data.get("Channels"),
            Condition=json_data.get("Condition"),
            Environments=json_data.get("Environments"),
            ExcludedEnvironments=json_data.get("ExcludedEnvironments"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsRequired=json_data.get("IsRequired"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition9),
            RunOnServer=json_data.get("RunOnServer"),
            ScriptBody=json_data.get("ScriptBody"),
            ScriptFileName=json_data.get("ScriptFileName"),
            ScriptParameters=json_data.get("ScriptParameters"),
            ScriptSource=json_data.get("ScriptSource"),
            ScriptSyntax=json_data.get("ScriptSyntax"),
            TenantTags=json_data.get("TenantTags"),
            VariableSubstitutionInFiles=json_data.get("VariableSubstitutionInFiles"),
            ActionTemplate=deserialize_list(json_data.get("ActionTemplate"), ActionTemplateDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Package=deserialize_list(json_data.get("Package"), PackageDefinition),
            PrimaryPackage=deserialize_list(json_data.get("PrimaryPackage"), PrimaryPackageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunScriptActionDefinition = RunScriptActionDefinition


@dataclass
class PropertiesDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition9 = PropertiesDefinition9


