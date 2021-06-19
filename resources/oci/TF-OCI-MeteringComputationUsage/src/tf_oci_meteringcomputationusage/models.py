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
    CompartmentDepth: Optional[float]
    Filter: Optional[str]
    Granularity: Optional[str]
    GroupBy: Optional[Sequence[str]]
    Id: Optional[str]
    IsAggregateByTime: Optional[bool]
    Items: Optional[Sequence["_ItemsDefinition2"]]
    QueryType: Optional[str]
    TenantId: Optional[str]
    TimeUsageEnded: Optional[str]
    TimeUsageStarted: Optional[str]
    Forecast: Optional[Sequence["_ForecastDefinition"]]
    GroupByTag: Optional[Sequence["_GroupByTagDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentDepth=json_data.get("CompartmentDepth"),
            Filter=json_data.get("Filter"),
            Granularity=json_data.get("Granularity"),
            GroupBy=json_data.get("GroupBy"),
            Id=json_data.get("Id"),
            IsAggregateByTime=json_data.get("IsAggregateByTime"),
            Items=deserialize_list(json_data.get("Items"), ItemsDefinition2),
            QueryType=json_data.get("QueryType"),
            TenantId=json_data.get("TenantId"),
            TimeUsageEnded=json_data.get("TimeUsageEnded"),
            TimeUsageStarted=json_data.get("TimeUsageStarted"),
            Forecast=deserialize_list(json_data.get("Forecast"), ForecastDefinition),
            GroupByTag=deserialize_list(json_data.get("GroupByTag"), GroupByTagDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ItemsDefinition2(BaseModel):
    Ad: Optional[str]
    CompartmentId: Optional[str]
    CompartmentName: Optional[str]
    CompartmentPath: Optional[str]
    ComputedAmount: Optional[float]
    ComputedQuantity: Optional[float]
    Currency: Optional[str]
    Discount: Optional[float]
    IsForecast: Optional[bool]
    ListRate: Optional[float]
    Overage: Optional[str]
    OveragesFlag: Optional[str]
    Platform: Optional[str]
    Region: Optional[str]
    ResourceId: Optional[str]
    ResourceName: Optional[str]
    Service: Optional[str]
    Shape: Optional[str]
    SkuName: Optional[str]
    SkuPartNumber: Optional[str]
    SubscriptionId: Optional[str]
    Tags: Optional[Sequence["_ItemsDefinition"]]
    TenantId: Optional[str]
    TenantName: Optional[str]
    TimeUsageEnded: Optional[str]
    TimeUsageStarted: Optional[str]
    Unit: Optional[str]
    UnitPrice: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Ad=json_data.get("Ad"),
            CompartmentId=json_data.get("CompartmentId"),
            CompartmentName=json_data.get("CompartmentName"),
            CompartmentPath=json_data.get("CompartmentPath"),
            ComputedAmount=json_data.get("ComputedAmount"),
            ComputedQuantity=json_data.get("ComputedQuantity"),
            Currency=json_data.get("Currency"),
            Discount=json_data.get("Discount"),
            IsForecast=json_data.get("IsForecast"),
            ListRate=json_data.get("ListRate"),
            Overage=json_data.get("Overage"),
            OveragesFlag=json_data.get("OveragesFlag"),
            Platform=json_data.get("Platform"),
            Region=json_data.get("Region"),
            ResourceId=json_data.get("ResourceId"),
            ResourceName=json_data.get("ResourceName"),
            Service=json_data.get("Service"),
            Shape=json_data.get("Shape"),
            SkuName=json_data.get("SkuName"),
            SkuPartNumber=json_data.get("SkuPartNumber"),
            SubscriptionId=json_data.get("SubscriptionId"),
            Tags=deserialize_list(json_data.get("Tags"), ItemsDefinition),
            TenantId=json_data.get("TenantId"),
            TenantName=json_data.get("TenantName"),
            TimeUsageEnded=json_data.get("TimeUsageEnded"),
            TimeUsageStarted=json_data.get("TimeUsageStarted"),
            Unit=json_data.get("Unit"),
            UnitPrice=json_data.get("UnitPrice"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsDefinition2 = ItemsDefinition2


@dataclass
class ItemsDefinition(BaseModel):
    Key: Optional[str]
    Namespace: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Namespace=json_data.get("Namespace"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsDefinition = ItemsDefinition


@dataclass
class ForecastDefinition(BaseModel):
    ForecastType: Optional[str]
    TimeForecastEnded: Optional[str]
    TimeForecastStarted: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForecastDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForecastDefinition"]:
        if not json_data:
            return None
        return cls(
            ForecastType=json_data.get("ForecastType"),
            TimeForecastEnded=json_data.get("TimeForecastEnded"),
            TimeForecastStarted=json_data.get("TimeForecastStarted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForecastDefinition = ForecastDefinition


@dataclass
class GroupByTagDefinition(BaseModel):
    Key: Optional[str]
    Namespace: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupByTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupByTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Namespace=json_data.get("Namespace"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupByTagDefinition = GroupByTagDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


