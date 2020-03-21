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
    CreateTime: Optional[str]
    Description: Optional[str]
    Disabled: Optional[bool]
    Filename: Optional[str]
    Id: Optional[str]
    IgnoredFiles: Optional[Sequence[str]]
    IncludedFiles: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    Substitutions: Optional[Sequence["_Substitutions"]]
    TriggerId: Optional[str]
    Build: Optional[Sequence["_Build"]]
    Timeouts: Optional["_Timeouts"]
    TriggerTemplate: Optional[Sequence["_TriggerTemplate"]]
    Step: Optional[Sequence["_Step"]]
    Volumes: Optional[Sequence["_Volumes"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Substitutions=json_data.get("Substitutions"),
            TriggerId=json_data.get("TriggerId"),
            Build=json_data.get("Build"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            TriggerTemplate=json_data.get("TriggerTemplate"),
            Step=json_data.get("Step"),
            Volumes=json_data.get("Volumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Substitutions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Substitutions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Substitutions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Substitutions = Substitutions


@dataclass
class Build:
    Images: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    Timeout: Optional[str]
    Step: Optional[Sequence["_Step"]]

    @classmethod
    def _deserialize(
        cls: Type["_Build"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Build"]:
        if not json_data:
            return None
        return cls(
            Images=json_data.get("Images"),
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            Step=json_data.get("Step"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Build = Build


@dataclass
class Step:
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
    Volumes: Optional[Sequence["_Volumes"]]

    @classmethod
    def _deserialize(
        cls: Type["_Step"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Step"]:
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
            Volumes=json_data.get("Volumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Step = Step


@dataclass
class Volumes:
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volumes"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volumes = Volumes


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


@dataclass
class TriggerTemplate:
    BranchName: Optional[str]
    CommitSha: Optional[str]
    Dir: Optional[str]
    ProjectId: Optional[str]
    RepoName: Optional[str]
    TagName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerTemplate"]:
        if not json_data:
            return None
        return cls(
            BranchName=json_data.get("BranchName"),
            CommitSha=json_data.get("CommitSha"),
            Dir=json_data.get("Dir"),
            ProjectId=json_data.get("ProjectId"),
            RepoName=json_data.get("RepoName"),
            TagName=json_data.get("TagName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerTemplate = TriggerTemplate


