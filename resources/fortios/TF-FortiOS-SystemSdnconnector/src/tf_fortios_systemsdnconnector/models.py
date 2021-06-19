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
    AccessKey: Optional[str]
    ApiKey: Optional[str]
    AzureRegion: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    CompartmentId: Optional[str]
    ComputeGeneration: Optional[float]
    Domain: Optional[str]
    DynamicSortSubtable: Optional[str]
    GcpProject: Optional[str]
    GroupName: Optional[str]
    HaStatus: Optional[str]
    IbmRegion: Optional[str]
    Id: Optional[str]
    KeyPasswd: Optional[str]
    LoginEndpoint: Optional[str]
    Name: Optional[str]
    OciCert: Optional[str]
    OciFingerprint: Optional[str]
    OciRegion: Optional[str]
    OciRegionType: Optional[str]
    Password: Optional[str]
    PrivateKey: Optional[str]
    Region: Optional[str]
    ResourceGroup: Optional[str]
    ResourceUrl: Optional[str]
    SecretKey: Optional[str]
    SecretToken: Optional[str]
    Server: Optional[str]
    ServerPort: Optional[float]
    ServiceAccount: Optional[str]
    Status: Optional[str]
    SubscriptionId: Optional[str]
    TenantId: Optional[str]
    Type: Optional[str]
    UpdateInterval: Optional[float]
    UseMetadataIam: Optional[str]
    UserId: Optional[str]
    Username: Optional[str]
    VcenterPassword: Optional[str]
    VcenterServer: Optional[str]
    VcenterUsername: Optional[str]
    Vdomparam: Optional[str]
    VpcId: Optional[str]
    ExternalIp: Optional[Sequence["_ExternalIpDefinition"]]
    Nic: Optional[Sequence["_NicDefinition"]]
    Route: Optional[Sequence["_RouteDefinition"]]
    RouteTable: Optional[Sequence["_RouteTableDefinition"]]

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
            AccessKey=json_data.get("AccessKey"),
            ApiKey=json_data.get("ApiKey"),
            AzureRegion=json_data.get("AzureRegion"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            CompartmentId=json_data.get("CompartmentId"),
            ComputeGeneration=json_data.get("ComputeGeneration"),
            Domain=json_data.get("Domain"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GcpProject=json_data.get("GcpProject"),
            GroupName=json_data.get("GroupName"),
            HaStatus=json_data.get("HaStatus"),
            IbmRegion=json_data.get("IbmRegion"),
            Id=json_data.get("Id"),
            KeyPasswd=json_data.get("KeyPasswd"),
            LoginEndpoint=json_data.get("LoginEndpoint"),
            Name=json_data.get("Name"),
            OciCert=json_data.get("OciCert"),
            OciFingerprint=json_data.get("OciFingerprint"),
            OciRegion=json_data.get("OciRegion"),
            OciRegionType=json_data.get("OciRegionType"),
            Password=json_data.get("Password"),
            PrivateKey=json_data.get("PrivateKey"),
            Region=json_data.get("Region"),
            ResourceGroup=json_data.get("ResourceGroup"),
            ResourceUrl=json_data.get("ResourceUrl"),
            SecretKey=json_data.get("SecretKey"),
            SecretToken=json_data.get("SecretToken"),
            Server=json_data.get("Server"),
            ServerPort=json_data.get("ServerPort"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Status=json_data.get("Status"),
            SubscriptionId=json_data.get("SubscriptionId"),
            TenantId=json_data.get("TenantId"),
            Type=json_data.get("Type"),
            UpdateInterval=json_data.get("UpdateInterval"),
            UseMetadataIam=json_data.get("UseMetadataIam"),
            UserId=json_data.get("UserId"),
            Username=json_data.get("Username"),
            VcenterPassword=json_data.get("VcenterPassword"),
            VcenterServer=json_data.get("VcenterServer"),
            VcenterUsername=json_data.get("VcenterUsername"),
            Vdomparam=json_data.get("Vdomparam"),
            VpcId=json_data.get("VpcId"),
            ExternalIp=deserialize_list(json_data.get("ExternalIp"), ExternalIpDefinition),
            Nic=deserialize_list(json_data.get("Nic"), NicDefinition),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
            RouteTable=deserialize_list(json_data.get("RouteTable"), RouteTableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExternalIpDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalIpDefinition = ExternalIpDefinition


@dataclass
class NicDefinition(BaseModel):
    Name: Optional[str]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NicDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NicDefinition = NicDefinition


@dataclass
class IpDefinition(BaseModel):
    Name: Optional[str]
    PublicIp: Optional[str]
    ResourceGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            ResourceGroup=json_data.get("ResourceGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class RouteDefinition(BaseModel):
    Name: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class RouteTableDefinition(BaseModel):
    Name: Optional[str]
    ResourceGroup: Optional[str]
    SubscriptionId: Optional[str]
    Route: Optional[Sequence["_RouteDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ResourceGroup=json_data.get("ResourceGroup"),
            SubscriptionId=json_data.get("SubscriptionId"),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteTableDefinition = RouteTableDefinition


