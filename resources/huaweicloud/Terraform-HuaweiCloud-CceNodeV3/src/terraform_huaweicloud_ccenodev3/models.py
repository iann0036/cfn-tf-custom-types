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
    Annotations: Optional[Sequence["_Annotations"]]
    AvailabilityZone: Optional[str]
    BandwidthChargeMode: Optional[str]
    BandwidthSize: Optional[float]
    BillingMode: Optional[float]
    ClusterId: Optional[str]
    EcsPerformanceType: Optional[str]
    EipCount: Optional[float]
    EipIds: Optional[Sequence[str]]
    ExtendParamChargingMode: Optional[float]
    FlavorId: Optional[str]
    Id: Optional[str]
    Iptype: Optional[str]
    KeyPair: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MaxPods: Optional[float]
    Name: Optional[str]
    OrderId: Optional[str]
    Os: Optional[str]
    Password: Optional[str]
    Postinstall: Optional[str]
    Preinstall: Optional[str]
    PrivateIp: Optional[str]
    ProductId: Optional[str]
    PublicIp: Optional[str]
    PublicKey: Optional[str]
    Region: Optional[str]
    ServerId: Optional[str]
    Sharetype: Optional[str]
    DataVolumes: Optional[Sequence["_DataVolumes"]]
    RootVolume: Optional[Sequence["_RootVolume"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Annotations=json_data.get("Annotations"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BandwidthChargeMode=json_data.get("BandwidthChargeMode"),
            BandwidthSize=json_data.get("BandwidthSize"),
            BillingMode=json_data.get("BillingMode"),
            ClusterId=json_data.get("ClusterId"),
            EcsPerformanceType=json_data.get("EcsPerformanceType"),
            EipCount=json_data.get("EipCount"),
            EipIds=json_data.get("EipIds"),
            ExtendParamChargingMode=json_data.get("ExtendParamChargingMode"),
            FlavorId=json_data.get("FlavorId"),
            Id=json_data.get("Id"),
            Iptype=json_data.get("Iptype"),
            KeyPair=json_data.get("KeyPair"),
            Labels=json_data.get("Labels"),
            MaxPods=json_data.get("MaxPods"),
            Name=json_data.get("Name"),
            OrderId=json_data.get("OrderId"),
            Os=json_data.get("Os"),
            Password=json_data.get("Password"),
            Postinstall=json_data.get("Postinstall"),
            Preinstall=json_data.get("Preinstall"),
            PrivateIp=json_data.get("PrivateIp"),
            ProductId=json_data.get("ProductId"),
            PublicIp=json_data.get("PublicIp"),
            PublicKey=json_data.get("PublicKey"),
            Region=json_data.get("Region"),
            ServerId=json_data.get("ServerId"),
            Sharetype=json_data.get("Sharetype"),
            DataVolumes=json_data.get("DataVolumes"),
            RootVolume=json_data.get("RootVolume"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Annotations:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class DataVolumes:
    ExtendParam: Optional[str]
    Size: Optional[float]
    Volumetype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataVolumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataVolumes"]:
        if not json_data:
            return None
        return cls(
            ExtendParam=json_data.get("ExtendParam"),
            Size=json_data.get("Size"),
            Volumetype=json_data.get("Volumetype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataVolumes = DataVolumes


@dataclass
class RootVolume:
    ExtendParam: Optional[str]
    Size: Optional[float]
    Volumetype: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootVolume"]:
        if not json_data:
            return None
        return cls(
            ExtendParam=json_data.get("ExtendParam"),
            Size=json_data.get("Size"),
            Volumetype=json_data.get("Volumetype"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootVolume = RootVolume


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


