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
    ArchiveBackupKeepCount: Optional[float]
    ArchiveBackupKeepPolicy: Optional[str]
    ArchiveBackupRetentionPeriod: Optional[float]
    BackupPeriod: Optional[Sequence[str]]
    BackupRetentionPeriod: Optional[float]
    BackupTime: Optional[str]
    CompressType: Optional[str]
    EnableBackupLog: Optional[bool]
    HighSpaceUsageProtection: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    LocalLogRetentionHours: Optional[float]
    LocalLogRetentionSpace: Optional[float]
    LogBackup: Optional[bool]
    LogBackupFrequency: Optional[str]
    LogBackupRetentionPeriod: Optional[float]
    LogRetentionPeriod: Optional[float]
    PreferredBackupPeriod: Optional[Sequence[str]]
    PreferredBackupTime: Optional[str]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ArchiveBackupKeepCount=json_data.get("ArchiveBackupKeepCount"),
            ArchiveBackupKeepPolicy=json_data.get("ArchiveBackupKeepPolicy"),
            ArchiveBackupRetentionPeriod=json_data.get("ArchiveBackupRetentionPeriod"),
            BackupPeriod=json_data.get("BackupPeriod"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            BackupTime=json_data.get("BackupTime"),
            CompressType=json_data.get("CompressType"),
            EnableBackupLog=json_data.get("EnableBackupLog"),
            HighSpaceUsageProtection=json_data.get("HighSpaceUsageProtection"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            LocalLogRetentionHours=json_data.get("LocalLogRetentionHours"),
            LocalLogRetentionSpace=json_data.get("LocalLogRetentionSpace"),
            LogBackup=json_data.get("LogBackup"),
            LogBackupFrequency=json_data.get("LogBackupFrequency"),
            LogBackupRetentionPeriod=json_data.get("LogBackupRetentionPeriod"),
            LogRetentionPeriod=json_data.get("LogRetentionPeriod"),
            PreferredBackupPeriod=json_data.get("PreferredBackupPeriod"),
            PreferredBackupTime=json_data.get("PreferredBackupTime"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


