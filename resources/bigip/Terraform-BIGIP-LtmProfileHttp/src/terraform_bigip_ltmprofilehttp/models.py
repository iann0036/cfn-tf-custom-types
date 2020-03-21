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
    AcceptXff: Optional[str]
    AppService: Optional[str]
    BasicAuthRealm: Optional[str]
    DefaultsFrom: Optional[str]
    Description: Optional[str]
    EncryptCookieSecret: Optional[str]
    EncryptCookies: Optional[Sequence[str]]
    FallbackHost: Optional[str]
    FallbackStatusCodes: Optional[Sequence[str]]
    HeadErase: Optional[str]
    HeadInsert: Optional[str]
    InsertXforwardedFor: Optional[str]
    LwsSeparator: Optional[str]
    Name: Optional[str]
    OneconnectTransformations: Optional[str]
    ProxyType: Optional[str]
    RedirectRewrite: Optional[str]
    RequestChunking: Optional[str]
    ResponseChunking: Optional[str]
    ResponseHeadersPermitted: Optional[Sequence[str]]
    ServerAgentName: Optional[str]
    TmPartition: Optional[str]
    ViaHostName: Optional[str]
    ViaRequest: Optional[str]
    ViaResponse: Optional[str]
    XffAlternativeNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptXff=json_data.get("AcceptXff"),
            AppService=json_data.get("AppService"),
            BasicAuthRealm=json_data.get("BasicAuthRealm"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            Description=json_data.get("Description"),
            EncryptCookieSecret=json_data.get("EncryptCookieSecret"),
            EncryptCookies=json_data.get("EncryptCookies"),
            FallbackHost=json_data.get("FallbackHost"),
            FallbackStatusCodes=json_data.get("FallbackStatusCodes"),
            HeadErase=json_data.get("HeadErase"),
            HeadInsert=json_data.get("HeadInsert"),
            InsertXforwardedFor=json_data.get("InsertXforwardedFor"),
            LwsSeparator=json_data.get("LwsSeparator"),
            Name=json_data.get("Name"),
            OneconnectTransformations=json_data.get("OneconnectTransformations"),
            ProxyType=json_data.get("ProxyType"),
            RedirectRewrite=json_data.get("RedirectRewrite"),
            RequestChunking=json_data.get("RequestChunking"),
            ResponseChunking=json_data.get("ResponseChunking"),
            ResponseHeadersPermitted=json_data.get("ResponseHeadersPermitted"),
            ServerAgentName=json_data.get("ServerAgentName"),
            TmPartition=json_data.get("TmPartition"),
            ViaHostName=json_data.get("ViaHostName"),
            ViaRequest=json_data.get("ViaRequest"),
            ViaResponse=json_data.get("ViaResponse"),
            XffAlternativeNames=json_data.get("XffAlternativeNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


