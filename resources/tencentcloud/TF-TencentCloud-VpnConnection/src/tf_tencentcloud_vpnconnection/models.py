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
    CreateTime: Optional[str]
    CustomerGatewayId: Optional[str]
    EncryptProto: Optional[str]
    Id: Optional[str]
    IkeDhGroupName: Optional[str]
    IkeExchangeMode: Optional[str]
    IkeLocalAddress: Optional[str]
    IkeLocalFqdnName: Optional[str]
    IkeLocalIdentity: Optional[str]
    IkeProtoAuthenAlgorithm: Optional[str]
    IkeProtoEncryAlgorithm: Optional[str]
    IkeRemoteAddress: Optional[str]
    IkeRemoteFqdnName: Optional[str]
    IkeRemoteIdentity: Optional[str]
    IkeSaLifetimeSeconds: Optional[float]
    IkeVersion: Optional[str]
    IpsecEncryptAlgorithm: Optional[str]
    IpsecIntegrityAlgorithm: Optional[str]
    IpsecPfsDhGroup: Optional[str]
    IpsecSaLifetimeSeconds: Optional[float]
    IpsecSaLifetimeTraffic: Optional[float]
    IsCcnType: Optional[bool]
    Name: Optional[str]
    NetStatus: Optional[str]
    PreShareKey: Optional[str]
    RouteType: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpcId: Optional[str]
    VpnGatewayId: Optional[str]
    VpnProto: Optional[str]
    SecurityGroupPolicy: Optional[Sequence["_SecurityGroupPolicyDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            EncryptProto=json_data.get("EncryptProto"),
            Id=json_data.get("Id"),
            IkeDhGroupName=json_data.get("IkeDhGroupName"),
            IkeExchangeMode=json_data.get("IkeExchangeMode"),
            IkeLocalAddress=json_data.get("IkeLocalAddress"),
            IkeLocalFqdnName=json_data.get("IkeLocalFqdnName"),
            IkeLocalIdentity=json_data.get("IkeLocalIdentity"),
            IkeProtoAuthenAlgorithm=json_data.get("IkeProtoAuthenAlgorithm"),
            IkeProtoEncryAlgorithm=json_data.get("IkeProtoEncryAlgorithm"),
            IkeRemoteAddress=json_data.get("IkeRemoteAddress"),
            IkeRemoteFqdnName=json_data.get("IkeRemoteFqdnName"),
            IkeRemoteIdentity=json_data.get("IkeRemoteIdentity"),
            IkeSaLifetimeSeconds=json_data.get("IkeSaLifetimeSeconds"),
            IkeVersion=json_data.get("IkeVersion"),
            IpsecEncryptAlgorithm=json_data.get("IpsecEncryptAlgorithm"),
            IpsecIntegrityAlgorithm=json_data.get("IpsecIntegrityAlgorithm"),
            IpsecPfsDhGroup=json_data.get("IpsecPfsDhGroup"),
            IpsecSaLifetimeSeconds=json_data.get("IpsecSaLifetimeSeconds"),
            IpsecSaLifetimeTraffic=json_data.get("IpsecSaLifetimeTraffic"),
            IsCcnType=json_data.get("IsCcnType"),
            Name=json_data.get("Name"),
            NetStatus=json_data.get("NetStatus"),
            PreShareKey=json_data.get("PreShareKey"),
            RouteType=json_data.get("RouteType"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpcId=json_data.get("VpcId"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            VpnProto=json_data.get("VpnProto"),
            SecurityGroupPolicy=deserialize_list(json_data.get("SecurityGroupPolicy"), SecurityGroupPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class SecurityGroupPolicyDefinition(BaseModel):
    LocalCidrBlock: Optional[str]
    RemoteCidrBlock: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityGroupPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityGroupPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalCidrBlock=json_data.get("LocalCidrBlock"),
            RemoteCidrBlock=json_data.get("RemoteCidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityGroupPolicyDefinition = SecurityGroupPolicyDefinition


