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
    Accprofile: Optional[str]
    ActionType: Optional[str]
    AlicloudAccessKeyId: Optional[str]
    AlicloudAccessKeySecret: Optional[str]
    AlicloudAccountId: Optional[str]
    AlicloudFunction: Optional[str]
    AlicloudFunctionAuthorization: Optional[str]
    AlicloudFunctionDomain: Optional[str]
    AlicloudRegion: Optional[str]
    AlicloudService: Optional[str]
    AlicloudVersion: Optional[str]
    AwsApiId: Optional[str]
    AwsApiKey: Optional[str]
    AwsApiPath: Optional[str]
    AwsApiStage: Optional[str]
    AwsDomain: Optional[str]
    AwsRegion: Optional[str]
    AzureApiKey: Optional[str]
    AzureApp: Optional[str]
    AzureDomain: Optional[str]
    AzureFunction: Optional[str]
    AzureFunctionAuthorization: Optional[str]
    Delay: Optional[float]
    DynamicSortSubtable: Optional[str]
    EmailBody: Optional[str]
    EmailFrom: Optional[str]
    EmailSubject: Optional[str]
    GcpFunction: Optional[str]
    GcpFunctionDomain: Optional[str]
    GcpFunctionRegion: Optional[str]
    GcpProject: Optional[str]
    HttpBody: Optional[str]
    Id: Optional[str]
    Message: Optional[str]
    Method: Optional[str]
    MinimumInterval: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ReplacementMessage: Optional[str]
    Required: Optional[str]
    Script: Optional[str]
    SecurityTag: Optional[str]
    TlsCertificate: Optional[str]
    Uri: Optional[str]
    Vdomparam: Optional[str]
    EmailTo: Optional[Sequence["_EmailToDefinition"]]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    SdnConnector: Optional[Sequence["_SdnConnectorDefinition"]]

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
            Accprofile=json_data.get("Accprofile"),
            ActionType=json_data.get("ActionType"),
            AlicloudAccessKeyId=json_data.get("AlicloudAccessKeyId"),
            AlicloudAccessKeySecret=json_data.get("AlicloudAccessKeySecret"),
            AlicloudAccountId=json_data.get("AlicloudAccountId"),
            AlicloudFunction=json_data.get("AlicloudFunction"),
            AlicloudFunctionAuthorization=json_data.get("AlicloudFunctionAuthorization"),
            AlicloudFunctionDomain=json_data.get("AlicloudFunctionDomain"),
            AlicloudRegion=json_data.get("AlicloudRegion"),
            AlicloudService=json_data.get("AlicloudService"),
            AlicloudVersion=json_data.get("AlicloudVersion"),
            AwsApiId=json_data.get("AwsApiId"),
            AwsApiKey=json_data.get("AwsApiKey"),
            AwsApiPath=json_data.get("AwsApiPath"),
            AwsApiStage=json_data.get("AwsApiStage"),
            AwsDomain=json_data.get("AwsDomain"),
            AwsRegion=json_data.get("AwsRegion"),
            AzureApiKey=json_data.get("AzureApiKey"),
            AzureApp=json_data.get("AzureApp"),
            AzureDomain=json_data.get("AzureDomain"),
            AzureFunction=json_data.get("AzureFunction"),
            AzureFunctionAuthorization=json_data.get("AzureFunctionAuthorization"),
            Delay=json_data.get("Delay"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailBody=json_data.get("EmailBody"),
            EmailFrom=json_data.get("EmailFrom"),
            EmailSubject=json_data.get("EmailSubject"),
            GcpFunction=json_data.get("GcpFunction"),
            GcpFunctionDomain=json_data.get("GcpFunctionDomain"),
            GcpFunctionRegion=json_data.get("GcpFunctionRegion"),
            GcpProject=json_data.get("GcpProject"),
            HttpBody=json_data.get("HttpBody"),
            Id=json_data.get("Id"),
            Message=json_data.get("Message"),
            Method=json_data.get("Method"),
            MinimumInterval=json_data.get("MinimumInterval"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ReplacementMessage=json_data.get("ReplacementMessage"),
            Required=json_data.get("Required"),
            Script=json_data.get("Script"),
            SecurityTag=json_data.get("SecurityTag"),
            TlsCertificate=json_data.get("TlsCertificate"),
            Uri=json_data.get("Uri"),
            Vdomparam=json_data.get("Vdomparam"),
            EmailTo=deserialize_list(json_data.get("EmailTo"), EmailToDefinition),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            SdnConnector=deserialize_list(json_data.get("SdnConnector"), SdnConnectorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EmailToDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailToDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailToDefinition = EmailToDefinition


@dataclass
class HeadersDefinition(BaseModel):
    Header: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class SdnConnectorDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SdnConnectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdnConnectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdnConnectorDefinition = SdnConnectorDefinition


