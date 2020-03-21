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
    Bandwidth: Optional[float]
    ChargeMode: Optional[str]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    Duration: Optional[float]
    ExpireTime: Optional[str]
    InternetType: Optional[str]
    IpSet: Optional[Sequence["_IpSet"]]
    Name: Optional[str]
    PublicIp: Optional[str]
    Remark: Optional[str]
    Resource: Optional[Sequence["_Resource"]]
    Status: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bandwidth=json_data.get("Bandwidth"),
            ChargeMode=json_data.get("ChargeMode"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            Duration=json_data.get("Duration"),
            ExpireTime=json_data.get("ExpireTime"),
            InternetType=json_data.get("InternetType"),
            IpSet=json_data.get("IpSet"),
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            Remark=json_data.get("Remark"),
            Resource=json_data.get("Resource"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
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


@dataclass
class Resource:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Resource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resource"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resource = Resource


