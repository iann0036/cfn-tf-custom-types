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
    ConnectAddress: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    MaintainBegin: Optional[str]
    MaintainEnd: Optional[str]
    Name: Optional[str]
    OrderId: Optional[str]
    PartitionNum: Optional[float]
    Password: Optional[str]
    Port: Optional[str]
    ProductId: Optional[str]
    ResourceSpecCode: Optional[str]
    SecurityGroupId: Optional[str]
    SecurityGroupName: Optional[str]
    Specification: Optional[str]
    Status: Optional[str]
    StorageSpace: Optional[float]
    StorageSpecCode: Optional[str]
    SubnetId: Optional[str]
    SubnetName: Optional[str]
    Type: Optional[str]
    UsedStorageSpace: Optional[float]
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
            ConnectAddress=json_data.get("ConnectAddress"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            MaintainBegin=json_data.get("MaintainBegin"),
            MaintainEnd=json_data.get("MaintainEnd"),
            Name=json_data.get("Name"),
            OrderId=json_data.get("OrderId"),
            PartitionNum=json_data.get("PartitionNum"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ProductId=json_data.get("ProductId"),
            ResourceSpecCode=json_data.get("ResourceSpecCode"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SecurityGroupName=json_data.get("SecurityGroupName"),
            Specification=json_data.get("Specification"),
            Status=json_data.get("Status"),
            StorageSpace=json_data.get("StorageSpace"),
            StorageSpecCode=json_data.get("StorageSpecCode"),
            SubnetId=json_data.get("SubnetId"),
            SubnetName=json_data.get("SubnetName"),
            Type=json_data.get("Type"),
            UsedStorageSpace=json_data.get("UsedStorageSpace"),
            UserId=json_data.get("UserId"),
            VpcId=json_data.get("VpcId"),
            VpcName=json_data.get("VpcName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


