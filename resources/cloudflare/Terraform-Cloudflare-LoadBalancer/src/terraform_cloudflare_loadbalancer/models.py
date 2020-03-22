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
    SteeringPolicy: Optional[str]
    Ttl: Optional[float]
    ZoneId: Optional[str]
    PopPools: Optional[Sequence["_PopPools"]]
    RegionPools: Optional[Sequence["_RegionPools"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            SteeringPolicy=json_data.get("SteeringPolicy"),
            Ttl=json_data.get("Ttl"),
            ZoneId=json_data.get("ZoneId"),
            PopPools=json_data.get("PopPools"),
            RegionPools=json_data.get("RegionPools"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PopPools:
    PoolIds: Optional[Sequence[str]]
    Pop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PopPools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PopPools"]:
        if not json_data:
            return None
        return cls(
            PoolIds=json_data.get("PoolIds"),
            Pop=json_data.get("Pop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PopPools = PopPools


@dataclass
class RegionPools:
    PoolIds: Optional[Sequence[str]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionPools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionPools"]:
        if not json_data:
            return None
        return cls(
            PoolIds=json_data.get("PoolIds"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionPools = RegionPools


