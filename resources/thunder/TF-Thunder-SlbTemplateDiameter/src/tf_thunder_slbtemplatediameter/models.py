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
    AvpCode: Optional[float]
    AvpString: Optional[str]
    CustomizeCea: Optional[float]
    DwrTime: Optional[float]
    DwrUpRetry: Optional[float]
    ForwardToLatestServer: Optional[float]
    ForwardUnknownSessionId: Optional[float]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    LoadBalanceOnSessionId: Optional[float]
    MultipleOriginHost: Optional[float]
    Name: Optional[str]
    OriginRealm: Optional[str]
    ProductName: Optional[str]
    ServiceGroupName: Optional[str]
    SessionAge: Optional[float]
    TerminateOnCcaT: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    VendorId: Optional[float]
    AvpList: Optional[Sequence["_AvpListDefinition"]]
    MessageCodeList: Optional[Sequence["_MessageCodeListDefinition"]]
    OriginHost: Optional[Sequence["_OriginHostDefinition"]]

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
            AvpCode=json_data.get("AvpCode"),
            AvpString=json_data.get("AvpString"),
            CustomizeCea=json_data.get("CustomizeCea"),
            DwrTime=json_data.get("DwrTime"),
            DwrUpRetry=json_data.get("DwrUpRetry"),
            ForwardToLatestServer=json_data.get("ForwardToLatestServer"),
            ForwardUnknownSessionId=json_data.get("ForwardUnknownSessionId"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            LoadBalanceOnSessionId=json_data.get("LoadBalanceOnSessionId"),
            MultipleOriginHost=json_data.get("MultipleOriginHost"),
            Name=json_data.get("Name"),
            OriginRealm=json_data.get("OriginRealm"),
            ProductName=json_data.get("ProductName"),
            ServiceGroupName=json_data.get("ServiceGroupName"),
            SessionAge=json_data.get("SessionAge"),
            TerminateOnCcaT=json_data.get("TerminateOnCcaT"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            VendorId=json_data.get("VendorId"),
            AvpList=deserialize_list(json_data.get("AvpList"), AvpListDefinition),
            MessageCodeList=deserialize_list(json_data.get("MessageCodeList"), MessageCodeListDefinition),
            OriginHost=deserialize_list(json_data.get("OriginHost"), OriginHostDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvpListDefinition(BaseModel):
    Avp: Optional[float]
    Int32: Optional[float]
    Int64: Optional[float]
    Mandatory: Optional[float]
    String: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvpListDefinition"]:
        if not json_data:
            return None
        return cls(
            Avp=json_data.get("Avp"),
            Int32=json_data.get("Int32"),
            Int64=json_data.get("Int64"),
            Mandatory=json_data.get("Mandatory"),
            String=json_data.get("String"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvpListDefinition = AvpListDefinition


@dataclass
class MessageCodeListDefinition(BaseModel):
    MessageCode: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MessageCodeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageCodeListDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageCode=json_data.get("MessageCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageCodeListDefinition = MessageCodeListDefinition


@dataclass
class OriginHostDefinition(BaseModel):
    OriginHostName: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginHostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginHostDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginHostName=json_data.get("OriginHostName"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginHostDefinition = OriginHostDefinition


