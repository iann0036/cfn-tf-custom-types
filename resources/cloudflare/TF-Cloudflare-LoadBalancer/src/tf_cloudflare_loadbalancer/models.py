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
    CreatedOn: Optional[str]
    DefaultPoolIds: Optional[Sequence[str]]
    Description: Optional[str]
    Enabled: Optional[bool]
    FallbackPoolId: Optional[str]
    Id: Optional[str]
    ModifiedOn: Optional[str]
    Name: Optional[str]
    Proxied: Optional[bool]
    SessionAffinity: Optional[str]
    SessionAffinityAttributes: Optional[Sequence["_SessionAffinityAttributesDefinition"]]
    SessionAffinityTtl: Optional[float]
    SteeringPolicy: Optional[str]
    Ttl: Optional[float]
    ZoneId: Optional[str]
    PopPools: Optional[Sequence["_PopPoolsDefinition"]]
    RegionPools: Optional[Sequence["_RegionPoolsDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            CreatedOn=json_data.get("CreatedOn"),
            DefaultPoolIds=json_data.get("DefaultPoolIds"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            FallbackPoolId=json_data.get("FallbackPoolId"),
            Id=json_data.get("Id"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Name=json_data.get("Name"),
            Proxied=json_data.get("Proxied"),
            SessionAffinity=json_data.get("SessionAffinity"),
            SessionAffinityAttributes=deserialize_list(json_data.get("SessionAffinityAttributes"), SessionAffinityAttributesDefinition),
            SessionAffinityTtl=json_data.get("SessionAffinityTtl"),
            SteeringPolicy=json_data.get("SteeringPolicy"),
            Ttl=json_data.get("Ttl"),
            ZoneId=json_data.get("ZoneId"),
            PopPools=deserialize_list(json_data.get("PopPools"), PopPoolsDefinition),
            RegionPools=deserialize_list(json_data.get("RegionPools"), RegionPoolsDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SessionAffinityAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SessionAffinityAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionAffinityAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionAffinityAttributesDefinition = SessionAffinityAttributesDefinition


@dataclass
class PopPoolsDefinition(BaseModel):
    PoolIds: Optional[Sequence[str]]
    Pop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PopPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PopPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            PoolIds=json_data.get("PoolIds"),
            Pop=json_data.get("Pop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PopPoolsDefinition = PopPoolsDefinition


@dataclass
class RegionPoolsDefinition(BaseModel):
    PoolIds: Optional[Sequence[str]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            PoolIds=json_data.get("PoolIds"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionPoolsDefinition = RegionPoolsDefinition


@dataclass
class RulesDefinition(BaseModel):
    Condition: Optional[str]
    Disabled: Optional[bool]
    FixedResponse: Optional[Sequence["_FixedResponseDefinition"]]
    Name: Optional[str]
    Priority: Optional[float]
    Terminates: Optional[bool]
    Overrides: Optional[Sequence["_OverridesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Disabled=json_data.get("Disabled"),
            FixedResponse=deserialize_list(json_data.get("FixedResponse"), FixedResponseDefinition),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Terminates=json_data.get("Terminates"),
            Overrides=deserialize_list(json_data.get("Overrides"), OverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class FixedResponseDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponseDefinition = FixedResponseDefinition


@dataclass
class OverridesDefinition(BaseModel):
    DefaultPools: Optional[Sequence[str]]
    FallbackPool: Optional[str]
    SessionAffinity: Optional[str]
    SessionAffinityAttributes: Optional[Sequence["_SessionAffinityAttributesDefinition2"]]
    SessionAffinityTtl: Optional[float]
    SteeringPolicy: Optional[str]
    Ttl: Optional[float]
    PopPools: Optional[Sequence["_PopPoolsDefinition"]]
    RegionPools: Optional[Sequence["_RegionPoolsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultPools=json_data.get("DefaultPools"),
            FallbackPool=json_data.get("FallbackPool"),
            SessionAffinity=json_data.get("SessionAffinity"),
            SessionAffinityAttributes=deserialize_list(json_data.get("SessionAffinityAttributes"), SessionAffinityAttributesDefinition2),
            SessionAffinityTtl=json_data.get("SessionAffinityTtl"),
            SteeringPolicy=json_data.get("SteeringPolicy"),
            Ttl=json_data.get("Ttl"),
            PopPools=deserialize_list(json_data.get("PopPools"), PopPoolsDefinition),
            RegionPools=deserialize_list(json_data.get("RegionPools"), RegionPoolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverridesDefinition = OverridesDefinition


@dataclass
class SessionAffinityAttributesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SessionAffinityAttributesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionAffinityAttributesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionAffinityAttributesDefinition2 = SessionAffinityAttributesDefinition2


