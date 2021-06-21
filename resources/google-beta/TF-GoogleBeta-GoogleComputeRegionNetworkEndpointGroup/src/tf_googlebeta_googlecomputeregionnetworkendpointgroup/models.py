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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NetworkEndpointType: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    AppEngine: Optional[Sequence["_AppEngineDefinition"]]
    CloudFunction: Optional[Sequence["_CloudFunctionDefinition"]]
    CloudRun: Optional[Sequence["_CloudRunDefinition"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkEndpointType=json_data.get("NetworkEndpointType"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            AppEngine=deserialize_list(json_data.get("AppEngine"), AppEngineDefinition),
            CloudFunction=deserialize_list(json_data.get("CloudFunction"), CloudFunctionDefinition),
            CloudRun=deserialize_list(json_data.get("CloudRun"), CloudRunDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppEngineDefinition(BaseModel):
    Service: Optional[str]
    UrlMask: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppEngineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppEngineDefinition"]:
        if not json_data:
            return None
        return cls(
            Service=json_data.get("Service"),
            UrlMask=json_data.get("UrlMask"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppEngineDefinition = AppEngineDefinition


@dataclass
class CloudFunctionDefinition(BaseModel):
    Function: Optional[str]
    UrlMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudFunctionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudFunctionDefinition"]:
        if not json_data:
            return None
        return cls(
            Function=json_data.get("Function"),
            UrlMask=json_data.get("UrlMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudFunctionDefinition = CloudFunctionDefinition


@dataclass
class CloudRunDefinition(BaseModel):
    Service: Optional[str]
    Tag: Optional[str]
    UrlMask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudRunDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudRunDefinition"]:
        if not json_data:
            return None
        return cls(
            Service=json_data.get("Service"),
            Tag=json_data.get("Tag"),
            UrlMask=json_data.get("UrlMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudRunDefinition = CloudRunDefinition


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

