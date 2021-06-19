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
    Id: Optional[str]
    Ifnum: Optional[float]
    Uuid: Optional[str]
    EnableCfg: Optional[Sequence["_EnableCfgDefinition"]]
    NotificationCfg: Optional[Sequence["_NotificationCfgDefinition"]]
    TxDot1Cfg: Optional[Sequence["_TxDot1CfgDefinition"]]
    TxTlvsCfg: Optional[Sequence["_TxTlvsCfgDefinition"]]

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
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
            Uuid=json_data.get("Uuid"),
            EnableCfg=deserialize_list(json_data.get("EnableCfg"), EnableCfgDefinition),
            NotificationCfg=deserialize_list(json_data.get("NotificationCfg"), NotificationCfgDefinition),
            TxDot1Cfg=deserialize_list(json_data.get("TxDot1Cfg"), TxDot1CfgDefinition),
            TxTlvsCfg=deserialize_list(json_data.get("TxTlvsCfg"), TxTlvsCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnableCfgDefinition(BaseModel):
    RtEnable: Optional[float]
    Rx: Optional[float]
    Tx: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EnableCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RtEnable=json_data.get("RtEnable"),
            Rx=json_data.get("Rx"),
            Tx=json_data.get("Tx"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableCfgDefinition = EnableCfgDefinition


@dataclass
class NotificationCfgDefinition(BaseModel):
    NotifEnable: Optional[float]
    Notification: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NotifEnable=json_data.get("NotifEnable"),
            Notification=json_data.get("Notification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationCfgDefinition = NotificationCfgDefinition


@dataclass
class TxDot1CfgDefinition(BaseModel):
    LinkAggregation: Optional[float]
    TxDot1Tlvs: Optional[float]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TxDot1CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxDot1CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkAggregation=json_data.get("LinkAggregation"),
            TxDot1Tlvs=json_data.get("TxDot1Tlvs"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxDot1CfgDefinition = TxDot1CfgDefinition


@dataclass
class TxTlvsCfgDefinition(BaseModel):
    Exclude: Optional[float]
    ManagementAddress: Optional[float]
    PortDescription: Optional[float]
    SystemCapabilities: Optional[float]
    SystemDescription: Optional[float]
    SystemName: Optional[float]
    TxTlvs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TxTlvsCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxTlvsCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            ManagementAddress=json_data.get("ManagementAddress"),
            PortDescription=json_data.get("PortDescription"),
            SystemCapabilities=json_data.get("SystemCapabilities"),
            SystemDescription=json_data.get("SystemDescription"),
            SystemName=json_data.get("SystemName"),
            TxTlvs=json_data.get("TxTlvs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxTlvsCfgDefinition = TxTlvsCfgDefinition


