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
    AutoScalingComputeEnabled: Optional[bool]
    AutoScalingComputeScaleDownEnabled: Optional[bool]
    AutoScalingDiskGbEnabled: Optional[bool]
    BackingProviderName: Optional[str]
    BackupEnabled: Optional[bool]
    BiConnector: Optional[Sequence["_BiConnectorDefinition"]]
    ClusterId: Optional[str]
    ClusterType: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition5"]]
    ContainerId: Optional[str]
    DiskSizeGb: Optional[float]
    EncryptionAtRestProvider: Optional[str]
    Id: Optional[str]
    MongoDbMajorVersion: Optional[str]
    MongoDbVersion: Optional[str]
    MongoUri: Optional[str]
    MongoUriUpdated: Optional[str]
    MongoUriWithOptions: Optional[str]
    Name: Optional[str]
    NumShards: Optional[float]
    Paused: Optional[bool]
    PitEnabled: Optional[bool]
    ProjectId: Optional[str]
    ProviderAutoScalingComputeMaxInstanceSize: Optional[str]
    ProviderAutoScalingComputeMinInstanceSize: Optional[str]
    ProviderBackupEnabled: Optional[bool]
    ProviderDiskIops: Optional[float]
    ProviderDiskTypeName: Optional[str]
    ProviderEncryptEbsVolume: Optional[bool]
    ProviderEncryptEbsVolumeFlag: Optional[bool]
    ProviderInstanceSizeName: Optional[str]
    ProviderName: Optional[str]
    ProviderRegionName: Optional[str]
    ProviderVolumeType: Optional[str]
    ReplicationFactor: Optional[float]
    SnapshotBackupPolicy: Optional[Sequence["_SnapshotBackupPolicyDefinition3"]]
    SrvAddress: Optional[str]
    StateName: Optional[str]
    AdvancedConfiguration: Optional[Sequence["_AdvancedConfigurationDefinition"]]
    BiConnectorConfig: Optional[Sequence["_BiConnectorConfigDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    ReplicationSpecs: Optional[Sequence["_ReplicationSpecsDefinition"]]

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
            AutoScalingComputeEnabled=json_data.get("AutoScalingComputeEnabled"),
            AutoScalingComputeScaleDownEnabled=json_data.get("AutoScalingComputeScaleDownEnabled"),
            AutoScalingDiskGbEnabled=json_data.get("AutoScalingDiskGbEnabled"),
            BackingProviderName=json_data.get("BackingProviderName"),
            BackupEnabled=json_data.get("BackupEnabled"),
            BiConnector=deserialize_list(json_data.get("BiConnector"), BiConnectorDefinition),
            ClusterId=json_data.get("ClusterId"),
            ClusterType=json_data.get("ClusterType"),
            ConnectionStrings=deserialize_list(json_data.get("ConnectionStrings"), ConnectionStringsDefinition5),
            ContainerId=json_data.get("ContainerId"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            EncryptionAtRestProvider=json_data.get("EncryptionAtRestProvider"),
            Id=json_data.get("Id"),
            MongoDbMajorVersion=json_data.get("MongoDbMajorVersion"),
            MongoDbVersion=json_data.get("MongoDbVersion"),
            MongoUri=json_data.get("MongoUri"),
            MongoUriUpdated=json_data.get("MongoUriUpdated"),
            MongoUriWithOptions=json_data.get("MongoUriWithOptions"),
            Name=json_data.get("Name"),
            NumShards=json_data.get("NumShards"),
            Paused=json_data.get("Paused"),
            PitEnabled=json_data.get("PitEnabled"),
            ProjectId=json_data.get("ProjectId"),
            ProviderAutoScalingComputeMaxInstanceSize=json_data.get("ProviderAutoScalingComputeMaxInstanceSize"),
            ProviderAutoScalingComputeMinInstanceSize=json_data.get("ProviderAutoScalingComputeMinInstanceSize"),
            ProviderBackupEnabled=json_data.get("ProviderBackupEnabled"),
            ProviderDiskIops=json_data.get("ProviderDiskIops"),
            ProviderDiskTypeName=json_data.get("ProviderDiskTypeName"),
            ProviderEncryptEbsVolume=json_data.get("ProviderEncryptEbsVolume"),
            ProviderEncryptEbsVolumeFlag=json_data.get("ProviderEncryptEbsVolumeFlag"),
            ProviderInstanceSizeName=json_data.get("ProviderInstanceSizeName"),
            ProviderName=json_data.get("ProviderName"),
            ProviderRegionName=json_data.get("ProviderRegionName"),
            ProviderVolumeType=json_data.get("ProviderVolumeType"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            SnapshotBackupPolicy=deserialize_list(json_data.get("SnapshotBackupPolicy"), SnapshotBackupPolicyDefinition3),
            SrvAddress=json_data.get("SrvAddress"),
            StateName=json_data.get("StateName"),
            AdvancedConfiguration=deserialize_list(json_data.get("AdvancedConfiguration"), AdvancedConfigurationDefinition),
            BiConnectorConfig=deserialize_list(json_data.get("BiConnectorConfig"), BiConnectorConfigDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            ReplicationSpecs=deserialize_list(json_data.get("ReplicationSpecs"), ReplicationSpecsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BiConnectorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BiConnectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BiConnectorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BiConnectorDefinition = BiConnectorDefinition


@dataclass
class ConnectionStringsDefinition5(BaseModel):
    AwsPrivateLink: Optional[Sequence["_ConnectionStringsDefinition"]]
    AwsPrivateLinkSrv: Optional[Sequence["_ConnectionStringsDefinition2"]]
    Private: Optional[str]
    PrivateEndpoint: Optional[Sequence["_ConnectionStringsDefinition4"]]
    PrivateSrv: Optional[str]
    Standard: Optional[str]
    StandardSrv: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition5"]:
        if not json_data:
            return None
        return cls(
            AwsPrivateLink=deserialize_list(json_data.get("AwsPrivateLink"), ConnectionStringsDefinition),
            AwsPrivateLinkSrv=deserialize_list(json_data.get("AwsPrivateLinkSrv"), ConnectionStringsDefinition2),
            Private=json_data.get("Private"),
            PrivateEndpoint=deserialize_list(json_data.get("PrivateEndpoint"), ConnectionStringsDefinition4),
            PrivateSrv=json_data.get("PrivateSrv"),
            Standard=json_data.get("Standard"),
            StandardSrv=json_data.get("StandardSrv"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition5 = ConnectionStringsDefinition5


@dataclass
class ConnectionStringsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition = ConnectionStringsDefinition


@dataclass
class ConnectionStringsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition2 = ConnectionStringsDefinition2


@dataclass
class ConnectionStringsDefinition4(BaseModel):
    ConnectionString: Optional[str]
    Endpoints: Optional[Sequence["_ConnectionStringsDefinition3"]]
    SrvConnectionString: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition4"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), ConnectionStringsDefinition3),
            SrvConnectionString=json_data.get("SrvConnectionString"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition4 = ConnectionStringsDefinition4


@dataclass
class ConnectionStringsDefinition3(BaseModel):
    EndpointId: Optional[str]
    ProviderName: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition3"]:
        if not json_data:
            return None
        return cls(
            EndpointId=json_data.get("EndpointId"),
            ProviderName=json_data.get("ProviderName"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition3 = ConnectionStringsDefinition3


@dataclass
class SnapshotBackupPolicyDefinition3(BaseModel):
    ClusterId: Optional[str]
    ClusterName: Optional[str]
    NextSnapshot: Optional[str]
    Policies: Optional[Sequence["_SnapshotBackupPolicyDefinition2"]]
    ReferenceHourOfDay: Optional[float]
    ReferenceMinuteOfHour: Optional[float]
    RestoreWindowDays: Optional[float]
    UpdateSnapshots: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotBackupPolicyDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotBackupPolicyDefinition3"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            ClusterName=json_data.get("ClusterName"),
            NextSnapshot=json_data.get("NextSnapshot"),
            Policies=deserialize_list(json_data.get("Policies"), SnapshotBackupPolicyDefinition2),
            ReferenceHourOfDay=json_data.get("ReferenceHourOfDay"),
            ReferenceMinuteOfHour=json_data.get("ReferenceMinuteOfHour"),
            RestoreWindowDays=json_data.get("RestoreWindowDays"),
            UpdateSnapshots=json_data.get("UpdateSnapshots"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotBackupPolicyDefinition3 = SnapshotBackupPolicyDefinition3


@dataclass
class SnapshotBackupPolicyDefinition2(BaseModel):
    Id: Optional[str]
    PolicyItem: Optional[Sequence["_SnapshotBackupPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotBackupPolicyDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotBackupPolicyDefinition2"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            PolicyItem=deserialize_list(json_data.get("PolicyItem"), SnapshotBackupPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotBackupPolicyDefinition2 = SnapshotBackupPolicyDefinition2


@dataclass
class SnapshotBackupPolicyDefinition(BaseModel):
    FrequencyInterval: Optional[float]
    FrequencyType: Optional[str]
    Id: Optional[str]
    RetentionUnit: Optional[str]
    RetentionValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotBackupPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotBackupPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            FrequencyInterval=json_data.get("FrequencyInterval"),
            FrequencyType=json_data.get("FrequencyType"),
            Id=json_data.get("Id"),
            RetentionUnit=json_data.get("RetentionUnit"),
            RetentionValue=json_data.get("RetentionValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotBackupPolicyDefinition = SnapshotBackupPolicyDefinition


@dataclass
class AdvancedConfigurationDefinition(BaseModel):
    FailIndexKeyTooLong: Optional[bool]
    JavascriptEnabled: Optional[bool]
    MinimumEnabledTlsProtocol: Optional[str]
    NoTableScan: Optional[bool]
    OplogSizeMb: Optional[float]
    SampleRefreshIntervalBiConnector: Optional[float]
    SampleSizeBiConnector: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            FailIndexKeyTooLong=json_data.get("FailIndexKeyTooLong"),
            JavascriptEnabled=json_data.get("JavascriptEnabled"),
            MinimumEnabledTlsProtocol=json_data.get("MinimumEnabledTlsProtocol"),
            NoTableScan=json_data.get("NoTableScan"),
            OplogSizeMb=json_data.get("OplogSizeMb"),
            SampleRefreshIntervalBiConnector=json_data.get("SampleRefreshIntervalBiConnector"),
            SampleSizeBiConnector=json_data.get("SampleSizeBiConnector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedConfigurationDefinition = AdvancedConfigurationDefinition


@dataclass
class BiConnectorConfigDefinition(BaseModel):
    Enabled: Optional[bool]
    ReadPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BiConnectorConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BiConnectorConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            ReadPreference=json_data.get("ReadPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BiConnectorConfigDefinition = BiConnectorConfigDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ReplicationSpecsDefinition(BaseModel):
    Id: Optional[str]
    NumShards: Optional[float]
    ZoneName: Optional[str]
    RegionsConfig: Optional[Sequence["_RegionsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationSpecsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationSpecsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            NumShards=json_data.get("NumShards"),
            ZoneName=json_data.get("ZoneName"),
            RegionsConfig=deserialize_list(json_data.get("RegionsConfig"), RegionsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationSpecsDefinition = ReplicationSpecsDefinition


@dataclass
class RegionsConfigDefinition(BaseModel):
    AnalyticsNodes: Optional[float]
    ElectableNodes: Optional[float]
    Priority: Optional[float]
    ReadOnlyNodes: Optional[float]
    RegionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AnalyticsNodes=json_data.get("AnalyticsNodes"),
            ElectableNodes=json_data.get("ElectableNodes"),
            Priority=json_data.get("Priority"),
            ReadOnlyNodes=json_data.get("ReadOnlyNodes"),
            RegionName=json_data.get("RegionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionsConfigDefinition = RegionsConfigDefinition


