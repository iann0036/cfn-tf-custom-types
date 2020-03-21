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
    CreateTime: Optional[str]
    CustomerGatewayId: Optional[str]
    Name: Optional[str]
    Remark: Optional[str]
    Tag: Optional[str]
    VpcId: Optional[str]
    VpnGatewayId: Optional[str]
    IkeConfig: Optional[Sequence["_IkeConfig"]]
    IpsecConfig: Optional[Sequence["_IpsecConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateTime=json_data.get("CreateTime"),
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            Name=json_data.get("Name"),
            Remark=json_data.get("Remark"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            IkeConfig=json_data.get("IkeConfig"),
            IpsecConfig=json_data.get("IpsecConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IkeConfig:
    AuthenticationAlgorithm: Optional[str]
    DhGroup: Optional[str]
    EncryptionAlgorithm: Optional[str]
    ExchangeMode: Optional[str]
    IkeVersion: Optional[str]
    LocalId: Optional[str]
    PreSharedKey: Optional[str]
    RemoteId: Optional[str]
    SaLifeTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IkeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IkeConfig"]:
        if not json_data:
            return None
        return cls(
            AuthenticationAlgorithm=json_data.get("AuthenticationAlgorithm"),
            DhGroup=json_data.get("DhGroup"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            ExchangeMode=json_data.get("ExchangeMode"),
            IkeVersion=json_data.get("IkeVersion"),
            LocalId=json_data.get("LocalId"),
            PreSharedKey=json_data.get("PreSharedKey"),
            RemoteId=json_data.get("RemoteId"),
            SaLifeTime=json_data.get("SaLifeTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IkeConfig = IkeConfig


@dataclass
class IpsecConfig:
    AuthenticationAlgorithm: Optional[str]
    EncryptionAlgorithm: Optional[str]
    LocalSubnetIds: Optional[Sequence[str]]
    PfsDhGroup: Optional[str]
    Protocol: Optional[str]
    RemoteSubnets: Optional[Sequence[str]]
    SaLifeTime: Optional[float]
    SaLifeTimeBytes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecConfig"]:
        if not json_data:
            return None
        return cls(
            AuthenticationAlgorithm=json_data.get("AuthenticationAlgorithm"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            LocalSubnetIds=json_data.get("LocalSubnetIds"),
            PfsDhGroup=json_data.get("PfsDhGroup"),
            Protocol=json_data.get("Protocol"),
            RemoteSubnets=json_data.get("RemoteSubnets"),
            SaLifeTime=json_data.get("SaLifeTime"),
            SaLifeTimeBytes=json_data.get("SaLifeTimeBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecConfig = IpsecConfig


