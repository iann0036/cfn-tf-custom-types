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
    AlwaysLogErrors: Optional[bool]
    ApiManagementLoggerId: Optional[str]
    ApiManagementName: Optional[str]
    ApiName: Optional[str]
    HttpCorrelationProtocol: Optional[str]
    Id: Optional[str]
    Identifier: Optional[str]
    LogClientIp: Optional[bool]
    ResourceGroupName: Optional[str]
    SamplingPercentage: Optional[float]
    Verbosity: Optional[str]
    BackendRequest: Optional[Sequence["_BackendRequestDefinition"]]
    BackendResponse: Optional[Sequence["_BackendResponseDefinition"]]
    FrontendRequest: Optional[Sequence["_FrontendRequestDefinition"]]
    FrontendResponse: Optional[Sequence["_FrontendResponseDefinition"]]
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
            AlwaysLogErrors=json_data.get("AlwaysLogErrors"),
            ApiManagementLoggerId=json_data.get("ApiManagementLoggerId"),
            ApiManagementName=json_data.get("ApiManagementName"),
            ApiName=json_data.get("ApiName"),
            HttpCorrelationProtocol=json_data.get("HttpCorrelationProtocol"),
            Id=json_data.get("Id"),
            Identifier=json_data.get("Identifier"),
            LogClientIp=json_data.get("LogClientIp"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SamplingPercentage=json_data.get("SamplingPercentage"),
            Verbosity=json_data.get("Verbosity"),
            BackendRequest=deserialize_list(json_data.get("BackendRequest"), BackendRequestDefinition),
            BackendResponse=deserialize_list(json_data.get("BackendResponse"), BackendResponseDefinition),
            FrontendRequest=deserialize_list(json_data.get("FrontendRequest"), FrontendRequestDefinition),
            FrontendResponse=deserialize_list(json_data.get("FrontendResponse"), FrontendResponseDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendRequestDefinition(BaseModel):
    BodyBytes: Optional[float]
    HeadersToLog: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendRequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendRequestDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyBytes=json_data.get("BodyBytes"),
            HeadersToLog=json_data.get("HeadersToLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendRequestDefinition = BackendRequestDefinition


@dataclass
class BackendResponseDefinition(BaseModel):
    BodyBytes: Optional[float]
    HeadersToLog: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyBytes=json_data.get("BodyBytes"),
            HeadersToLog=json_data.get("HeadersToLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendResponseDefinition = BackendResponseDefinition


@dataclass
class FrontendRequestDefinition(BaseModel):
    BodyBytes: Optional[float]
    HeadersToLog: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendRequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendRequestDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyBytes=json_data.get("BodyBytes"),
            HeadersToLog=json_data.get("HeadersToLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendRequestDefinition = FrontendRequestDefinition


@dataclass
class FrontendResponseDefinition(BaseModel):
    BodyBytes: Optional[float]
    HeadersToLog: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FrontendResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrontendResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyBytes=json_data.get("BodyBytes"),
            HeadersToLog=json_data.get("HeadersToLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrontendResponseDefinition = FrontendResponseDefinition


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


