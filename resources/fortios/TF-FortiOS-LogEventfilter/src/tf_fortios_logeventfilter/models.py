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
    Cifs: Optional[str]
    ComplianceCheck: Optional[str]
    Connector: Optional[str]
    Endpoint: Optional[str]
    Event: Optional[str]
    Fortiextender: Optional[str]
    Ha: Optional[str]
    Id: Optional[str]
    Router: Optional[str]
    Sdwan: Optional[str]
    SecurityRating: Optional[str]
    SwitchController: Optional[str]
    System: Optional[str]
    User: Optional[str]
    Vdomparam: Optional[str]
    Vpn: Optional[str]
    WanOpt: Optional[str]
    WirelessActivity: Optional[str]

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
            Cifs=json_data.get("Cifs"),
            ComplianceCheck=json_data.get("ComplianceCheck"),
            Connector=json_data.get("Connector"),
            Endpoint=json_data.get("Endpoint"),
            Event=json_data.get("Event"),
            Fortiextender=json_data.get("Fortiextender"),
            Ha=json_data.get("Ha"),
            Id=json_data.get("Id"),
            Router=json_data.get("Router"),
            Sdwan=json_data.get("Sdwan"),
            SecurityRating=json_data.get("SecurityRating"),
            SwitchController=json_data.get("SwitchController"),
            System=json_data.get("System"),
            User=json_data.get("User"),
            Vdomparam=json_data.get("Vdomparam"),
            Vpn=json_data.get("Vpn"),
            WanOpt=json_data.get("WanOpt"),
            WirelessActivity=json_data.get("WirelessActivity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


