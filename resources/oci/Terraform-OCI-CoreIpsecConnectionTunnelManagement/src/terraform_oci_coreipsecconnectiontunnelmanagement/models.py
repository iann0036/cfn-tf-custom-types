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
    CompartmentId: Optional[str]
    CpeIp: Optional[str]
    DisplayName: Optional[str]
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
    BgpSessionInfo: Optional[Sequence["_BgpSessionInfo"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            CpeIp=json_data.get("CpeIp"),
            DisplayName=json_data.get("DisplayName"),
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
            BgpSessionInfo=json_data.get("BgpSessionInfo"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpSessionInfo:
    CustomerBgpAsn: Optional[str]
    CustomerInterfaceIp: Optional[str]
    OracleInterfaceIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpSessionInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpSessionInfo"]:
        if not json_data:
            return None
        return cls(
            CustomerBgpAsn=json_data.get("CustomerBgpAsn"),
            CustomerInterfaceIp=json_data.get("CustomerInterfaceIp"),
            OracleInterfaceIp=json_data.get("OracleInterfaceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpSessionInfo = BgpSessionInfo


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


