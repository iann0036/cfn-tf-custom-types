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
    Arn: Optional[str]
    BadgeEnabled: Optional[bool]
    BadgeUrl: Optional[str]
    BuildTimeout: Optional[float]
    Description: Optional[str]
    EncryptionKey: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    QueuedTimeout: Optional[float]
    ServiceRole: Optional[str]
    SourceVersion: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Artifacts: Optional[Sequence["_Artifacts"]]
    Cache: Optional[Sequence["_Cache"]]
    Environment: Optional[Sequence["_Environment"]]
    LogsConfig: Optional[Sequence["_LogsConfig"]]
    SecondaryArtifacts: Optional[Sequence["_SecondaryArtifacts"]]
    SecondarySources: Optional[Sequence["_SecondarySources"]]
    Source: Optional[Sequence["_Source"]]
    VpcConfig: Optional[Sequence["_VpcConfig"]]
    EnvironmentVariable: Optional[Sequence["_EnvironmentVariable"]]
    RegistryCredential: Optional[Sequence["_RegistryCredential"]]
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogs"]]
    S3Logs: Optional[Sequence["_S3Logs"]]
    Auth: Optional[Sequence["_Auth"]]
    GitSubmodulesConfig: Optional[Sequence["_GitSubmodulesConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            BadgeEnabled=json_data.get("BadgeEnabled"),
            BadgeUrl=json_data.get("BadgeUrl"),
            BuildTimeout=json_data.get("BuildTimeout"),
            Description=json_data.get("Description"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            QueuedTimeout=json_data.get("QueuedTimeout"),
            ServiceRole=json_data.get("ServiceRole"),
            SourceVersion=json_data.get("SourceVersion"),
            Tags=json_data.get("Tags"),
            Artifacts=json_data.get("Artifacts"),
            Cache=json_data.get("Cache"),
            Environment=json_data.get("Environment"),
            LogsConfig=json_data.get("LogsConfig"),
            SecondaryArtifacts=json_data.get("SecondaryArtifacts"),
            SecondarySources=json_data.get("SecondarySources"),
            Source=json_data.get("Source"),
            VpcConfig=json_data.get("VpcConfig"),
            EnvironmentVariable=json_data.get("EnvironmentVariable"),
            RegistryCredential=json_data.get("RegistryCredential"),
            CloudwatchLogs=json_data.get("CloudwatchLogs"),
            S3Logs=json_data.get("S3Logs"),
            Auth=json_data.get("Auth"),
            GitSubmodulesConfig=json_data.get("GitSubmodulesConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Artifacts:
    ArtifactIdentifier: Optional[str]
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    NamespaceType: Optional[str]
    OverrideArtifactName: Optional[bool]
    Packaging: Optional[str]
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Artifacts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Artifacts"]:
        if not json_data:
            return None
        return cls(
            ArtifactIdentifier=json_data.get("ArtifactIdentifier"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NamespaceType=json_data.get("NamespaceType"),
            OverrideArtifactName=json_data.get("OverrideArtifactName"),
            Packaging=json_data.get("Packaging"),
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Artifacts = Artifacts


@dataclass
class Cache:
    Location: Optional[str]
    Modes: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cache"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cache"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Modes=json_data.get("Modes"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cache = Cache


@dataclass
class Environment:
    Certificate: Optional[str]
    ComputeType: Optional[str]
    Image: Optional[str]
    ImagePullCredentialsType: Optional[str]
    PrivilegedMode: Optional[bool]
    Type: Optional[str]
    EnvironmentVariable: Optional[Sequence["_EnvironmentVariable"]]
    RegistryCredential: Optional[Sequence["_RegistryCredential"]]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ComputeType=json_data.get("ComputeType"),
            Image=json_data.get("Image"),
            ImagePullCredentialsType=json_data.get("ImagePullCredentialsType"),
            PrivilegedMode=json_data.get("PrivilegedMode"),
            Type=json_data.get("Type"),
            EnvironmentVariable=json_data.get("EnvironmentVariable"),
            RegistryCredential=json_data.get("RegistryCredential"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class EnvironmentVariable:
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariable = EnvironmentVariable


@dataclass
class RegistryCredential:
    Credential: Optional[str]
    CredentialProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryCredential"]:
        if not json_data:
            return None
        return cls(
            Credential=json_data.get("Credential"),
            CredentialProvider=json_data.get("CredentialProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryCredential = RegistryCredential


@dataclass
class LogsConfig:
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogs"]]
    S3Logs: Optional[Sequence["_S3Logs"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsConfig"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogs=json_data.get("CloudwatchLogs"),
            S3Logs=json_data.get("S3Logs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsConfig = LogsConfig


@dataclass
class CloudwatchLogs:
    GroupName: Optional[str]
    Status: Optional[str]
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLogs"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Status=json_data.get("Status"),
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLogs = CloudwatchLogs


@dataclass
class S3Logs:
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Logs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Logs"]:
        if not json_data:
            return None
        return cls(
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Logs = S3Logs


@dataclass
class SecondaryArtifacts:
    ArtifactIdentifier: Optional[str]
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    NamespaceType: Optional[str]
    OverrideArtifactName: Optional[bool]
    Packaging: Optional[str]
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryArtifacts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryArtifacts"]:
        if not json_data:
            return None
        return cls(
            ArtifactIdentifier=json_data.get("ArtifactIdentifier"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NamespaceType=json_data.get("NamespaceType"),
            OverrideArtifactName=json_data.get("OverrideArtifactName"),
            Packaging=json_data.get("Packaging"),
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryArtifacts = SecondaryArtifacts


@dataclass
class SecondarySources:
    Buildspec: Optional[str]
    GitCloneDepth: Optional[float]
    InsecureSsl: Optional[bool]
    Location: Optional[str]
    ReportBuildStatus: Optional[bool]
    SourceIdentifier: Optional[str]
    Type: Optional[str]
    Auth: Optional[Sequence["_Auth"]]
    GitSubmodulesConfig: Optional[Sequence["_GitSubmodulesConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondarySources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondarySources"]:
        if not json_data:
            return None
        return cls(
            Buildspec=json_data.get("Buildspec"),
            GitCloneDepth=json_data.get("GitCloneDepth"),
            InsecureSsl=json_data.get("InsecureSsl"),
            Location=json_data.get("Location"),
            ReportBuildStatus=json_data.get("ReportBuildStatus"),
            SourceIdentifier=json_data.get("SourceIdentifier"),
            Type=json_data.get("Type"),
            Auth=json_data.get("Auth"),
            GitSubmodulesConfig=json_data.get("GitSubmodulesConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondarySources = SecondarySources


@dataclass
class Auth:
    Resource: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Auth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Auth"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Auth = Auth


@dataclass
class GitSubmodulesConfig:
    FetchSubmodules: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GitSubmodulesConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitSubmodulesConfig"]:
        if not json_data:
            return None
        return cls(
            FetchSubmodules=json_data.get("FetchSubmodules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitSubmodulesConfig = GitSubmodulesConfig


@dataclass
class Source:
    Buildspec: Optional[str]
    GitCloneDepth: Optional[float]
    InsecureSsl: Optional[bool]
    Location: Optional[str]
    ReportBuildStatus: Optional[bool]
    Type: Optional[str]
    Auth: Optional[Sequence["_Auth"]]
    GitSubmodulesConfig: Optional[Sequence["_GitSubmodulesConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Buildspec=json_data.get("Buildspec"),
            GitCloneDepth=json_data.get("GitCloneDepth"),
            InsecureSsl=json_data.get("InsecureSsl"),
            Location=json_data.get("Location"),
            ReportBuildStatus=json_data.get("ReportBuildStatus"),
            Type=json_data.get("Type"),
            Auth=json_data.get("Auth"),
            GitSubmodulesConfig=json_data.get("GitSubmodulesConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class VpcConfig:
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


