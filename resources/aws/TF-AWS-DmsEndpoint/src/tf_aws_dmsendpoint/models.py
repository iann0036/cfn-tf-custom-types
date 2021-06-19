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
    CertificateArn: Optional[str]
    DatabaseName: Optional[str]
    EndpointArn: Optional[str]
    EndpointId: Optional[str]
    EndpointType: Optional[str]
    EngineName: Optional[str]
    ExtraConnectionAttributes: Optional[str]
    Id: Optional[str]
    KmsKeyArn: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    ServerName: Optional[str]
    ServiceAccessRole: Optional[str]
    SslMode: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Username: Optional[str]
    ElasticsearchSettings: Optional[Sequence["_ElasticsearchSettingsDefinition"]]
    KafkaSettings: Optional[Sequence["_KafkaSettingsDefinition"]]
    KinesisSettings: Optional[Sequence["_KinesisSettingsDefinition"]]
    MongodbSettings: Optional[Sequence["_MongodbSettingsDefinition"]]
    S3Settings: Optional[Sequence["_S3SettingsDefinition"]]

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
            CertificateArn=json_data.get("CertificateArn"),
            DatabaseName=json_data.get("DatabaseName"),
            EndpointArn=json_data.get("EndpointArn"),
            EndpointId=json_data.get("EndpointId"),
            EndpointType=json_data.get("EndpointType"),
            EngineName=json_data.get("EngineName"),
            ExtraConnectionAttributes=json_data.get("ExtraConnectionAttributes"),
            Id=json_data.get("Id"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            ServerName=json_data.get("ServerName"),
            ServiceAccessRole=json_data.get("ServiceAccessRole"),
            SslMode=json_data.get("SslMode"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Username=json_data.get("Username"),
            ElasticsearchSettings=deserialize_list(json_data.get("ElasticsearchSettings"), ElasticsearchSettingsDefinition),
            KafkaSettings=deserialize_list(json_data.get("KafkaSettings"), KafkaSettingsDefinition),
            KinesisSettings=deserialize_list(json_data.get("KinesisSettings"), KinesisSettingsDefinition),
            MongodbSettings=deserialize_list(json_data.get("MongodbSettings"), MongodbSettingsDefinition),
            S3Settings=deserialize_list(json_data.get("S3Settings"), S3SettingsDefinition),
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
class ElasticsearchSettingsDefinition(BaseModel):
    EndpointUri: Optional[str]
    ErrorRetryDuration: Optional[float]
    FullLoadErrorPercentage: Optional[float]
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointUri=json_data.get("EndpointUri"),
            ErrorRetryDuration=json_data.get("ErrorRetryDuration"),
            FullLoadErrorPercentage=json_data.get("FullLoadErrorPercentage"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchSettingsDefinition = ElasticsearchSettingsDefinition


@dataclass
class KafkaSettingsDefinition(BaseModel):
    Broker: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Broker=json_data.get("Broker"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaSettingsDefinition = KafkaSettingsDefinition


@dataclass
class KinesisSettingsDefinition(BaseModel):
    MessageFormat: Optional[str]
    ServiceAccessRoleArn: Optional[str]
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageFormat=json_data.get("MessageFormat"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisSettingsDefinition = KinesisSettingsDefinition


@dataclass
class MongodbSettingsDefinition(BaseModel):
    AuthMechanism: Optional[str]
    AuthSource: Optional[str]
    AuthType: Optional[str]
    DocsToInvestigate: Optional[str]
    ExtractDocId: Optional[str]
    NestingLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongodbSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongodbSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMechanism=json_data.get("AuthMechanism"),
            AuthSource=json_data.get("AuthSource"),
            AuthType=json_data.get("AuthType"),
            DocsToInvestigate=json_data.get("DocsToInvestigate"),
            ExtractDocId=json_data.get("ExtractDocId"),
            NestingLevel=json_data.get("NestingLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongodbSettingsDefinition = MongodbSettingsDefinition


@dataclass
class S3SettingsDefinition(BaseModel):
    BucketFolder: Optional[str]
    BucketName: Optional[str]
    CompressionType: Optional[str]
    CsvDelimiter: Optional[str]
    CsvRowDelimiter: Optional[str]
    DatePartitionEnabled: Optional[bool]
    ExternalTableDefinition: Optional[str]
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketFolder=json_data.get("BucketFolder"),
            BucketName=json_data.get("BucketName"),
            CompressionType=json_data.get("CompressionType"),
            CsvDelimiter=json_data.get("CsvDelimiter"),
            CsvRowDelimiter=json_data.get("CsvRowDelimiter"),
            DatePartitionEnabled=json_data.get("DatePartitionEnabled"),
            ExternalTableDefinition=json_data.get("ExternalTableDefinition"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3SettingsDefinition = S3SettingsDefinition


