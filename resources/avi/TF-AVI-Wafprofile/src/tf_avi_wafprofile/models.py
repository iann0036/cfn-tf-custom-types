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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Files: Optional[Sequence["_FilesDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Files=deserialize_list(json_data.get("Files"), FilesDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    AllowedHttpVersions: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedRequestContentTypes: Optional[Sequence[str]]
    ArgumentSeparator: Optional[str]
    ClientRequestMaxBodySize: Optional[float]
    CookieFormatVersion: Optional[float]
    IgnoreIncompleteRequestBodyError: Optional[bool]
    MaxExecutionTime: Optional[float]
    RegexMatchLimit: Optional[float]
    RegexRecursionLimit: Optional[float]
    RequestBodyDefaultAction: Optional[str]
    RequestHdrDefaultAction: Optional[str]
    ResponseBodyDefaultAction: Optional[str]
    ResponseHdrDefaultAction: Optional[str]
    RestrictedExtensions: Optional[Sequence[str]]
    RestrictedHeaders: Optional[Sequence[str]]
    SendStatusHeader: Optional[bool]
    ServerResponseMaxBodySize: Optional[float]
    StaticExtensions: Optional[Sequence[str]]
    StatusCodeForRejectedRequests: Optional[str]
    StatusHeaderName: Optional[str]
    XmlXxeProtection: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHttpVersions=json_data.get("AllowedHttpVersions"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedRequestContentTypes=json_data.get("AllowedRequestContentTypes"),
            ArgumentSeparator=json_data.get("ArgumentSeparator"),
            ClientRequestMaxBodySize=json_data.get("ClientRequestMaxBodySize"),
            CookieFormatVersion=json_data.get("CookieFormatVersion"),
            IgnoreIncompleteRequestBodyError=json_data.get("IgnoreIncompleteRequestBodyError"),
            MaxExecutionTime=json_data.get("MaxExecutionTime"),
            RegexMatchLimit=json_data.get("RegexMatchLimit"),
            RegexRecursionLimit=json_data.get("RegexRecursionLimit"),
            RequestBodyDefaultAction=json_data.get("RequestBodyDefaultAction"),
            RequestHdrDefaultAction=json_data.get("RequestHdrDefaultAction"),
            ResponseBodyDefaultAction=json_data.get("ResponseBodyDefaultAction"),
            ResponseHdrDefaultAction=json_data.get("ResponseHdrDefaultAction"),
            RestrictedExtensions=json_data.get("RestrictedExtensions"),
            RestrictedHeaders=json_data.get("RestrictedHeaders"),
            SendStatusHeader=json_data.get("SendStatusHeader"),
            ServerResponseMaxBodySize=json_data.get("ServerResponseMaxBodySize"),
            StaticExtensions=json_data.get("StaticExtensions"),
            StatusCodeForRejectedRequests=json_data.get("StatusCodeForRejectedRequests"),
            StatusHeaderName=json_data.get("StatusHeaderName"),
            XmlXxeProtection=json_data.get("XmlXxeProtection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class FilesDefinition(BaseModel):
    Data: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilesDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilesDefinition = FilesDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


