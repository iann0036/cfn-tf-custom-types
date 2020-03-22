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
    Tags: Optional[Sequence["_Tags"]]
    Username: Optional[str]
    MongodbSettings: Optional[Sequence["_MongodbSettings"]]
    S3Settings: Optional[Sequence["_S3Settings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            Username=json_data.get("Username"),
            MongodbSettings=json_data.get("MongodbSettings"),
            S3Settings=json_data.get("S3Settings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class MongodbSettings:
    AuthMechanism: Optional[str]
    AuthSource: Optional[str]
    AuthType: Optional[str]
    DocsToInvestigate: Optional[str]
    ExtractDocId: Optional[str]
    NestingLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongodbSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongodbSettings"]:
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
_MongodbSettings = MongodbSettings


@dataclass
class S3Settings:
    BucketFolder: Optional[str]
    BucketName: Optional[str]
    CompressionType: Optional[str]
    CsvDelimiter: Optional[str]
    CsvRowDelimiter: Optional[str]
    ExternalTableDefinition: Optional[str]
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Settings"]:
        if not json_data:
            return None
        return cls(
            BucketFolder=json_data.get("BucketFolder"),
            BucketName=json_data.get("BucketName"),
            CompressionType=json_data.get("CompressionType"),
            CsvDelimiter=json_data.get("CsvDelimiter"),
            CsvRowDelimiter=json_data.get("CsvRowDelimiter"),
            ExternalTableDefinition=json_data.get("ExternalTableDefinition"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Settings = S3Settings


