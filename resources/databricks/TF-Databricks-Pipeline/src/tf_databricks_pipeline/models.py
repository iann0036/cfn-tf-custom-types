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
    AllowDuplicateNames: Optional[bool]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    Continuous: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Storage: Optional[str]
    Cluster: Optional[Sequence["_ClusterDefinition"]]
    Filters: Optional[Sequence["_FiltersDefinition"]]
    Library: Optional[Sequence["_LibraryDefinition"]]
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
            AllowDuplicateNames=json_data.get("AllowDuplicateNames"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            Continuous=json_data.get("Continuous"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Storage=json_data.get("Storage"),
            Cluster=deserialize_list(json_data.get("Cluster"), ClusterDefinition),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
            Library=deserialize_list(json_data.get("Library"), LibraryDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class ClusterDefinition(BaseModel):
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]
    DriverNodeTypeId: Optional[str]
    InstancePoolId: Optional[str]
    Label: Optional[str]
    NodeTypeId: Optional[str]
    NumWorkers: Optional[float]
    SparkConf: Optional[Sequence["_SparkConfDefinition"]]
    SparkEnvVars: Optional[Sequence["_SparkEnvVarsDefinition"]]
    SshPublicKeys: Optional[Sequence[str]]
    Autoscale: Optional[Sequence["_AutoscaleDefinition"]]
    AwsAttributes: Optional[Sequence["_AwsAttributesDefinition"]]
    ClusterLogConf: Optional[Sequence["_ClusterLogConfDefinition"]]
    InitScripts: Optional[Sequence["_InitScriptsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
            DriverNodeTypeId=json_data.get("DriverNodeTypeId"),
            InstancePoolId=json_data.get("InstancePoolId"),
            Label=json_data.get("Label"),
            NodeTypeId=json_data.get("NodeTypeId"),
            NumWorkers=json_data.get("NumWorkers"),
            SparkConf=deserialize_list(json_data.get("SparkConf"), SparkConfDefinition),
            SparkEnvVars=deserialize_list(json_data.get("SparkEnvVars"), SparkEnvVarsDefinition),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            Autoscale=deserialize_list(json_data.get("Autoscale"), AutoscaleDefinition),
            AwsAttributes=deserialize_list(json_data.get("AwsAttributes"), AwsAttributesDefinition),
            ClusterLogConf=deserialize_list(json_data.get("ClusterLogConf"), ClusterLogConfDefinition),
            InitScripts=deserialize_list(json_data.get("InitScripts"), InitScriptsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterDefinition = ClusterDefinition


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
class SparkConfDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SparkConfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkConfDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkConfDefinition = SparkConfDefinition


@dataclass
class SparkEnvVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SparkEnvVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkEnvVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkEnvVarsDefinition = SparkEnvVarsDefinition


@dataclass
class AutoscaleDefinition(BaseModel):
    MaxWorkers: Optional[float]
    MinWorkers: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxWorkers=json_data.get("MaxWorkers"),
            MinWorkers=json_data.get("MinWorkers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDefinition = AutoscaleDefinition


@dataclass
class AwsAttributesDefinition(BaseModel):
    InstanceProfileArn: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAttributesDefinition = AwsAttributesDefinition


@dataclass
class ClusterLogConfDefinition(BaseModel):
    Dbfs: Optional[Sequence["_DbfsDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterLogConfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterLogConfDefinition"]:
        if not json_data:
            return None
        return cls(
            Dbfs=deserialize_list(json_data.get("Dbfs"), DbfsDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterLogConfDefinition = ClusterLogConfDefinition


@dataclass
class DbfsDefinition(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbfsDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbfsDefinition = DbfsDefinition


@dataclass
class S3Definition(BaseModel):
    CannedAcl: Optional[str]
    Destination: Optional[str]
    EnableEncryption: Optional[bool]
    EncryptionType: Optional[str]
    Endpoint: Optional[str]
    KmsKey: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            CannedAcl=json_data.get("CannedAcl"),
            Destination=json_data.get("Destination"),
            EnableEncryption=json_data.get("EnableEncryption"),
            EncryptionType=json_data.get("EncryptionType"),
            Endpoint=json_data.get("Endpoint"),
            KmsKey=json_data.get("KmsKey"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


@dataclass
class InitScriptsDefinition(BaseModel):
    Dbfs: Optional[Sequence["_DbfsDefinition"]]
    File: Optional[Sequence["_FileDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InitScriptsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitScriptsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dbfs=deserialize_list(json_data.get("Dbfs"), DbfsDefinition),
            File=deserialize_list(json_data.get("File"), FileDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitScriptsDefinition = InitScriptsDefinition


@dataclass
class FileDefinition(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Exclude: Optional[Sequence[str]]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class LibraryDefinition(BaseModel):
    Jar: Optional[str]
    Whl: Optional[str]
    Maven: Optional[Sequence["_MavenDefinition"]]
    Notebook: Optional[Sequence["_NotebookDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LibraryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LibraryDefinition"]:
        if not json_data:
            return None
        return cls(
            Jar=json_data.get("Jar"),
            Whl=json_data.get("Whl"),
            Maven=deserialize_list(json_data.get("Maven"), MavenDefinition),
            Notebook=deserialize_list(json_data.get("Notebook"), NotebookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LibraryDefinition = LibraryDefinition


@dataclass
class MavenDefinition(BaseModel):
    Coordinates: Optional[str]
    Exclusions: Optional[Sequence[str]]
    Repo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MavenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MavenDefinition"]:
        if not json_data:
            return None
        return cls(
            Coordinates=json_data.get("Coordinates"),
            Exclusions=json_data.get("Exclusions"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MavenDefinition = MavenDefinition


@dataclass
class NotebookDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotebookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotebookDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotebookDefinition = NotebookDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


