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
    Authorized: Optional[str]
    Description: Optional[str]
    ExtName: Optional[str]
    Fosid: Optional[str]
    Id: Optional[str]
    LoginPassword: Optional[str]
    Name: Optional[str]
    Vdom: Optional[float]
    Vdomparam: Optional[str]
    ControllerReport: Optional[Sequence["_ControllerReportDefinition"]]
    Modem1: Optional[Sequence["_Modem1Definition"]]
    Modem2: Optional[Sequence["_Modem2Definition"]]

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
            Authorized=json_data.get("Authorized"),
            Description=json_data.get("Description"),
            ExtName=json_data.get("ExtName"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            LoginPassword=json_data.get("LoginPassword"),
            Name=json_data.get("Name"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            ControllerReport=deserialize_list(json_data.get("ControllerReport"), ControllerReportDefinition),
            Modem1=deserialize_list(json_data.get("Modem1"), Modem1Definition),
            Modem2=deserialize_list(json_data.get("Modem2"), Modem2Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ControllerReportDefinition(BaseModel):
    Interval: Optional[float]
    SignalThreshold: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerReportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerReportDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            SignalThreshold=json_data.get("SignalThreshold"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerReportDefinition = ControllerReportDefinition


@dataclass
class Modem1Definition(BaseModel):
    ConnStatus: Optional[float]
    DefaultSim: Optional[str]
    Gps: Optional[str]
    Ifname: Optional[str]
    PreferredCarrier: Optional[str]
    RedundantIntf: Optional[str]
    RedundantMode: Optional[str]
    Sim1Pin: Optional[str]
    Sim1PinCode: Optional[str]
    Sim2Pin: Optional[str]
    Sim2PinCode: Optional[str]
    AutoSwitch: Optional[Sequence["_AutoSwitchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Modem1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Modem1Definition"]:
        if not json_data:
            return None
        return cls(
            ConnStatus=json_data.get("ConnStatus"),
            DefaultSim=json_data.get("DefaultSim"),
            Gps=json_data.get("Gps"),
            Ifname=json_data.get("Ifname"),
            PreferredCarrier=json_data.get("PreferredCarrier"),
            RedundantIntf=json_data.get("RedundantIntf"),
            RedundantMode=json_data.get("RedundantMode"),
            Sim1Pin=json_data.get("Sim1Pin"),
            Sim1PinCode=json_data.get("Sim1PinCode"),
            Sim2Pin=json_data.get("Sim2Pin"),
            Sim2PinCode=json_data.get("Sim2PinCode"),
            AutoSwitch=deserialize_list(json_data.get("AutoSwitch"), AutoSwitchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Modem1Definition = Modem1Definition


@dataclass
class AutoSwitchDefinition(BaseModel):
    Dataplan: Optional[str]
    Disconnect: Optional[str]
    DisconnectPeriod: Optional[float]
    DisconnectThreshold: Optional[float]
    Signal: Optional[str]
    SwitchBack: Optional[str]
    SwitchBackTime: Optional[str]
    SwitchBackTimer: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoSwitchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoSwitchDefinition"]:
        if not json_data:
            return None
        return cls(
            Dataplan=json_data.get("Dataplan"),
            Disconnect=json_data.get("Disconnect"),
            DisconnectPeriod=json_data.get("DisconnectPeriod"),
            DisconnectThreshold=json_data.get("DisconnectThreshold"),
            Signal=json_data.get("Signal"),
            SwitchBack=json_data.get("SwitchBack"),
            SwitchBackTime=json_data.get("SwitchBackTime"),
            SwitchBackTimer=json_data.get("SwitchBackTimer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoSwitchDefinition = AutoSwitchDefinition


@dataclass
class Modem2Definition(BaseModel):
    ConnStatus: Optional[float]
    DefaultSim: Optional[str]
    Gps: Optional[str]
    Ifname: Optional[str]
    PreferredCarrier: Optional[str]
    RedundantIntf: Optional[str]
    RedundantMode: Optional[str]
    Sim1Pin: Optional[str]
    Sim1PinCode: Optional[str]
    Sim2Pin: Optional[str]
    Sim2PinCode: Optional[str]
    AutoSwitch: Optional[Sequence["_AutoSwitchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Modem2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Modem2Definition"]:
        if not json_data:
            return None
        return cls(
            ConnStatus=json_data.get("ConnStatus"),
            DefaultSim=json_data.get("DefaultSim"),
            Gps=json_data.get("Gps"),
            Ifname=json_data.get("Ifname"),
            PreferredCarrier=json_data.get("PreferredCarrier"),
            RedundantIntf=json_data.get("RedundantIntf"),
            RedundantMode=json_data.get("RedundantMode"),
            Sim1Pin=json_data.get("Sim1Pin"),
            Sim1PinCode=json_data.get("Sim1PinCode"),
            Sim2Pin=json_data.get("Sim2Pin"),
            Sim2PinCode=json_data.get("Sim2PinCode"),
            AutoSwitch=deserialize_list(json_data.get("AutoSwitch"), AutoSwitchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Modem2Definition = Modem2Definition


