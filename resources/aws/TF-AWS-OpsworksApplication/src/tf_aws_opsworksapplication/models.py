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
    AutoBundleOnDeploy: Optional[str]
    AwsFlowRubySettings: Optional[str]
    DataSourceArn: Optional[str]
    DataSourceDatabaseName: Optional[str]
    DataSourceType: Optional[str]
    Description: Optional[str]
    DocumentRoot: Optional[str]
    Domains: Optional[Sequence[str]]
    EnableSsl: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    RailsEnv: Optional[str]
    ShortName: Optional[str]
    StackId: Optional[str]
    Type: Optional[str]
    AppSource: Optional[Sequence["_AppSourceDefinition"]]
    Environment: Optional[Sequence["_EnvironmentDefinition"]]
    SslConfiguration: Optional[Sequence["_SslConfigurationDefinition"]]

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
            AutoBundleOnDeploy=json_data.get("AutoBundleOnDeploy"),
            AwsFlowRubySettings=json_data.get("AwsFlowRubySettings"),
            DataSourceArn=json_data.get("DataSourceArn"),
            DataSourceDatabaseName=json_data.get("DataSourceDatabaseName"),
            DataSourceType=json_data.get("DataSourceType"),
            Description=json_data.get("Description"),
            DocumentRoot=json_data.get("DocumentRoot"),
            Domains=json_data.get("Domains"),
            EnableSsl=json_data.get("EnableSsl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RailsEnv=json_data.get("RailsEnv"),
            ShortName=json_data.get("ShortName"),
            StackId=json_data.get("StackId"),
            Type=json_data.get("Type"),
            AppSource=deserialize_list(json_data.get("AppSource"), AppSourceDefinition),
            Environment=deserialize_list(json_data.get("Environment"), EnvironmentDefinition),
            SslConfiguration=deserialize_list(json_data.get("SslConfiguration"), SslConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppSourceDefinition(BaseModel):
    Password: Optional[str]
    Revision: Optional[str]
    SshKey: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Revision=json_data.get("Revision"),
            SshKey=json_data.get("SshKey"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppSourceDefinition = AppSourceDefinition


@dataclass
class EnvironmentDefinition(BaseModel):
    Key: Optional[str]
    Secure: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Secure=json_data.get("Secure"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentDefinition = EnvironmentDefinition


@dataclass
class SslConfigurationDefinition(BaseModel):
    Certificate: Optional[str]
    Chain: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Chain=json_data.get("Chain"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfigurationDefinition = SslConfigurationDefinition


