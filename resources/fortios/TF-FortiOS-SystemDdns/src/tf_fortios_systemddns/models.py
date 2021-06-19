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
    BoundIp: Optional[str]
    ClearText: Optional[str]
    DdnsAuth: Optional[str]
    DdnsDomain: Optional[str]
    DdnsKey: Optional[str]
    DdnsKeyname: Optional[str]
    DdnsPassword: Optional[str]
    DdnsServer: Optional[str]
    DdnsServerIp: Optional[str]
    DdnsSn: Optional[str]
    DdnsTtl: Optional[float]
    DdnsUsername: Optional[str]
    DdnsZone: Optional[str]
    Ddnsid: Optional[float]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    SslCertificate: Optional[str]
    UpdateInterval: Optional[float]
    UsePublicIp: Optional[str]
    Vdomparam: Optional[str]
    MonitorInterface: Optional[Sequence["_MonitorInterfaceDefinition"]]

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
            BoundIp=json_data.get("BoundIp"),
            ClearText=json_data.get("ClearText"),
            DdnsAuth=json_data.get("DdnsAuth"),
            DdnsDomain=json_data.get("DdnsDomain"),
            DdnsKey=json_data.get("DdnsKey"),
            DdnsKeyname=json_data.get("DdnsKeyname"),
            DdnsPassword=json_data.get("DdnsPassword"),
            DdnsServer=json_data.get("DdnsServer"),
            DdnsServerIp=json_data.get("DdnsServerIp"),
            DdnsSn=json_data.get("DdnsSn"),
            DdnsTtl=json_data.get("DdnsTtl"),
            DdnsUsername=json_data.get("DdnsUsername"),
            DdnsZone=json_data.get("DdnsZone"),
            Ddnsid=json_data.get("Ddnsid"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            SslCertificate=json_data.get("SslCertificate"),
            UpdateInterval=json_data.get("UpdateInterval"),
            UsePublicIp=json_data.get("UsePublicIp"),
            Vdomparam=json_data.get("Vdomparam"),
            MonitorInterface=deserialize_list(json_data.get("MonitorInterface"), MonitorInterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonitorInterfaceDefinition(BaseModel):
    InterfaceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceName=json_data.get("InterfaceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorInterfaceDefinition = MonitorInterfaceDefinition


