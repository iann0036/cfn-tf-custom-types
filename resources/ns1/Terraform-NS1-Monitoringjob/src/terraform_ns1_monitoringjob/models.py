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
    Active: Optional[bool]
    Config: Optional[Sequence["_Config"]]
    Frequency: Optional[float]
    Id: Optional[str]
    JobType: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    NotifyDelay: Optional[float]
    NotifyFailback: Optional[bool]
    NotifyList: Optional[str]
    NotifyRegional: Optional[bool]
    NotifyRepeat: Optional[float]
    Policy: Optional[str]
    RapidRecheck: Optional[bool]
    Regions: Optional[Sequence[str]]
    Rules: Optional[Sequence["_Rules"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Active=json_data.get("Active"),
            Config=json_data.get("Config"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            JobType=json_data.get("JobType"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            NotifyDelay=json_data.get("NotifyDelay"),
            NotifyFailback=json_data.get("NotifyFailback"),
            NotifyList=json_data.get("NotifyList"),
            NotifyRegional=json_data.get("NotifyRegional"),
            NotifyRepeat=json_data.get("NotifyRepeat"),
            Policy=json_data.get("Policy"),
            RapidRecheck=json_data.get("RapidRecheck"),
            Regions=json_data.get("Regions"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Config:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Rules:
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


