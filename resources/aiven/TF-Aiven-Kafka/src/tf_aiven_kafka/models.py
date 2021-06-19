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
    CloudName: Optional[str]
    Components: Optional[Sequence["_ComponentsDefinition"]]
    DefaultAcl: Optional[bool]
    Id: Optional[str]
    MaintenanceWindowDow: Optional[str]
    MaintenanceWindowTime: Optional[str]
    Plan: Optional[str]
    Project: Optional[str]
    ProjectVpcId: Optional[str]
    ServiceHost: Optional[str]
    ServiceName: Optional[str]
    ServicePassword: Optional[str]
    ServicePort: Optional[float]
    ServiceType: Optional[str]
    ServiceUri: Optional[str]
    ServiceUsername: Optional[str]
    State: Optional[str]
    TerminationProtection: Optional[bool]
    Kafka: Optional[Sequence["_KafkaDefinition"]]
    KafkaUserConfig: Optional[Sequence["_KafkaUserConfigDefinition"]]
    ServiceIntegrations: Optional[Sequence["_ServiceIntegrationsDefinition"]]
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
            CloudName=json_data.get("CloudName"),
            Components=deserialize_list(json_data.get("Components"), ComponentsDefinition),
            DefaultAcl=json_data.get("DefaultAcl"),
            Id=json_data.get("Id"),
            MaintenanceWindowDow=json_data.get("MaintenanceWindowDow"),
            MaintenanceWindowTime=json_data.get("MaintenanceWindowTime"),
            Plan=json_data.get("Plan"),
            Project=json_data.get("Project"),
            ProjectVpcId=json_data.get("ProjectVpcId"),
            ServiceHost=json_data.get("ServiceHost"),
            ServiceName=json_data.get("ServiceName"),
            ServicePassword=json_data.get("ServicePassword"),
            ServicePort=json_data.get("ServicePort"),
            ServiceType=json_data.get("ServiceType"),
            ServiceUri=json_data.get("ServiceUri"),
            ServiceUsername=json_data.get("ServiceUsername"),
            State=json_data.get("State"),
            TerminationProtection=json_data.get("TerminationProtection"),
            Kafka=deserialize_list(json_data.get("Kafka"), KafkaDefinition),
            KafkaUserConfig=deserialize_list(json_data.get("KafkaUserConfig"), KafkaUserConfigDefinition),
            ServiceIntegrations=deserialize_list(json_data.get("ServiceIntegrations"), ServiceIntegrationsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComponentsDefinition(BaseModel):
    Component: Optional[str]
    Host: Optional[str]
    KafkaAuthenticationMethod: Optional[str]
    Port: Optional[float]
    Route: Optional[str]
    Ssl: Optional[bool]
    Usage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Component=json_data.get("Component"),
            Host=json_data.get("Host"),
            KafkaAuthenticationMethod=json_data.get("KafkaAuthenticationMethod"),
            Port=json_data.get("Port"),
            Route=json_data.get("Route"),
            Ssl=json_data.get("Ssl"),
            Usage=json_data.get("Usage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentsDefinition = ComponentsDefinition


@dataclass
class KafkaDefinition(BaseModel):
    AutoCreateTopicsEnable: Optional[str]
    CompressionType: Optional[str]
    ConnectionsMaxIdleMs: Optional[str]
    DefaultReplicationFactor: Optional[str]
    GroupInitialRebalanceDelayMs: Optional[str]
    GroupMaxSessionTimeoutMs: Optional[str]
    GroupMinSessionTimeoutMs: Optional[str]
    LogCleanerDeleteRetentionMs: Optional[str]
    LogCleanerMaxCompactionLagMs: Optional[str]
    LogCleanerMinCleanableRatio: Optional[str]
    LogCleanerMinCompactionLagMs: Optional[str]
    LogCleanupPolicy: Optional[str]
    LogFlushIntervalMessages: Optional[str]
    LogFlushIntervalMs: Optional[str]
    LogIndexIntervalBytes: Optional[str]
    LogIndexSizeMaxBytes: Optional[str]
    LogMessageDownconversionEnable: Optional[str]
    LogMessageTimestampDifferenceMaxMs: Optional[str]
    LogMessageTimestampType: Optional[str]
    LogPreallocate: Optional[str]
    LogRetentionBytes: Optional[str]
    LogRetentionHours: Optional[str]
    LogRetentionMs: Optional[str]
    LogRollJitterMs: Optional[str]
    LogRollMs: Optional[str]
    LogSegmentBytes: Optional[str]
    LogSegmentDeleteDelayMs: Optional[str]
    MaxConnectionsPerIp: Optional[str]
    MaxIncrementalFetchSessionCacheSlots: Optional[str]
    MessageMaxBytes: Optional[str]
    MinInsyncReplicas: Optional[str]
    NumPartitions: Optional[str]
    OffsetsRetentionMinutes: Optional[str]
    ProducerPurgatoryPurgeIntervalRequests: Optional[str]
    ReplicaFetchMaxBytes: Optional[str]
    ReplicaFetchResponseMaxBytes: Optional[str]
    SocketRequestMaxBytes: Optional[str]
    TransactionRemoveExpiredTransactionCleanupIntervalMs: Optional[str]
    TransactionStateLogSegmentBytes: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoCreateTopicsEnable=json_data.get("AutoCreateTopicsEnable"),
            CompressionType=json_data.get("CompressionType"),
            ConnectionsMaxIdleMs=json_data.get("ConnectionsMaxIdleMs"),
            DefaultReplicationFactor=json_data.get("DefaultReplicationFactor"),
            GroupInitialRebalanceDelayMs=json_data.get("GroupInitialRebalanceDelayMs"),
            GroupMaxSessionTimeoutMs=json_data.get("GroupMaxSessionTimeoutMs"),
            GroupMinSessionTimeoutMs=json_data.get("GroupMinSessionTimeoutMs"),
            LogCleanerDeleteRetentionMs=json_data.get("LogCleanerDeleteRetentionMs"),
            LogCleanerMaxCompactionLagMs=json_data.get("LogCleanerMaxCompactionLagMs"),
            LogCleanerMinCleanableRatio=json_data.get("LogCleanerMinCleanableRatio"),
            LogCleanerMinCompactionLagMs=json_data.get("LogCleanerMinCompactionLagMs"),
            LogCleanupPolicy=json_data.get("LogCleanupPolicy"),
            LogFlushIntervalMessages=json_data.get("LogFlushIntervalMessages"),
            LogFlushIntervalMs=json_data.get("LogFlushIntervalMs"),
            LogIndexIntervalBytes=json_data.get("LogIndexIntervalBytes"),
            LogIndexSizeMaxBytes=json_data.get("LogIndexSizeMaxBytes"),
            LogMessageDownconversionEnable=json_data.get("LogMessageDownconversionEnable"),
            LogMessageTimestampDifferenceMaxMs=json_data.get("LogMessageTimestampDifferenceMaxMs"),
            LogMessageTimestampType=json_data.get("LogMessageTimestampType"),
            LogPreallocate=json_data.get("LogPreallocate"),
            LogRetentionBytes=json_data.get("LogRetentionBytes"),
            LogRetentionHours=json_data.get("LogRetentionHours"),
            LogRetentionMs=json_data.get("LogRetentionMs"),
            LogRollJitterMs=json_data.get("LogRollJitterMs"),
            LogRollMs=json_data.get("LogRollMs"),
            LogSegmentBytes=json_data.get("LogSegmentBytes"),
            LogSegmentDeleteDelayMs=json_data.get("LogSegmentDeleteDelayMs"),
            MaxConnectionsPerIp=json_data.get("MaxConnectionsPerIp"),
            MaxIncrementalFetchSessionCacheSlots=json_data.get("MaxIncrementalFetchSessionCacheSlots"),
            MessageMaxBytes=json_data.get("MessageMaxBytes"),
            MinInsyncReplicas=json_data.get("MinInsyncReplicas"),
            NumPartitions=json_data.get("NumPartitions"),
            OffsetsRetentionMinutes=json_data.get("OffsetsRetentionMinutes"),
            ProducerPurgatoryPurgeIntervalRequests=json_data.get("ProducerPurgatoryPurgeIntervalRequests"),
            ReplicaFetchMaxBytes=json_data.get("ReplicaFetchMaxBytes"),
            ReplicaFetchResponseMaxBytes=json_data.get("ReplicaFetchResponseMaxBytes"),
            SocketRequestMaxBytes=json_data.get("SocketRequestMaxBytes"),
            TransactionRemoveExpiredTransactionCleanupIntervalMs=json_data.get("TransactionRemoveExpiredTransactionCleanupIntervalMs"),
            TransactionStateLogSegmentBytes=json_data.get("TransactionStateLogSegmentBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaDefinition = KafkaDefinition


@dataclass
class KafkaUserConfigDefinition(BaseModel):
    CustomDomain: Optional[str]
    IpFilter: Optional[Sequence[str]]
    KafkaConnect: Optional[str]
    KafkaRest: Optional[str]
    KafkaVersion: Optional[str]
    SchemaRegistry: Optional[str]
    Kafka: Optional[Sequence["_KafkaDefinition"]]
    KafkaAuthenticationMethods: Optional[Sequence["_KafkaAuthenticationMethodsDefinition"]]
    KafkaConnectConfig: Optional[Sequence["_KafkaConnectConfigDefinition"]]
    KafkaRestConfig: Optional[Sequence["_KafkaRestConfigDefinition"]]
    PrivateAccess: Optional[Sequence["_PrivateAccessDefinition"]]
    PrivatelinkAccess: Optional[Sequence["_PrivatelinkAccessDefinition"]]
    PublicAccess: Optional[Sequence["_PublicAccessDefinition"]]
    SchemaRegistryConfig: Optional[Sequence["_SchemaRegistryConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomDomain=json_data.get("CustomDomain"),
            IpFilter=json_data.get("IpFilter"),
            KafkaConnect=json_data.get("KafkaConnect"),
            KafkaRest=json_data.get("KafkaRest"),
            KafkaVersion=json_data.get("KafkaVersion"),
            SchemaRegistry=json_data.get("SchemaRegistry"),
            Kafka=deserialize_list(json_data.get("Kafka"), KafkaDefinition),
            KafkaAuthenticationMethods=deserialize_list(json_data.get("KafkaAuthenticationMethods"), KafkaAuthenticationMethodsDefinition),
            KafkaConnectConfig=deserialize_list(json_data.get("KafkaConnectConfig"), KafkaConnectConfigDefinition),
            KafkaRestConfig=deserialize_list(json_data.get("KafkaRestConfig"), KafkaRestConfigDefinition),
            PrivateAccess=deserialize_list(json_data.get("PrivateAccess"), PrivateAccessDefinition),
            PrivatelinkAccess=deserialize_list(json_data.get("PrivatelinkAccess"), PrivatelinkAccessDefinition),
            PublicAccess=deserialize_list(json_data.get("PublicAccess"), PublicAccessDefinition),
            SchemaRegistryConfig=deserialize_list(json_data.get("SchemaRegistryConfig"), SchemaRegistryConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaUserConfigDefinition = KafkaUserConfigDefinition


@dataclass
class KafkaAuthenticationMethodsDefinition(BaseModel):
    Certificate: Optional[str]
    Sasl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaAuthenticationMethodsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaAuthenticationMethodsDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Sasl=json_data.get("Sasl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaAuthenticationMethodsDefinition = KafkaAuthenticationMethodsDefinition


@dataclass
class KafkaConnectConfigDefinition(BaseModel):
    ConnectorClientConfigOverridePolicy: Optional[str]
    ConsumerAutoOffsetReset: Optional[str]
    ConsumerFetchMaxBytes: Optional[str]
    ConsumerIsolationLevel: Optional[str]
    ConsumerMaxPartitionFetchBytes: Optional[str]
    ConsumerMaxPollIntervalMs: Optional[str]
    ConsumerMaxPollRecords: Optional[str]
    OffsetFlushIntervalMs: Optional[str]
    OffsetFlushTimeoutMs: Optional[str]
    ProducerMaxRequestSize: Optional[str]
    SessionTimeoutMs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaConnectConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaConnectConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectorClientConfigOverridePolicy=json_data.get("ConnectorClientConfigOverridePolicy"),
            ConsumerAutoOffsetReset=json_data.get("ConsumerAutoOffsetReset"),
            ConsumerFetchMaxBytes=json_data.get("ConsumerFetchMaxBytes"),
            ConsumerIsolationLevel=json_data.get("ConsumerIsolationLevel"),
            ConsumerMaxPartitionFetchBytes=json_data.get("ConsumerMaxPartitionFetchBytes"),
            ConsumerMaxPollIntervalMs=json_data.get("ConsumerMaxPollIntervalMs"),
            ConsumerMaxPollRecords=json_data.get("ConsumerMaxPollRecords"),
            OffsetFlushIntervalMs=json_data.get("OffsetFlushIntervalMs"),
            OffsetFlushTimeoutMs=json_data.get("OffsetFlushTimeoutMs"),
            ProducerMaxRequestSize=json_data.get("ProducerMaxRequestSize"),
            SessionTimeoutMs=json_data.get("SessionTimeoutMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaConnectConfigDefinition = KafkaConnectConfigDefinition


@dataclass
class KafkaRestConfigDefinition(BaseModel):
    ConsumerEnableAutoCommit: Optional[str]
    ConsumerRequestMaxBytes: Optional[str]
    ConsumerRequestTimeoutMs: Optional[str]
    ProducerAcks: Optional[str]
    ProducerLingerMs: Optional[str]
    SimpleconsumerPoolSizeMax: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaRestConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaRestConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsumerEnableAutoCommit=json_data.get("ConsumerEnableAutoCommit"),
            ConsumerRequestMaxBytes=json_data.get("ConsumerRequestMaxBytes"),
            ConsumerRequestTimeoutMs=json_data.get("ConsumerRequestTimeoutMs"),
            ProducerAcks=json_data.get("ProducerAcks"),
            ProducerLingerMs=json_data.get("ProducerLingerMs"),
            SimpleconsumerPoolSizeMax=json_data.get("SimpleconsumerPoolSizeMax"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaRestConfigDefinition = KafkaRestConfigDefinition


@dataclass
class PrivateAccessDefinition(BaseModel):
    Prometheus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Prometheus=json_data.get("Prometheus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateAccessDefinition = PrivateAccessDefinition


@dataclass
class PrivatelinkAccessDefinition(BaseModel):
    Kafka: Optional[str]
    KafkaConnect: Optional[str]
    KafkaRest: Optional[str]
    SchemaRegistry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivatelinkAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivatelinkAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Kafka=json_data.get("Kafka"),
            KafkaConnect=json_data.get("KafkaConnect"),
            KafkaRest=json_data.get("KafkaRest"),
            SchemaRegistry=json_data.get("SchemaRegistry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivatelinkAccessDefinition = PrivatelinkAccessDefinition


@dataclass
class PublicAccessDefinition(BaseModel):
    Kafka: Optional[str]
    KafkaConnect: Optional[str]
    KafkaRest: Optional[str]
    Prometheus: Optional[str]
    SchemaRegistry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Kafka=json_data.get("Kafka"),
            KafkaConnect=json_data.get("KafkaConnect"),
            KafkaRest=json_data.get("KafkaRest"),
            Prometheus=json_data.get("Prometheus"),
            SchemaRegistry=json_data.get("SchemaRegistry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessDefinition = PublicAccessDefinition


@dataclass
class SchemaRegistryConfigDefinition(BaseModel):
    LeaderEligibility: Optional[str]
    TopicName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaRegistryConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaRegistryConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LeaderEligibility=json_data.get("LeaderEligibility"),
            TopicName=json_data.get("TopicName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaRegistryConfigDefinition = SchemaRegistryConfigDefinition


@dataclass
class ServiceIntegrationsDefinition(BaseModel):
    IntegrationType: Optional[str]
    SourceServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIntegrationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIntegrationsDefinition"]:
        if not json_data:
            return None
        return cls(
            IntegrationType=json_data.get("IntegrationType"),
            SourceServiceName=json_data.get("SourceServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIntegrationsDefinition = ServiceIntegrationsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


