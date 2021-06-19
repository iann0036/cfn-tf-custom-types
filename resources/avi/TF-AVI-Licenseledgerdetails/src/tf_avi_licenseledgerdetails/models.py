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
    Id: Optional[str]
    Uuid: Optional[str]
    EscrowInfos: Optional[Sequence["_EscrowInfosDefinition"]]
    SeInfos: Optional[Sequence["_SeInfosDefinition"]]
    TierUsages: Optional[Sequence["_TierUsagesDefinition"]]

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
            Id=json_data.get("Id"),
            Uuid=json_data.get("Uuid"),
            EscrowInfos=deserialize_list(json_data.get("EscrowInfos"), EscrowInfosDefinition),
            SeInfos=deserialize_list(json_data.get("SeInfos"), SeInfosDefinition),
            TierUsages=deserialize_list(json_data.get("TierUsages"), TierUsagesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EscrowInfosDefinition(BaseModel):
    LastUpdated: Optional[float]
    ServiceCores: Optional[float]
    TenantUuid: Optional[str]
    Tier: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EscrowInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscrowInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            LastUpdated=json_data.get("LastUpdated"),
            ServiceCores=json_data.get("ServiceCores"),
            TenantUuid=json_data.get("TenantUuid"),
            Tier=json_data.get("Tier"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscrowInfosDefinition = EscrowInfosDefinition


@dataclass
class SeInfosDefinition(BaseModel):
    LastUpdated: Optional[float]
    ServiceCores: Optional[float]
    TenantUuid: Optional[str]
    Tier: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            LastUpdated=json_data.get("LastUpdated"),
            ServiceCores=json_data.get("ServiceCores"),
            TenantUuid=json_data.get("TenantUuid"),
            Tier=json_data.get("Tier"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeInfosDefinition = SeInfosDefinition


@dataclass
class TierUsagesDefinition(BaseModel):
    Tier: Optional[str]
    Usage: Optional[Sequence["_UsageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TierUsagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TierUsagesDefinition"]:
        if not json_data:
            return None
        return cls(
            Tier=json_data.get("Tier"),
            Usage=deserialize_list(json_data.get("Usage"), UsageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TierUsagesDefinition = TierUsagesDefinition


@dataclass
class UsageDefinition(BaseModel):
    Available: Optional[float]
    Consumed: Optional[float]
    Escrow: Optional[float]
    Remaining: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UsageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsageDefinition"]:
        if not json_data:
            return None
        return cls(
            Available=json_data.get("Available"),
            Consumed=json_data.get("Consumed"),
            Escrow=json_data.get("Escrow"),
            Remaining=json_data.get("Remaining"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsageDefinition = UsageDefinition


