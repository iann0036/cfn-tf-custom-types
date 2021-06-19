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
    AutoScalingConfigurationArn: Optional[str]
    Id: Optional[str]
    ServiceId: Optional[str]
    ServiceName: Optional[str]
    ServiceUrl: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfigurationDefinition"]]
    HealthCheckConfiguration: Optional[Sequence["_HealthCheckConfigurationDefinition"]]
    InstanceConfiguration: Optional[Sequence["_InstanceConfigurationDefinition"]]
    SourceConfiguration: Optional[Sequence["_SourceConfigurationDefinition"]]

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
            AutoScalingConfigurationArn=json_data.get("AutoScalingConfigurationArn"),
            Id=json_data.get("Id"),
            ServiceId=json_data.get("ServiceId"),
            ServiceName=json_data.get("ServiceName"),
            ServiceUrl=json_data.get("ServiceUrl"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            EncryptionConfiguration=deserialize_list(json_data.get("EncryptionConfiguration"), EncryptionConfigurationDefinition),
            HealthCheckConfiguration=deserialize_list(json_data.get("HealthCheckConfiguration"), HealthCheckConfigurationDefinition),
            InstanceConfiguration=deserialize_list(json_data.get("InstanceConfiguration"), InstanceConfigurationDefinition),
            SourceConfiguration=deserialize_list(json_data.get("SourceConfiguration"), SourceConfigurationDefinition),
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
class EncryptionConfigurationDefinition(BaseModel):
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigurationDefinition = EncryptionConfigurationDefinition


@dataclass
class HealthCheckConfigurationDefinition(BaseModel):
    HealthyThreshold: Optional[float]
    Interval: Optional[float]
    Path: Optional[str]
    Protocol: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Interval=json_data.get("Interval"),
            Path=json_data.get("Path"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfigurationDefinition = HealthCheckConfigurationDefinition


@dataclass
class InstanceConfigurationDefinition(BaseModel):
    Cpu: Optional[str]
    InstanceRoleArn: Optional[str]
    Memory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            InstanceRoleArn=json_data.get("InstanceRoleArn"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceConfigurationDefinition = InstanceConfigurationDefinition


@dataclass
class SourceConfigurationDefinition(BaseModel):
    AutoDeploymentsEnabled: Optional[bool]
    AuthenticationConfiguration: Optional[Sequence["_AuthenticationConfigurationDefinition"]]
    CodeRepository: Optional[Sequence["_CodeRepositoryDefinition"]]
    ImageRepository: Optional[Sequence["_ImageRepositoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoDeploymentsEnabled=json_data.get("AutoDeploymentsEnabled"),
            AuthenticationConfiguration=deserialize_list(json_data.get("AuthenticationConfiguration"), AuthenticationConfigurationDefinition),
            CodeRepository=deserialize_list(json_data.get("CodeRepository"), CodeRepositoryDefinition),
            ImageRepository=deserialize_list(json_data.get("ImageRepository"), ImageRepositoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConfigurationDefinition = SourceConfigurationDefinition


@dataclass
class AuthenticationConfigurationDefinition(BaseModel):
    AccessRoleArn: Optional[str]
    ConnectionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessRoleArn=json_data.get("AccessRoleArn"),
            ConnectionArn=json_data.get("ConnectionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationConfigurationDefinition = AuthenticationConfigurationDefinition


@dataclass
class CodeRepositoryDefinition(BaseModel):
    RepositoryUrl: Optional[str]
    CodeConfiguration: Optional[Sequence["_CodeConfigurationDefinition"]]
    SourceCodeVersion: Optional[Sequence["_SourceCodeVersionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CodeRepositoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeRepositoryDefinition"]:
        if not json_data:
            return None
        return cls(
            RepositoryUrl=json_data.get("RepositoryUrl"),
            CodeConfiguration=deserialize_list(json_data.get("CodeConfiguration"), CodeConfigurationDefinition),
            SourceCodeVersion=deserialize_list(json_data.get("SourceCodeVersion"), SourceCodeVersionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeRepositoryDefinition = CodeRepositoryDefinition


@dataclass
class CodeConfigurationDefinition(BaseModel):
    ConfigurationSource: Optional[str]
    CodeConfigurationValues: Optional[Sequence["_CodeConfigurationValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CodeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigurationSource=json_data.get("ConfigurationSource"),
            CodeConfigurationValues=deserialize_list(json_data.get("CodeConfigurationValues"), CodeConfigurationValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeConfigurationDefinition = CodeConfigurationDefinition


@dataclass
class CodeConfigurationValuesDefinition(BaseModel):
    BuildCommand: Optional[str]
    Port: Optional[str]
    Runtime: Optional[str]
    RuntimeEnvironmentVariables: Optional[Sequence["_RuntimeEnvironmentVariablesDefinition2"]]
    StartCommand: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeConfigurationValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeConfigurationValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildCommand=json_data.get("BuildCommand"),
            Port=json_data.get("Port"),
            Runtime=json_data.get("Runtime"),
            RuntimeEnvironmentVariables=deserialize_list(json_data.get("RuntimeEnvironmentVariables"), RuntimeEnvironmentVariablesDefinition2),
            StartCommand=json_data.get("StartCommand"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeConfigurationValuesDefinition = CodeConfigurationValuesDefinition


@dataclass
class RuntimeEnvironmentVariablesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeEnvironmentVariablesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeEnvironmentVariablesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeEnvironmentVariablesDefinition2 = RuntimeEnvironmentVariablesDefinition2


@dataclass
class SourceCodeVersionDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceCodeVersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceCodeVersionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceCodeVersionDefinition = SourceCodeVersionDefinition


@dataclass
class ImageRepositoryDefinition(BaseModel):
    ImageIdentifier: Optional[str]
    ImageRepositoryType: Optional[str]
    ImageConfiguration: Optional[Sequence["_ImageConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageRepositoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageRepositoryDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageIdentifier=json_data.get("ImageIdentifier"),
            ImageRepositoryType=json_data.get("ImageRepositoryType"),
            ImageConfiguration=deserialize_list(json_data.get("ImageConfiguration"), ImageConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageRepositoryDefinition = ImageRepositoryDefinition


@dataclass
class ImageConfigurationDefinition(BaseModel):
    Port: Optional[str]
    RuntimeEnvironmentVariables: Optional[Sequence["_RuntimeEnvironmentVariablesDefinition"]]
    StartCommand: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            RuntimeEnvironmentVariables=deserialize_list(json_data.get("RuntimeEnvironmentVariables"), RuntimeEnvironmentVariablesDefinition),
            StartCommand=json_data.get("StartCommand"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfigurationDefinition = ImageConfigurationDefinition


@dataclass
class RuntimeEnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeEnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeEnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeEnvironmentVariablesDefinition = RuntimeEnvironmentVariablesDefinition


