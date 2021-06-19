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
    AcdIdentifier: Optional[str]
    AksName: Optional[str]
    AksResourceGroupName: Optional[str]
    ControllerClusterId: Optional[str]
    CustomData: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SshPublicKey: Optional[str]
    UserName: Optional[str]
    Autoscaler: Optional[Sequence["_AutoscalerDefinition"]]
    Extension: Optional[Sequence["_ExtensionDefinition"]]
    Health: Optional[Sequence["_HealthDefinition"]]
    Image: Optional[Sequence["_ImageDefinition"]]
    LoadBalancer: Optional[Sequence["_LoadBalancerDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]
    OsDisk: Optional[Sequence["_OsDiskDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    VmSizes: Optional[Sequence["_VmSizesDefinition"]]

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
            AcdIdentifier=json_data.get("AcdIdentifier"),
            AksName=json_data.get("AksName"),
            AksResourceGroupName=json_data.get("AksResourceGroupName"),
            ControllerClusterId=json_data.get("ControllerClusterId"),
            CustomData=json_data.get("CustomData"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SshPublicKey=json_data.get("SshPublicKey"),
            UserName=json_data.get("UserName"),
            Autoscaler=deserialize_list(json_data.get("Autoscaler"), AutoscalerDefinition),
            Extension=deserialize_list(json_data.get("Extension"), ExtensionDefinition),
            Health=deserialize_list(json_data.get("Health"), HealthDefinition),
            Image=deserialize_list(json_data.get("Image"), ImageDefinition),
            LoadBalancer=deserialize_list(json_data.get("LoadBalancer"), LoadBalancerDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            OsDisk=deserialize_list(json_data.get("OsDisk"), OsDiskDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            VmSizes=deserialize_list(json_data.get("VmSizes"), VmSizesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalerDefinition(BaseModel):
    AutoscaleIsEnabled: Optional[bool]
    AutoscaleDown: Optional[Sequence["_AutoscaleDownDefinition"]]
    AutoscaleHeadroom: Optional[Sequence["_AutoscaleHeadroomDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalerDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscaleIsEnabled=json_data.get("AutoscaleIsEnabled"),
            AutoscaleDown=deserialize_list(json_data.get("AutoscaleDown"), AutoscaleDownDefinition),
            AutoscaleHeadroom=deserialize_list(json_data.get("AutoscaleHeadroom"), AutoscaleHeadroomDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalerDefinition = AutoscalerDefinition


@dataclass
class AutoscaleDownDefinition(BaseModel):
    MaxScaleDownPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleDownDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleDownDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxScaleDownPercentage=json_data.get("MaxScaleDownPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleDownDefinition = AutoscaleDownDefinition


@dataclass
class AutoscaleHeadroomDefinition(BaseModel):
    Automatic: Optional[Sequence["_AutomaticDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroomDefinition"]:
        if not json_data:
            return None
        return cls(
            Automatic=deserialize_list(json_data.get("Automatic"), AutomaticDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomDefinition = AutoscaleHeadroomDefinition


@dataclass
class AutomaticDefinition(BaseModel):
    IsEnabled: Optional[bool]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticDefinition = AutomaticDefinition


@dataclass
class ResourceLimitsDefinition(BaseModel):
    MaxMemoryGib: Optional[float]
    MaxVcpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxMemoryGib=json_data.get("MaxMemoryGib"),
            MaxVcpu=json_data.get("MaxVcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class ExtensionDefinition(BaseModel):
    ApiVersion: Optional[str]
    MinorVersionAutoUpgrade: Optional[bool]
    Name: Optional[str]
    Publisher: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiVersion=json_data.get("ApiVersion"),
            MinorVersionAutoUpgrade=json_data.get("MinorVersionAutoUpgrade"),
            Name=json_data.get("Name"),
            Publisher=json_data.get("Publisher"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionDefinition = ExtensionDefinition


@dataclass
class HealthDefinition(BaseModel):
    GracePeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthDefinition"]:
        if not json_data:
            return None
        return cls(
            GracePeriod=json_data.get("GracePeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthDefinition = HealthDefinition


@dataclass
class ImageDefinition(BaseModel):
    Marketplace: Optional[Sequence["_MarketplaceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Marketplace=deserialize_list(json_data.get("Marketplace"), MarketplaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageDefinition = ImageDefinition


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
class LoadBalancerDefinition(BaseModel):
    BackendPoolNames: Optional[Sequence[str]]
    LoadBalancerSku: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPoolNames=json_data.get("BackendPoolNames"),
            LoadBalancerSku=json_data.get("LoadBalancerSku"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerDefinition = LoadBalancerDefinition


@dataclass
class NetworkDefinition(BaseModel):
    ResourceGroupName: Optional[str]
    VirtualNetworkName: Optional[str]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]

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
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    AssignPublicIp: Optional[bool]
    IsPrimary: Optional[bool]
    SubnetName: Optional[str]
    AdditionalIpConfig: Optional[Sequence["_AdditionalIpConfigDefinition"]]
    SecurityGroup: Optional[Sequence["_SecurityGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            IsPrimary=json_data.get("IsPrimary"),
            SubnetName=json_data.get("SubnetName"),
            AdditionalIpConfig=deserialize_list(json_data.get("AdditionalIpConfig"), AdditionalIpConfigDefinition),
            SecurityGroup=deserialize_list(json_data.get("SecurityGroup"), SecurityGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class AdditionalIpConfigDefinition(BaseModel):
    Name: Optional[str]
    PrivateIpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalIpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalIpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpVersion=json_data.get("PrivateIpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalIpConfigDefinition = AdditionalIpConfigDefinition


@dataclass
class SecurityGroupDefinition(BaseModel):
    Name: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityGroupDefinition = SecurityGroupDefinition


@dataclass
class OsDiskDefinition(BaseModel):
    SizeGb: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OsDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            SizeGb=json_data.get("SizeGb"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsDiskDefinition = OsDiskDefinition


@dataclass
class StrategyDefinition(BaseModel):
    FallbackToOndemand: Optional[bool]
    SpotPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            FallbackToOndemand=json_data.get("FallbackToOndemand"),
            SpotPercentage=json_data.get("SpotPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class TagDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class VmSizesDefinition(BaseModel):
    Whitelist: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VmSizesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmSizesDefinition"]:
        if not json_data:
            return None
        return cls(
            Whitelist=json_data.get("Whitelist"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmSizesDefinition = VmSizesDefinition


