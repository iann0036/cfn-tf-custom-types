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
    AccessMode: Optional[str]
    BasicAuthEnabled: Optional[bool]
    BasicAuthPassword: Optional[str]
    BasicAuthUsername: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    IsDefault: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]
    JsonData: Optional[Sequence["_JsonDataDefinition"]]
    SecureJsonData: Optional[Sequence["_SecureJsonDataDefinition"]]

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
            AccessMode=json_data.get("AccessMode"),
            BasicAuthEnabled=json_data.get("BasicAuthEnabled"),
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            BasicAuthUsername=json_data.get("BasicAuthUsername"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
            JsonData=deserialize_list(json_data.get("JsonData"), JsonDataDefinition),
            SecureJsonData=deserialize_list(json_data.get("SecureJsonData"), SecureJsonDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JsonDataDefinition(BaseModel):
    AssumeRoleArn: Optional[str]
    AuthType: Optional[str]
    AuthenticationType: Optional[str]
    ClientEmail: Optional[str]
    ConnMaxLifetime: Optional[float]
    CustomMetricsNamespaces: Optional[str]
    DefaultProject: Optional[str]
    DefaultRegion: Optional[str]
    Encrypt: Optional[str]
    EsVersion: Optional[float]
    GraphiteVersion: Optional[str]
    HttpMethod: Optional[str]
    Interval: Optional[str]
    LogLevelField: Optional[str]
    LogMessageField: Optional[str]
    MaxIdleConns: Optional[float]
    MaxOpenConns: Optional[float]
    PostgresVersion: Optional[float]
    Profile: Optional[str]
    QueryTimeout: Optional[str]
    SslMode: Optional[str]
    TimeField: Optional[str]
    TimeInterval: Optional[str]
    Timescaledb: Optional[bool]
    TlsAuth: Optional[bool]
    TlsAuthWithCaCert: Optional[bool]
    TlsSkipVerify: Optional[bool]
    TokenUri: Optional[str]
    TsdbResolution: Optional[str]
    TsdbVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AssumeRoleArn=json_data.get("AssumeRoleArn"),
            AuthType=json_data.get("AuthType"),
            AuthenticationType=json_data.get("AuthenticationType"),
            ClientEmail=json_data.get("ClientEmail"),
            ConnMaxLifetime=json_data.get("ConnMaxLifetime"),
            CustomMetricsNamespaces=json_data.get("CustomMetricsNamespaces"),
            DefaultProject=json_data.get("DefaultProject"),
            DefaultRegion=json_data.get("DefaultRegion"),
            Encrypt=json_data.get("Encrypt"),
            EsVersion=json_data.get("EsVersion"),
            GraphiteVersion=json_data.get("GraphiteVersion"),
            HttpMethod=json_data.get("HttpMethod"),
            Interval=json_data.get("Interval"),
            LogLevelField=json_data.get("LogLevelField"),
            LogMessageField=json_data.get("LogMessageField"),
            MaxIdleConns=json_data.get("MaxIdleConns"),
            MaxOpenConns=json_data.get("MaxOpenConns"),
            PostgresVersion=json_data.get("PostgresVersion"),
            Profile=json_data.get("Profile"),
            QueryTimeout=json_data.get("QueryTimeout"),
            SslMode=json_data.get("SslMode"),
            TimeField=json_data.get("TimeField"),
            TimeInterval=json_data.get("TimeInterval"),
            Timescaledb=json_data.get("Timescaledb"),
            TlsAuth=json_data.get("TlsAuth"),
            TlsAuthWithCaCert=json_data.get("TlsAuthWithCaCert"),
            TlsSkipVerify=json_data.get("TlsSkipVerify"),
            TokenUri=json_data.get("TokenUri"),
            TsdbResolution=json_data.get("TsdbResolution"),
            TsdbVersion=json_data.get("TsdbVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonDataDefinition = JsonDataDefinition


@dataclass
class SecureJsonDataDefinition(BaseModel):
    AccessKey: Optional[str]
    BasicAuthPassword: Optional[str]
    Password: Optional[str]
    PrivateKey: Optional[str]
    SecretKey: Optional[str]
    TlsCaCert: Optional[str]
    TlsClientCert: Optional[str]
    TlsClientKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecureJsonDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecureJsonDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            Password=json_data.get("Password"),
            PrivateKey=json_data.get("PrivateKey"),
            SecretKey=json_data.get("SecretKey"),
            TlsCaCert=json_data.get("TlsCaCert"),
            TlsClientCert=json_data.get("TlsClientCert"),
            TlsClientKey=json_data.get("TlsClientKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecureJsonDataDefinition = SecureJsonDataDefinition


