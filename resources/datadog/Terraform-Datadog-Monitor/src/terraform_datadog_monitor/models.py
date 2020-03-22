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
    EnableLogsSample: Optional[bool]
    EscalationMessage: Optional[str]
    EvaluationDelay: Optional[float]
    Id: Optional[str]
    IncludeTags: Optional[bool]
    Locked: Optional[bool]
    Message: Optional[str]
    Name: Optional[str]
    NewHostDelay: Optional[float]
    NoDataTimeframe: Optional[float]
    NotifyAudit: Optional[bool]
    NotifyNoData: Optional[bool]
    Query: Optional[str]
    RenotifyInterval: Optional[float]
    RequireFullWindow: Optional[bool]
    Silenced: Optional[Sequence["_Silenced"]]
    Tags: Optional[Sequence[str]]
    ThresholdWindows: Optional[Sequence["_ThresholdWindows"]]
    Thresholds: Optional[Sequence["_Thresholds"]]
    TimeoutH: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EnableLogsSample=json_data.get("EnableLogsSample"),
            EscalationMessage=json_data.get("EscalationMessage"),
            EvaluationDelay=json_data.get("EvaluationDelay"),
            Id=json_data.get("Id"),
            IncludeTags=json_data.get("IncludeTags"),
            Locked=json_data.get("Locked"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            NewHostDelay=json_data.get("NewHostDelay"),
            NoDataTimeframe=json_data.get("NoDataTimeframe"),
            NotifyAudit=json_data.get("NotifyAudit"),
            NotifyNoData=json_data.get("NotifyNoData"),
            Query=json_data.get("Query"),
            RenotifyInterval=json_data.get("RenotifyInterval"),
            RequireFullWindow=json_data.get("RequireFullWindow"),
            Silenced=json_data.get("Silenced"),
            Tags=json_data.get("Tags"),
            ThresholdWindows=json_data.get("ThresholdWindows"),
            Thresholds=json_data.get("Thresholds"),
            TimeoutH=json_data.get("TimeoutH"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Silenced:
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Silenced"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Silenced"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Silenced = Silenced


@dataclass
class ThresholdWindows:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdWindows"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdWindows"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdWindows = ThresholdWindows


@dataclass
class Thresholds:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Thresholds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Thresholds"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Thresholds = Thresholds


