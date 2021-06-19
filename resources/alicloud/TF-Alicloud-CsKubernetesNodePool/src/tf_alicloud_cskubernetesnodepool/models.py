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
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    ClusterId: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstallCloudMonitor: Optional[bool]
    InstanceChargeType: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyName: Optional[str]
    KmsEncryptedPassword: Optional[str]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeNameMode: Optional[str]
    Password: Optional[str]
    Period: Optional[float]
    PeriodUnit: Optional[str]
    ResourceGroupId: Optional[str]
    ScalingGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    SpotStrategy: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskPerformanceLevel: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Unschedulable: Optional[bool]
    UserData: Optional[str]
    VpcId: Optional[str]
    VswitchIds: Optional[Sequence[str]]
    DataDisks: Optional[Sequence["_DataDisksDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Management: Optional[Sequence["_ManagementDefinition"]]
    ScalingConfig: Optional[Sequence["_ScalingConfigDefinition"]]
    SpotPriceLimit: Optional[Sequence["_SpotPriceLimitDefinition"]]
    Taints: Optional[Sequence["_TaintsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            ClusterId=json_data.get("ClusterId"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstallCloudMonitor=json_data.get("InstallCloudMonitor"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceTypes=json_data.get("InstanceTypes"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyName=json_data.get("KeyName"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeNameMode=json_data.get("NodeNameMode"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            PeriodUnit=json_data.get("PeriodUnit"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SpotStrategy=json_data.get("SpotStrategy"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskPerformanceLevel=json_data.get("SystemDiskPerformanceLevel"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Unschedulable=json_data.get("Unschedulable"),
            UserData=json_data.get("UserData"),
            VpcId=json_data.get("VpcId"),
            VswitchIds=json_data.get("VswitchIds"),
            DataDisks=deserialize_list(json_data.get("DataDisks"), DataDisksDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Management=deserialize_list(json_data.get("Management"), ManagementDefinition),
            ScalingConfig=deserialize_list(json_data.get("ScalingConfig"), ScalingConfigDefinition),
            SpotPriceLimit=deserialize_list(json_data.get("SpotPriceLimit"), SpotPriceLimitDefinition),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class DataDisksDefinition(BaseModel):
    AutoSnapshotPolicyId: Optional[str]
    Category: Optional[str]
    Device: Optional[str]
    Encrypted: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    PerformanceLevel: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisksDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoSnapshotPolicyId=json_data.get("AutoSnapshotPolicyId"),
            Category=json_data.get("Category"),
            Device=json_data.get("Device"),
            Encrypted=json_data.get("Encrypted"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisksDefinition = DataDisksDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ManagementDefinition(BaseModel):
    AutoRepair: Optional[bool]
    AutoUpgrade: Optional[bool]
    MaxUnavailable: Optional[float]
    Surge: Optional[float]
    SurgePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoRepair=json_data.get("AutoRepair"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
            Surge=json_data.get("Surge"),
            SurgePercentage=json_data.get("SurgePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementDefinition = ManagementDefinition


@dataclass
class ScalingConfigDefinition(BaseModel):
    EipBandwidth: Optional[float]
    EipInternetChargeType: Optional[str]
    IsBondEip: Optional[bool]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EipBandwidth=json_data.get("EipBandwidth"),
            EipInternetChargeType=json_data.get("EipInternetChargeType"),
            IsBondEip=json_data.get("IsBondEip"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfigDefinition = ScalingConfigDefinition


@dataclass
class SpotPriceLimitDefinition(BaseModel):
    InstanceType: Optional[str]
    PriceLimit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotPriceLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotPriceLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            PriceLimit=json_data.get("PriceLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotPriceLimitDefinition = SpotPriceLimitDefinition


@dataclass
class TaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintsDefinition = TaintsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


