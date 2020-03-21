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
    AccountPassword: Optional[str]
    BackupPeriod: Optional[Sequence[str]]
    BackupTime: Optional[str]
    DbInstanceClass: Optional[str]
    DbInstanceStorage: Optional[float]
    EngineVersion: Optional[str]
    InstanceChargeType: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
    MaintainEndTime: Optional[str]
    MaintainStartTime: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    ReplicaSetName: Optional[str]
    ReplicationFactor: Optional[float]
    RetentionPeriod: Optional[float]
    SecurityGroupId: Optional[str]
    SecurityIpList: Optional[Sequence[str]]
    StorageEngine: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TdeStatus: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountPassword=json_data.get("AccountPassword"),
            BackupPeriod=json_data.get("BackupPeriod"),
            BackupTime=json_data.get("BackupTime"),
            DbInstanceClass=json_data.get("DbInstanceClass"),
            DbInstanceStorage=json_data.get("DbInstanceStorage"),
            EngineVersion=json_data.get("EngineVersion"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            MaintainEndTime=json_data.get("MaintainEndTime"),
            MaintainStartTime=json_data.get("MaintainStartTime"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            ReplicaSetName=json_data.get("ReplicaSetName"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityIpList=json_data.get("SecurityIpList"),
            StorageEngine=json_data.get("StorageEngine"),
            Tags=json_data.get("Tags"),
            TdeStatus=json_data.get("TdeStatus"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionContext:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContext"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContext = KmsEncryptionContext


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


