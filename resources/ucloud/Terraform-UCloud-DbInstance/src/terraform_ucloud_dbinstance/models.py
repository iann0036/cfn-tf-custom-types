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
    AvailabilityZone: Optional[str]
    BackupBeginTime: Optional[float]
    BackupBlackList: Optional[Sequence[str]]
    BackupCount: Optional[float]
    BackupDate: Optional[str]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    Duration: Optional[float]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    ExpireTime: Optional[str]
    Id: Optional[str]
    InstanceStorage: Optional[float]
    InstanceType: Optional[str]
    ModifyTime: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    PrivateIp: Optional[str]
    StandbyZone: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
    Tag: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupBeginTime=json_data.get("BackupBeginTime"),
            BackupBlackList=json_data.get("BackupBlackList"),
            BackupCount=json_data.get("BackupCount"),
            BackupDate=json_data.get("BackupDate"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            Duration=json_data.get("Duration"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            ExpireTime=json_data.get("ExpireTime"),
            Id=json_data.get("Id"),
            InstanceStorage=json_data.get("InstanceStorage"),
            InstanceType=json_data.get("InstanceType"),
            ModifyTime=json_data.get("ModifyTime"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            PrivateIp=json_data.get("PrivateIp"),
            StandbyZone=json_data.get("StandbyZone"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


