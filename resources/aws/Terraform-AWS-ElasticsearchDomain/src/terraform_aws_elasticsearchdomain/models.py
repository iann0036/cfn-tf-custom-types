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
    AccessPolicies: Optional[str]
    AdvancedOptions: Optional[Sequence["_AdvancedOptions"]]
    Arn: Optional[str]
    DomainId: Optional[str]
    DomainName: Optional[str]
    ElasticsearchVersion: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    KibanaEndpoint: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ClusterConfig: Optional[Sequence["_ClusterConfig"]]
    CognitoOptions: Optional[Sequence["_CognitoOptions"]]
    DomainEndpointOptions: Optional[Sequence["_DomainEndpointOptions"]]
    EbsOptions: Optional[Sequence["_EbsOptions"]]
    EncryptAtRest: Optional[Sequence["_EncryptAtRest"]]
    LogPublishingOptions: Optional[Sequence["_LogPublishingOptions"]]
    NodeToNodeEncryption: Optional[Sequence["_NodeToNodeEncryption"]]
    SnapshotOptions: Optional[Sequence["_SnapshotOptions"]]
    VpcOptions: Optional[Sequence["_VpcOptions"]]
    ZoneAwarenessConfig: Optional[Sequence["_ZoneAwarenessConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessPolicies=json_data.get("AccessPolicies"),
            AdvancedOptions=json_data.get("AdvancedOptions"),
            Arn=json_data.get("Arn"),
            DomainId=json_data.get("DomainId"),
            DomainName=json_data.get("DomainName"),
            ElasticsearchVersion=json_data.get("ElasticsearchVersion"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            KibanaEndpoint=json_data.get("KibanaEndpoint"),
            Tags=json_data.get("Tags"),
            ClusterConfig=json_data.get("ClusterConfig"),
            CognitoOptions=json_data.get("CognitoOptions"),
            DomainEndpointOptions=json_data.get("DomainEndpointOptions"),
            EbsOptions=json_data.get("EbsOptions"),
            EncryptAtRest=json_data.get("EncryptAtRest"),
            LogPublishingOptions=json_data.get("LogPublishingOptions"),
            NodeToNodeEncryption=json_data.get("NodeToNodeEncryption"),
            SnapshotOptions=json_data.get("SnapshotOptions"),
            VpcOptions=json_data.get("VpcOptions"),
            ZoneAwarenessConfig=json_data.get("ZoneAwarenessConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdvancedOptions:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedOptions"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedOptions = AdvancedOptions


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
class ClusterConfig:
    DedicatedMasterCount: Optional[float]
    DedicatedMasterEnabled: Optional[bool]
    DedicatedMasterType: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    ZoneAwarenessEnabled: Optional[bool]
    ZoneAwarenessConfig: Optional[Sequence["_ZoneAwarenessConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfig"]:
        if not json_data:
            return None
        return cls(
            DedicatedMasterCount=json_data.get("DedicatedMasterCount"),
            DedicatedMasterEnabled=json_data.get("DedicatedMasterEnabled"),
            DedicatedMasterType=json_data.get("DedicatedMasterType"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            ZoneAwarenessEnabled=json_data.get("ZoneAwarenessEnabled"),
            ZoneAwarenessConfig=json_data.get("ZoneAwarenessConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfig = ClusterConfig


@dataclass
class ZoneAwarenessConfig:
    AvailabilityZoneCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneAwarenessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneAwarenessConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneCount=json_data.get("AvailabilityZoneCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneAwarenessConfig = ZoneAwarenessConfig


@dataclass
class CognitoOptions:
    Enabled: Optional[bool]
    IdentityPoolId: Optional[str]
    RoleArn: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            RoleArn=json_data.get("RoleArn"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoOptions = CognitoOptions


@dataclass
class DomainEndpointOptions:
    EnforceHttps: Optional[bool]
    TlsSecurityPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainEndpointOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainEndpointOptions"]:
        if not json_data:
            return None
        return cls(
            EnforceHttps=json_data.get("EnforceHttps"),
            TlsSecurityPolicy=json_data.get("TlsSecurityPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainEndpointOptions = DomainEndpointOptions


@dataclass
class EbsOptions:
    EbsEnabled: Optional[bool]
    Iops: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsOptions"]:
        if not json_data:
            return None
        return cls(
            EbsEnabled=json_data.get("EbsEnabled"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsOptions = EbsOptions


@dataclass
class EncryptAtRest:
    Enabled: Optional[bool]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptAtRest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptAtRest"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptAtRest = EncryptAtRest


@dataclass
class LogPublishingOptions:
    CloudwatchLogGroupArn: Optional[str]
    Enabled: Optional[bool]
    LogType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogPublishingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPublishingOptions"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            Enabled=json_data.get("Enabled"),
            LogType=json_data.get("LogType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPublishingOptions = LogPublishingOptions


@dataclass
class NodeToNodeEncryption:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeToNodeEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeToNodeEncryption"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeToNodeEncryption = NodeToNodeEncryption


@dataclass
class SnapshotOptions:
    AutomatedSnapshotStartHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotOptions"]:
        if not json_data:
            return None
        return cls(
            AutomatedSnapshotStartHour=json_data.get("AutomatedSnapshotStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotOptions = SnapshotOptions


@dataclass
class VpcOptions:
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcOptions"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcOptions = VpcOptions


