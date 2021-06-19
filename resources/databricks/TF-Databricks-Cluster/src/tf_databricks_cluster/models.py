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
    AutoterminationMinutes: Optional[float]
    ClusterId: Optional[str]
    ClusterName: Optional[str]
    CustomTags: Optional[Sequence["_CustomTagsDefinition"]]
    DefaultTags: Optional[Sequence["_DefaultTagsDefinition"]]
    DriverNodeTypeId: Optional[str]
    EnableElasticDisk: Optional[bool]
    EnableLocalDiskEncryption: Optional[bool]
    Id: Optional[str]
    IdempotencyToken: Optional[str]
    InstancePoolId: Optional[str]
    IsPinned: Optional[bool]
    NodeTypeId: Optional[str]
    NumWorkers: Optional[float]
    PolicyId: Optional[str]
    SingleUserName: Optional[str]
    SparkConf: Optional[Sequence["_SparkConfDefinition"]]
    SparkEnvVars: Optional[Sequence["_SparkEnvVarsDefinition"]]
    SparkVersion: Optional[str]
    SshPublicKeys: Optional[Sequence[str]]
    State: Optional[str]
    Url: Optional[str]
    Autoscale: Optional[Sequence["_AutoscaleDefinition"]]
    AwsAttributes: Optional[Sequence["_AwsAttributesDefinition"]]
    AzureAttributes: Optional[Sequence["_AzureAttributesDefinition"]]
    ClusterLogConf: Optional[Sequence["_ClusterLogConfDefinition"]]
    DockerImage: Optional[Sequence["_DockerImageDefinition"]]
    GcpAttributes: Optional[Sequence["_GcpAttributesDefinition"]]
    InitScripts: Optional[Sequence["_InitScriptsDefinition"]]
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
            AutoterminationMinutes=json_data.get("AutoterminationMinutes"),
            ClusterId=json_data.get("ClusterId"),
            ClusterName=json_data.get("ClusterName"),
            CustomTags=deserialize_list(json_data.get("CustomTags"), CustomTagsDefinition),
            DefaultTags=deserialize_list(json_data.get("DefaultTags"), DefaultTagsDefinition),
            DriverNodeTypeId=json_data.get("DriverNodeTypeId"),
            EnableElasticDisk=json_data.get("EnableElasticDisk"),
            EnableLocalDiskEncryption=json_data.get("EnableLocalDiskEncryption"),
            Id=json_data.get("Id"),
            IdempotencyToken=json_data.get("IdempotencyToken"),
            InstancePoolId=json_data.get("InstancePoolId"),
            IsPinned=json_data.get("IsPinned"),
            NodeTypeId=json_data.get("NodeTypeId"),
            NumWorkers=json_data.get("NumWorkers"),
            PolicyId=json_data.get("PolicyId"),
            SingleUserName=json_data.get("SingleUserName"),
            SparkConf=deserialize_list(json_data.get("SparkConf"), SparkConfDefinition),
            SparkEnvVars=deserialize_list(json_data.get("SparkEnvVars"), SparkEnvVarsDefinition),
            SparkVersion=json_data.get("SparkVersion"),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            State=json_data.get("State"),
            Url=json_data.get("Url"),
            Autoscale=deserialize_list(json_data.get("Autoscale"), AutoscaleDefinition),
            AwsAttributes=deserialize_list(json_data.get("AwsAttributes"), AwsAttributesDefinition),
            AzureAttributes=deserialize_list(json_data.get("AzureAttributes"), AzureAttributesDefinition),
            ClusterLogConf=deserialize_list(json_data.get("ClusterLogConf"), ClusterLogConfDefinition),
            DockerImage=deserialize_list(json_data.get("DockerImage"), DockerImageDefinition),
            GcpAttributes=deserialize_list(json_data.get("GcpAttributes"), GcpAttributesDefinition),
            InitScripts=deserialize_list(json_data.get("InitScripts"), InitScriptsDefinition),
            Library=deserialize_list(json_data.get("Library"), LibraryDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class DefaultTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultTagsDefinition = DefaultTagsDefinition


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
    Availability: Optional[str]
    EbsVolumeCount: Optional[float]
    EbsVolumeSize: Optional[float]
    EbsVolumeType: Optional[str]
    FirstOnDemand: Optional[float]
    InstanceProfileArn: Optional[str]
    SpotBidPricePercent: Optional[float]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            EbsVolumeCount=json_data.get("EbsVolumeCount"),
            EbsVolumeSize=json_data.get("EbsVolumeSize"),
            EbsVolumeType=json_data.get("EbsVolumeType"),
            FirstOnDemand=json_data.get("FirstOnDemand"),
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            SpotBidPricePercent=json_data.get("SpotBidPricePercent"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAttributesDefinition = AwsAttributesDefinition


@dataclass
class AzureAttributesDefinition(BaseModel):
    Availability: Optional[str]
    FirstOnDemand: Optional[float]
    SpotBidMaxPrice: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Availability=json_data.get("Availability"),
            FirstOnDemand=json_data.get("FirstOnDemand"),
            SpotBidMaxPrice=json_data.get("SpotBidMaxPrice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureAttributesDefinition = AzureAttributesDefinition


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
class DockerImageDefinition(BaseModel):
    Url: Optional[str]
    BasicAuth: Optional[Sequence["_BasicAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DockerImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
            BasicAuth=deserialize_list(json_data.get("BasicAuth"), BasicAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerImageDefinition = DockerImageDefinition


@dataclass
class BasicAuthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthDefinition = BasicAuthDefinition


@dataclass
class GcpAttributesDefinition(BaseModel):
    GoogleServiceAccount: Optional[str]
    UsePreemptibleExecutors: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcpAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            GoogleServiceAccount=json_data.get("GoogleServiceAccount"),
            UsePreemptibleExecutors=json_data.get("UsePreemptibleExecutors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpAttributesDefinition = GcpAttributesDefinition


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
class LibraryDefinition(BaseModel):
    Egg: Optional[str]
    Jar: Optional[str]
    Whl: Optional[str]
    Cran: Optional[Sequence["_CranDefinition"]]
    Maven: Optional[Sequence["_MavenDefinition"]]
    Pypi: Optional[Sequence["_PypiDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LibraryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LibraryDefinition"]:
        if not json_data:
            return None
        return cls(
            Egg=json_data.get("Egg"),
            Jar=json_data.get("Jar"),
            Whl=json_data.get("Whl"),
            Cran=deserialize_list(json_data.get("Cran"), CranDefinition),
            Maven=deserialize_list(json_data.get("Maven"), MavenDefinition),
            Pypi=deserialize_list(json_data.get("Pypi"), PypiDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LibraryDefinition = LibraryDefinition


@dataclass
class CranDefinition(BaseModel):
    Package: Optional[str]
    Repo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CranDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CranDefinition"]:
        if not json_data:
            return None
        return cls(
            Package=json_data.get("Package"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CranDefinition = CranDefinition


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
class PypiDefinition(BaseModel):
    Package: Optional[str]
    Repo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PypiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PypiDefinition"]:
        if not json_data:
            return None
        return cls(
            Package=json_data.get("Package"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PypiDefinition = PypiDefinition


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


