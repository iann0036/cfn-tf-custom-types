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
    AutoPauseDelayInMinutes: Optional[float]
    Collation: Optional[str]
    CreateMode: Optional[str]
    CreationSourceDatabaseId: Optional[str]
    ElasticPoolId: Optional[str]
    ExtendedAuditingPolicy: Optional[Sequence["_ExtendedAuditingPolicyDefinition"]]
    GeoBackupEnabled: Optional[bool]
    Id: Optional[str]
    LicenseType: Optional[str]
    MaxSizeGb: Optional[float]
    MinCapacity: Optional[float]
    Name: Optional[str]
    ReadReplicaCount: Optional[float]
    ReadScale: Optional[bool]
    RecoverDatabaseId: Optional[str]
    RestoreDroppedDatabaseId: Optional[str]
    RestorePointInTime: Optional[str]
    SampleName: Optional[str]
    ServerId: Optional[str]
    SkuName: Optional[str]
    StorageAccountType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ZoneRedundant: Optional[bool]
    LongTermRetentionPolicy: Optional[Sequence["_LongTermRetentionPolicyDefinition"]]
    ShortTermRetentionPolicy: Optional[Sequence["_ShortTermRetentionPolicyDefinition"]]
    ThreatDetectionPolicy: Optional[Sequence["_ThreatDetectionPolicyDefinition"]]
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
            AutoPauseDelayInMinutes=json_data.get("AutoPauseDelayInMinutes"),
            Collation=json_data.get("Collation"),
            CreateMode=json_data.get("CreateMode"),
            CreationSourceDatabaseId=json_data.get("CreationSourceDatabaseId"),
            ElasticPoolId=json_data.get("ElasticPoolId"),
            ExtendedAuditingPolicy=deserialize_list(json_data.get("ExtendedAuditingPolicy"), ExtendedAuditingPolicyDefinition),
            GeoBackupEnabled=json_data.get("GeoBackupEnabled"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            MaxSizeGb=json_data.get("MaxSizeGb"),
            MinCapacity=json_data.get("MinCapacity"),
            Name=json_data.get("Name"),
            ReadReplicaCount=json_data.get("ReadReplicaCount"),
            ReadScale=json_data.get("ReadScale"),
            RecoverDatabaseId=json_data.get("RecoverDatabaseId"),
            RestoreDroppedDatabaseId=json_data.get("RestoreDroppedDatabaseId"),
            RestorePointInTime=json_data.get("RestorePointInTime"),
            SampleName=json_data.get("SampleName"),
            ServerId=json_data.get("ServerId"),
            SkuName=json_data.get("SkuName"),
            StorageAccountType=json_data.get("StorageAccountType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            LongTermRetentionPolicy=deserialize_list(json_data.get("LongTermRetentionPolicy"), LongTermRetentionPolicyDefinition),
            ShortTermRetentionPolicy=deserialize_list(json_data.get("ShortTermRetentionPolicy"), ShortTermRetentionPolicyDefinition),
            ThreatDetectionPolicy=deserialize_list(json_data.get("ThreatDetectionPolicy"), ThreatDetectionPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtendedAuditingPolicyDefinition(BaseModel):
    LogMonitoringEnabled: Optional[bool]
    RetentionInDays: Optional[float]
    StorageAccountAccessKey: Optional[str]
    StorageAccountAccessKeyIsSecondary: Optional[bool]
    StorageEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedAuditingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedAuditingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LogMonitoringEnabled=json_data.get("LogMonitoringEnabled"),
            RetentionInDays=json_data.get("RetentionInDays"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageAccountAccessKeyIsSecondary=json_data.get("StorageAccountAccessKeyIsSecondary"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedAuditingPolicyDefinition = ExtendedAuditingPolicyDefinition


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
class LongTermRetentionPolicyDefinition(BaseModel):
    MonthlyRetention: Optional[str]
    WeekOfYear: Optional[float]
    WeeklyRetention: Optional[str]
    YearlyRetention: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LongTermRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LongTermRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MonthlyRetention=json_data.get("MonthlyRetention"),
            WeekOfYear=json_data.get("WeekOfYear"),
            WeeklyRetention=json_data.get("WeeklyRetention"),
            YearlyRetention=json_data.get("YearlyRetention"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LongTermRetentionPolicyDefinition = LongTermRetentionPolicyDefinition


@dataclass
class ShortTermRetentionPolicyDefinition(BaseModel):
    RetentionDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShortTermRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShortTermRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RetentionDays=json_data.get("RetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShortTermRetentionPolicyDefinition = ShortTermRetentionPolicyDefinition


@dataclass
class ThreatDetectionPolicyDefinition(BaseModel):
    DisabledAlerts: Optional[Sequence[str]]
    EmailAccountAdmins: Optional[str]
    EmailAddresses: Optional[Sequence[str]]
    RetentionDays: Optional[float]
    State: Optional[str]
    StorageAccountAccessKey: Optional[str]
    StorageEndpoint: Optional[str]
    UseServerDefault: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatDetectionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatDetectionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DisabledAlerts=json_data.get("DisabledAlerts"),
            EmailAccountAdmins=json_data.get("EmailAccountAdmins"),
            EmailAddresses=json_data.get("EmailAddresses"),
            RetentionDays=json_data.get("RetentionDays"),
            State=json_data.get("State"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
            UseServerDefault=json_data.get("UseServerDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatDetectionPolicyDefinition = ThreatDetectionPolicyDefinition


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


