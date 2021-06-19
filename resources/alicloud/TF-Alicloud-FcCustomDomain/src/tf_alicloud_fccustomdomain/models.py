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
    AccountId: Optional[str]
    ApiVersion: Optional[str]
    CreatedTime: Optional[str]
    DomainName: Optional[str]
    Id: Optional[str]
    LastModifiedTime: Optional[str]
    Protocol: Optional[str]
    CertConfig: Optional[Sequence["_CertConfigDefinition"]]
    RouteConfig: Optional[Sequence["_RouteConfigDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            ApiVersion=json_data.get("ApiVersion"),
            CreatedTime=json_data.get("CreatedTime"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Protocol=json_data.get("Protocol"),
            CertConfig=deserialize_list(json_data.get("CertConfig"), CertConfigDefinition),
            RouteConfig=deserialize_list(json_data.get("RouteConfig"), RouteConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertConfigDefinition(BaseModel):
    CertName: Optional[str]
    Certificate: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertName=json_data.get("CertName"),
            Certificate=json_data.get("Certificate"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertConfigDefinition = CertConfigDefinition


@dataclass
class RouteConfigDefinition(BaseModel):
    FunctionName: Optional[str]
    Methods: Optional[Sequence[str]]
    Path: Optional[str]
    Qualifier: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionName=json_data.get("FunctionName"),
            Methods=json_data.get("Methods"),
            Path=json_data.get("Path"),
            Qualifier=json_data.get("Qualifier"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteConfigDefinition = RouteConfigDefinition


