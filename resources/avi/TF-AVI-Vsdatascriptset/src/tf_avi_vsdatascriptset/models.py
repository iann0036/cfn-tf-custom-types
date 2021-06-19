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
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpReputationDbRef: Optional[str]
    IpgroupRefs: Optional[Sequence[str]]
    Name: Optional[str]
    PoolGroupRefs: Optional[Sequence[str]]
    PoolRefs: Optional[Sequence[str]]
    ProtocolParserRefs: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Datascript: Optional[Sequence["_DatascriptDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    RateLimiters: Optional[Sequence["_RateLimitersDefinition"]]

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
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpReputationDbRef=json_data.get("IpReputationDbRef"),
            IpgroupRefs=json_data.get("IpgroupRefs"),
            Name=json_data.get("Name"),
            PoolGroupRefs=json_data.get("PoolGroupRefs"),
            PoolRefs=json_data.get("PoolRefs"),
            ProtocolParserRefs=json_data.get("ProtocolParserRefs"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Datascript=deserialize_list(json_data.get("Datascript"), DatascriptDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            RateLimiters=deserialize_list(json_data.get("RateLimiters"), RateLimitersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DatascriptDefinition(BaseModel):
    Evt: Optional[str]
    Script: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatascriptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatascriptDefinition"]:
        if not json_data:
            return None
        return cls(
            Evt=json_data.get("Evt"),
            Script=json_data.get("Script"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatascriptDefinition = DatascriptDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class RateLimitersDefinition(BaseModel):
    BurstSz: Optional[float]
    Count: Optional[float]
    Name: Optional[str]
    Period: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitersDefinition"]:
        if not json_data:
            return None
        return cls(
            BurstSz=json_data.get("BurstSz"),
            Count=json_data.get("Count"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitersDefinition = RateLimitersDefinition


