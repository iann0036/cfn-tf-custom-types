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
    Account: Optional[Sequence["_AccountDefinition"]]
    AccountMoid: Optional[str]
    Action: Optional[str]
    AdditionalProperties: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    AssociatedObject: Optional[Sequence["_AssociatedObjectDefinition"]]
    ClassId: Optional[str]
    CleanupTime: Optional[str]
    CreateTime: Optional[str]
    DomainGroupMoid: Optional[str]
    Email: Optional[str]
    EndTime: Optional[str]
    FailedWorkflowCleanupDuration: Optional[float]
    Id: Optional[str]
    Input: Optional[Sequence["_InputDefinition"]]
    InstId: Optional[str]
    Internal: Optional[bool]
    LastAction: Optional[str]
    Message: Optional[Sequence["_MessageDefinition"]]
    MetaVersion: Optional[float]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Output: Optional[Sequence["_OutputDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    ParentTaskInfo: Optional[Sequence["_ParentTaskInfoDefinition"]]
    PauseReason: Optional[str]
    PendingDynamicWorkflowInfo: Optional[Sequence["_PendingDynamicWorkflowInfoDefinition"]]
    Permission: Optional[Sequence["_PermissionDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Progress: Optional[float]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    RetryFromTaskName: Optional[str]
    SharedScope: Optional[str]
    Src: Optional[str]
    StartTime: Optional[str]
    Status: Optional[str]
    SuccessWorkflowCleanupDuration: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskInfos: Optional[Sequence["_TaskInfosDefinition"]]
    TraceId: Optional[str]
    Type: Optional[str]
    UserActionRequired: Optional[bool]
    UserId: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    WaitReason: Optional[str]
    WorkflowCtx: Optional[Sequence["_WorkflowCtxDefinition3"]]
    WorkflowDefinition: Optional[Sequence["_WorkflowDefinitionDefinition"]]
    WorkflowMetaType: Optional[str]
    WorkflowTaskCount: Optional[float]
    WorkflowWorkerTaskCount: Optional[float]

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
            Account=deserialize_list(json_data.get("Account"), AccountDefinition),
            AccountMoid=json_data.get("AccountMoid"),
            Action=json_data.get("Action"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            AssociatedObject=deserialize_list(json_data.get("AssociatedObject"), AssociatedObjectDefinition),
            ClassId=json_data.get("ClassId"),
            CleanupTime=json_data.get("CleanupTime"),
            CreateTime=json_data.get("CreateTime"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            Email=json_data.get("Email"),
            EndTime=json_data.get("EndTime"),
            FailedWorkflowCleanupDuration=json_data.get("FailedWorkflowCleanupDuration"),
            Id=json_data.get("Id"),
            Input=deserialize_list(json_data.get("Input"), InputDefinition),
            InstId=json_data.get("InstId"),
            Internal=json_data.get("Internal"),
            LastAction=json_data.get("LastAction"),
            Message=deserialize_list(json_data.get("Message"), MessageDefinition),
            MetaVersion=json_data.get("MetaVersion"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Output=deserialize_list(json_data.get("Output"), OutputDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            ParentTaskInfo=deserialize_list(json_data.get("ParentTaskInfo"), ParentTaskInfoDefinition),
            PauseReason=json_data.get("PauseReason"),
            PendingDynamicWorkflowInfo=deserialize_list(json_data.get("PendingDynamicWorkflowInfo"), PendingDynamicWorkflowInfoDefinition),
            Permission=deserialize_list(json_data.get("Permission"), PermissionDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Progress=json_data.get("Progress"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            RetryFromTaskName=json_data.get("RetryFromTaskName"),
            SharedScope=json_data.get("SharedScope"),
            Src=json_data.get("Src"),
            StartTime=json_data.get("StartTime"),
            Status=json_data.get("Status"),
            SuccessWorkflowCleanupDuration=json_data.get("SuccessWorkflowCleanupDuration"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskInfos=deserialize_list(json_data.get("TaskInfos"), TaskInfosDefinition),
            TraceId=json_data.get("TraceId"),
            Type=json_data.get("Type"),
            UserActionRequired=json_data.get("UserActionRequired"),
            UserId=json_data.get("UserId"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            WaitReason=json_data.get("WaitReason"),
            WorkflowCtx=deserialize_list(json_data.get("WorkflowCtx"), WorkflowCtxDefinition3),
            WorkflowDefinition=deserialize_list(json_data.get("WorkflowDefinition"), WorkflowDefinitionDefinition),
            WorkflowMetaType=json_data.get("WorkflowMetaType"),
            WorkflowTaskCount=json_data.get("WorkflowTaskCount"),
            WorkflowWorkerTaskCount=json_data.get("WorkflowWorkerTaskCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountDefinition = AccountDefinition


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class AssociatedObjectDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedObjectDefinition = AssociatedObjectDefinition


@dataclass
class InputDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinition = InputDefinition


@dataclass
class MessageDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Message: Optional[str]
    ObjectType: Optional[str]
    Severity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MessageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Message=json_data.get("Message"),
            ObjectType=json_data.get("ObjectType"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageDefinition = MessageDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationDefinition = OrganizationDefinition


@dataclass
class OutputDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinition = OutputDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class ParentTaskInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentTaskInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentTaskInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentTaskInfoDefinition = ParentTaskInfoDefinition


@dataclass
class PendingDynamicWorkflowInfoDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PendingDynamicWorkflowInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PendingDynamicWorkflowInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PendingDynamicWorkflowInfoDefinition = PendingDynamicWorkflowInfoDefinition


@dataclass
class PermissionDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionDefinition = PermissionDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    Retryable: Optional[bool]
    RollbackAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            Retryable=json_data.get("Retryable"),
            RollbackAction=json_data.get("RollbackAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TaskInfosDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskInfosDefinition = TaskInfosDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


@dataclass
class WorkflowCtxDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InitiatorCtx: Optional[Sequence["_WorkflowCtxDefinition"]]
    ObjectType: Optional[str]
    TargetCtxList: Optional[Sequence["_WorkflowCtxDefinition2"]]
    WorkflowMetaName: Optional[str]
    WorkflowSubtype: Optional[str]
    WorkflowType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowCtxDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowCtxDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InitiatorCtx=deserialize_list(json_data.get("InitiatorCtx"), WorkflowCtxDefinition),
            ObjectType=json_data.get("ObjectType"),
            TargetCtxList=deserialize_list(json_data.get("TargetCtxList"), WorkflowCtxDefinition2),
            WorkflowMetaName=json_data.get("WorkflowMetaName"),
            WorkflowSubtype=json_data.get("WorkflowSubtype"),
            WorkflowType=json_data.get("WorkflowType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowCtxDefinition3 = WorkflowCtxDefinition3


@dataclass
class WorkflowCtxDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InitiatorMoid: Optional[str]
    InitiatorName: Optional[str]
    InitiatorType: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowCtxDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowCtxDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InitiatorMoid=json_data.get("InitiatorMoid"),
            InitiatorName=json_data.get("InitiatorName"),
            InitiatorType=json_data.get("InitiatorType"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowCtxDefinition = WorkflowCtxDefinition


@dataclass
class WorkflowCtxDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]
    TargetMoid: Optional[str]
    TargetName: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowCtxDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowCtxDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
            TargetMoid=json_data.get("TargetMoid"),
            TargetName=json_data.get("TargetName"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowCtxDefinition2 = WorkflowCtxDefinition2


@dataclass
class WorkflowDefinitionDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowDefinitionDefinition = WorkflowDefinitionDefinition


