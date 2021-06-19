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
    Arn: Optional[str]
    BadgeEnabled: Optional[bool]
    BadgeUrl: Optional[str]
    BuildTimeout: Optional[float]
    ConcurrentBuildLimit: Optional[float]
    Description: Optional[str]
    EncryptionKey: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    QueuedTimeout: Optional[float]
    ServiceRole: Optional[str]
    SourceVersion: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Artifacts: Optional[Sequence["_ArtifactsDefinition"]]
    BuildBatchConfig: Optional[Sequence["_BuildBatchConfigDefinition"]]
    Cache: Optional[Sequence["_CacheDefinition"]]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    FileSystemLocations: Optional[Sequence["_FileSystemLocationsDefinition"]]
    LogsConfig: Optional[Sequence["_LogsConfigDefinition"]]
    SecondaryArtifacts: Optional[Sequence["_SecondaryArtifactsDefinition"]]
    SecondarySources: Optional[Sequence["_SecondarySourcesDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

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
            Arn=json_data.get("Arn"),
            BadgeEnabled=json_data.get("BadgeEnabled"),
            BadgeUrl=json_data.get("BadgeUrl"),
            BuildTimeout=json_data.get("BuildTimeout"),
            ConcurrentBuildLimit=json_data.get("ConcurrentBuildLimit"),
            Description=json_data.get("Description"),
            EncryptionKey=json_data.get("EncryptionKey"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            QueuedTimeout=json_data.get("QueuedTimeout"),
            ServiceRole=json_data.get("ServiceRole"),
            SourceVersion=json_data.get("SourceVersion"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Artifacts=deserialize_list(json_data.get("Artifacts"), ArtifactsDefinition),
            BuildBatchConfig=deserialize_list(json_data.get("BuildBatchConfig"), BuildBatchConfigDefinition),
            Cache=deserialize_list(json_data.get("Cache"), CacheDefinition),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            FileSystemLocations=deserialize_list(json_data.get("FileSystemLocations"), FileSystemLocationsDefinition),
            LogsConfig=deserialize_list(json_data.get("LogsConfig"), LogsConfigDefinition),
            SecondaryArtifacts=deserialize_list(json_data.get("SecondaryArtifacts"), SecondaryArtifactsDefinition),
            SecondarySources=deserialize_list(json_data.get("SecondarySources"), SecondarySourcesDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class ArtifactsDefinition(BaseModel):
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
        cls: Type["_ArtifactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactsDefinition"]:
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
_ArtifactsDefinition = ArtifactsDefinition


@dataclass
class BuildBatchConfigDefinition(BaseModel):
    CombineArtifacts: Optional[bool]
    ServiceRole: Optional[str]
    TimeoutInMins: Optional[float]
    Restrictions: Optional[Sequence["_RestrictionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BuildBatchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildBatchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CombineArtifacts=json_data.get("CombineArtifacts"),
            ServiceRole=json_data.get("ServiceRole"),
            TimeoutInMins=json_data.get("TimeoutInMins"),
            Restrictions=deserialize_list(json_data.get("Restrictions"), RestrictionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildBatchConfigDefinition = BuildBatchConfigDefinition


@dataclass
class RestrictionsDefinition(BaseModel):
    ComputeTypesAllowed: Optional[Sequence[str]]
    MaximumBuildsAllowed: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ComputeTypesAllowed=json_data.get("ComputeTypesAllowed"),
            MaximumBuildsAllowed=json_data.get("MaximumBuildsAllowed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionsDefinition = RestrictionsDefinition


@dataclass
class CacheDefinition(BaseModel):
    Location: Optional[str]
    Modes: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Modes=json_data.get("Modes"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheDefinition = CacheDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    Certificate: Optional[str]
    ComputeType: Optional[str]
    Image: Optional[str]
    ImagePullCredentialsType: Optional[str]
    PrivilegedMode: Optional[bool]
    Type: Optional[str]
    EnvironmentVariable: Optional[Sequence["_EnvironmentVariableDefinition"]]
    RegistryCredential: Optional[Sequence["_RegistryCredentialDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ComputeType=json_data.get("ComputeType"),
            Image=json_data.get("Image"),
            ImagePullCredentialsType=json_data.get("ImagePullCredentialsType"),
            PrivilegedMode=json_data.get("PrivilegedMode"),
            Type=json_data.get("Type"),
            EnvironmentVariable=deserialize_list(json_data.get("EnvironmentVariable"), EnvironmentVariableDefinition),
            RegistryCredential=deserialize_list(json_data.get("RegistryCredential"), RegistryCredentialDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class EnvironmentVariableDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariableDefinition = EnvironmentVariableDefinition


@dataclass
class RegistryCredentialDefinition(BaseModel):
    Credential: Optional[str]
    CredentialProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            Credential=json_data.get("Credential"),
            CredentialProvider=json_data.get("CredentialProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryCredentialDefinition = RegistryCredentialDefinition


@dataclass
class FileSystemLocationsDefinition(BaseModel):
    Identifier: Optional[str]
    Location: Optional[str]
    MountOptions: Optional[str]
    MountPoint: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemLocationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemLocationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Identifier=json_data.get("Identifier"),
            Location=json_data.get("Location"),
            MountOptions=json_data.get("MountOptions"),
            MountPoint=json_data.get("MountPoint"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemLocationsDefinition = FileSystemLocationsDefinition


@dataclass
class LogsConfigDefinition(BaseModel):
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogsDefinition"]]
    S3Logs: Optional[Sequence["_S3LogsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogs=deserialize_list(json_data.get("CloudwatchLogs"), CloudwatchLogsDefinition),
            S3Logs=deserialize_list(json_data.get("S3Logs"), S3LogsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsConfigDefinition = LogsConfigDefinition


@dataclass
class CloudwatchLogsDefinition(BaseModel):
    GroupName: Optional[str]
    Status: Optional[str]
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Status=json_data.get("Status"),
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLogsDefinition = CloudwatchLogsDefinition


@dataclass
class S3LogsDefinition(BaseModel):
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3LogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3LogsDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3LogsDefinition = S3LogsDefinition


@dataclass
class SecondaryArtifactsDefinition(BaseModel):
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
        cls: Type["_SecondaryArtifactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryArtifactsDefinition"]:
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
_SecondaryArtifactsDefinition = SecondaryArtifactsDefinition


@dataclass
class SecondarySourcesDefinition(BaseModel):
    Buildspec: Optional[str]
    GitCloneDepth: Optional[float]
    InsecureSsl: Optional[bool]
    Location: Optional[str]
    ReportBuildStatus: Optional[bool]
    SourceIdentifier: Optional[str]
    Type: Optional[str]
    Auth: Optional[Sequence["_AuthDefinition"]]
    BuildStatusConfig: Optional[Sequence["_BuildStatusConfigDefinition"]]
    GitSubmodulesConfig: Optional[Sequence["_GitSubmodulesConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondarySourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondarySourcesDefinition"]:
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
            Auth=deserialize_list(json_data.get("Auth"), AuthDefinition),
            BuildStatusConfig=deserialize_list(json_data.get("BuildStatusConfig"), BuildStatusConfigDefinition),
            GitSubmodulesConfig=deserialize_list(json_data.get("GitSubmodulesConfig"), GitSubmodulesConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondarySourcesDefinition = SecondarySourcesDefinition


@dataclass
class AuthDefinition(BaseModel):
    Resource: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthDefinition = AuthDefinition


@dataclass
class BuildStatusConfigDefinition(BaseModel):
    Context: Optional[str]
    TargetUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BuildStatusConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildStatusConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            TargetUrl=json_data.get("TargetUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildStatusConfigDefinition = BuildStatusConfigDefinition


@dataclass
class GitSubmodulesConfigDefinition(BaseModel):
    FetchSubmodules: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GitSubmodulesConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitSubmodulesConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FetchSubmodules=json_data.get("FetchSubmodules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitSubmodulesConfigDefinition = GitSubmodulesConfigDefinition


@dataclass
class SourceDefinition(BaseModel):
    Buildspec: Optional[str]
    GitCloneDepth: Optional[float]
    InsecureSsl: Optional[bool]
    Location: Optional[str]
    ReportBuildStatus: Optional[bool]
    Type: Optional[str]
    Auth: Optional[Sequence["_AuthDefinition"]]
    BuildStatusConfig: Optional[Sequence["_BuildStatusConfigDefinition"]]
    GitSubmodulesConfig: Optional[Sequence["_GitSubmodulesConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Buildspec=json_data.get("Buildspec"),
            GitCloneDepth=json_data.get("GitCloneDepth"),
            InsecureSsl=json_data.get("InsecureSsl"),
            Location=json_data.get("Location"),
            ReportBuildStatus=json_data.get("ReportBuildStatus"),
            Type=json_data.get("Type"),
            Auth=deserialize_list(json_data.get("Auth"), AuthDefinition),
            BuildStatusConfig=deserialize_list(json_data.get("BuildStatusConfig"), BuildStatusConfigDefinition),
            GitSubmodulesConfig=deserialize_list(json_data.get("GitSubmodulesConfig"), GitSubmodulesConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class VpcConfigDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


