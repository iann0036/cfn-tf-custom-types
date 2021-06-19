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
    AssociatePublicIpAddress: Optional[bool]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    Name: Optional[str]
    OceanId: Optional[str]
    RestrictScaleDown: Optional[bool]
    RootVolumeSize: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    UserData: Optional[str]
    AutoscaleHeadrooms: Optional[Sequence["_AutoscaleHeadroomsDefinition"]]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMappingsDefinition"]]
    CreateOptions: Optional[Sequence["_CreateOptionsDefinition"]]
    ElasticIpPool: Optional[Sequence["_ElasticIpPoolDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    ResourceLimits: Optional[Sequence["_ResourceLimitsDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Taints: Optional[Sequence["_TaintsDefinition"]]

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
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceTypes=json_data.get("InstanceTypes"),
            Name=json_data.get("Name"),
            OceanId=json_data.get("OceanId"),
            RestrictScaleDown=json_data.get("RestrictScaleDown"),
            RootVolumeSize=json_data.get("RootVolumeSize"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetIds=json_data.get("SubnetIds"),
            UserData=json_data.get("UserData"),
            AutoscaleHeadrooms=deserialize_list(json_data.get("AutoscaleHeadrooms"), AutoscaleHeadroomsDefinition),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMappingsDefinition),
            CreateOptions=deserialize_list(json_data.get("CreateOptions"), CreateOptionsDefinition),
            ElasticIpPool=deserialize_list(json_data.get("ElasticIpPool"), ElasticIpPoolDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            ResourceLimits=deserialize_list(json_data.get("ResourceLimits"), ResourceLimitsDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Taints=deserialize_list(json_data.get("Taints"), TaintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscaleHeadroomsDefinition(BaseModel):
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadroomsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadroomsDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadroomsDefinition = AutoscaleHeadroomsDefinition


@dataclass
class BlockDeviceMappingsDefinition(BaseModel):
    DeviceName: Optional[str]
    NoDevice: Optional[str]
    VirtualName: Optional[str]
    Ebs: Optional[Sequence["_EbsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=deserialize_list(json_data.get("Ebs"), EbsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappingsDefinition = BlockDeviceMappingsDefinition


@dataclass
class EbsDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]
    DynamicVolumeSize: Optional[Sequence["_DynamicVolumeSizeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
            DynamicVolumeSize=deserialize_list(json_data.get("DynamicVolumeSize"), DynamicVolumeSizeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsDefinition = EbsDefinition


@dataclass
class DynamicVolumeSizeDefinition(BaseModel):
    BaseSize: Optional[float]
    Resource: Optional[str]
    SizePerResourceUnit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicVolumeSizeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicVolumeSizeDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseSize=json_data.get("BaseSize"),
            Resource=json_data.get("Resource"),
            SizePerResourceUnit=json_data.get("SizePerResourceUnit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicVolumeSizeDefinition = DynamicVolumeSizeDefinition


@dataclass
class CreateOptionsDefinition(BaseModel):
    InitialNodes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CreateOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            InitialNodes=json_data.get("InitialNodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateOptionsDefinition = CreateOptionsDefinition


@dataclass
class ElasticIpPoolDefinition(BaseModel):
    TagSelector: Optional[Sequence["_TagSelectorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticIpPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticIpPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            TagSelector=deserialize_list(json_data.get("TagSelector"), TagSelectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticIpPoolDefinition = ElasticIpPoolDefinition


@dataclass
class TagSelectorDefinition(BaseModel):
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSelectorDefinition = TagSelectorDefinition


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
class ResourceLimitsDefinition(BaseModel):
    MaxInstanceCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstanceCount=json_data.get("MaxInstanceCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitsDefinition = ResourceLimitsDefinition


@dataclass
class StrategyDefinition(BaseModel):
    SpotPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            SpotPercentage=json_data.get("SpotPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


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


