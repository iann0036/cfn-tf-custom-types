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
    Elasticsearch: Optional[Sequence["_ElasticsearchDefinition"]]
    ElasticsearchUserConfig: Optional[Sequence["_ElasticsearchUserConfigDefinition"]]
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
            Elasticsearch=deserialize_list(json_data.get("Elasticsearch"), ElasticsearchDefinition),
            ElasticsearchUserConfig=deserialize_list(json_data.get("ElasticsearchUserConfig"), ElasticsearchUserConfigDefinition),
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
class ElasticsearchDefinition(BaseModel):
    ActionAutoCreateIndexEnabled: Optional[str]
    ActionDestructiveRequiresName: Optional[str]
    ClusterMaxShardsPerNode: Optional[str]
    HttpMaxContentLength: Optional[str]
    HttpMaxHeaderSize: Optional[str]
    HttpMaxInitialLineLength: Optional[str]
    IndicesFielddataCacheSize: Optional[str]
    IndicesMemoryIndexBufferSize: Optional[str]
    IndicesQueriesCacheSize: Optional[str]
    IndicesQueryBoolMaxClauseCount: Optional[str]
    ReindexRemoteWhitelist: Optional[Sequence[str]]
    SearchMaxBuckets: Optional[str]
    ThreadPoolAnalyzeQueueSize: Optional[str]
    ThreadPoolAnalyzeSize: Optional[str]
    ThreadPoolForceMergeSize: Optional[str]
    ThreadPoolGetQueueSize: Optional[str]
    ThreadPoolGetSize: Optional[str]
    ThreadPoolIndexQueueSize: Optional[str]
    ThreadPoolIndexSize: Optional[str]
    ThreadPoolSearchQueueSize: Optional[str]
    ThreadPoolSearchSize: Optional[str]
    ThreadPoolSearchThrottledQueueSize: Optional[str]
    ThreadPoolSearchThrottledSize: Optional[str]
    ThreadPoolWriteQueueSize: Optional[str]
    ThreadPoolWriteSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionAutoCreateIndexEnabled=json_data.get("ActionAutoCreateIndexEnabled"),
            ActionDestructiveRequiresName=json_data.get("ActionDestructiveRequiresName"),
            ClusterMaxShardsPerNode=json_data.get("ClusterMaxShardsPerNode"),
            HttpMaxContentLength=json_data.get("HttpMaxContentLength"),
            HttpMaxHeaderSize=json_data.get("HttpMaxHeaderSize"),
            HttpMaxInitialLineLength=json_data.get("HttpMaxInitialLineLength"),
            IndicesFielddataCacheSize=json_data.get("IndicesFielddataCacheSize"),
            IndicesMemoryIndexBufferSize=json_data.get("IndicesMemoryIndexBufferSize"),
            IndicesQueriesCacheSize=json_data.get("IndicesQueriesCacheSize"),
            IndicesQueryBoolMaxClauseCount=json_data.get("IndicesQueryBoolMaxClauseCount"),
            ReindexRemoteWhitelist=json_data.get("ReindexRemoteWhitelist"),
            SearchMaxBuckets=json_data.get("SearchMaxBuckets"),
            ThreadPoolAnalyzeQueueSize=json_data.get("ThreadPoolAnalyzeQueueSize"),
            ThreadPoolAnalyzeSize=json_data.get("ThreadPoolAnalyzeSize"),
            ThreadPoolForceMergeSize=json_data.get("ThreadPoolForceMergeSize"),
            ThreadPoolGetQueueSize=json_data.get("ThreadPoolGetQueueSize"),
            ThreadPoolGetSize=json_data.get("ThreadPoolGetSize"),
            ThreadPoolIndexQueueSize=json_data.get("ThreadPoolIndexQueueSize"),
            ThreadPoolIndexSize=json_data.get("ThreadPoolIndexSize"),
            ThreadPoolSearchQueueSize=json_data.get("ThreadPoolSearchQueueSize"),
            ThreadPoolSearchSize=json_data.get("ThreadPoolSearchSize"),
            ThreadPoolSearchThrottledQueueSize=json_data.get("ThreadPoolSearchThrottledQueueSize"),
            ThreadPoolSearchThrottledSize=json_data.get("ThreadPoolSearchThrottledSize"),
            ThreadPoolWriteQueueSize=json_data.get("ThreadPoolWriteQueueSize"),
            ThreadPoolWriteSize=json_data.get("ThreadPoolWriteSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchDefinition = ElasticsearchDefinition


@dataclass
class ElasticsearchUserConfigDefinition(BaseModel):
    CustomDomain: Optional[str]
    DisableReplicationFactorAdjustment: Optional[str]
    ElasticsearchVersion: Optional[str]
    IpFilter: Optional[Sequence[str]]
    MaxIndexCount: Optional[str]
    ProjectToForkFrom: Optional[str]
    RecoveryBasebackupName: Optional[str]
    ServiceToForkFrom: Optional[str]
    Elasticsearch: Optional[Sequence["_ElasticsearchDefinition"]]
    IndexPatterns: Optional[Sequence["_IndexPatternsDefinition"]]
    IndexTemplate: Optional[Sequence["_IndexTemplateDefinition"]]
    Kibana: Optional[Sequence["_KibanaDefinition"]]
    PrivateAccess: Optional[Sequence["_PrivateAccessDefinition"]]
    PrivatelinkAccess: Optional[Sequence["_PrivatelinkAccessDefinition"]]
    PublicAccess: Optional[Sequence["_PublicAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomDomain=json_data.get("CustomDomain"),
            DisableReplicationFactorAdjustment=json_data.get("DisableReplicationFactorAdjustment"),
            ElasticsearchVersion=json_data.get("ElasticsearchVersion"),
            IpFilter=json_data.get("IpFilter"),
            MaxIndexCount=json_data.get("MaxIndexCount"),
            ProjectToForkFrom=json_data.get("ProjectToForkFrom"),
            RecoveryBasebackupName=json_data.get("RecoveryBasebackupName"),
            ServiceToForkFrom=json_data.get("ServiceToForkFrom"),
            Elasticsearch=deserialize_list(json_data.get("Elasticsearch"), ElasticsearchDefinition),
            IndexPatterns=deserialize_list(json_data.get("IndexPatterns"), IndexPatternsDefinition),
            IndexTemplate=deserialize_list(json_data.get("IndexTemplate"), IndexTemplateDefinition),
            Kibana=deserialize_list(json_data.get("Kibana"), KibanaDefinition),
            PrivateAccess=deserialize_list(json_data.get("PrivateAccess"), PrivateAccessDefinition),
            PrivatelinkAccess=deserialize_list(json_data.get("PrivatelinkAccess"), PrivatelinkAccessDefinition),
            PublicAccess=deserialize_list(json_data.get("PublicAccess"), PublicAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchUserConfigDefinition = ElasticsearchUserConfigDefinition


@dataclass
class IndexPatternsDefinition(BaseModel):
    MaxIndexCount: Optional[str]
    Pattern: Optional[str]
    SortingAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexPatternsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexPatternsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxIndexCount=json_data.get("MaxIndexCount"),
            Pattern=json_data.get("Pattern"),
            SortingAlgorithm=json_data.get("SortingAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexPatternsDefinition = IndexPatternsDefinition


@dataclass
class IndexTemplateDefinition(BaseModel):
    MappingNestedObjectsLimit: Optional[str]
    NumberOfReplicas: Optional[str]
    NumberOfShards: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            MappingNestedObjectsLimit=json_data.get("MappingNestedObjectsLimit"),
            NumberOfReplicas=json_data.get("NumberOfReplicas"),
            NumberOfShards=json_data.get("NumberOfShards"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexTemplateDefinition = IndexTemplateDefinition


@dataclass
class KibanaDefinition(BaseModel):
    ElasticsearchRequestTimeout: Optional[str]
    Enabled: Optional[str]
    MaxOldSpaceSize: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KibanaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KibanaDefinition"]:
        if not json_data:
            return None
        return cls(
            ElasticsearchRequestTimeout=json_data.get("ElasticsearchRequestTimeout"),
            Enabled=json_data.get("Enabled"),
            MaxOldSpaceSize=json_data.get("MaxOldSpaceSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KibanaDefinition = KibanaDefinition


@dataclass
class PrivateAccessDefinition(BaseModel):
    Elasticsearch: Optional[str]
    Kibana: Optional[str]
    Prometheus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Elasticsearch=json_data.get("Elasticsearch"),
            Kibana=json_data.get("Kibana"),
            Prometheus=json_data.get("Prometheus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateAccessDefinition = PrivateAccessDefinition


@dataclass
class PrivatelinkAccessDefinition(BaseModel):
    Elasticsearch: Optional[str]
    Kibana: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivatelinkAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivatelinkAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Elasticsearch=json_data.get("Elasticsearch"),
            Kibana=json_data.get("Kibana"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivatelinkAccessDefinition = PrivatelinkAccessDefinition


@dataclass
class PublicAccessDefinition(BaseModel):
    Elasticsearch: Optional[str]
    Kibana: Optional[str]
    Prometheus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Elasticsearch=json_data.get("Elasticsearch"),
            Kibana=json_data.get("Kibana"),
            Prometheus=json_data.get("Prometheus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessDefinition = PublicAccessDefinition


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


