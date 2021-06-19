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
    AccessToken: Optional[str]
    AdbDomain: Optional[str]
    AdditionalProperties: Optional[Sequence["_AdditionalPropertiesDefinition"]]
    Annotations: Optional[Sequence[str]]
    DataFactoryName: Optional[str]
    Description: Optional[str]
    ExistingClusterId: Optional[str]
    Id: Optional[str]
    IntegrationRuntimeName: Optional[str]
    MsiWorkSpaceResourceId: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    ResourceGroupName: Optional[str]
    InstancePool: Optional[Sequence["_InstancePoolDefinition"]]
    KeyVaultPassword: Optional[Sequence["_KeyVaultPasswordDefinition"]]
    NewClusterConfig: Optional[Sequence["_NewClusterConfigDefinition"]]
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
            AccessToken=json_data.get("AccessToken"),
            AdbDomain=json_data.get("AdbDomain"),
            AdditionalProperties=deserialize_list(json_data.get("AdditionalProperties"), AdditionalPropertiesDefinition),
            Annotations=json_data.get("Annotations"),
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            ExistingClusterId=json_data.get("ExistingClusterId"),
            Id=json_data.get("Id"),
            IntegrationRuntimeName=json_data.get("IntegrationRuntimeName"),
            MsiWorkSpaceResourceId=json_data.get("MsiWorkSpaceResourceId"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            InstancePool=deserialize_list(json_data.get("InstancePool"), InstancePoolDefinition),
            KeyVaultPassword=deserialize_list(json_data.get("KeyVaultPassword"), KeyVaultPasswordDefinition),
            NewClusterConfig=deserialize_list(json_data.get("NewClusterConfig"), NewClusterConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalPropertiesDefinition = AdditionalPropertiesDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class InstancePoolDefinition(BaseModel):
    ClusterVersion: Optional[str]
    InstancePoolId: Optional[str]
    MaxNumberOfWorkers: Optional[float]
    MinNumberOfWorkers: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstancePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            InstancePoolId=json_data.get("InstancePoolId"),
            MaxNumberOfWorkers=json_data.get("MaxNumberOfWorkers"),
            MinNumberOfWorkers=json_data.get("MinNumberOfWorkers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancePoolDefinition = InstancePoolDefinition


@dataclass
class KeyVaultPasswordDefinition(BaseModel):
    LinkedServiceName: Optional[str]
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyVaultPasswordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyVaultPasswordDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkedServiceName=json_data.get("LinkedServiceName"),
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyVaultPasswordDefinition = KeyVaultPasswordDefinition


@dataclass
class NewClusterConfigDefinition(BaseModel):
    ClusterVersion: Optional[str]
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]
    DriverNodeType: Optional[str]
    InitScripts: Optional[Sequence[str]]
    LogDestination: Optional[str]
    MaxNumberOfWorkers: Optional[float]
    MinNumberOfWorkers: Optional[float]
    NodeType: Optional[str]
    SparkConfig: Optional[Sequence["_SparkConfigDefinition"]]
    SparkEnvironmentVariables: Optional[Sequence["_SparkEnvironmentVariablesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NewClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
            DriverNodeType=json_data.get("DriverNodeType"),
            InitScripts=json_data.get("InitScripts"),
            LogDestination=json_data.get("LogDestination"),
            MaxNumberOfWorkers=json_data.get("MaxNumberOfWorkers"),
            MinNumberOfWorkers=json_data.get("MinNumberOfWorkers"),
            NodeType=json_data.get("NodeType"),
            SparkConfig=deserialize_list(json_data.get("SparkConfig"), SparkConfigDefinition),
            SparkEnvironmentVariables=deserialize_list(json_data.get("SparkEnvironmentVariables"), SparkEnvironmentVariablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewClusterConfigDefinition = NewClusterConfigDefinition


@dataclass
class CustomTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTagsDefinition = CustomTagsDefinition


@dataclass
class SparkConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SparkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkConfigDefinition = SparkConfigDefinition


@dataclass
class SparkEnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SparkEnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkEnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkEnvironmentVariablesDefinition = SparkEnvironmentVariablesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


