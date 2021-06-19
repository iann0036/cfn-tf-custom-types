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
    Name: Optional[str]
    Vdomparam: Optional[str]
    Bookmarks: Optional[Sequence["_BookmarksDefinition"]]

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
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Bookmarks=deserialize_list(json_data.get("Bookmarks"), BookmarksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BookmarksDefinition(BaseModel):
    AdditionalParams: Optional[str]
    Apptype: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    Folder: Optional[str]
    Host: Optional[str]
    ListeningPort: Optional[float]
    LoadBalancingInfo: Optional[str]
    LogonPassword: Optional[str]
    LogonUser: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PreconnectionBlob: Optional[str]
    PreconnectionId: Optional[float]
    RemotePort: Optional[float]
    Security: Optional[str]
    ServerLayout: Optional[str]
    ShowStatusWindow: Optional[str]
    Sso: Optional[str]
    SsoCredential: Optional[str]
    SsoCredentialSentOnce: Optional[str]
    SsoPassword: Optional[str]
    SsoUsername: Optional[str]
    Url: Optional[str]
    FormData: Optional[Sequence["_FormDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BookmarksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BookmarksDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalParams=json_data.get("AdditionalParams"),
            Apptype=json_data.get("Apptype"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            Folder=json_data.get("Folder"),
            Host=json_data.get("Host"),
            ListeningPort=json_data.get("ListeningPort"),
            LoadBalancingInfo=json_data.get("LoadBalancingInfo"),
            LogonPassword=json_data.get("LogonPassword"),
            LogonUser=json_data.get("LogonUser"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PreconnectionBlob=json_data.get("PreconnectionBlob"),
            PreconnectionId=json_data.get("PreconnectionId"),
            RemotePort=json_data.get("RemotePort"),
            Security=json_data.get("Security"),
            ServerLayout=json_data.get("ServerLayout"),
            ShowStatusWindow=json_data.get("ShowStatusWindow"),
            Sso=json_data.get("Sso"),
            SsoCredential=json_data.get("SsoCredential"),
            SsoCredentialSentOnce=json_data.get("SsoCredentialSentOnce"),
            SsoPassword=json_data.get("SsoPassword"),
            SsoUsername=json_data.get("SsoUsername"),
            Url=json_data.get("Url"),
            FormData=deserialize_list(json_data.get("FormData"), FormDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BookmarksDefinition = BookmarksDefinition


@dataclass
class FormDataDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormDataDefinition = FormDataDefinition


