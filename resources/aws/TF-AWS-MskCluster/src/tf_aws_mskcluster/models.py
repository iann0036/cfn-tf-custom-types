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
    Arn: Optional[str]
    BootstrapBrokers: Optional[str]
    BootstrapBrokersSaslIam: Optional[str]
    BootstrapBrokersSaslScram: Optional[str]
    BootstrapBrokersTls: Optional[str]
    ClusterName: Optional[str]
    CurrentVersion: Optional[str]
    EnhancedMonitoring: Optional[str]
    Id: Optional[str]
    KafkaVersion: Optional[str]
    NumberOfBrokerNodes: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ZookeeperConnectString: Optional[str]
    BrokerNodeGroupInfo: Optional[Sequence["_BrokerNodeGroupInfoDefinition"]]
    ClientAuthentication: Optional[Sequence["_ClientAuthenticationDefinition"]]
    ConfigurationInfo: Optional[Sequence["_ConfigurationInfoDefinition"]]
    EncryptionInfo: Optional[Sequence["_EncryptionInfoDefinition"]]
    LoggingInfo: Optional[Sequence["_LoggingInfoDefinition"]]
    OpenMonitoring: Optional[Sequence["_OpenMonitoringDefinition"]]
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
            Arn=json_data.get("Arn"),
            BootstrapBrokers=json_data.get("BootstrapBrokers"),
            BootstrapBrokersSaslIam=json_data.get("BootstrapBrokersSaslIam"),
            BootstrapBrokersSaslScram=json_data.get("BootstrapBrokersSaslScram"),
            BootstrapBrokersTls=json_data.get("BootstrapBrokersTls"),
            ClusterName=json_data.get("ClusterName"),
            CurrentVersion=json_data.get("CurrentVersion"),
            EnhancedMonitoring=json_data.get("EnhancedMonitoring"),
            Id=json_data.get("Id"),
            KafkaVersion=json_data.get("KafkaVersion"),
            NumberOfBrokerNodes=json_data.get("NumberOfBrokerNodes"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ZookeeperConnectString=json_data.get("ZookeeperConnectString"),
            BrokerNodeGroupInfo=deserialize_list(json_data.get("BrokerNodeGroupInfo"), BrokerNodeGroupInfoDefinition),
            ClientAuthentication=deserialize_list(json_data.get("ClientAuthentication"), ClientAuthenticationDefinition),
            ConfigurationInfo=deserialize_list(json_data.get("ConfigurationInfo"), ConfigurationInfoDefinition),
            EncryptionInfo=deserialize_list(json_data.get("EncryptionInfo"), EncryptionInfoDefinition),
            LoggingInfo=deserialize_list(json_data.get("LoggingInfo"), LoggingInfoDefinition),
            OpenMonitoring=deserialize_list(json_data.get("OpenMonitoring"), OpenMonitoringDefinition),
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
class BrokerNodeGroupInfoDefinition(BaseModel):
    AzDistribution: Optional[str]
    ClientSubnets: Optional[Sequence[str]]
    EbsVolumeSize: Optional[float]
    InstanceType: Optional[str]
    SecurityGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerNodeGroupInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerNodeGroupInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AzDistribution=json_data.get("AzDistribution"),
            ClientSubnets=json_data.get("ClientSubnets"),
            EbsVolumeSize=json_data.get("EbsVolumeSize"),
            InstanceType=json_data.get("InstanceType"),
            SecurityGroups=json_data.get("SecurityGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerNodeGroupInfoDefinition = BrokerNodeGroupInfoDefinition


@dataclass
class ClientAuthenticationDefinition(BaseModel):
    Sasl: Optional[Sequence["_SaslDefinition"]]
    Tls: Optional[Sequence["_TlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            Sasl=deserialize_list(json_data.get("Sasl"), SaslDefinition),
            Tls=deserialize_list(json_data.get("Tls"), TlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthenticationDefinition = ClientAuthenticationDefinition


@dataclass
class SaslDefinition(BaseModel):
    Iam: Optional[bool]
    Scram: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SaslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SaslDefinition"]:
        if not json_data:
            return None
        return cls(
            Iam=json_data.get("Iam"),
            Scram=json_data.get("Scram"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SaslDefinition = SaslDefinition


@dataclass
class TlsDefinition(BaseModel):
    CertificateAuthorityArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArns=json_data.get("CertificateAuthorityArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsDefinition = TlsDefinition


@dataclass
class ConfigurationInfoDefinition(BaseModel):
    Arn: Optional[str]
    Revision: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationInfoDefinition = ConfigurationInfoDefinition


@dataclass
class EncryptionInfoDefinition(BaseModel):
    EncryptionAtRestKmsKeyArn: Optional[str]
    EncryptionInTransit: Optional[Sequence["_EncryptionInTransitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionAtRestKmsKeyArn=json_data.get("EncryptionAtRestKmsKeyArn"),
            EncryptionInTransit=deserialize_list(json_data.get("EncryptionInTransit"), EncryptionInTransitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInfoDefinition = EncryptionInfoDefinition


@dataclass
class EncryptionInTransitDefinition(BaseModel):
    ClientBroker: Optional[str]
    InCluster: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInTransitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInTransitDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientBroker=json_data.get("ClientBroker"),
            InCluster=json_data.get("InCluster"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInTransitDefinition = EncryptionInTransitDefinition


@dataclass
class LoggingInfoDefinition(BaseModel):
    BrokerLogs: Optional[Sequence["_BrokerLogsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            BrokerLogs=deserialize_list(json_data.get("BrokerLogs"), BrokerLogsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingInfoDefinition = LoggingInfoDefinition


@dataclass
class BrokerLogsDefinition(BaseModel):
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogsDefinition"]]
    Firehose: Optional[Sequence["_FirehoseDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogs=deserialize_list(json_data.get("CloudwatchLogs"), CloudwatchLogsDefinition),
            Firehose=deserialize_list(json_data.get("Firehose"), FirehoseDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerLogsDefinition = BrokerLogsDefinition


@dataclass
class CloudwatchLogsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLogsDefinition = CloudwatchLogsDefinition


@dataclass
class FirehoseDefinition(BaseModel):
    DeliveryStream: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FirehoseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirehoseDefinition"]:
        if not json_data:
            return None
        return cls(
            DeliveryStream=json_data.get("DeliveryStream"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirehoseDefinition = FirehoseDefinition


@dataclass
class S3Definition(BaseModel):
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


@dataclass
class OpenMonitoringDefinition(BaseModel):
    Prometheus: Optional[Sequence["_PrometheusDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenMonitoringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenMonitoringDefinition"]:
        if not json_data:
            return None
        return cls(
            Prometheus=deserialize_list(json_data.get("Prometheus"), PrometheusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenMonitoringDefinition = OpenMonitoringDefinition


@dataclass
class PrometheusDefinition(BaseModel):
    JmxExporter: Optional[Sequence["_JmxExporterDefinition"]]
    NodeExporter: Optional[Sequence["_NodeExporterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrometheusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrometheusDefinition"]:
        if not json_data:
            return None
        return cls(
            JmxExporter=deserialize_list(json_data.get("JmxExporter"), JmxExporterDefinition),
            NodeExporter=deserialize_list(json_data.get("NodeExporter"), NodeExporterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrometheusDefinition = PrometheusDefinition


@dataclass
class JmxExporterDefinition(BaseModel):
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_JmxExporterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JmxExporterDefinition"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JmxExporterDefinition = JmxExporterDefinition


@dataclass
class NodeExporterDefinition(BaseModel):
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeExporterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeExporterDefinition"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeExporterDefinition = NodeExporterDefinition


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


