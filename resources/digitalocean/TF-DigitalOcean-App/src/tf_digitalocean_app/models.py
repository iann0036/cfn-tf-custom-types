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
    ActiveDeploymentId: Optional[str]
    CreatedAt: Optional[str]
    DefaultIngress: Optional[str]
    Id: Optional[str]
    LiveUrl: Optional[str]
    UpdatedAt: Optional[str]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            ActiveDeploymentId=json_data.get("ActiveDeploymentId"),
            CreatedAt=json_data.get("CreatedAt"),
            DefaultIngress=json_data.get("DefaultIngress"),
            Id=json_data.get("Id"),
            LiveUrl=json_data.get("LiveUrl"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SpecDefinition(BaseModel):
    Domains: Optional[Sequence[str]]
    Name: Optional[str]
    Region: Optional[str]
    Database: Optional[Sequence["_DatabaseDefinition"]]
    Domain: Optional[Sequence["_DomainDefinition"]]
    Env: Optional[Sequence["_EnvDefinition"]]
    Job: Optional[Sequence["_JobDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    StaticSite: Optional[Sequence["_StaticSiteDefinition"]]
    Worker: Optional[Sequence["_WorkerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Domains=json_data.get("Domains"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Domain=deserialize_list(json_data.get("Domain"), DomainDefinition),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            Job=deserialize_list(json_data.get("Job"), JobDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            StaticSite=deserialize_list(json_data.get("StaticSite"), StaticSiteDefinition),
            Worker=deserialize_list(json_data.get("Worker"), WorkerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    ClusterName: Optional[str]
    DbName: Optional[str]
    DbUser: Optional[str]
    Engine: Optional[str]
    Name: Optional[str]
    Production: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterName=json_data.get("ClusterName"),
            DbName=json_data.get("DbName"),
            DbUser=json_data.get("DbUser"),
            Engine=json_data.get("Engine"),
            Name=json_data.get("Name"),
            Production=json_data.get("Production"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class DomainDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Wildcard: Optional[bool]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Wildcard=json_data.get("Wildcard"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainDefinition = DomainDefinition


@dataclass
class EnvDefinition(BaseModel):
    Key: Optional[str]
    Scope: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Scope=json_data.get("Scope"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvDefinition = EnvDefinition


@dataclass
class JobDefinition(BaseModel):
    BuildCommand: Optional[str]
    DockerfilePath: Optional[str]
    EnvironmentSlug: Optional[str]
    InstanceCount: Optional[float]
    InstanceSizeSlug: Optional[str]
    Kind: Optional[str]
    Name: Optional[str]
    RunCommand: Optional[str]
    SourceDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    Git: Optional[Sequence["_GitDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gitlab: Optional[Sequence["_GitlabDefinition"]]
    Image: Optional[Sequence["_ImageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildCommand=json_data.get("BuildCommand"),
            DockerfilePath=json_data.get("DockerfilePath"),
            EnvironmentSlug=json_data.get("EnvironmentSlug"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceSizeSlug=json_data.get("InstanceSizeSlug"),
            Kind=json_data.get("Kind"),
            Name=json_data.get("Name"),
            RunCommand=json_data.get("RunCommand"),
            SourceDir=json_data.get("SourceDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            Git=deserialize_list(json_data.get("Git"), GitDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gitlab=deserialize_list(json_data.get("Gitlab"), GitlabDefinition),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobDefinition = JobDefinition


@dataclass
class GitDefinition(BaseModel):
    Branch: Optional[str]
    RepoCloneUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            RepoCloneUrl=json_data.get("RepoCloneUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitDefinition = GitDefinition


@dataclass
class GithubDefinition(BaseModel):
    Branch: Optional[str]
    DeployOnPush: Optional[bool]
    Repo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GithubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            DeployOnPush=json_data.get("DeployOnPush"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubDefinition = GithubDefinition


@dataclass
class GitlabDefinition(BaseModel):
    Branch: Optional[str]
    DeployOnPush: Optional[bool]
    Repo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitlabDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitlabDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            DeployOnPush=json_data.get("DeployOnPush"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitlabDefinition = GitlabDefinition


@dataclass
class ImageDefinition(BaseModel):
    Registry: Optional[str]
    RegistryType: Optional[str]
    Repository: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Registry=json_data.get("Registry"),
            RegistryType=json_data.get("RegistryType"),
            Repository=json_data.get("Repository"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinition = ImageDefinition


@dataclass
class ServiceDefinition(BaseModel):
    BuildCommand: Optional[str]
    DockerfilePath: Optional[str]
    EnvironmentSlug: Optional[str]
    HttpPort: Optional[float]
    InstanceCount: Optional[float]
    InstanceSizeSlug: Optional[str]
    InternalPorts: Optional[Sequence[float]]
    Name: Optional[str]
    RunCommand: Optional[str]
    SourceDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    Git: Optional[Sequence["_GitDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gitlab: Optional[Sequence["_GitlabDefinition"]]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Image: Optional[Sequence["_ImageDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildCommand=json_data.get("BuildCommand"),
            DockerfilePath=json_data.get("DockerfilePath"),
            EnvironmentSlug=json_data.get("EnvironmentSlug"),
            HttpPort=json_data.get("HttpPort"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceSizeSlug=json_data.get("InstanceSizeSlug"),
            InternalPorts=json_data.get("InternalPorts"),
            Name=json_data.get("Name"),
            RunCommand=json_data.get("RunCommand"),
            SourceDir=json_data.get("SourceDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            Git=deserialize_list(json_data.get("Git"), GitDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gitlab=deserialize_list(json_data.get("Gitlab"), GitlabDefinition),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class HealthCheckDefinition(BaseModel):
    FailureThreshold: Optional[float]
    HttpPath: Optional[str]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            HttpPath=json_data.get("HttpPath"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class RoutesDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutesDefinition = RoutesDefinition


@dataclass
class StaticSiteDefinition(BaseModel):
    BuildCommand: Optional[str]
    CatchallDocument: Optional[str]
    DockerfilePath: Optional[str]
    EnvironmentSlug: Optional[str]
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]
    Name: Optional[str]
    OutputDir: Optional[str]
    SourceDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    Git: Optional[Sequence["_GitDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gitlab: Optional[Sequence["_GitlabDefinition"]]
    Routes: Optional[Sequence["_RoutesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StaticSiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticSiteDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildCommand=json_data.get("BuildCommand"),
            CatchallDocument=json_data.get("CatchallDocument"),
            DockerfilePath=json_data.get("DockerfilePath"),
            EnvironmentSlug=json_data.get("EnvironmentSlug"),
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
            Name=json_data.get("Name"),
            OutputDir=json_data.get("OutputDir"),
            SourceDir=json_data.get("SourceDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            Git=deserialize_list(json_data.get("Git"), GitDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gitlab=deserialize_list(json_data.get("Gitlab"), GitlabDefinition),
            Routes=deserialize_list(json_data.get("Routes"), RoutesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticSiteDefinition = StaticSiteDefinition


@dataclass
class WorkerDefinition(BaseModel):
    BuildCommand: Optional[str]
    DockerfilePath: Optional[str]
    EnvironmentSlug: Optional[str]
    InstanceCount: Optional[float]
    InstanceSizeSlug: Optional[str]
    Name: Optional[str]
    RunCommand: Optional[str]
    SourceDir: Optional[str]
    Env: Optional[Sequence["_EnvDefinition"]]
    Git: Optional[Sequence["_GitDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    Gitlab: Optional[Sequence["_GitlabDefinition"]]
    Image: Optional[Sequence["_ImageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildCommand=json_data.get("BuildCommand"),
            DockerfilePath=json_data.get("DockerfilePath"),
            EnvironmentSlug=json_data.get("EnvironmentSlug"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceSizeSlug=json_data.get("InstanceSizeSlug"),
            Name=json_data.get("Name"),
            RunCommand=json_data.get("RunCommand"),
            SourceDir=json_data.get("SourceDir"),
            Env=deserialize_list(json_data.get("Env"), EnvDefinition),
            Git=deserialize_list(json_data.get("Git"), GitDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            Gitlab=deserialize_list(json_data.get("Gitlab"), GitlabDefinition),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerDefinition = WorkerDefinition


