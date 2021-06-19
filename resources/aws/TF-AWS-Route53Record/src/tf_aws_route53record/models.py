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
    AllowOverwrite: Optional[bool]
    Fqdn: Optional[str]
    HealthCheckId: Optional[str]
    Id: Optional[str]
    MultivalueAnswerRoutingPolicy: Optional[bool]
    Name: Optional[str]
    Records: Optional[Sequence[str]]
    SetIdentifier: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    ZoneId: Optional[str]
    Alias: Optional[Sequence["_AliasDefinition"]]
    FailoverRoutingPolicy: Optional[Sequence["_FailoverRoutingPolicyDefinition"]]
    GeolocationRoutingPolicy: Optional[Sequence["_GeolocationRoutingPolicyDefinition"]]
    LatencyRoutingPolicy: Optional[Sequence["_LatencyRoutingPolicyDefinition"]]
    WeightedRoutingPolicy: Optional[Sequence["_WeightedRoutingPolicyDefinition"]]

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
            AllowOverwrite=json_data.get("AllowOverwrite"),
            Fqdn=json_data.get("Fqdn"),
            HealthCheckId=json_data.get("HealthCheckId"),
            Id=json_data.get("Id"),
            MultivalueAnswerRoutingPolicy=json_data.get("MultivalueAnswerRoutingPolicy"),
            Name=json_data.get("Name"),
            Records=json_data.get("Records"),
            SetIdentifier=json_data.get("SetIdentifier"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            ZoneId=json_data.get("ZoneId"),
            Alias=deserialize_list(json_data.get("Alias"), AliasDefinition),
            FailoverRoutingPolicy=deserialize_list(json_data.get("FailoverRoutingPolicy"), FailoverRoutingPolicyDefinition),
            GeolocationRoutingPolicy=deserialize_list(json_data.get("GeolocationRoutingPolicy"), GeolocationRoutingPolicyDefinition),
            LatencyRoutingPolicy=deserialize_list(json_data.get("LatencyRoutingPolicy"), LatencyRoutingPolicyDefinition),
            WeightedRoutingPolicy=deserialize_list(json_data.get("WeightedRoutingPolicy"), WeightedRoutingPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AliasDefinition(BaseModel):
    EvaluateTargetHealth: Optional[bool]
    Name: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AliasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluateTargetHealth=json_data.get("EvaluateTargetHealth"),
            Name=json_data.get("Name"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasDefinition = AliasDefinition


@dataclass
class FailoverRoutingPolicyDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverRoutingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverRoutingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverRoutingPolicyDefinition = FailoverRoutingPolicyDefinition


@dataclass
class GeolocationRoutingPolicyDefinition(BaseModel):
    Continent: Optional[str]
    Country: Optional[str]
    Subdivision: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeolocationRoutingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeolocationRoutingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Continent=json_data.get("Continent"),
            Country=json_data.get("Country"),
            Subdivision=json_data.get("Subdivision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeolocationRoutingPolicyDefinition = GeolocationRoutingPolicyDefinition


@dataclass
class LatencyRoutingPolicyDefinition(BaseModel):
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LatencyRoutingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LatencyRoutingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LatencyRoutingPolicyDefinition = LatencyRoutingPolicyDefinition


@dataclass
class WeightedRoutingPolicyDefinition(BaseModel):
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedRoutingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedRoutingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedRoutingPolicyDefinition = WeightedRoutingPolicyDefinition


