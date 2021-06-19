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
    DesiredCapacity: Optional[float]
    Id: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    OdSizes: Optional[Sequence[str]]
    Os: Optional[str]
    Region: Optional[str]
    ResourceGroupName: Optional[str]
    SpotSizes: Optional[Sequence[str]]
    Image: Optional[Sequence["_ImageDefinition"]]
    Login: Optional[Sequence["_LoginDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]

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
            DesiredCapacity=json_data.get("DesiredCapacity"),
            Id=json_data.get("Id"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            OdSizes=json_data.get("OdSizes"),
            Os=json_data.get("Os"),
            Region=json_data.get("Region"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SpotSizes=json_data.get("SpotSizes"),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
            Login=deserialize_list(json_data.get("Login"), LoginDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ImageDefinition(BaseModel):
    Custom: Optional[Sequence["_CustomDefinition"]]
    Marketplace: Optional[Sequence["_MarketplaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
            Marketplace=deserialize_list(json_data.get("Marketplace"), MarketplaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinition = ImageDefinition


@dataclass
class CustomDefinition(BaseModel):
    ImageName: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageName=json_data.get("ImageName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDefinition = CustomDefinition


@dataclass
class MarketplaceDefinition(BaseModel):
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MarketplaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketplaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketplaceDefinition = MarketplaceDefinition


@dataclass
class LoginDefinition(BaseModel):
    Password: Optional[str]
    SshPublicKey: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoginDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SshPublicKey=json_data.get("SshPublicKey"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoginDefinition = LoginDefinition


@dataclass
class NetworkDefinition(BaseModel):
    ResourceGroupName: Optional[str]
    VirtualNetworkName: Optional[str]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfacesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceGroupName=json_data.get("ResourceGroupName"),
            VirtualNetworkName=json_data.get("VirtualNetworkName"),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class NetworkInterfacesDefinition(BaseModel):
    AssignPublicIp: Optional[bool]
    IsPrimary: Optional[bool]
    SubnetName: Optional[str]
    AdditionalIpConfigs: Optional[Sequence["_AdditionalIpConfigsDefinition"]]
    ApplicationSecurityGroup: Optional[Sequence["_ApplicationSecurityGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            IsPrimary=json_data.get("IsPrimary"),
            SubnetName=json_data.get("SubnetName"),
            AdditionalIpConfigs=deserialize_list(json_data.get("AdditionalIpConfigs"), AdditionalIpConfigsDefinition),
            ApplicationSecurityGroup=deserialize_list(json_data.get("ApplicationSecurityGroup"), ApplicationSecurityGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfacesDefinition = NetworkInterfacesDefinition


@dataclass
class AdditionalIpConfigsDefinition(BaseModel):
    Name: Optional[str]
    PrivateIpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalIpConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalIpConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpVersion=json_data.get("PrivateIpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalIpConfigsDefinition = AdditionalIpConfigsDefinition


@dataclass
class ApplicationSecurityGroupDefinition(BaseModel):
    Name: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSecurityGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSecurityGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSecurityGroupDefinition = ApplicationSecurityGroupDefinition


@dataclass
class StrategyDefinition(BaseModel):
    DrainingTimeout: Optional[float]
    FallbackToOnDemand: Optional[bool]
    OdCount: Optional[float]
    SpotPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            DrainingTimeout=json_data.get("DrainingTimeout"),
            FallbackToOnDemand=json_data.get("FallbackToOnDemand"),
            OdCount=json_data.get("OdCount"),
            SpotPercentage=json_data.get("SpotPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


