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
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    Duration: Optional[float]
    ExpireTime: Optional[str]
    InstanceType: Optional[str]
    IpSet: Optional[Sequence["_IpSet"]]
    Name: Optional[str]
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
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            Duration=json_data.get("Duration"),
            ExpireTime=json_data.get("ExpireTime"),
            InstanceType=json_data.get("InstanceType"),
            IpSet=json_data.get("IpSet"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpSet:
    Ip: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSet"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSet = IpSet


