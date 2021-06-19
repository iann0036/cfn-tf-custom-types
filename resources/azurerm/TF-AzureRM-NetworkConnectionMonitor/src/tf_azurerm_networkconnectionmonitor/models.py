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
    AutoStart: Optional[bool]
    Id: Optional[str]
    IntervalInSeconds: Optional[float]
    Location: Optional[str]
    Name: Optional[str]
    NetworkWatcherId: Optional[str]
    Notes: Optional[str]
    OutputWorkspaceResourceIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Endpoint: Optional[Sequence["_EndpointDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
    TestConfiguration: Optional[Sequence["_TestConfigurationDefinition"]]
    TestGroup: Optional[Sequence["_TestGroupDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AutoStart=json_data.get("AutoStart"),
            Id=json_data.get("Id"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkWatcherId=json_data.get("NetworkWatcherId"),
            Notes=json_data.get("Notes"),
            OutputWorkspaceResourceIds=json_data.get("OutputWorkspaceResourceIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            TestConfiguration=deserialize_list(json_data.get("TestConfiguration"), TestConfigurationDefinition),
            TestGroup=deserialize_list(json_data.get("TestGroup"), TestGroupDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class DestinationDefinition(BaseModel):
    Address: Optional[str]
    Port: Optional[float]
    VirtualMachineId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class EndpointDefinition(BaseModel):
    Address: Optional[str]
    CoverageLevel: Optional[str]
    ExcludedIpAddresses: Optional[Sequence[str]]
    IncludedIpAddresses: Optional[Sequence[str]]
    Name: Optional[str]
    TargetResourceId: Optional[str]
    TargetResourceType: Optional[str]
    VirtualMachineId: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            CoverageLevel=json_data.get("CoverageLevel"),
            ExcludedIpAddresses=json_data.get("ExcludedIpAddresses"),
            IncludedIpAddresses=json_data.get("IncludedIpAddresses"),
            Name=json_data.get("Name"),
            TargetResourceId=json_data.get("TargetResourceId"),
            TargetResourceType=json_data.get("TargetResourceType"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class FilterDefinition(BaseModel):
    Type: Optional[str]
    Item: Optional[Sequence["_ItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Item=deserialize_list(json_data.get("Item"), ItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class ItemDefinition(BaseModel):
    Address: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemDefinition = ItemDefinition


@dataclass
class SourceDefinition(BaseModel):
    Port: Optional[float]
    VirtualMachineId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class TestConfigurationDefinition(BaseModel):
    Name: Optional[str]
    PreferredIpVersion: Optional[str]
    Protocol: Optional[str]
    TestFrequencyInSeconds: Optional[float]
    HttpConfiguration: Optional[Sequence["_HttpConfigurationDefinition"]]
    IcmpConfiguration: Optional[Sequence["_IcmpConfigurationDefinition"]]
    SuccessThreshold: Optional[Sequence["_SuccessThresholdDefinition"]]
    TcpConfiguration: Optional[Sequence["_TcpConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TestConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PreferredIpVersion=json_data.get("PreferredIpVersion"),
            Protocol=json_data.get("Protocol"),
            TestFrequencyInSeconds=json_data.get("TestFrequencyInSeconds"),
            HttpConfiguration=deserialize_list(json_data.get("HttpConfiguration"), HttpConfigurationDefinition),
            IcmpConfiguration=deserialize_list(json_data.get("IcmpConfiguration"), IcmpConfigurationDefinition),
            SuccessThreshold=deserialize_list(json_data.get("SuccessThreshold"), SuccessThresholdDefinition),
            TcpConfiguration=deserialize_list(json_data.get("TcpConfiguration"), TcpConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestConfigurationDefinition = TestConfigurationDefinition


@dataclass
class HttpConfigurationDefinition(BaseModel):
    Method: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    PreferHttps: Optional[bool]
    ValidStatusCodeRanges: Optional[Sequence[str]]
    RequestHeader: Optional[Sequence["_RequestHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            PreferHttps=json_data.get("PreferHttps"),
            ValidStatusCodeRanges=json_data.get("ValidStatusCodeRanges"),
            RequestHeader=deserialize_list(json_data.get("RequestHeader"), RequestHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfigurationDefinition = HttpConfigurationDefinition


@dataclass
class RequestHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderDefinition = RequestHeaderDefinition


@dataclass
class IcmpConfigurationDefinition(BaseModel):
    TraceRouteEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            TraceRouteEnabled=json_data.get("TraceRouteEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpConfigurationDefinition = IcmpConfigurationDefinition


@dataclass
class SuccessThresholdDefinition(BaseModel):
    ChecksFailedPercent: Optional[float]
    RoundTripTimeMs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SuccessThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuccessThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            ChecksFailedPercent=json_data.get("ChecksFailedPercent"),
            RoundTripTimeMs=json_data.get("RoundTripTimeMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuccessThresholdDefinition = SuccessThresholdDefinition


@dataclass
class TcpConfigurationDefinition(BaseModel):
    Port: Optional[float]
    TraceRouteEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TcpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            TraceRouteEnabled=json_data.get("TraceRouteEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpConfigurationDefinition = TcpConfigurationDefinition


@dataclass
class TestGroupDefinition(BaseModel):
    DestinationEndpoints: Optional[Sequence[str]]
    Enabled: Optional[bool]
    Name: Optional[str]
    SourceEndpoints: Optional[Sequence[str]]
    TestConfigurationNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TestGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationEndpoints=json_data.get("DestinationEndpoints"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            SourceEndpoints=json_data.get("SourceEndpoints"),
            TestConfigurationNames=json_data.get("TestConfigurationNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestGroupDefinition = TestGroupDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


