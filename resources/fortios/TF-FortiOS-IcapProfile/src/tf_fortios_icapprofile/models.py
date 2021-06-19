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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Methods: Optional[str]
    Name: Optional[str]
    Preview: Optional[str]
    PreviewDataLength: Optional[float]
    ReplacemsgGroup: Optional[str]
    Request: Optional[str]
    RequestFailure: Optional[str]
    RequestPath: Optional[str]
    RequestServer: Optional[str]
    RespmodDefaultAction: Optional[str]
    Response: Optional[str]
    ResponseFailure: Optional[str]
    ResponsePath: Optional[str]
    ResponseReqHdr: Optional[str]
    ResponseServer: Optional[str]
    StreamingContentBypass: Optional[str]
    Vdomparam: Optional[str]
    IcapHeaders: Optional[Sequence["_IcapHeadersDefinition"]]
    RespmodForwardRules: Optional[Sequence["_RespmodForwardRulesDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Methods=json_data.get("Methods"),
            Name=json_data.get("Name"),
            Preview=json_data.get("Preview"),
            PreviewDataLength=json_data.get("PreviewDataLength"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            Request=json_data.get("Request"),
            RequestFailure=json_data.get("RequestFailure"),
            RequestPath=json_data.get("RequestPath"),
            RequestServer=json_data.get("RequestServer"),
            RespmodDefaultAction=json_data.get("RespmodDefaultAction"),
            Response=json_data.get("Response"),
            ResponseFailure=json_data.get("ResponseFailure"),
            ResponsePath=json_data.get("ResponsePath"),
            ResponseReqHdr=json_data.get("ResponseReqHdr"),
            ResponseServer=json_data.get("ResponseServer"),
            StreamingContentBypass=json_data.get("StreamingContentBypass"),
            Vdomparam=json_data.get("Vdomparam"),
            IcapHeaders=deserialize_list(json_data.get("IcapHeaders"), IcapHeadersDefinition),
            RespmodForwardRules=deserialize_list(json_data.get("RespmodForwardRules"), RespmodForwardRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IcapHeadersDefinition(BaseModel):
    Base64Encoding: Optional[str]
    Content: Optional[str]
    Id: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcapHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcapHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Base64Encoding=json_data.get("Base64Encoding"),
            Content=json_data.get("Content"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcapHeadersDefinition = IcapHeadersDefinition


@dataclass
class RespmodForwardRulesDefinition(BaseModel):
    Action: Optional[str]
    Host: Optional[str]
    Name: Optional[str]
    HeaderGroup: Optional[Sequence["_HeaderGroupDefinition"]]
    HttpRespStatusCode: Optional[Sequence["_HttpRespStatusCodeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RespmodForwardRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RespmodForwardRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Host=json_data.get("Host"),
            Name=json_data.get("Name"),
            HeaderGroup=deserialize_list(json_data.get("HeaderGroup"), HeaderGroupDefinition),
            HttpRespStatusCode=deserialize_list(json_data.get("HttpRespStatusCode"), HttpRespStatusCodeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RespmodForwardRulesDefinition = RespmodForwardRulesDefinition


@dataclass
class HeaderGroupDefinition(BaseModel):
    CaseSensitivity: Optional[str]
    Header: Optional[str]
    HeaderName: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitivity=json_data.get("CaseSensitivity"),
            Header=json_data.get("Header"),
            HeaderName=json_data.get("HeaderName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderGroupDefinition = HeaderGroupDefinition


@dataclass
class HttpRespStatusCodeDefinition(BaseModel):
    Code: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRespStatusCodeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRespStatusCodeDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRespStatusCodeDefinition = HttpRespStatusCodeDefinition


