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
    EngineVersion: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
    Name: Optional[str]
    Period: Optional[float]
    RetentionPeriod: Optional[float]
    SecurityIpList: Optional[Sequence[str]]
    StorageEngine: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    MongoList: Optional[Sequence["_MongoList"]]
    ShardList: Optional[Sequence["_ShardList"]]

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
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            SecurityIpList=json_data.get("SecurityIpList"),
            StorageEngine=json_data.get("StorageEngine"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            MongoList=json_data.get("MongoList"),
            ShardList=json_data.get("ShardList"),
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
class MongoList:
    NodeClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoList"]:
        if not json_data:
            return None
        return cls(
            NodeClass=json_data.get("NodeClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoList = MongoList


@dataclass
class ShardList:
    NodeClass: Optional[str]
    NodeStorage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShardList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShardList"]:
        if not json_data:
            return None
        return cls(
            NodeClass=json_data.get("NodeClass"),
            NodeStorage=json_data.get("NodeStorage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShardList = ShardList


