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
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    CurrentPrice: Optional[float]
    Id: Optional[str]
    Kubeconfig: Optional[str]
    Labels: Optional[Sequence[str]]
    ListenPort: Optional[Sequence["_ListenPortDefinition"]]
    Name: Optional[str]
    NetworkUuid: Optional[str]
    Password: Optional[str]
    SecurityZoneUuid: Optional[str]
    ServiceTemplateUuid: Optional[str]
    ServiceTemplateUuidComputed: Optional[str]
    Status: Optional[str]
    UsageInMinute: Optional[float]
    Username: Optional[str]
    Parameter: Optional[Sequence["_ParameterDefinition"]]
    ResourceLimit: Optional[Sequence["_ResourceLimitDefinition"]]
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
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            CurrentPrice=json_data.get("CurrentPrice"),
            Id=json_data.get("Id"),
            Kubeconfig=json_data.get("Kubeconfig"),
            Labels=json_data.get("Labels"),
            ListenPort=deserialize_list(json_data.get("ListenPort"), ListenPortDefinition),
            Name=json_data.get("Name"),
            NetworkUuid=json_data.get("NetworkUuid"),
            Password=json_data.get("Password"),
            SecurityZoneUuid=json_data.get("SecurityZoneUuid"),
            ServiceTemplateUuid=json_data.get("ServiceTemplateUuid"),
            ServiceTemplateUuidComputed=json_data.get("ServiceTemplateUuidComputed"),
            Status=json_data.get("Status"),
            UsageInMinute=json_data.get("UsageInMinute"),
            Username=json_data.get("Username"),
            Parameter=deserialize_list(json_data.get("Parameter"), ParameterDefinition),
            ResourceLimit=deserialize_list(json_data.get("ResourceLimit"), ResourceLimitDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ListenPortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListenPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenPortDefinition = ListenPortDefinition


@dataclass
class ParameterDefinition(BaseModel):
    Param: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            Param=json_data.get("Param"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDefinition = ParameterDefinition


@dataclass
class ResourceLimitDefinition(BaseModel):
    Limit: Optional[float]
    Resource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceLimitDefinition = ResourceLimitDefinition


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


