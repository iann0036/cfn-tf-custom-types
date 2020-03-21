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
    AllowOverwrite: Optional[bool]
    Fqdn: Optional[str]
    HealthCheckId: Optional[str]
    MultivalueAnswerRoutingPolicy: Optional[bool]
    Name: Optional[str]
    Records: Optional[Sequence[str]]
    SetIdentifier: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    ZoneId: Optional[str]
    Alias: Optional[Sequence["_Alias"]]
    FailoverRoutingPolicy: Optional[Sequence["_FailoverRoutingPolicy"]]
    GeolocationRoutingPolicy: Optional[Sequence["_GeolocationRoutingPolicy"]]
    LatencyRoutingPolicy: Optional[Sequence["_LatencyRoutingPolicy"]]
    WeightedRoutingPolicy: Optional[Sequence["_WeightedRoutingPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowOverwrite=json_data.get("AllowOverwrite"),
            Fqdn=json_data.get("Fqdn"),
            HealthCheckId=json_data.get("HealthCheckId"),
            MultivalueAnswerRoutingPolicy=json_data.get("MultivalueAnswerRoutingPolicy"),
            Name=json_data.get("Name"),
            Records=json_data.get("Records"),
            SetIdentifier=json_data.get("SetIdentifier"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            ZoneId=json_data.get("ZoneId"),
            Alias=json_data.get("Alias"),
            FailoverRoutingPolicy=json_data.get("FailoverRoutingPolicy"),
            GeolocationRoutingPolicy=json_data.get("GeolocationRoutingPolicy"),
            LatencyRoutingPolicy=json_data.get("LatencyRoutingPolicy"),
            WeightedRoutingPolicy=json_data.get("WeightedRoutingPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Alias:
    EvaluateTargetHealth: Optional[bool]
    Name: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alias"]:
        if not json_data:
            return None
        return cls(
            EvaluateTargetHealth=json_data.get("EvaluateTargetHealth"),
            Name=json_data.get("Name"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alias = Alias


@dataclass
class FailoverRoutingPolicy:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverRoutingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverRoutingPolicy"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverRoutingPolicy = FailoverRoutingPolicy


@dataclass
class GeolocationRoutingPolicy:
    Continent: Optional[str]
    Country: Optional[str]
    Subdivision: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeolocationRoutingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeolocationRoutingPolicy"]:
        if not json_data:
            return None
        return cls(
            Continent=json_data.get("Continent"),
            Country=json_data.get("Country"),
            Subdivision=json_data.get("Subdivision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeolocationRoutingPolicy = GeolocationRoutingPolicy


@dataclass
class LatencyRoutingPolicy:
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LatencyRoutingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LatencyRoutingPolicy"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LatencyRoutingPolicy = LatencyRoutingPolicy


@dataclass
class WeightedRoutingPolicy:
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedRoutingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedRoutingPolicy"]:
        if not json_data:
            return None
        return cls(
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedRoutingPolicy = WeightedRoutingPolicy


