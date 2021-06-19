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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    BackupRetentionPeriod: Optional[float]
    ClusterIdentifier: Optional[str]
    ClusterIdentifierPrefix: Optional[str]
    ClusterMembers: Optional[Sequence[str]]
    ClusterResourceId: Optional[str]
    DbClusterParameterGroupName: Optional[str]
    DbSubnetGroupName: Optional[str]
    DeletionProtection: Optional[bool]
    EnabledCloudwatchLogsExports: Optional[Sequence[str]]
    Endpoint: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    FinalSnapshotIdentifier: Optional[str]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    MasterPassword: Optional[str]
    MasterUsername: Optional[str]
    Port: Optional[float]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    ReaderEndpoint: Optional[str]
    SkipFinalSnapshot: Optional[bool]
    SnapshotIdentifier: Optional[str]
    StorageEncrypted: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
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
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            ClusterIdentifierPrefix=json_data.get("ClusterIdentifierPrefix"),
            ClusterMembers=json_data.get("ClusterMembers"),
            ClusterResourceId=json_data.get("ClusterResourceId"),
            DbClusterParameterGroupName=json_data.get("DbClusterParameterGroupName"),
            DbSubnetGroupName=json_data.get("DbSubnetGroupName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EnabledCloudwatchLogsExports=json_data.get("EnabledCloudwatchLogsExports"),
            Endpoint=json_data.get("Endpoint"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MasterPassword=json_data.get("MasterPassword"),
            MasterUsername=json_data.get("MasterUsername"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            ReaderEndpoint=json_data.get("ReaderEndpoint"),
            SkipFinalSnapshot=json_data.get("SkipFinalSnapshot"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
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


