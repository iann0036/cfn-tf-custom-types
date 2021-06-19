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
    CreateTime: Optional[str]
    Description: Optional[str]
    Disabled: Optional[bool]
    Filename: Optional[str]
    Id: Optional[str]
    IgnoredFiles: Optional[Sequence[str]]
    IncludedFiles: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    Substitutions: Optional[Sequence["_SubstitutionsDefinition"]]
    Tags: Optional[Sequence[str]]
    TriggerId: Optional[str]
    Build: Optional[Sequence["_BuildDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TriggerTemplate: Optional[Sequence["_TriggerTemplateDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Filename=json_data.get("Filename"),
            Id=json_data.get("Id"),
            IgnoredFiles=json_data.get("IgnoredFiles"),
            IncludedFiles=json_data.get("IncludedFiles"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Substitutions=deserialize_list(json_data.get("Substitutions"), SubstitutionsDefinition),
            Tags=json_data.get("Tags"),
            TriggerId=json_data.get("TriggerId"),
            Build=deserialize_list(json_data.get("Build"), BuildDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TriggerTemplate=deserialize_list(json_data.get("TriggerTemplate"), TriggerTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubstitutionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubstitutionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubstitutionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubstitutionsDefinition = SubstitutionsDefinition


@dataclass
class BuildDefinition(BaseModel):
    Images: Optional[Sequence[str]]
    LogsBucket: Optional[str]
    QueueTtl: Optional[str]
    Substitutions: Optional[Sequence["_SubstitutionsDefinition2"]]
    Tags: Optional[Sequence[str]]
    Timeout: Optional[str]
    Artifacts: Optional[Sequence["_ArtifactsDefinition"]]
    Options: Optional[Sequence["_OptionsDefinition"]]
    Secret: Optional[Sequence["_SecretDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
    Step: Optional[Sequence["_StepDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BuildDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildDefinition"]:
        if not json_data:
            return None
        return cls(
            Images=json_data.get("Images"),
            LogsBucket=json_data.get("LogsBucket"),
            QueueTtl=json_data.get("QueueTtl"),
            Substitutions=deserialize_list(json_data.get("Substitutions"), SubstitutionsDefinition2),
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            Artifacts=deserialize_list(json_data.get("Artifacts"), ArtifactsDefinition),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            Step=deserialize_list(json_data.get("Step"), StepDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildDefinition = BuildDefinition


@dataclass
class SubstitutionsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubstitutionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubstitutionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubstitutionsDefinition2 = SubstitutionsDefinition2


@dataclass
class ArtifactsDefinition(BaseModel):
    Images: Optional[Sequence[str]]
    Objects: Optional[Sequence["_ObjectsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactsDefinition"]:
        if not json_data:
            return None
        return cls(
            Images=json_data.get("Images"),
            Objects=deserialize_list(json_data.get("Objects"), ObjectsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactsDefinition = ArtifactsDefinition


@dataclass
class ObjectsDefinition(BaseModel):
    Location: Optional[str]
    Paths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectsDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Paths=json_data.get("Paths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectsDefinition = ObjectsDefinition


@dataclass
class OptionsDefinition(BaseModel):
    DiskSizeGb: Optional[float]
    DynamicSubstitutions: Optional[bool]
    Env: Optional[Sequence[str]]
    LogStreamingOption: Optional[str]
    Logging: Optional[str]
    MachineType: Optional[str]
    RequestedVerifyOption: Optional[str]
    SecretEnv: Optional[Sequence[str]]
    SourceProvenanceHash: Optional[Sequence[str]]
    SubstitutionOption: Optional[str]
    WorkerPool: Optional[str]
    Volumes: Optional[Sequence["_VolumesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DynamicSubstitutions=json_data.get("DynamicSubstitutions"),
            Env=json_data.get("Env"),
            LogStreamingOption=json_data.get("LogStreamingOption"),
            Logging=json_data.get("Logging"),
            MachineType=json_data.get("MachineType"),
            RequestedVerifyOption=json_data.get("RequestedVerifyOption"),
            SecretEnv=json_data.get("SecretEnv"),
            SourceProvenanceHash=json_data.get("SourceProvenanceHash"),
            SubstitutionOption=json_data.get("SubstitutionOption"),
            WorkerPool=json_data.get("WorkerPool"),
            Volumes=deserialize_list(json_data.get("Volumes"), VolumesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class VolumesDefinition(BaseModel):
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumesDefinition = VolumesDefinition


@dataclass
class SecretDefinition(BaseModel):
    KmsKeyName: Optional[str]
    SecretEnv: Optional[Sequence["_SecretEnvDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
            SecretEnv=deserialize_list(json_data.get("SecretEnv"), SecretEnvDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretDefinition = SecretDefinition


@dataclass
class SecretEnvDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretEnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretEnvDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretEnvDefinition = SecretEnvDefinition


@dataclass
class SourceDefinition(BaseModel):
    RepoSource: Optional[Sequence["_RepoSourceDefinition"]]
    StorageSource: Optional[Sequence["_StorageSourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            RepoSource=deserialize_list(json_data.get("RepoSource"), RepoSourceDefinition),
            StorageSource=deserialize_list(json_data.get("StorageSource"), StorageSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class RepoSourceDefinition(BaseModel):
    BranchName: Optional[str]
    CommitSha: Optional[str]
    Dir: Optional[str]
    InvertRegex: Optional[bool]
    ProjectId: Optional[str]
    RepoName: Optional[str]
    Substitutions: Optional[Sequence["_SubstitutionsDefinition3"]]
    TagName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepoSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepoSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            BranchName=json_data.get("BranchName"),
            CommitSha=json_data.get("CommitSha"),
            Dir=json_data.get("Dir"),
            InvertRegex=json_data.get("InvertRegex"),
            ProjectId=json_data.get("ProjectId"),
            RepoName=json_data.get("RepoName"),
            Substitutions=deserialize_list(json_data.get("Substitutions"), SubstitutionsDefinition3),
            TagName=json_data.get("TagName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepoSourceDefinition = RepoSourceDefinition


@dataclass
class SubstitutionsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubstitutionsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubstitutionsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubstitutionsDefinition3 = SubstitutionsDefinition3


@dataclass
class StorageSourceDefinition(BaseModel):
    Bucket: Optional[str]
    Generation: Optional[str]
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Generation=json_data.get("Generation"),
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageSourceDefinition = StorageSourceDefinition


@dataclass
class StepDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Dir: Optional[str]
    Entrypoint: Optional[str]
    Env: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    SecretEnv: Optional[Sequence[str]]
    Timeout: Optional[str]
    Timing: Optional[str]
    WaitFor: Optional[Sequence[str]]
    Volumes: Optional[Sequence["_VolumesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Dir=json_data.get("Dir"),
            Entrypoint=json_data.get("Entrypoint"),
            Env=json_data.get("Env"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SecretEnv=json_data.get("SecretEnv"),
            Timeout=json_data.get("Timeout"),
            Timing=json_data.get("Timing"),
            WaitFor=json_data.get("WaitFor"),
            Volumes=deserialize_list(json_data.get("Volumes"), VolumesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition = StepDefinition


@dataclass
class GithubDefinition(BaseModel):
    Name: Optional[str]
    Owner: Optional[str]
    PullRequest: Optional[Sequence["_PullRequestDefinition"]]
    Push: Optional[Sequence["_PushDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GithubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            PullRequest=deserialize_list(json_data.get("PullRequest"), PullRequestDefinition),
            Push=deserialize_list(json_data.get("Push"), PushDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubDefinition = GithubDefinition


@dataclass
class PullRequestDefinition(BaseModel):
    Branch: Optional[str]
    CommentControl: Optional[str]
    InvertRegex: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PullRequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PullRequestDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            CommentControl=json_data.get("CommentControl"),
            InvertRegex=json_data.get("InvertRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PullRequestDefinition = PullRequestDefinition


@dataclass
class PushDefinition(BaseModel):
    Branch: Optional[str]
    InvertRegex: Optional[bool]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PushDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PushDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            InvertRegex=json_data.get("InvertRegex"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PushDefinition = PushDefinition


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


@dataclass
class TriggerTemplateDefinition(BaseModel):
    BranchName: Optional[str]
    CommitSha: Optional[str]
    Dir: Optional[str]
    InvertRegex: Optional[bool]
    ProjectId: Optional[str]
    RepoName: Optional[str]
    TagName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            BranchName=json_data.get("BranchName"),
            CommitSha=json_data.get("CommitSha"),
            Dir=json_data.get("Dir"),
            InvertRegex=json_data.get("InvertRegex"),
            ProjectId=json_data.get("ProjectId"),
            RepoName=json_data.get("RepoName"),
            TagName=json_data.get("TagName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerTemplateDefinition = TriggerTemplateDefinition


