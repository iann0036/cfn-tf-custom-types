# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Apis: Optional[Sequence["_Apis"]]
    ConfigId: Optional[str]
    DnsAddress: Optional[str]
    Endpoints: Optional[Sequence["_Endpoints"]]
    GrpcConfig: Optional[str]
    Id: Optional[str]
    OpenapiConfig: Optional[str]
    Project: Optional[str]
    ProtocOutputBase64: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Apis=json_data.get("Apis"),
            ConfigId=json_data.get("ConfigId"),
            DnsAddress=json_data.get("DnsAddress"),
            Endpoints=json_data.get("Endpoints"),
            GrpcConfig=json_data.get("GrpcConfig"),
            Id=json_data.get("Id"),
            OpenapiConfig=json_data.get("OpenapiConfig"),
            Project=json_data.get("Project"),
            ProtocOutputBase64=json_data.get("ProtocOutputBase64"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Apis:
    Methods: Optional[Sequence["_Methods"]]
    Name: Optional[str]
    Syntax: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Apis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Apis"]:
        if not json_data:
            return None
        return cls(
            Methods=json_data.get("Methods"),
            Name=json_data.get("Name"),
            Syntax=json_data.get("Syntax"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Apis = Apis


@dataclass
class Methods:
    Name: Optional[str]
    RequestType: Optional[str]
    ResponseType: Optional[str]
    Syntax: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Methods"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Methods"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RequestType=json_data.get("RequestType"),
            ResponseType=json_data.get("ResponseType"),
            Syntax=json_data.get("Syntax"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Methods = Methods


@dataclass
class Endpoints:
    Address: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoints"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoints = Endpoints


