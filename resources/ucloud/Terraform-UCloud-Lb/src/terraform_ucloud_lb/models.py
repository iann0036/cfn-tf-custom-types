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
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    ExpireTime: Optional[str]
    Internal: Optional[bool]
    IpSet: Optional[Sequence["_IpSet"]]
    Name: Optional[str]
    PrivateIp: Optional[str]
    Remark: Optional[str]
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
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            ExpireTime=json_data.get("ExpireTime"),
            Internal=json_data.get("Internal"),
            IpSet=json_data.get("IpSet"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            Remark=json_data.get("Remark"),
            SubnetId=json_data.get("SubnetId"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpSet:
    InternetType: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSet"]:
        if not json_data:
            return None
        return cls(
            InternetType=json_data.get("InternetType"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSet = IpSet


