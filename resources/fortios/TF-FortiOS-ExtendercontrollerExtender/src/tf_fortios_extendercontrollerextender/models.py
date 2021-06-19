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
    AaaSharedSecret: Optional[str]
    AccessPointName: Optional[str]
    Admin: Optional[str]
    AtDialScript: Optional[str]
    BillingStartDay: Optional[float]
    CdmaAaaSpi: Optional[str]
    CdmaHaSpi: Optional[str]
    CdmaNai: Optional[str]
    ConnStatus: Optional[float]
    Description: Optional[str]
    DialMode: Optional[str]
    DialStatus: Optional[float]
    ExtName: Optional[str]
    Fosid: Optional[str]
    HaSharedSecret: Optional[str]
    Id: Optional[str]
    Ifname: Optional[str]
    InitiatedUpdate: Optional[str]
    Mode: Optional[str]
    ModemPasswd: Optional[str]
    ModemType: Optional[str]
    MultiMode: Optional[str]
    PppAuthProtocol: Optional[str]
    PppEchoRequest: Optional[str]
    PppPassword: Optional[str]
    PppUsername: Optional[str]
    PrimaryHa: Optional[str]
    QuotaLimitMb: Optional[float]
    Redial: Optional[str]
    RedundantIntf: Optional[str]
    Roaming: Optional[str]
    Role: Optional[str]
    SecondaryHa: Optional[str]
    SimPin: Optional[str]
    Vdom: Optional[float]
    Vdomparam: Optional[str]
    WimaxAuthProtocol: Optional[str]
    WimaxCarrier: Optional[str]
    WimaxRealm: Optional[str]

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
            AaaSharedSecret=json_data.get("AaaSharedSecret"),
            AccessPointName=json_data.get("AccessPointName"),
            Admin=json_data.get("Admin"),
            AtDialScript=json_data.get("AtDialScript"),
            BillingStartDay=json_data.get("BillingStartDay"),
            CdmaAaaSpi=json_data.get("CdmaAaaSpi"),
            CdmaHaSpi=json_data.get("CdmaHaSpi"),
            CdmaNai=json_data.get("CdmaNai"),
            ConnStatus=json_data.get("ConnStatus"),
            Description=json_data.get("Description"),
            DialMode=json_data.get("DialMode"),
            DialStatus=json_data.get("DialStatus"),
            ExtName=json_data.get("ExtName"),
            Fosid=json_data.get("Fosid"),
            HaSharedSecret=json_data.get("HaSharedSecret"),
            Id=json_data.get("Id"),
            Ifname=json_data.get("Ifname"),
            InitiatedUpdate=json_data.get("InitiatedUpdate"),
            Mode=json_data.get("Mode"),
            ModemPasswd=json_data.get("ModemPasswd"),
            ModemType=json_data.get("ModemType"),
            MultiMode=json_data.get("MultiMode"),
            PppAuthProtocol=json_data.get("PppAuthProtocol"),
            PppEchoRequest=json_data.get("PppEchoRequest"),
            PppPassword=json_data.get("PppPassword"),
            PppUsername=json_data.get("PppUsername"),
            PrimaryHa=json_data.get("PrimaryHa"),
            QuotaLimitMb=json_data.get("QuotaLimitMb"),
            Redial=json_data.get("Redial"),
            RedundantIntf=json_data.get("RedundantIntf"),
            Roaming=json_data.get("Roaming"),
            Role=json_data.get("Role"),
            SecondaryHa=json_data.get("SecondaryHa"),
            SimPin=json_data.get("SimPin"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            WimaxAuthProtocol=json_data.get("WimaxAuthProtocol"),
            WimaxCarrier=json_data.get("WimaxCarrier"),
            WimaxRealm=json_data.get("WimaxRealm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


