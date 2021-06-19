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
    AppUrl: Optional[str]
    ArchiveUrl: Optional[str]
    AuthType: Optional[str]
    AvailabilityDomain: Optional[Sequence[str]]
    DeploymentFile: Optional[str]
    GitPassword: Optional[str]
    GitRepository: Optional[str]
    GitUsername: Optional[str]
    Id: Optional[str]
    LoadBalancerSubnets: Optional[Sequence[str]]
    ManifestFile: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    NotificationEmail: Optional[str]
    Region: Optional[str]
    Runtime: Optional[str]
    SubscriptionType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    WebUrl: Optional[str]
    Deployment: Optional[Sequence["_DeploymentDefinition"]]
    Manifest: Optional[Sequence["_ManifestDefinition"]]
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
            AppUrl=json_data.get("AppUrl"),
            ArchiveUrl=json_data.get("ArchiveUrl"),
            AuthType=json_data.get("AuthType"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            DeploymentFile=json_data.get("DeploymentFile"),
            GitPassword=json_data.get("GitPassword"),
            GitRepository=json_data.get("GitRepository"),
            GitUsername=json_data.get("GitUsername"),
            Id=json_data.get("Id"),
            LoadBalancerSubnets=json_data.get("LoadBalancerSubnets"),
            ManifestFile=json_data.get("ManifestFile"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Region=json_data.get("Region"),
            Runtime=json_data.get("Runtime"),
            SubscriptionType=json_data.get("SubscriptionType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            WebUrl=json_data.get("WebUrl"),
            Deployment=deserialize_list(json_data.get("Deployment"), DeploymentDefinition),
            Manifest=deserialize_list(json_data.get("Manifest"), ManifestDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class DeploymentDefinition(BaseModel):
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    Instances: Optional[float]
    JavaSystemProperties: Optional[Sequence["_JavaSystemPropertiesDefinition"]]
    Memory: Optional[str]
    Notes: Optional[str]
    SecureEnvironment: Optional[Sequence[str]]
    Services: Optional[Sequence["_ServicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentDefinition"]:
        if not json_data:
            return None
        return cls(
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            Instances=json_data.get("Instances"),
            JavaSystemProperties=deserialize_list(json_data.get("JavaSystemProperties"), JavaSystemPropertiesDefinition),
            Memory=json_data.get("Memory"),
            Notes=json_data.get("Notes"),
            SecureEnvironment=json_data.get("SecureEnvironment"),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentDefinition = DeploymentDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class JavaSystemPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JavaSystemPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JavaSystemPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JavaSystemPropertiesDefinition = JavaSystemPropertiesDefinition


@dataclass
class ServicesDefinition(BaseModel):
    Identifier: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Type: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Identifier=json_data.get("Identifier"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Type=json_data.get("Type"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesDefinition = ServicesDefinition


@dataclass
class ManifestDefinition(BaseModel):
    Clustered: Optional[bool]
    Command: Optional[str]
    HealthCheckEndpoint: Optional[str]
    Home: Optional[str]
    Mode: Optional[str]
    Notes: Optional[str]
    ShutdownTime: Optional[float]
    StartupTime: Optional[float]
    Type: Optional[str]
    Release: Optional[Sequence["_ReleaseDefinition"]]
    Runtime: Optional[Sequence["_RuntimeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManifestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManifestDefinition"]:
        if not json_data:
            return None
        return cls(
            Clustered=json_data.get("Clustered"),
            Command=json_data.get("Command"),
            HealthCheckEndpoint=json_data.get("HealthCheckEndpoint"),
            Home=json_data.get("Home"),
            Mode=json_data.get("Mode"),
            Notes=json_data.get("Notes"),
            ShutdownTime=json_data.get("ShutdownTime"),
            StartupTime=json_data.get("StartupTime"),
            Type=json_data.get("Type"),
            Release=deserialize_list(json_data.get("Release"), ReleaseDefinition),
            Runtime=deserialize_list(json_data.get("Runtime"), RuntimeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManifestDefinition = ManifestDefinition


@dataclass
class ReleaseDefinition(BaseModel):
    Build: Optional[str]
    Commit: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReleaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReleaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Build=json_data.get("Build"),
            Commit=json_data.get("Commit"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReleaseDefinition = ReleaseDefinition


@dataclass
class RuntimeDefinition(BaseModel):
    MajorVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeDefinition"]:
        if not json_data:
            return None
        return cls(
            MajorVersion=json_data.get("MajorVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeDefinition = RuntimeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


