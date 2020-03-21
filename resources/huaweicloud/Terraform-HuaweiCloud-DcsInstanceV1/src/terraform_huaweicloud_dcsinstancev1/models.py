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
    AccessUser: Optional[str]
    AvailableZones: Optional[Sequence[str]]
    BackupAt: Optional[Sequence[float]]
    BackupType: Optional[str]
    BeginAt: Optional[str]
    Capacity: Optional[float]
    Description: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    InternalVersion: Optional[str]
    Ip: Optional[str]
    MaintainBegin: Optional[str]
    MaintainEnd: Optional[str]
    MaxMemory: Optional[str]
    Name: Optional[str]
    OrderId: Optional[str]
    Password: Optional[str]
    PeriodType: Optional[str]
    Port: Optional[str]
    ProductId: Optional[str]
    ResourceSpecCode: Optional[str]
    SaveDays: Optional[float]
    SecurityGroupId: Optional[str]
    SecurityGroupName: Optional[str]
    SubnetId: Optional[str]
    SubnetName: Optional[str]
    UsedMemory: Optional[float]
    UserId: Optional[str]
    VpcId: Optional[str]
    VpcName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessUser=json_data.get("AccessUser"),
            AvailableZones=json_data.get("AvailableZones"),
            BackupAt=json_data.get("BackupAt"),
            BackupType=json_data.get("BackupType"),
            BeginAt=json_data.get("BeginAt"),
            Capacity=json_data.get("Capacity"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            InternalVersion=json_data.get("InternalVersion"),
            Ip=json_data.get("Ip"),
            MaintainBegin=json_data.get("MaintainBegin"),
            MaintainEnd=json_data.get("MaintainEnd"),
            MaxMemory=json_data.get("MaxMemory"),
            Name=json_data.get("Name"),
            OrderId=json_data.get("OrderId"),
            Password=json_data.get("Password"),
            PeriodType=json_data.get("PeriodType"),
            Port=json_data.get("Port"),
            ProductId=json_data.get("ProductId"),
            ResourceSpecCode=json_data.get("ResourceSpecCode"),
            SaveDays=json_data.get("SaveDays"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupName=json_data.get("SecurityGroupName"),
            SubnetId=json_data.get("SubnetId"),
            SubnetName=json_data.get("SubnetName"),
            UsedMemory=json_data.get("UsedMemory"),
            UserId=json_data.get("UserId"),
            VpcId=json_data.get("VpcId"),
            VpcName=json_data.get("VpcName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


