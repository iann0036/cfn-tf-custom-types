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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    ClusterId: Optional[str]
    EnableJsonParsing: Optional[bool]
    Id: Optional[str]
    Kind: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    NamespaceId: Optional[str]
    OutputFlushInterval: Optional[float]
    OutputTags: Optional[Sequence["_OutputTagsDefinition"]]
    CustomTargetConfig: Optional[Sequence["_CustomTargetConfigDefinition"]]
    ElasticsearchConfig: Optional[Sequence["_ElasticsearchConfigDefinition"]]
    FluentdConfig: Optional[Sequence["_FluentdConfigDefinition"]]
    KafkaConfig: Optional[Sequence["_KafkaConfigDefinition"]]
    SplunkConfig: Optional[Sequence["_SplunkConfigDefinition"]]
    SyslogConfig: Optional[Sequence["_SyslogConfigDefinition"]]
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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            ClusterId=json_data.get("ClusterId"),
            EnableJsonParsing=json_data.get("EnableJsonParsing"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            OutputFlushInterval=json_data.get("OutputFlushInterval"),
            OutputTags=deserialize_list(json_data.get("OutputTags"), OutputTagsDefinition),
            CustomTargetConfig=deserialize_list(json_data.get("CustomTargetConfig"), CustomTargetConfigDefinition),
            ElasticsearchConfig=deserialize_list(json_data.get("ElasticsearchConfig"), ElasticsearchConfigDefinition),
            FluentdConfig=deserialize_list(json_data.get("FluentdConfig"), FluentdConfigDefinition),
            KafkaConfig=deserialize_list(json_data.get("KafkaConfig"), KafkaConfigDefinition),
            SplunkConfig=deserialize_list(json_data.get("SplunkConfig"), SplunkConfigDefinition),
            SyslogConfig=deserialize_list(json_data.get("SyslogConfig"), SyslogConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class OutputTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputTagsDefinition = OutputTagsDefinition


@dataclass
class CustomTargetConfigDefinition(BaseModel):
    Certificate: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTargetConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTargetConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTargetConfigDefinition = CustomTargetConfigDefinition


@dataclass
class ElasticsearchConfigDefinition(BaseModel):
    AuthPassword: Optional[str]
    AuthUsername: Optional[str]
    Certificate: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClientKeyPass: Optional[str]
    DateFormat: Optional[str]
    Endpoint: Optional[str]
    IndexPrefix: Optional[str]
    SslVerify: Optional[bool]
    SslVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthPassword=json_data.get("AuthPassword"),
            AuthUsername=json_data.get("AuthUsername"),
            Certificate=json_data.get("Certificate"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClientKeyPass=json_data.get("ClientKeyPass"),
            DateFormat=json_data.get("DateFormat"),
            Endpoint=json_data.get("Endpoint"),
            IndexPrefix=json_data.get("IndexPrefix"),
            SslVerify=json_data.get("SslVerify"),
            SslVersion=json_data.get("SslVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfigDefinition = ElasticsearchConfigDefinition


@dataclass
class FluentdConfigDefinition(BaseModel):
    Certificate: Optional[str]
    Compress: Optional[bool]
    EnableTls: Optional[bool]
    FluentServers: Optional[Sequence["_FluentServersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FluentdConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FluentdConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Compress=json_data.get("Compress"),
            EnableTls=json_data.get("EnableTls"),
            FluentServers=deserialize_list(json_data.get("FluentServers"), FluentServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FluentdConfigDefinition = FluentdConfigDefinition


@dataclass
class FluentServersDefinition(BaseModel):
    Endpoint: Optional[str]
    Hostname: Optional[str]
    Password: Optional[str]
    SharedKey: Optional[str]
    Standby: Optional[bool]
    Username: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FluentServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FluentServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Hostname=json_data.get("Hostname"),
            Password=json_data.get("Password"),
            SharedKey=json_data.get("SharedKey"),
            Standby=json_data.get("Standby"),
            Username=json_data.get("Username"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FluentServersDefinition = FluentServersDefinition


@dataclass
class KafkaConfigDefinition(BaseModel):
    BrokerEndpoints: Optional[Sequence[str]]
    Certificate: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    Topic: Optional[str]
    ZookeeperEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BrokerEndpoints=json_data.get("BrokerEndpoints"),
            Certificate=json_data.get("Certificate"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            Topic=json_data.get("Topic"),
            ZookeeperEndpoint=json_data.get("ZookeeperEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaConfigDefinition = KafkaConfigDefinition


@dataclass
class SplunkConfigDefinition(BaseModel):
    Certificate: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClientKeyPass: Optional[str]
    Endpoint: Optional[str]
    Index: Optional[str]
    Source: Optional[str]
    SslVerify: Optional[bool]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClientKeyPass=json_data.get("ClientKeyPass"),
            Endpoint=json_data.get("Endpoint"),
            Index=json_data.get("Index"),
            Source=json_data.get("Source"),
            SslVerify=json_data.get("SslVerify"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkConfigDefinition = SplunkConfigDefinition


@dataclass
class SyslogConfigDefinition(BaseModel):
    Certificate: Optional[str]
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    EnableTls: Optional[bool]
    Endpoint: Optional[str]
    Program: Optional[str]
    Protocol: Optional[str]
    Severity: Optional[str]
    SslVerify: Optional[bool]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SyslogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyslogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            EnableTls=json_data.get("EnableTls"),
            Endpoint=json_data.get("Endpoint"),
            Program=json_data.get("Program"),
            Protocol=json_data.get("Protocol"),
            Severity=json_data.get("Severity"),
            SslVerify=json_data.get("SslVerify"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogConfigDefinition = SyslogConfigDefinition


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


