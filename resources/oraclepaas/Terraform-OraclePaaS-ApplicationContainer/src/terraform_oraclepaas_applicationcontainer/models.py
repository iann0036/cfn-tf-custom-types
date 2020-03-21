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
    Runtime: Optional[Sequence["_Runtime"]]
    SubscriptionType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    WebUrl: Optional[str]
    Deployment: Optional[Sequence["_Deployment"]]
    Manifest: Optional[Sequence["_Manifest"]]
    Timeouts: Optional["_Timeouts"]
    Services: Optional[Sequence["_Services"]]
    Release: Optional[Sequence["_Release"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            WebUrl=json_data.get("WebUrl"),
            Deployment=json_data.get("Deployment"),
            Manifest=json_data.get("Manifest"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Services=json_data.get("Services"),
            Release=json_data.get("Release"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Runtime:
    MajorVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Runtime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Runtime"]:
        if not json_data:
            return None
        return cls(
            MajorVersion=json_data.get("MajorVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Runtime = Runtime


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Deployment:
    Environment: Optional[Sequence["_Environment"]]
    Instances: Optional[float]
    JavaSystemProperties: Optional[Sequence["_JavaSystemProperties"]]
    Memory: Optional[str]
    Notes: Optional[str]
    SecureEnvironment: Optional[Sequence[str]]
    Services: Optional[Sequence["_Services"]]

    @classmethod
    def _deserialize(
        cls: Type["_Deployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deployment"]:
        if not json_data:
            return None
        return cls(
            Environment=json_data.get("Environment"),
            Instances=json_data.get("Instances"),
            JavaSystemProperties=json_data.get("JavaSystemProperties"),
            Memory=json_data.get("Memory"),
            Notes=json_data.get("Notes"),
            SecureEnvironment=json_data.get("SecureEnvironment"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deployment = Deployment


@dataclass
class Environment:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class JavaSystemProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JavaSystemProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JavaSystemProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JavaSystemProperties = JavaSystemProperties


@dataclass
class Services:
    Identifier: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Type: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Services"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Services"]:
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
_Services = Services


@dataclass
class Manifest:
    Clustered: Optional[bool]
    Command: Optional[str]
    HealthCheckEndpoint: Optional[str]
    Home: Optional[str]
    Mode: Optional[str]
    Notes: Optional[str]
    ShutdownTime: Optional[float]
    StartupTime: Optional[float]
    Type: Optional[str]
    Release: Optional[Sequence["_Release"]]
    Runtime: Optional[Sequence["_Runtime"]]

    @classmethod
    def _deserialize(
        cls: Type["_Manifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Manifest"]:
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
            Release=json_data.get("Release"),
            Runtime=json_data.get("Runtime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Manifest = Manifest


@dataclass
class Release:
    Build: Optional[str]
    Commit: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Release"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Release"]:
        if not json_data:
            return None
        return cls(
            Build=json_data.get("Build"),
            Commit=json_data.get("Commit"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Release = Release


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


