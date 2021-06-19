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
    EndpointConfig: Optional[Sequence["_EndpointConfigDefinition"]]
    EndpointName: Optional[str]
    EndpointType: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    DatadogUserConfig: Optional[Sequence["_DatadogUserConfigDefinition"]]
    ExternalAwsCloudwatchLogsUserConfig: Optional[Sequence["_ExternalAwsCloudwatchLogsUserConfigDefinition"]]
    ExternalAwsCloudwatchMetricsUserConfig: Optional[Sequence["_ExternalAwsCloudwatchMetricsUserConfigDefinition"]]
    ExternalElasticsearchLogsUserConfig: Optional[Sequence["_ExternalElasticsearchLogsUserConfigDefinition"]]
    ExternalGoogleCloudLoggingUserConfig: Optional[Sequence["_ExternalGoogleCloudLoggingUserConfigDefinition"]]
    ExternalKafkaUserConfig: Optional[Sequence["_ExternalKafkaUserConfigDefinition"]]
    ExternalSchemaRegistryUserConfig: Optional[Sequence["_ExternalSchemaRegistryUserConfigDefinition"]]
    JolokiaUserConfig: Optional[Sequence["_JolokiaUserConfigDefinition"]]
    PrometheusUserConfig: Optional[Sequence["_PrometheusUserConfigDefinition"]]
    RsyslogUserConfig: Optional[Sequence["_RsyslogUserConfigDefinition"]]
    SignalfxUserConfig: Optional[Sequence["_SignalfxUserConfigDefinition"]]

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
            EndpointConfig=deserialize_list(json_data.get("EndpointConfig"), EndpointConfigDefinition),
            EndpointName=json_data.get("EndpointName"),
            EndpointType=json_data.get("EndpointType"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            DatadogUserConfig=deserialize_list(json_data.get("DatadogUserConfig"), DatadogUserConfigDefinition),
            ExternalAwsCloudwatchLogsUserConfig=deserialize_list(json_data.get("ExternalAwsCloudwatchLogsUserConfig"), ExternalAwsCloudwatchLogsUserConfigDefinition),
            ExternalAwsCloudwatchMetricsUserConfig=deserialize_list(json_data.get("ExternalAwsCloudwatchMetricsUserConfig"), ExternalAwsCloudwatchMetricsUserConfigDefinition),
            ExternalElasticsearchLogsUserConfig=deserialize_list(json_data.get("ExternalElasticsearchLogsUserConfig"), ExternalElasticsearchLogsUserConfigDefinition),
            ExternalGoogleCloudLoggingUserConfig=deserialize_list(json_data.get("ExternalGoogleCloudLoggingUserConfig"), ExternalGoogleCloudLoggingUserConfigDefinition),
            ExternalKafkaUserConfig=deserialize_list(json_data.get("ExternalKafkaUserConfig"), ExternalKafkaUserConfigDefinition),
            ExternalSchemaRegistryUserConfig=deserialize_list(json_data.get("ExternalSchemaRegistryUserConfig"), ExternalSchemaRegistryUserConfigDefinition),
            JolokiaUserConfig=deserialize_list(json_data.get("JolokiaUserConfig"), JolokiaUserConfigDefinition),
            PrometheusUserConfig=deserialize_list(json_data.get("PrometheusUserConfig"), PrometheusUserConfigDefinition),
            RsyslogUserConfig=deserialize_list(json_data.get("RsyslogUserConfig"), RsyslogUserConfigDefinition),
            SignalfxUserConfig=deserialize_list(json_data.get("SignalfxUserConfig"), SignalfxUserConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigDefinition = EndpointConfigDefinition


@dataclass
class DatadogUserConfigDefinition(BaseModel):
    DatadogApiKey: Optional[str]
    DisableConsumerStats: Optional[str]
    MaxPartitionContexts: Optional[str]
    Site: Optional[str]
    DatadogTags: Optional[Sequence["_DatadogTagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DatadogApiKey=json_data.get("DatadogApiKey"),
            DisableConsumerStats=json_data.get("DisableConsumerStats"),
            MaxPartitionContexts=json_data.get("MaxPartitionContexts"),
            Site=json_data.get("Site"),
            DatadogTags=deserialize_list(json_data.get("DatadogTags"), DatadogTagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogUserConfigDefinition = DatadogUserConfigDefinition


@dataclass
class DatadogTagsDefinition(BaseModel):
    Comment: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogTagsDefinition = DatadogTagsDefinition


@dataclass
class ExternalAwsCloudwatchLogsUserConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    LogGroupName: Optional[str]
    Region: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalAwsCloudwatchLogsUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalAwsCloudwatchLogsUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            LogGroupName=json_data.get("LogGroupName"),
            Region=json_data.get("Region"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalAwsCloudwatchLogsUserConfigDefinition = ExternalAwsCloudwatchLogsUserConfigDefinition


@dataclass
class ExternalAwsCloudwatchMetricsUserConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    Namespace: Optional[str]
    Region: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalAwsCloudwatchMetricsUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalAwsCloudwatchMetricsUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            Namespace=json_data.get("Namespace"),
            Region=json_data.get("Region"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalAwsCloudwatchMetricsUserConfigDefinition = ExternalAwsCloudwatchMetricsUserConfigDefinition


@dataclass
class ExternalElasticsearchLogsUserConfigDefinition(BaseModel):
    Ca: Optional[str]
    IndexDaysMax: Optional[str]
    IndexPrefix: Optional[str]
    Timeout: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalElasticsearchLogsUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalElasticsearchLogsUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ca=json_data.get("Ca"),
            IndexDaysMax=json_data.get("IndexDaysMax"),
            IndexPrefix=json_data.get("IndexPrefix"),
            Timeout=json_data.get("Timeout"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalElasticsearchLogsUserConfigDefinition = ExternalElasticsearchLogsUserConfigDefinition


@dataclass
class ExternalGoogleCloudLoggingUserConfigDefinition(BaseModel):
    LogId: Optional[str]
    ProjectId: Optional[str]
    ServiceAccountCredentials: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalGoogleCloudLoggingUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalGoogleCloudLoggingUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LogId=json_data.get("LogId"),
            ProjectId=json_data.get("ProjectId"),
            ServiceAccountCredentials=json_data.get("ServiceAccountCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalGoogleCloudLoggingUserConfigDefinition = ExternalGoogleCloudLoggingUserConfigDefinition


@dataclass
class ExternalKafkaUserConfigDefinition(BaseModel):
    BootstrapServers: Optional[str]
    SaslMechanism: Optional[str]
    SaslPlainPassword: Optional[str]
    SaslPlainUsername: Optional[str]
    SecurityProtocol: Optional[str]
    SslCaCert: Optional[str]
    SslClientCert: Optional[str]
    SslClientKey: Optional[str]
    SslEndpointIdentificationAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalKafkaUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalKafkaUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BootstrapServers=json_data.get("BootstrapServers"),
            SaslMechanism=json_data.get("SaslMechanism"),
            SaslPlainPassword=json_data.get("SaslPlainPassword"),
            SaslPlainUsername=json_data.get("SaslPlainUsername"),
            SecurityProtocol=json_data.get("SecurityProtocol"),
            SslCaCert=json_data.get("SslCaCert"),
            SslClientCert=json_data.get("SslClientCert"),
            SslClientKey=json_data.get("SslClientKey"),
            SslEndpointIdentificationAlgorithm=json_data.get("SslEndpointIdentificationAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalKafkaUserConfigDefinition = ExternalKafkaUserConfigDefinition


@dataclass
class ExternalSchemaRegistryUserConfigDefinition(BaseModel):
    Authentication: Optional[str]
    BasicAuthPassword: Optional[str]
    BasicAuthUsername: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalSchemaRegistryUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalSchemaRegistryUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            BasicAuthUsername=json_data.get("BasicAuthUsername"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalSchemaRegistryUserConfigDefinition = ExternalSchemaRegistryUserConfigDefinition


@dataclass
class JolokiaUserConfigDefinition(BaseModel):
    BasicAuthPassword: Optional[str]
    BasicAuthUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JolokiaUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JolokiaUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            BasicAuthUsername=json_data.get("BasicAuthUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JolokiaUserConfigDefinition = JolokiaUserConfigDefinition


@dataclass
class PrometheusUserConfigDefinition(BaseModel):
    BasicAuthPassword: Optional[str]
    BasicAuthUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrometheusUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrometheusUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            BasicAuthUsername=json_data.get("BasicAuthUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrometheusUserConfigDefinition = PrometheusUserConfigDefinition


@dataclass
class RsyslogUserConfigDefinition(BaseModel):
    Ca: Optional[str]
    Cert: Optional[str]
    Format: Optional[str]
    Key: Optional[str]
    Logline: Optional[str]
    Port: Optional[str]
    Sd: Optional[str]
    Server: Optional[str]
    Tls: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RsyslogUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RsyslogUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Ca=json_data.get("Ca"),
            Cert=json_data.get("Cert"),
            Format=json_data.get("Format"),
            Key=json_data.get("Key"),
            Logline=json_data.get("Logline"),
            Port=json_data.get("Port"),
            Sd=json_data.get("Sd"),
            Server=json_data.get("Server"),
            Tls=json_data.get("Tls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RsyslogUserConfigDefinition = RsyslogUserConfigDefinition


@dataclass
class SignalfxUserConfigDefinition(BaseModel):
    EnabledMetrics: Optional[Sequence[str]]
    SignalfxApiKey: Optional[str]
    SignalfxRealm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SignalfxUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignalfxUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnabledMetrics=json_data.get("EnabledMetrics"),
            SignalfxApiKey=json_data.get("SignalfxApiKey"),
            SignalfxRealm=json_data.get("SignalfxRealm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignalfxUserConfigDefinition = SignalfxUserConfigDefinition


