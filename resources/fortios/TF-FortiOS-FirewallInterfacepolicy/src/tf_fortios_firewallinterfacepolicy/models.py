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
    AddressType: Optional[str]
    ApplicationList: Optional[str]
    ApplicationListStatus: Optional[str]
    AvProfile: Optional[str]
    AvProfileStatus: Optional[str]
    Comments: Optional[str]
    DlpSensor: Optional[str]
    DlpSensorStatus: Optional[str]
    Dsri: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailfilterProfile: Optional[str]
    EmailfilterProfileStatus: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    IpsSensor: Optional[str]
    IpsSensorStatus: Optional[str]
    Label: Optional[str]
    Logtraffic: Optional[str]
    Policyid: Optional[float]
    ScanBotnetConnections: Optional[str]
    SpamfilterProfile: Optional[str]
    SpamfilterProfileStatus: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    WebfilterProfile: Optional[str]
    WebfilterProfileStatus: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]

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
            AddressType=json_data.get("AddressType"),
            ApplicationList=json_data.get("ApplicationList"),
            ApplicationListStatus=json_data.get("ApplicationListStatus"),
            AvProfile=json_data.get("AvProfile"),
            AvProfileStatus=json_data.get("AvProfileStatus"),
            Comments=json_data.get("Comments"),
            DlpSensor=json_data.get("DlpSensor"),
            DlpSensorStatus=json_data.get("DlpSensorStatus"),
            Dsri=json_data.get("Dsri"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            EmailfilterProfileStatus=json_data.get("EmailfilterProfileStatus"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpsSensor=json_data.get("IpsSensor"),
            IpsSensorStatus=json_data.get("IpsSensorStatus"),
            Label=json_data.get("Label"),
            Logtraffic=json_data.get("Logtraffic"),
            Policyid=json_data.get("Policyid"),
            ScanBotnetConnections=json_data.get("ScanBotnetConnections"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SpamfilterProfileStatus=json_data.get("SpamfilterProfileStatus"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebfilterProfileStatus=json_data.get("WebfilterProfileStatus"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


