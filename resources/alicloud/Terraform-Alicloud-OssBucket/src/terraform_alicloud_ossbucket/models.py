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
    Acl: Optional[str]
    Bucket: Optional[str]
    CreationDate: Optional[str]
    ExtranetEndpoint: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    IntranetEndpoint: Optional[str]
    Location: Optional[str]
    LoggingIsenable: Optional[bool]
    Owner: Optional[str]
    Policy: Optional[str]
    StorageClass: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CorsRule: Optional[Sequence["_CorsRule"]]
    LifecycleRule: Optional[Sequence["_LifecycleRule"]]
    Logging: Optional[Sequence["_Logging"]]
    RefererConfig: Optional[Sequence["_RefererConfig"]]
    ServerSideEncryptionRule: Optional[Sequence["_ServerSideEncryptionRule"]]
    Versioning: Optional[Sequence["_Versioning"]]
    Website: Optional[Sequence["_Website"]]
    Expiration: Optional[Sequence["_Expiration"]]
    Transitions: Optional[Sequence["_Transitions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            CreationDate=json_data.get("CreationDate"),
            ExtranetEndpoint=json_data.get("ExtranetEndpoint"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            IntranetEndpoint=json_data.get("IntranetEndpoint"),
            Location=json_data.get("Location"),
            LoggingIsenable=json_data.get("LoggingIsenable"),
            Owner=json_data.get("Owner"),
            Policy=json_data.get("Policy"),
            StorageClass=json_data.get("StorageClass"),
            Tags=json_data.get("Tags"),
            CorsRule=json_data.get("CorsRule"),
            LifecycleRule=json_data.get("LifecycleRule"),
            Logging=json_data.get("Logging"),
            RefererConfig=json_data.get("RefererConfig"),
            ServerSideEncryptionRule=json_data.get("ServerSideEncryptionRule"),
            Versioning=json_data.get("Versioning"),
            Website=json_data.get("Website"),
            Expiration=json_data.get("Expiration"),
            Transitions=json_data.get("Transitions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CorsRule:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRule = CorsRule


@dataclass
class LifecycleRule:
    Enabled: Optional[bool]
    Id: Optional[str]
    Prefix: Optional[str]
    Expiration: Optional[Sequence["_Expiration"]]
    Transitions: Optional[Sequence["_Transitions"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRule"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Expiration=json_data.get("Expiration"),
            Transitions=json_data.get("Transitions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRule = LifecycleRule


@dataclass
class Expiration:
    Date: Optional[str]
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Expiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Expiration"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Expiration = Expiration


@dataclass
class Transitions:
    CreatedBeforeDate: Optional[str]
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Transitions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transitions"]:
        if not json_data:
            return None
        return cls(
            CreatedBeforeDate=json_data.get("CreatedBeforeDate"),
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transitions = Transitions


@dataclass
class Logging:
    TargetBucket: Optional[str]
    TargetPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            TargetBucket=json_data.get("TargetBucket"),
            TargetPrefix=json_data.get("TargetPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class RefererConfig:
    AllowEmpty: Optional[bool]
    Referers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RefererConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RefererConfig"]:
        if not json_data:
            return None
        return cls(
            AllowEmpty=json_data.get("AllowEmpty"),
            Referers=json_data.get("Referers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RefererConfig = RefererConfig


@dataclass
class ServerSideEncryptionRule:
    SseAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionRule"]:
        if not json_data:
            return None
        return cls(
            SseAlgorithm=json_data.get("SseAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionRule = ServerSideEncryptionRule


@dataclass
class Versioning:
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Versioning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Versioning"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Versioning = Versioning


@dataclass
class Website:
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Website"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Website"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Website = Website


