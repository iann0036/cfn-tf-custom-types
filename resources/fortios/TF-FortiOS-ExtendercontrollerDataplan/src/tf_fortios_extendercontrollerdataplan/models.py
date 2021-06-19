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
    Apn: Optional[str]
    AuthType: Optional[str]
    BillingDate: Optional[float]
    Capacity: Optional[float]
    Carrier: Optional[str]
    Iccid: Optional[str]
    Id: Optional[str]
    ModemId: Optional[str]
    MonthlyFee: Optional[float]
    Name: Optional[str]
    Overage: Optional[str]
    Password: Optional[str]
    Pdn: Optional[str]
    PreferredSubnet: Optional[float]
    PrivateNetwork: Optional[str]
    SignalPeriod: Optional[float]
    SignalThreshold: Optional[float]
    Slot: Optional[str]
    Type: Optional[str]
    Username: Optional[str]
    Vdomparam: Optional[str]

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
            Apn=json_data.get("Apn"),
            AuthType=json_data.get("AuthType"),
            BillingDate=json_data.get("BillingDate"),
            Capacity=json_data.get("Capacity"),
            Carrier=json_data.get("Carrier"),
            Iccid=json_data.get("Iccid"),
            Id=json_data.get("Id"),
            ModemId=json_data.get("ModemId"),
            MonthlyFee=json_data.get("MonthlyFee"),
            Name=json_data.get("Name"),
            Overage=json_data.get("Overage"),
            Password=json_data.get("Password"),
            Pdn=json_data.get("Pdn"),
            PreferredSubnet=json_data.get("PreferredSubnet"),
            PrivateNetwork=json_data.get("PrivateNetwork"),
            SignalPeriod=json_data.get("SignalPeriod"),
            SignalThreshold=json_data.get("SignalThreshold"),
            Slot=json_data.get("Slot"),
            Type=json_data.get("Type"),
            Username=json_data.get("Username"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


