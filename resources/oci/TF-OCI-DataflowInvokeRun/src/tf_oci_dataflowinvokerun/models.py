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
    ApplicationId: Optional[str]
    ArchiveUri: Optional[str]
    Arguments: Optional[Sequence[str]]
    Asynchronous: Optional[bool]
    ClassName: Optional[str]
    CompartmentId: Optional[str]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    DataReadInBytes: Optional[str]
    DataWrittenInBytes: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    DriverShape: Optional[str]
    Execute: Optional[str]
    ExecutorShape: Optional[str]
    FileUri: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    Language: Optional[str]
    LifecycleDetails: Optional[str]
    LogsBucketUri: Optional[str]
    NumExecutors: Optional[float]
    OpcRequestId: Optional[str]
    OwnerPrincipalId: Optional[str]
    OwnerUserName: Optional[str]
    PrivateEndpointDnsZones: Optional[Sequence[str]]
    PrivateEndpointId: Optional[str]
    PrivateEndpointMaxHostCount: Optional[float]
    PrivateEndpointNsgIds: Optional[Sequence[str]]
    PrivateEndpointSubnetId: Optional[str]
    RunDurationInMilliseconds: Optional[str]
    SparkVersion: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    TotalOcpu: Optional[float]
    WarehouseBucketUri: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
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
            ApplicationId=json_data.get("ApplicationId"),
            ArchiveUri=json_data.get("ArchiveUri"),
            Arguments=json_data.get("Arguments"),
            Asynchronous=json_data.get("Asynchronous"),
            ClassName=json_data.get("ClassName"),
            CompartmentId=json_data.get("CompartmentId"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            DataReadInBytes=json_data.get("DataReadInBytes"),
            DataWrittenInBytes=json_data.get("DataWrittenInBytes"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            DriverShape=json_data.get("DriverShape"),
            Execute=json_data.get("Execute"),
            ExecutorShape=json_data.get("ExecutorShape"),
            FileUri=json_data.get("FileUri"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            Language=json_data.get("Language"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            LogsBucketUri=json_data.get("LogsBucketUri"),
            NumExecutors=json_data.get("NumExecutors"),
            OpcRequestId=json_data.get("OpcRequestId"),
            OwnerPrincipalId=json_data.get("OwnerPrincipalId"),
            OwnerUserName=json_data.get("OwnerUserName"),
            PrivateEndpointDnsZones=json_data.get("PrivateEndpointDnsZones"),
            PrivateEndpointId=json_data.get("PrivateEndpointId"),
            PrivateEndpointMaxHostCount=json_data.get("PrivateEndpointMaxHostCount"),
            PrivateEndpointNsgIds=json_data.get("PrivateEndpointNsgIds"),
            PrivateEndpointSubnetId=json_data.get("PrivateEndpointSubnetId"),
            RunDurationInMilliseconds=json_data.get("RunDurationInMilliseconds"),
            SparkVersion=json_data.get("SparkVersion"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TotalOcpu=json_data.get("TotalOcpu"),
            WarehouseBucketUri=json_data.get("WarehouseBucketUri"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


