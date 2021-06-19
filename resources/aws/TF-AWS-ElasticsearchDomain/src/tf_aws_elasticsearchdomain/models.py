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
    AccessPolicies: Optional[str]
    AdvancedOptions: Optional[Sequence["_AdvancedOptionsDefinition"]]
    Arn: Optional[str]
    DomainId: Optional[str]
    DomainName: Optional[str]
    ElasticsearchVersion: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    KibanaEndpoint: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    AdvancedSecurityOptions: Optional[Sequence["_AdvancedSecurityOptionsDefinition"]]
    ClusterConfig: Optional[Sequence["_ClusterConfigDefinition"]]
    CognitoOptions: Optional[Sequence["_CognitoOptionsDefinition"]]
    DomainEndpointOptions: Optional[Sequence["_DomainEndpointOptionsDefinition"]]
    EbsOptions: Optional[Sequence["_EbsOptionsDefinition"]]
    EncryptAtRest: Optional[Sequence["_EncryptAtRestDefinition"]]
    LogPublishingOptions: Optional[Sequence["_LogPublishingOptionsDefinition"]]
    NodeToNodeEncryption: Optional[Sequence["_NodeToNodeEncryptionDefinition"]]
    SnapshotOptions: Optional[Sequence["_SnapshotOptionsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VpcOptions: Optional[Sequence["_VpcOptionsDefinition"]]

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
            AccessPolicies=json_data.get("AccessPolicies"),
            AdvancedOptions=deserialize_list(json_data.get("AdvancedOptions"), AdvancedOptionsDefinition),
            Arn=json_data.get("Arn"),
            DomainId=json_data.get("DomainId"),
            DomainName=json_data.get("DomainName"),
            ElasticsearchVersion=json_data.get("ElasticsearchVersion"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            KibanaEndpoint=json_data.get("KibanaEndpoint"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            AdvancedSecurityOptions=deserialize_list(json_data.get("AdvancedSecurityOptions"), AdvancedSecurityOptionsDefinition),
            ClusterConfig=deserialize_list(json_data.get("ClusterConfig"), ClusterConfigDefinition),
            CognitoOptions=deserialize_list(json_data.get("CognitoOptions"), CognitoOptionsDefinition),
            DomainEndpointOptions=deserialize_list(json_data.get("DomainEndpointOptions"), DomainEndpointOptionsDefinition),
            EbsOptions=deserialize_list(json_data.get("EbsOptions"), EbsOptionsDefinition),
            EncryptAtRest=deserialize_list(json_data.get("EncryptAtRest"), EncryptAtRestDefinition),
            LogPublishingOptions=deserialize_list(json_data.get("LogPublishingOptions"), LogPublishingOptionsDefinition),
            NodeToNodeEncryption=deserialize_list(json_data.get("NodeToNodeEncryption"), NodeToNodeEncryptionDefinition),
            SnapshotOptions=deserialize_list(json_data.get("SnapshotOptions"), SnapshotOptionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VpcOptions=deserialize_list(json_data.get("VpcOptions"), VpcOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdvancedOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedOptionsDefinition = AdvancedOptionsDefinition


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
class AdvancedSecurityOptionsDefinition(BaseModel):
    Enabled: Optional[bool]
    InternalUserDatabaseEnabled: Optional[bool]
    MasterUserOptions: Optional[Sequence["_MasterUserOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedSecurityOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedSecurityOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            InternalUserDatabaseEnabled=json_data.get("InternalUserDatabaseEnabled"),
            MasterUserOptions=deserialize_list(json_data.get("MasterUserOptions"), MasterUserOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedSecurityOptionsDefinition = AdvancedSecurityOptionsDefinition


@dataclass
class MasterUserOptionsDefinition(BaseModel):
    MasterUserArn: Optional[str]
    MasterUserName: Optional[str]
    MasterUserPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterUserOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterUserOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MasterUserArn=json_data.get("MasterUserArn"),
            MasterUserName=json_data.get("MasterUserName"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterUserOptionsDefinition = MasterUserOptionsDefinition


@dataclass
class ClusterConfigDefinition(BaseModel):
    DedicatedMasterCount: Optional[float]
    DedicatedMasterEnabled: Optional[bool]
    DedicatedMasterType: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    WarmCount: Optional[float]
    WarmEnabled: Optional[bool]
    WarmType: Optional[str]
    ZoneAwarenessEnabled: Optional[bool]
    ZoneAwarenessConfig: Optional[Sequence["_ZoneAwarenessConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DedicatedMasterCount=json_data.get("DedicatedMasterCount"),
            DedicatedMasterEnabled=json_data.get("DedicatedMasterEnabled"),
            DedicatedMasterType=json_data.get("DedicatedMasterType"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            WarmCount=json_data.get("WarmCount"),
            WarmEnabled=json_data.get("WarmEnabled"),
            WarmType=json_data.get("WarmType"),
            ZoneAwarenessEnabled=json_data.get("ZoneAwarenessEnabled"),
            ZoneAwarenessConfig=deserialize_list(json_data.get("ZoneAwarenessConfig"), ZoneAwarenessConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfigDefinition = ClusterConfigDefinition


@dataclass
class ZoneAwarenessConfigDefinition(BaseModel):
    AvailabilityZoneCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneAwarenessConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneAwarenessConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneCount=json_data.get("AvailabilityZoneCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneAwarenessConfigDefinition = ZoneAwarenessConfigDefinition


@dataclass
class CognitoOptionsDefinition(BaseModel):
    Enabled: Optional[bool]
    IdentityPoolId: Optional[str]
    RoleArn: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            RoleArn=json_data.get("RoleArn"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoOptionsDefinition = CognitoOptionsDefinition


@dataclass
class DomainEndpointOptionsDefinition(BaseModel):
    CustomEndpoint: Optional[str]
    CustomEndpointCertificateArn: Optional[str]
    CustomEndpointEnabled: Optional[bool]
    EnforceHttps: Optional[bool]
    TlsSecurityPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainEndpointOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainEndpointOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomEndpoint=json_data.get("CustomEndpoint"),
            CustomEndpointCertificateArn=json_data.get("CustomEndpointCertificateArn"),
            CustomEndpointEnabled=json_data.get("CustomEndpointEnabled"),
            EnforceHttps=json_data.get("EnforceHttps"),
            TlsSecurityPolicy=json_data.get("TlsSecurityPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainEndpointOptionsDefinition = DomainEndpointOptionsDefinition


@dataclass
class EbsOptionsDefinition(BaseModel):
    EbsEnabled: Optional[bool]
    Iops: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            EbsEnabled=json_data.get("EbsEnabled"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsOptionsDefinition = EbsOptionsDefinition


@dataclass
class EncryptAtRestDefinition(BaseModel):
    Enabled: Optional[bool]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptAtRestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptAtRestDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptAtRestDefinition = EncryptAtRestDefinition


@dataclass
class LogPublishingOptionsDefinition(BaseModel):
    CloudwatchLogGroupArn: Optional[str]
    Enabled: Optional[bool]
    LogType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogPublishingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPublishingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            Enabled=json_data.get("Enabled"),
            LogType=json_data.get("LogType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPublishingOptionsDefinition = LogPublishingOptionsDefinition


@dataclass
class NodeToNodeEncryptionDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeToNodeEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeToNodeEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeToNodeEncryptionDefinition = NodeToNodeEncryptionDefinition


@dataclass
class SnapshotOptionsDefinition(BaseModel):
    AutomatedSnapshotStartHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomatedSnapshotStartHour=json_data.get("AutomatedSnapshotStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotOptionsDefinition = SnapshotOptionsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VpcOptionsDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcOptionsDefinition = VpcOptionsDefinition


