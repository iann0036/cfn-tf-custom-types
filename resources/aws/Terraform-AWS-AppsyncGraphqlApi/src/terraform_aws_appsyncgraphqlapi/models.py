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
    Arn: Optional[str]
    AuthenticationType: Optional[str]
    Name: Optional[str]
    Schema: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Uris: Optional[Sequence["_Uris"]]
    XrayEnabled: Optional[bool]
    AdditionalAuthenticationProvider: Optional[Sequence["_AdditionalAuthenticationProvider"]]
    LogConfig: Optional[Sequence["_LogConfig"]]
    OpenidConnectConfig: Optional[Sequence["_OpenidConnectConfig"]]
    UserPoolConfig: Optional[Sequence["_UserPoolConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AuthenticationType=json_data.get("AuthenticationType"),
            Name=json_data.get("Name"),
            Schema=json_data.get("Schema"),
            Tags=json_data.get("Tags"),
            Uris=json_data.get("Uris"),
            XrayEnabled=json_data.get("XrayEnabled"),
            AdditionalAuthenticationProvider=json_data.get("AdditionalAuthenticationProvider"),
            LogConfig=json_data.get("LogConfig"),
            OpenidConnectConfig=json_data.get("OpenidConnectConfig"),
            UserPoolConfig=json_data.get("UserPoolConfig"),
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
class Uris:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Uris"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Uris"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Uris = Uris


@dataclass
class AdditionalAuthenticationProvider:
    AuthenticationType: Optional[str]
    OpenidConnectConfig: Optional[Sequence["_OpenidConnectConfig"]]
    UserPoolConfig: Optional[Sequence["_UserPoolConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalAuthenticationProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalAuthenticationProvider"]:
        if not json_data:
            return None
        return cls(
            AuthenticationType=json_data.get("AuthenticationType"),
            OpenidConnectConfig=json_data.get("OpenidConnectConfig"),
            UserPoolConfig=json_data.get("UserPoolConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalAuthenticationProvider = AdditionalAuthenticationProvider


@dataclass
class OpenidConnectConfig:
    AuthTtl: Optional[float]
    ClientId: Optional[str]
    IatTtl: Optional[float]
    Issuer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenidConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenidConnectConfig"]:
        if not json_data:
            return None
        return cls(
            AuthTtl=json_data.get("AuthTtl"),
            ClientId=json_data.get("ClientId"),
            IatTtl=json_data.get("IatTtl"),
            Issuer=json_data.get("Issuer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenidConnectConfig = OpenidConnectConfig


@dataclass
class UserPoolConfig:
    AppIdClientRegex: Optional[str]
    AwsRegion: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolConfig"]:
        if not json_data:
            return None
        return cls(
            AppIdClientRegex=json_data.get("AppIdClientRegex"),
            AwsRegion=json_data.get("AwsRegion"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolConfig = UserPoolConfig


@dataclass
class LogConfig:
    CloudwatchLogsRoleArn: Optional[str]
    FieldLogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogsRoleArn=json_data.get("CloudwatchLogsRoleArn"),
            FieldLogLevel=json_data.get("FieldLogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


