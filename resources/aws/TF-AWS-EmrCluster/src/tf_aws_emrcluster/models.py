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
    AdditionalInfo: Optional[str]
    Applications: Optional[Sequence[str]]
    Arn: Optional[str]
    AutoscalingRole: Optional[str]
    ClusterState: Optional[str]
    Configurations: Optional[str]
    ConfigurationsJson: Optional[str]
    CustomAmiId: Optional[str]
    EbsRootVolumeSize: Optional[float]
    Id: Optional[str]
    KeepJobFlowAliveWhenNoSteps: Optional[bool]
    LogUri: Optional[str]
    MasterPublicDns: Optional[str]
    Name: Optional[str]
    ReleaseLabel: Optional[str]
    ScaleDownBehavior: Optional[str]
    SecurityConfiguration: Optional[str]
    ServiceRole: Optional[str]
    Step: Optional[Sequence["_StepDefinition3"]]
    StepConcurrencyLevel: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TerminationProtection: Optional[bool]
    VisibleToAllUsers: Optional[bool]
    BootstrapAction: Optional[Sequence["_BootstrapActionDefinition"]]
    CoreInstanceFleet: Optional[Sequence["_CoreInstanceFleetDefinition"]]
    CoreInstanceGroup: Optional[Sequence["_CoreInstanceGroupDefinition"]]
    Ec2Attributes: Optional[Sequence["_Ec2AttributesDefinition"]]
    KerberosAttributes: Optional[Sequence["_KerberosAttributesDefinition"]]
    MasterInstanceFleet: Optional[Sequence["_MasterInstanceFleetDefinition"]]
    MasterInstanceGroup: Optional[Sequence["_MasterInstanceGroupDefinition"]]

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
            AdditionalInfo=json_data.get("AdditionalInfo"),
            Applications=json_data.get("Applications"),
            Arn=json_data.get("Arn"),
            AutoscalingRole=json_data.get("AutoscalingRole"),
            ClusterState=json_data.get("ClusterState"),
            Configurations=json_data.get("Configurations"),
            ConfigurationsJson=json_data.get("ConfigurationsJson"),
            CustomAmiId=json_data.get("CustomAmiId"),
            EbsRootVolumeSize=json_data.get("EbsRootVolumeSize"),
            Id=json_data.get("Id"),
            KeepJobFlowAliveWhenNoSteps=json_data.get("KeepJobFlowAliveWhenNoSteps"),
            LogUri=json_data.get("LogUri"),
            MasterPublicDns=json_data.get("MasterPublicDns"),
            Name=json_data.get("Name"),
            ReleaseLabel=json_data.get("ReleaseLabel"),
            ScaleDownBehavior=json_data.get("ScaleDownBehavior"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            ServiceRole=json_data.get("ServiceRole"),
            Step=deserialize_list(json_data.get("Step"), StepDefinition3),
            StepConcurrencyLevel=json_data.get("StepConcurrencyLevel"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TerminationProtection=json_data.get("TerminationProtection"),
            VisibleToAllUsers=json_data.get("VisibleToAllUsers"),
            BootstrapAction=deserialize_list(json_data.get("BootstrapAction"), BootstrapActionDefinition),
            CoreInstanceFleet=deserialize_list(json_data.get("CoreInstanceFleet"), CoreInstanceFleetDefinition),
            CoreInstanceGroup=deserialize_list(json_data.get("CoreInstanceGroup"), CoreInstanceGroupDefinition),
            Ec2Attributes=deserialize_list(json_data.get("Ec2Attributes"), Ec2AttributesDefinition),
            KerberosAttributes=deserialize_list(json_data.get("KerberosAttributes"), KerberosAttributesDefinition),
            MasterInstanceFleet=deserialize_list(json_data.get("MasterInstanceFleet"), MasterInstanceFleetDefinition),
            MasterInstanceGroup=deserialize_list(json_data.get("MasterInstanceGroup"), MasterInstanceGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepDefinition3(BaseModel):
    ActionOnFailure: Optional[str]
    HadoopJarStep: Optional[Sequence["_StepDefinition2"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition3"]:
        if not json_data:
            return None
        return cls(
            ActionOnFailure=json_data.get("ActionOnFailure"),
            HadoopJarStep=deserialize_list(json_data.get("HadoopJarStep"), StepDefinition2),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition3 = StepDefinition3


@dataclass
class StepDefinition2(BaseModel):
    Args: Optional[Sequence[str]]
    Jar: Optional[str]
    MainClass: Optional[str]
    Properties: Optional[Sequence["_StepDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition2"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Jar=json_data.get("Jar"),
            MainClass=json_data.get("MainClass"),
            Properties=deserialize_list(json_data.get("Properties"), StepDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition2 = StepDefinition2


@dataclass
class StepDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition = StepDefinition


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class BootstrapActionDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapActionDefinition = BootstrapActionDefinition


@dataclass
class CoreInstanceFleetDefinition(BaseModel):
    Name: Optional[str]
    TargetOnDemandCapacity: Optional[float]
    TargetSpotCapacity: Optional[float]
    InstanceTypeConfigs: Optional[Sequence["_InstanceTypeConfigsDefinition"]]
    LaunchSpecifications: Optional[Sequence["_LaunchSpecificationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreInstanceFleetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreInstanceFleetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TargetOnDemandCapacity=json_data.get("TargetOnDemandCapacity"),
            TargetSpotCapacity=json_data.get("TargetSpotCapacity"),
            InstanceTypeConfigs=deserialize_list(json_data.get("InstanceTypeConfigs"), InstanceTypeConfigsDefinition),
            LaunchSpecifications=deserialize_list(json_data.get("LaunchSpecifications"), LaunchSpecificationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreInstanceFleetDefinition = CoreInstanceFleetDefinition


@dataclass
class InstanceTypeConfigsDefinition(BaseModel):
    BidPrice: Optional[str]
    BidPriceAsPercentageOfOnDemandPrice: Optional[float]
    InstanceType: Optional[str]
    WeightedCapacity: Optional[float]
    Configurations: Optional[Sequence["_ConfigurationsDefinition"]]
    EbsConfig: Optional[Sequence["_EbsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypeConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypeConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            BidPriceAsPercentageOfOnDemandPrice=json_data.get("BidPriceAsPercentageOfOnDemandPrice"),
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            Configurations=deserialize_list(json_data.get("Configurations"), ConfigurationsDefinition),
            EbsConfig=deserialize_list(json_data.get("EbsConfig"), EbsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypeConfigsDefinition = InstanceTypeConfigsDefinition


@dataclass
class ConfigurationsDefinition(BaseModel):
    Classification: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsDefinition = ConfigurationsDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class EbsConfigDefinition(BaseModel):
    Iops: Optional[float]
    Size: Optional[float]
    Type: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfigDefinition = EbsConfigDefinition


@dataclass
class LaunchSpecificationsDefinition(BaseModel):
    OnDemandSpecification: Optional[Sequence["_OnDemandSpecificationDefinition"]]
    SpotSpecification: Optional[Sequence["_SpotSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchSpecificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchSpecificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            OnDemandSpecification=deserialize_list(json_data.get("OnDemandSpecification"), OnDemandSpecificationDefinition),
            SpotSpecification=deserialize_list(json_data.get("SpotSpecification"), SpotSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchSpecificationsDefinition = LaunchSpecificationsDefinition


@dataclass
class OnDemandSpecificationDefinition(BaseModel):
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandSpecificationDefinition = OnDemandSpecificationDefinition


@dataclass
class SpotSpecificationDefinition(BaseModel):
    AllocationStrategy: Optional[str]
    BlockDurationMinutes: Optional[float]
    TimeoutAction: Optional[str]
    TimeoutDurationMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SpotSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
            TimeoutAction=json_data.get("TimeoutAction"),
            TimeoutDurationMinutes=json_data.get("TimeoutDurationMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotSpecificationDefinition = SpotSpecificationDefinition


@dataclass
class CoreInstanceGroupDefinition(BaseModel):
    AutoscalingPolicy: Optional[str]
    BidPrice: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreInstanceGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreInstanceGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            EbsConfig=deserialize_list(json_data.get("EbsConfig"), EbsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreInstanceGroupDefinition = CoreInstanceGroupDefinition


@dataclass
class Ec2AttributesDefinition(BaseModel):
    AdditionalMasterSecurityGroups: Optional[str]
    AdditionalSlaveSecurityGroups: Optional[str]
    EmrManagedMasterSecurityGroup: Optional[str]
    EmrManagedSlaveSecurityGroup: Optional[str]
    InstanceProfile: Optional[str]
    KeyName: Optional[str]
    ServiceAccessSecurityGroup: Optional[str]
    SubnetId: Optional[str]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2AttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2AttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalMasterSecurityGroups=json_data.get("AdditionalMasterSecurityGroups"),
            AdditionalSlaveSecurityGroups=json_data.get("AdditionalSlaveSecurityGroups"),
            EmrManagedMasterSecurityGroup=json_data.get("EmrManagedMasterSecurityGroup"),
            EmrManagedSlaveSecurityGroup=json_data.get("EmrManagedSlaveSecurityGroup"),
            InstanceProfile=json_data.get("InstanceProfile"),
            KeyName=json_data.get("KeyName"),
            ServiceAccessSecurityGroup=json_data.get("ServiceAccessSecurityGroup"),
            SubnetId=json_data.get("SubnetId"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2AttributesDefinition = Ec2AttributesDefinition


@dataclass
class KerberosAttributesDefinition(BaseModel):
    AdDomainJoinPassword: Optional[str]
    AdDomainJoinUser: Optional[str]
    CrossRealmTrustPrincipalPassword: Optional[str]
    KdcAdminPassword: Optional[str]
    Realm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdDomainJoinPassword=json_data.get("AdDomainJoinPassword"),
            AdDomainJoinUser=json_data.get("AdDomainJoinUser"),
            CrossRealmTrustPrincipalPassword=json_data.get("CrossRealmTrustPrincipalPassword"),
            KdcAdminPassword=json_data.get("KdcAdminPassword"),
            Realm=json_data.get("Realm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosAttributesDefinition = KerberosAttributesDefinition


@dataclass
class MasterInstanceFleetDefinition(BaseModel):
    Name: Optional[str]
    TargetOnDemandCapacity: Optional[float]
    TargetSpotCapacity: Optional[float]
    InstanceTypeConfigs: Optional[Sequence["_InstanceTypeConfigsDefinition"]]
    LaunchSpecifications: Optional[Sequence["_LaunchSpecificationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterInstanceFleetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterInstanceFleetDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TargetOnDemandCapacity=json_data.get("TargetOnDemandCapacity"),
            TargetSpotCapacity=json_data.get("TargetSpotCapacity"),
            InstanceTypeConfigs=deserialize_list(json_data.get("InstanceTypeConfigs"), InstanceTypeConfigsDefinition),
            LaunchSpecifications=deserialize_list(json_data.get("LaunchSpecifications"), LaunchSpecificationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterInstanceFleetDefinition = MasterInstanceFleetDefinition


@dataclass
class MasterInstanceGroupDefinition(BaseModel):
    BidPrice: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterInstanceGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterInstanceGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            EbsConfig=deserialize_list(json_data.get("EbsConfig"), EbsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterInstanceGroupDefinition = MasterInstanceGroupDefinition


