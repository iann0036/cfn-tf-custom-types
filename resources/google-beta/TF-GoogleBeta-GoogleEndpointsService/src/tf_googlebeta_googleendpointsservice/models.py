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
    Apis: Optional[Sequence["_ApisDefinition2"]]
    ConfigId: Optional[str]
    DnsAddress: Optional[str]
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]
    GrpcConfig: Optional[str]
    Id: Optional[str]
    OpenapiConfig: Optional[str]
    Project: Optional[str]
    ProtocOutputBase64: Optional[str]
    ServiceName: Optional[str]
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
            Apis=deserialize_list(json_data.get("Apis"), ApisDefinition2),
            ConfigId=json_data.get("ConfigId"),
            DnsAddress=json_data.get("DnsAddress"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
            GrpcConfig=json_data.get("GrpcConfig"),
            Id=json_data.get("Id"),
            OpenapiConfig=json_data.get("OpenapiConfig"),
            Project=json_data.get("Project"),
            ProtocOutputBase64=json_data.get("ProtocOutputBase64"),
            ServiceName=json_data.get("ServiceName"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApisDefinition2(BaseModel):
    Methods: Optional[Sequence["_ApisDefinition"]]
    Name: Optional[str]
    Syntax: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApisDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApisDefinition2"]:
        if not json_data:
            return None
        return cls(
            Methods=deserialize_list(json_data.get("Methods"), ApisDefinition),
            Name=json_data.get("Name"),
            Syntax=json_data.get("Syntax"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApisDefinition2 = ApisDefinition2


@dataclass
class ApisDefinition(BaseModel):
    Name: Optional[str]
    RequestType: Optional[str]
    ResponseType: Optional[str]
    Syntax: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApisDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RequestType=json_data.get("RequestType"),
            ResponseType=json_data.get("ResponseType"),
            Syntax=json_data.get("Syntax"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApisDefinition = ApisDefinition


@dataclass
class EndpointsDefinition(BaseModel):
    Address: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


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


