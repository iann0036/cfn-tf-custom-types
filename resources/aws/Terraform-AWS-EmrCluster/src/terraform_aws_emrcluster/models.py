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
    AdditionalInfo: Optional[str]
    Applications: Optional[Sequence[str]]
    Arn: Optional[str]
    AutoscalingRole: Optional[str]
    ClusterState: Optional[str]
    Configurations: Optional[str]
    ConfigurationsJson: Optional[str]
    CoreInstanceCount: Optional[float]
    CoreInstanceType: Optional[str]
    CustomAmiId: Optional[str]
    EbsRootVolumeSize: Optional[float]
    Id: Optional[str]
    KeepJobFlowAliveWhenNoSteps: Optional[bool]
    LogUri: Optional[str]
    MasterInstanceType: Optional[str]
    MasterPublicDns: Optional[str]
    Name: Optional[str]
    ReleaseLabel: Optional[str]
    ScaleDownBehavior: Optional[str]
    SecurityConfiguration: Optional[str]
    ServiceRole: Optional[str]
    Step: Optional[Sequence["_Step"]]
    StepConcurrencyLevel: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    TerminationProtection: Optional[bool]
    VisibleToAllUsers: Optional[bool]
    BootstrapAction: Optional[Sequence["_BootstrapAction"]]
    CoreInstanceGroup: Optional[Sequence["_CoreInstanceGroup"]]
    Ec2Attributes: Optional[Sequence["_Ec2Attributes"]]
    InstanceGroup: Optional[Sequence["_InstanceGroup"]]
    KerberosAttributes: Optional[Sequence["_KerberosAttributes"]]
    MasterInstanceGroup: Optional[Sequence["_MasterInstanceGroup"]]
    EbsConfig: Optional[Sequence["_EbsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalInfo=json_data.get("AdditionalInfo"),
            Applications=json_data.get("Applications"),
            Arn=json_data.get("Arn"),
            AutoscalingRole=json_data.get("AutoscalingRole"),
            ClusterState=json_data.get("ClusterState"),
            Configurations=json_data.get("Configurations"),
            ConfigurationsJson=json_data.get("ConfigurationsJson"),
            CoreInstanceCount=json_data.get("CoreInstanceCount"),
            CoreInstanceType=json_data.get("CoreInstanceType"),
            CustomAmiId=json_data.get("CustomAmiId"),
            EbsRootVolumeSize=json_data.get("EbsRootVolumeSize"),
            Id=json_data.get("Id"),
            KeepJobFlowAliveWhenNoSteps=json_data.get("KeepJobFlowAliveWhenNoSteps"),
            LogUri=json_data.get("LogUri"),
            MasterInstanceType=json_data.get("MasterInstanceType"),
            MasterPublicDns=json_data.get("MasterPublicDns"),
            Name=json_data.get("Name"),
            ReleaseLabel=json_data.get("ReleaseLabel"),
            ScaleDownBehavior=json_data.get("ScaleDownBehavior"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            ServiceRole=json_data.get("ServiceRole"),
            Step=json_data.get("Step"),
            StepConcurrencyLevel=json_data.get("StepConcurrencyLevel"),
            Tags=json_data.get("Tags"),
            TerminationProtection=json_data.get("TerminationProtection"),
            VisibleToAllUsers=json_data.get("VisibleToAllUsers"),
            BootstrapAction=json_data.get("BootstrapAction"),
            CoreInstanceGroup=json_data.get("CoreInstanceGroup"),
            Ec2Attributes=json_data.get("Ec2Attributes"),
            InstanceGroup=json_data.get("InstanceGroup"),
            KerberosAttributes=json_data.get("KerberosAttributes"),
            MasterInstanceGroup=json_data.get("MasterInstanceGroup"),
            EbsConfig=json_data.get("EbsConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Step:
    ActionOnFailure: Optional[str]
    HadoopJarStep: Optional[Sequence["_HadoopJarStep"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Step"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Step"]:
        if not json_data:
            return None
        return cls(
            ActionOnFailure=json_data.get("ActionOnFailure"),
            HadoopJarStep=json_data.get("HadoopJarStep"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Step = Step


@dataclass
class HadoopJarStep:
    Args: Optional[Sequence[str]]
    Jar: Optional[str]
    MainClass: Optional[str]
    Properties: Optional[Sequence["_Properties"]]

    @classmethod
    def _deserialize(
        cls: Type["_HadoopJarStep"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopJarStep"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Jar=json_data.get("Jar"),
            MainClass=json_data.get("MainClass"),
            Properties=json_data.get("Properties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HadoopJarStep = HadoopJarStep


@dataclass
class Properties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class BootstrapAction:
    Args: Optional[Sequence[str]]
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapAction"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapAction = BootstrapAction


@dataclass
class CoreInstanceGroup:
    AutoscalingPolicy: Optional[str]
    BidPrice: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreInstanceGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreInstanceGroup"]:
        if not json_data:
            return None
        return cls(
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            EbsConfig=json_data.get("EbsConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreInstanceGroup = CoreInstanceGroup


@dataclass
class EbsConfig:
    Iops: Optional[float]
    Size: Optional[float]
    Type: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfig"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfig = EbsConfig


@dataclass
class Ec2Attributes:
    AdditionalMasterSecurityGroups: Optional[str]
    AdditionalSlaveSecurityGroups: Optional[str]
    EmrManagedMasterSecurityGroup: Optional[str]
    EmrManagedSlaveSecurityGroup: Optional[str]
    InstanceProfile: Optional[str]
    KeyName: Optional[str]
    ServiceAccessSecurityGroup: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2Attributes"]:
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
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2Attributes = Ec2Attributes


@dataclass
class InstanceGroup:
    AutoscalingPolicy: Optional[str]
    BidPrice: Optional[str]
    InstanceCount: Optional[float]
    InstanceRole: Optional[str]
    InstanceType: Optional[str]
    Name: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceGroup"]:
        if not json_data:
            return None
        return cls(
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            EbsConfig=json_data.get("EbsConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceGroup = InstanceGroup


@dataclass
class KerberosAttributes:
    AdDomainJoinPassword: Optional[str]
    AdDomainJoinUser: Optional[str]
    CrossRealmTrustPrincipalPassword: Optional[str]
    KdcAdminPassword: Optional[str]
    Realm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosAttributes"]:
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
_KerberosAttributes = KerberosAttributes


@dataclass
class MasterInstanceGroup:
    BidPrice: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterInstanceGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterInstanceGroup"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            EbsConfig=json_data.get("EbsConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterInstanceGroup = MasterInstanceGroup


