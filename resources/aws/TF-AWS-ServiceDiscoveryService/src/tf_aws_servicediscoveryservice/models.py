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
    Arn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamespaceId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    DnsConfig: Optional[Sequence["_DnsConfigDefinition"]]
    HealthCheckConfig: Optional[Sequence["_HealthCheckConfigDefinition"]]
    HealthCheckCustomConfig: Optional[Sequence["_HealthCheckCustomConfigDefinition"]]

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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            DnsConfig=deserialize_list(json_data.get("DnsConfig"), DnsConfigDefinition),
            HealthCheckConfig=deserialize_list(json_data.get("HealthCheckConfig"), HealthCheckConfigDefinition),
            HealthCheckCustomConfig=deserialize_list(json_data.get("HealthCheckCustomConfig"), HealthCheckCustomConfigDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class DnsConfigDefinition(BaseModel):
    NamespaceId: Optional[str]
    RoutingPolicy: Optional[str]
    DnsRecords: Optional[Sequence["_DnsRecordsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NamespaceId=json_data.get("NamespaceId"),
            RoutingPolicy=json_data.get("RoutingPolicy"),
            DnsRecords=deserialize_list(json_data.get("DnsRecords"), DnsRecordsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigDefinition = DnsConfigDefinition


@dataclass
class DnsRecordsDefinition(BaseModel):
    Ttl: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsRecordsDefinition = DnsRecordsDefinition


@dataclass
class HealthCheckConfigDefinition(BaseModel):
    FailureThreshold: Optional[float]
    ResourcePath: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            ResourcePath=json_data.get("ResourcePath"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfigDefinition = HealthCheckConfigDefinition


@dataclass
class HealthCheckCustomConfigDefinition(BaseModel):
    FailureThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckCustomConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckCustomConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckCustomConfigDefinition = HealthCheckCustomConfigDefinition


