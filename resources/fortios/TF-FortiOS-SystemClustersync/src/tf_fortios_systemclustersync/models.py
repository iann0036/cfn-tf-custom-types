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
    HbInterval: Optional[float]
    HbLostThreshold: Optional[float]
    Id: Optional[str]
    IpsecTunnelSync: Optional[str]
    Peerip: Optional[str]
    Peervd: Optional[str]
    SlaveAddIkeRoutes: Optional[str]
    SyncId: Optional[float]
    Vdomparam: Optional[str]
    DownIntfsBeforeSessSync: Optional[Sequence["_DownIntfsBeforeSessSyncDefinition"]]
    SessionSyncFilter: Optional[Sequence["_SessionSyncFilterDefinition"]]
    Syncvd: Optional[Sequence["_SyncvdDefinition"]]

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
            HbInterval=json_data.get("HbInterval"),
            HbLostThreshold=json_data.get("HbLostThreshold"),
            Id=json_data.get("Id"),
            IpsecTunnelSync=json_data.get("IpsecTunnelSync"),
            Peerip=json_data.get("Peerip"),
            Peervd=json_data.get("Peervd"),
            SlaveAddIkeRoutes=json_data.get("SlaveAddIkeRoutes"),
            SyncId=json_data.get("SyncId"),
            Vdomparam=json_data.get("Vdomparam"),
            DownIntfsBeforeSessSync=deserialize_list(json_data.get("DownIntfsBeforeSessSync"), DownIntfsBeforeSessSyncDefinition),
            SessionSyncFilter=deserialize_list(json_data.get("SessionSyncFilter"), SessionSyncFilterDefinition),
            Syncvd=deserialize_list(json_data.get("Syncvd"), SyncvdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DownIntfsBeforeSessSyncDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DownIntfsBeforeSessSyncDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DownIntfsBeforeSessSyncDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DownIntfsBeforeSessSyncDefinition = DownIntfsBeforeSessSyncDefinition


@dataclass
class SessionSyncFilterDefinition(BaseModel):
    Dstaddr: Optional[str]
    Dstaddr6: Optional[str]
    Dstintf: Optional[str]
    Srcaddr: Optional[str]
    Srcaddr6: Optional[str]
    Srcintf: Optional[str]
    CustomService: Optional[Sequence["_CustomServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SessionSyncFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionSyncFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Dstaddr=json_data.get("Dstaddr"),
            Dstaddr6=json_data.get("Dstaddr6"),
            Dstintf=json_data.get("Dstintf"),
            Srcaddr=json_data.get("Srcaddr"),
            Srcaddr6=json_data.get("Srcaddr6"),
            Srcintf=json_data.get("Srcintf"),
            CustomService=deserialize_list(json_data.get("CustomService"), CustomServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionSyncFilterDefinition = SessionSyncFilterDefinition


@dataclass
class CustomServiceDefinition(BaseModel):
    DstPortRange: Optional[str]
    Id: Optional[float]
    SrcPortRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            DstPortRange=json_data.get("DstPortRange"),
            Id=json_data.get("Id"),
            SrcPortRange=json_data.get("SrcPortRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomServiceDefinition = CustomServiceDefinition


@dataclass
class SyncvdDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SyncvdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyncvdDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyncvdDefinition = SyncvdDefinition


