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
    Action: Optional[str]
    Adom: Optional[str]
    ApplicationList: Optional[Sequence[str]]
    AvProfile: Optional[Sequence[str]]
    CapturePacket: Optional[str]
    Comments: Optional[str]
    DnsfilterProfile: Optional[Sequence[str]]
    Dstaddr: Optional[Sequence[str]]
    Dstintf: Optional[Sequence[str]]
    Fixedport: Optional[str]
    Fsso: Optional[str]
    Groups: Optional[Sequence[str]]
    Id: Optional[str]
    Inbound: Optional[str]
    InternetService: Optional[str]
    InternetServiceId: Optional[Sequence[str]]
    InternetServiceName: Optional[Sequence[str]]
    InternetServiceSrc: Optional[str]
    InternetServiceSrcId: Optional[Sequence[str]]
    InternetServiceSrcName: Optional[Sequence[str]]
    Ippool: Optional[str]
    IpsSensor: Optional[Sequence[str]]
    Logtraffic: Optional[str]
    LogtrafficStart: Optional[str]
    Name: Optional[str]
    Nat: Optional[str]
    PackageName: Optional[str]
    PerIpShaper: Optional[Sequence[str]]
    Poolname: Optional[Sequence[str]]
    ProfileGroup: Optional[Sequence[str]]
    ProfileProtocolOptions: Optional[Sequence[str]]
    ProfileType: Optional[str]
    Rsso: Optional[str]
    Schedule: Optional[Sequence[str]]
    Service: Optional[Sequence[str]]
    Srcaddr: Optional[Sequence[str]]
    Srcintf: Optional[Sequence[str]]
    TrafficShaper: Optional[Sequence[str]]
    TrafficShaperReverse: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]
    UtmStatus: Optional[str]
    VpnTunnel: Optional[Sequence[str]]
    WafProfile: Optional[Sequence[str]]
    WebfilterProfile: Optional[Sequence[str]]

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
            Action=json_data.get("Action"),
            Adom=json_data.get("Adom"),
            ApplicationList=json_data.get("ApplicationList"),
            AvProfile=json_data.get("AvProfile"),
            CapturePacket=json_data.get("CapturePacket"),
            Comments=json_data.get("Comments"),
            DnsfilterProfile=json_data.get("DnsfilterProfile"),
            Dstaddr=json_data.get("Dstaddr"),
            Dstintf=json_data.get("Dstintf"),
            Fixedport=json_data.get("Fixedport"),
            Fsso=json_data.get("Fsso"),
            Groups=json_data.get("Groups"),
            Id=json_data.get("Id"),
            Inbound=json_data.get("Inbound"),
            InternetService=json_data.get("InternetService"),
            InternetServiceId=json_data.get("InternetServiceId"),
            InternetServiceName=json_data.get("InternetServiceName"),
            InternetServiceSrc=json_data.get("InternetServiceSrc"),
            InternetServiceSrcId=json_data.get("InternetServiceSrcId"),
            InternetServiceSrcName=json_data.get("InternetServiceSrcName"),
            Ippool=json_data.get("Ippool"),
            IpsSensor=json_data.get("IpsSensor"),
            Logtraffic=json_data.get("Logtraffic"),
            LogtrafficStart=json_data.get("LogtrafficStart"),
            Name=json_data.get("Name"),
            Nat=json_data.get("Nat"),
            PackageName=json_data.get("PackageName"),
            PerIpShaper=json_data.get("PerIpShaper"),
            Poolname=json_data.get("Poolname"),
            ProfileGroup=json_data.get("ProfileGroup"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            ProfileType=json_data.get("ProfileType"),
            Rsso=json_data.get("Rsso"),
            Schedule=json_data.get("Schedule"),
            Service=json_data.get("Service"),
            Srcaddr=json_data.get("Srcaddr"),
            Srcintf=json_data.get("Srcintf"),
            TrafficShaper=json_data.get("TrafficShaper"),
            TrafficShaperReverse=json_data.get("TrafficShaperReverse"),
            Users=json_data.get("Users"),
            UtmStatus=json_data.get("UtmStatus"),
            VpnTunnel=json_data.get("VpnTunnel"),
            WafProfile=json_data.get("WafProfile"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


