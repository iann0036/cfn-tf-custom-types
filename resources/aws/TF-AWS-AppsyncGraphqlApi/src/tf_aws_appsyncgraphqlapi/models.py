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
    AuthenticationType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Schema: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Uris: Optional[Sequence["_UrisDefinition"]]
    XrayEnabled: Optional[bool]
    AdditionalAuthenticationProvider: Optional[Sequence["_AdditionalAuthenticationProviderDefinition"]]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    OpenidConnectConfig: Optional[Sequence["_OpenidConnectConfigDefinition"]]
    UserPoolConfig: Optional[Sequence["_UserPoolConfigDefinition"]]

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
            AuthenticationType=json_data.get("AuthenticationType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Schema=json_data.get("Schema"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Uris=deserialize_list(json_data.get("Uris"), UrisDefinition),
            XrayEnabled=json_data.get("XrayEnabled"),
            AdditionalAuthenticationProvider=deserialize_list(json_data.get("AdditionalAuthenticationProvider"), AdditionalAuthenticationProviderDefinition),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            OpenidConnectConfig=deserialize_list(json_data.get("OpenidConnectConfig"), OpenidConnectConfigDefinition),
            UserPoolConfig=deserialize_list(json_data.get("UserPoolConfig"), UserPoolConfigDefinition),
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
class UrisDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrisDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrisDefinition = UrisDefinition


@dataclass
class AdditionalAuthenticationProviderDefinition(BaseModel):
    AuthenticationType: Optional[str]
    OpenidConnectConfig: Optional[Sequence["_OpenidConnectConfigDefinition"]]
    UserPoolConfig: Optional[Sequence["_UserPoolConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalAuthenticationProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalAuthenticationProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationType=json_data.get("AuthenticationType"),
            OpenidConnectConfig=deserialize_list(json_data.get("OpenidConnectConfig"), OpenidConnectConfigDefinition),
            UserPoolConfig=deserialize_list(json_data.get("UserPoolConfig"), UserPoolConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalAuthenticationProviderDefinition = AdditionalAuthenticationProviderDefinition


@dataclass
class OpenidConnectConfigDefinition(BaseModel):
    AuthTtl: Optional[float]
    ClientId: Optional[str]
    IatTtl: Optional[float]
    Issuer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenidConnectConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenidConnectConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthTtl=json_data.get("AuthTtl"),
            ClientId=json_data.get("ClientId"),
            IatTtl=json_data.get("IatTtl"),
            Issuer=json_data.get("Issuer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenidConnectConfigDefinition = OpenidConnectConfigDefinition


@dataclass
class UserPoolConfigDefinition(BaseModel):
    AppIdClientRegex: Optional[str]
    AwsRegion: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AppIdClientRegex=json_data.get("AppIdClientRegex"),
            AwsRegion=json_data.get("AwsRegion"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolConfigDefinition = UserPoolConfigDefinition


@dataclass
class LogConfigDefinition(BaseModel):
    CloudwatchLogsRoleArn: Optional[str]
    ExcludeVerboseContent: Optional[bool]
    FieldLogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogsRoleArn=json_data.get("CloudwatchLogsRoleArn"),
            ExcludeVerboseContent=json_data.get("ExcludeVerboseContent"),
            FieldLogLevel=json_data.get("FieldLogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


