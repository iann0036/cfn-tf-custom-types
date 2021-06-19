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
    CompartmentId: Optional[str]
    CpeIp: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    IkeVersion: Optional[str]
    IpsecId: Optional[str]
    Routing: Optional[str]
    SharedSecret: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    TimeCreated: Optional[str]
    TimeStatusUpdated: Optional[str]
    TunnelId: Optional[str]
    VpnIp: Optional[str]
    BgpSessionInfo: Optional[Sequence["_BgpSessionInfoDefinition"]]
    EncryptionDomainConfig: Optional[Sequence["_EncryptionDomainConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            CpeIp=json_data.get("CpeIp"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IkeVersion=json_data.get("IkeVersion"),
            IpsecId=json_data.get("IpsecId"),
            Routing=json_data.get("Routing"),
            SharedSecret=json_data.get("SharedSecret"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeStatusUpdated=json_data.get("TimeStatusUpdated"),
            TunnelId=json_data.get("TunnelId"),
            VpnIp=json_data.get("VpnIp"),
            BgpSessionInfo=deserialize_list(json_data.get("BgpSessionInfo"), BgpSessionInfoDefinition),
            EncryptionDomainConfig=deserialize_list(json_data.get("EncryptionDomainConfig"), EncryptionDomainConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpSessionInfoDefinition(BaseModel):
    CustomerBgpAsn: Optional[str]
    CustomerInterfaceIp: Optional[str]
    OracleInterfaceIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpSessionInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpSessionInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomerBgpAsn=json_data.get("CustomerBgpAsn"),
            CustomerInterfaceIp=json_data.get("CustomerInterfaceIp"),
            OracleInterfaceIp=json_data.get("OracleInterfaceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpSessionInfoDefinition = BgpSessionInfoDefinition


@dataclass
class EncryptionDomainConfigDefinition(BaseModel):
    CpeTrafficSelector: Optional[Sequence[str]]
    OracleTrafficSelector: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionDomainConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionDomainConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CpeTrafficSelector=json_data.get("CpeTrafficSelector"),
            OracleTrafficSelector=json_data.get("OracleTrafficSelector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionDomainConfigDefinition = EncryptionDomainConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


