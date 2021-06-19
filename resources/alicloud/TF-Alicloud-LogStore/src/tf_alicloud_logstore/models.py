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
    AppendMeta: Optional[bool]
    AutoSplit: Optional[bool]
    EnableWebTracking: Optional[bool]
    Id: Optional[str]
    MaxSplitShardCount: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    RetentionPeriod: Optional[float]
    ShardCount: Optional[float]
    Shards: Optional[Sequence["_ShardsDefinition"]]
    EncryptConf: Optional[Sequence["_EncryptConfDefinition"]]

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
            AppendMeta=json_data.get("AppendMeta"),
            AutoSplit=json_data.get("AutoSplit"),
            EnableWebTracking=json_data.get("EnableWebTracking"),
            Id=json_data.get("Id"),
            MaxSplitShardCount=json_data.get("MaxSplitShardCount"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            ShardCount=json_data.get("ShardCount"),
            Shards=deserialize_list(json_data.get("Shards"), ShardsDefinition),
            EncryptConf=deserialize_list(json_data.get("EncryptConf"), EncryptConfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ShardsDefinition(BaseModel):
    BeginKey: Optional[str]
    EndKey: Optional[str]
    Id: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShardsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShardsDefinition"]:
        if not json_data:
            return None
        return cls(
            BeginKey=json_data.get("BeginKey"),
            EndKey=json_data.get("EndKey"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShardsDefinition = ShardsDefinition


@dataclass
class EncryptConfDefinition(BaseModel):
    Enable: Optional[bool]
    EncryptType: Optional[str]
    UserCmkInfo: Optional[Sequence["_UserCmkInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptConfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptConfDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            EncryptType=json_data.get("EncryptType"),
            UserCmkInfo=deserialize_list(json_data.get("UserCmkInfo"), UserCmkInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptConfDefinition = EncryptConfDefinition


@dataclass
class UserCmkInfoDefinition(BaseModel):
    Arn: Optional[str]
    CmkKeyId: Optional[str]
    RegionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserCmkInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserCmkInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            CmkKeyId=json_data.get("CmkKeyId"),
            RegionId=json_data.get("RegionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserCmkInfoDefinition = UserCmkInfoDefinition


