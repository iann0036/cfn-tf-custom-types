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
    AccountPassword: Optional[str]
    BackupPeriod: Optional[Sequence[str]]
    BackupTime: Optional[str]
    DbInstanceClass: Optional[str]
    DbInstanceStorage: Optional[float]
    EngineVersion: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    MaintainEndTime: Optional[str]
    MaintainStartTime: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    ReplicaSetName: Optional[str]
    ReplicationFactor: Optional[float]
    RetentionPeriod: Optional[float]
    SecurityGroupId: Optional[str]
    SecurityIpList: Optional[Sequence[str]]
    SslAction: Optional[str]
    SslStatus: Optional[str]
    StorageEngine: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TdeStatus: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
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
            AccountPassword=json_data.get("AccountPassword"),
            BackupPeriod=json_data.get("BackupPeriod"),
            BackupTime=json_data.get("BackupTime"),
            DbInstanceClass=json_data.get("DbInstanceClass"),
            DbInstanceStorage=json_data.get("DbInstanceStorage"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            MaintainEndTime=json_data.get("MaintainEndTime"),
            MaintainStartTime=json_data.get("MaintainStartTime"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            ReplicaSetName=json_data.get("ReplicaSetName"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityIpList=json_data.get("SecurityIpList"),
            SslAction=json_data.get("SslAction"),
            SslStatus=json_data.get("SslStatus"),
            StorageEngine=json_data.get("StorageEngine"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TdeStatus=json_data.get("TdeStatus"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContextDefinition = KmsEncryptionContextDefinition


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


