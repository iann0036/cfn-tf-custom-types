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
    AclId: Optional[float]
    AclNameValue: Optional[str]
    AlgDestNat: Optional[float]
    AlgSourceNat: Optional[float]
    CallIdPersistDisable: Optional[float]
    ClientKeepAlive: Optional[float]
    DialogAware: Optional[float]
    DropWhenClientFail: Optional[float]
    DropWhenServerFail: Optional[float]
    FailedClientSelection: Optional[float]
    FailedClientSelectionMessage: Optional[str]
    FailedServerSelection: Optional[float]
    FailedServerSelectionMessage: Optional[str]
    Id: Optional[str]
    InsertClientIp: Optional[float]
    Interval: Optional[float]
    KeepServerIpIfMatchAcl: Optional[float]
    Name: Optional[str]
    PstnGw: Optional[str]
    ServerKeepAlive: Optional[float]
    ServerSelectionPerRequest: Optional[float]
    ServiceGroup: Optional[str]
    SmpCallIdRtpSession: Optional[float]
    Timeout: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    ClientRequestHeader: Optional[Sequence["_ClientRequestHeaderDefinition"]]
    ClientResponseHeader: Optional[Sequence["_ClientResponseHeaderDefinition"]]
    ExcludeTranslation: Optional[Sequence["_ExcludeTranslationDefinition"]]
    ServerRequestHeader: Optional[Sequence["_ServerRequestHeaderDefinition"]]
    ServerResponseHeader: Optional[Sequence["_ServerResponseHeaderDefinition"]]

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
            AclId=json_data.get("AclId"),
            AclNameValue=json_data.get("AclNameValue"),
            AlgDestNat=json_data.get("AlgDestNat"),
            AlgSourceNat=json_data.get("AlgSourceNat"),
            CallIdPersistDisable=json_data.get("CallIdPersistDisable"),
            ClientKeepAlive=json_data.get("ClientKeepAlive"),
            DialogAware=json_data.get("DialogAware"),
            DropWhenClientFail=json_data.get("DropWhenClientFail"),
            DropWhenServerFail=json_data.get("DropWhenServerFail"),
            FailedClientSelection=json_data.get("FailedClientSelection"),
            FailedClientSelectionMessage=json_data.get("FailedClientSelectionMessage"),
            FailedServerSelection=json_data.get("FailedServerSelection"),
            FailedServerSelectionMessage=json_data.get("FailedServerSelectionMessage"),
            Id=json_data.get("Id"),
            InsertClientIp=json_data.get("InsertClientIp"),
            Interval=json_data.get("Interval"),
            KeepServerIpIfMatchAcl=json_data.get("KeepServerIpIfMatchAcl"),
            Name=json_data.get("Name"),
            PstnGw=json_data.get("PstnGw"),
            ServerKeepAlive=json_data.get("ServerKeepAlive"),
            ServerSelectionPerRequest=json_data.get("ServerSelectionPerRequest"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SmpCallIdRtpSession=json_data.get("SmpCallIdRtpSession"),
            Timeout=json_data.get("Timeout"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            ClientRequestHeader=deserialize_list(json_data.get("ClientRequestHeader"), ClientRequestHeaderDefinition),
            ClientResponseHeader=deserialize_list(json_data.get("ClientResponseHeader"), ClientResponseHeaderDefinition),
            ExcludeTranslation=deserialize_list(json_data.get("ExcludeTranslation"), ExcludeTranslationDefinition),
            ServerRequestHeader=deserialize_list(json_data.get("ServerRequestHeader"), ServerRequestHeaderDefinition),
            ServerResponseHeader=deserialize_list(json_data.get("ServerResponseHeader"), ServerResponseHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClientRequestHeaderDefinition(BaseModel):
    ClientRequestEraseAll: Optional[float]
    ClientRequestHeaderErase: Optional[str]
    ClientRequestHeaderInsert: Optional[str]
    InsertConditionClientRequest: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRequestHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRequestHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientRequestEraseAll=json_data.get("ClientRequestEraseAll"),
            ClientRequestHeaderErase=json_data.get("ClientRequestHeaderErase"),
            ClientRequestHeaderInsert=json_data.get("ClientRequestHeaderInsert"),
            InsertConditionClientRequest=json_data.get("InsertConditionClientRequest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRequestHeaderDefinition = ClientRequestHeaderDefinition


@dataclass
class ClientResponseHeaderDefinition(BaseModel):
    ClientResponseEraseAll: Optional[float]
    ClientResponseHeaderErase: Optional[str]
    ClientResponseHeaderInsert: Optional[str]
    InsertConditionClientResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientResponseHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientResponseHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientResponseEraseAll=json_data.get("ClientResponseEraseAll"),
            ClientResponseHeaderErase=json_data.get("ClientResponseHeaderErase"),
            ClientResponseHeaderInsert=json_data.get("ClientResponseHeaderInsert"),
            InsertConditionClientResponse=json_data.get("InsertConditionClientResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientResponseHeaderDefinition = ClientResponseHeaderDefinition


@dataclass
class ExcludeTranslationDefinition(BaseModel):
    HeaderString: Optional[str]
    TranslationValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderString=json_data.get("HeaderString"),
            TranslationValue=json_data.get("TranslationValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeTranslationDefinition = ExcludeTranslationDefinition


@dataclass
class ServerRequestHeaderDefinition(BaseModel):
    InsertConditionServerRequest: Optional[str]
    ServerRequestEraseAll: Optional[float]
    ServerRequestHeaderErase: Optional[str]
    ServerRequestHeaderInsert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerRequestHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerRequestHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            InsertConditionServerRequest=json_data.get("InsertConditionServerRequest"),
            ServerRequestEraseAll=json_data.get("ServerRequestEraseAll"),
            ServerRequestHeaderErase=json_data.get("ServerRequestHeaderErase"),
            ServerRequestHeaderInsert=json_data.get("ServerRequestHeaderInsert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerRequestHeaderDefinition = ServerRequestHeaderDefinition


@dataclass
class ServerResponseHeaderDefinition(BaseModel):
    InsertConditionServerResponse: Optional[str]
    ServerResponseEraseAll: Optional[float]
    ServerResponseHeaderErase: Optional[str]
    ServerResponseHeaderInsert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerResponseHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerResponseHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            InsertConditionServerResponse=json_data.get("InsertConditionServerResponse"),
            ServerResponseEraseAll=json_data.get("ServerResponseEraseAll"),
            ServerResponseHeaderErase=json_data.get("ServerResponseHeaderErase"),
            ServerResponseHeaderInsert=json_data.get("ServerResponseHeaderInsert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerResponseHeaderDefinition = ServerResponseHeaderDefinition


