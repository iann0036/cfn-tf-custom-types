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
    ApplicationDescriotion: Optional[str]
    ApplicationName: Optional[str]
    ClusterId: Optional[str]
    Command: Optional[str]
    CommandArgs: Optional[Sequence[str]]
    EdasContainerVersion: Optional[str]
    Envs: Optional[Sequence["_EnvsDefinition"]]
    Id: Optional[str]
    ImageUrl: Optional[str]
    InternetSlbId: Optional[str]
    InternetSlbPort: Optional[float]
    InternetSlbProtocol: Optional[str]
    InternetTargetPort: Optional[float]
    Jdk: Optional[str]
    LimitMCpu: Optional[float]
    LimitMem: Optional[float]
    Liveness: Optional[str]
    LocalVolume: Optional[str]
    LogicalRegionId: Optional[str]
    MountDescs: Optional[str]
    Namespace: Optional[str]
    NasId: Optional[str]
    PackageType: Optional[str]
    PackageUrl: Optional[str]
    PackageVersion: Optional[str]
    PostStart: Optional[str]
    PreStop: Optional[str]
    Readiness: Optional[str]
    Replicas: Optional[float]
    RequestsMCpu: Optional[float]
    RequestsMem: Optional[float]
    WebContainer: Optional[str]
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
            ApplicationDescriotion=json_data.get("ApplicationDescriotion"),
            ApplicationName=json_data.get("ApplicationName"),
            ClusterId=json_data.get("ClusterId"),
            Command=json_data.get("Command"),
            CommandArgs=json_data.get("CommandArgs"),
            EdasContainerVersion=json_data.get("EdasContainerVersion"),
            Envs=deserialize_list(json_data.get("Envs"), EnvsDefinition),
            Id=json_data.get("Id"),
            ImageUrl=json_data.get("ImageUrl"),
            InternetSlbId=json_data.get("InternetSlbId"),
            InternetSlbPort=json_data.get("InternetSlbPort"),
            InternetSlbProtocol=json_data.get("InternetSlbProtocol"),
            InternetTargetPort=json_data.get("InternetTargetPort"),
            Jdk=json_data.get("Jdk"),
            LimitMCpu=json_data.get("LimitMCpu"),
            LimitMem=json_data.get("LimitMem"),
            Liveness=json_data.get("Liveness"),
            LocalVolume=json_data.get("LocalVolume"),
            LogicalRegionId=json_data.get("LogicalRegionId"),
            MountDescs=json_data.get("MountDescs"),
            Namespace=json_data.get("Namespace"),
            NasId=json_data.get("NasId"),
            PackageType=json_data.get("PackageType"),
            PackageUrl=json_data.get("PackageUrl"),
            PackageVersion=json_data.get("PackageVersion"),
            PostStart=json_data.get("PostStart"),
            PreStop=json_data.get("PreStop"),
            Readiness=json_data.get("Readiness"),
            Replicas=json_data.get("Replicas"),
            RequestsMCpu=json_data.get("RequestsMCpu"),
            RequestsMem=json_data.get("RequestsMem"),
            WebContainer=json_data.get("WebContainer"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvsDefinition = EnvsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


