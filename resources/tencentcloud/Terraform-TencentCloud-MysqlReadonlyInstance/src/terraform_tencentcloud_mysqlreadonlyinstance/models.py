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
    AutoRenewFlag: Optional[float]
    Id: Optional[str]
    InstanceName: Optional[str]
    IntranetIp: Optional[str]
    IntranetPort: Optional[float]
    Locked: Optional[float]
    MasterInstanceId: Optional[str]
    MemSize: Optional[float]
    PayType: Optional[float]
    Period: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    Status: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TaskStatus: Optional[float]
    VolumeSize: Optional[float]
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
            AutoRenewFlag=json_data.get("AutoRenewFlag"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            IntranetIp=json_data.get("IntranetIp"),
            IntranetPort=json_data.get("IntranetPort"),
            Locked=json_data.get("Locked"),
            MasterInstanceId=json_data.get("MasterInstanceId"),
            MemSize=json_data.get("MemSize"),
            PayType=json_data.get("PayType"),
            Period=json_data.get("Period"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            TaskStatus=json_data.get("TaskStatus"),
            VolumeSize=json_data.get("VolumeSize"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


