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
    AccountId: Optional[str]
    Arn: Optional[str]
    BudgetType: Optional[str]
    CostFilters: Optional[Sequence["_CostFiltersDefinition"]]
    Id: Optional[str]
    LimitAmount: Optional[str]
    LimitUnit: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    TimePeriodEnd: Optional[str]
    TimePeriodStart: Optional[str]
    TimeUnit: Optional[str]
    CostTypes: Optional[Sequence["_CostTypesDefinition"]]
    Notification: Optional[Sequence["_NotificationDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            Arn=json_data.get("Arn"),
            BudgetType=json_data.get("BudgetType"),
            CostFilters=deserialize_list(json_data.get("CostFilters"), CostFiltersDefinition),
            Id=json_data.get("Id"),
            LimitAmount=json_data.get("LimitAmount"),
            LimitUnit=json_data.get("LimitUnit"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            TimePeriodEnd=json_data.get("TimePeriodEnd"),
            TimePeriodStart=json_data.get("TimePeriodStart"),
            TimeUnit=json_data.get("TimeUnit"),
            CostTypes=deserialize_list(json_data.get("CostTypes"), CostTypesDefinition),
            Notification=deserialize_list(json_data.get("Notification"), NotificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CostFiltersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CostFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CostFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CostFiltersDefinition = CostFiltersDefinition


@dataclass
class CostTypesDefinition(BaseModel):
    IncludeCredit: Optional[bool]
    IncludeDiscount: Optional[bool]
    IncludeOtherSubscription: Optional[bool]
    IncludeRecurring: Optional[bool]
    IncludeRefund: Optional[bool]
    IncludeSubscription: Optional[bool]
    IncludeSupport: Optional[bool]
    IncludeTax: Optional[bool]
    IncludeUpfront: Optional[bool]
    UseAmortized: Optional[bool]
    UseBlended: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CostTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CostTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeCredit=json_data.get("IncludeCredit"),
            IncludeDiscount=json_data.get("IncludeDiscount"),
            IncludeOtherSubscription=json_data.get("IncludeOtherSubscription"),
            IncludeRecurring=json_data.get("IncludeRecurring"),
            IncludeRefund=json_data.get("IncludeRefund"),
            IncludeSubscription=json_data.get("IncludeSubscription"),
            IncludeSupport=json_data.get("IncludeSupport"),
            IncludeTax=json_data.get("IncludeTax"),
            IncludeUpfront=json_data.get("IncludeUpfront"),
            UseAmortized=json_data.get("UseAmortized"),
            UseBlended=json_data.get("UseBlended"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CostTypesDefinition = CostTypesDefinition


@dataclass
class NotificationDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    NotificationType: Optional[str]
    SubscriberEmailAddresses: Optional[Sequence[str]]
    SubscriberSnsTopicArns: Optional[Sequence[str]]
    Threshold: Optional[float]
    ThresholdType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            NotificationType=json_data.get("NotificationType"),
            SubscriberEmailAddresses=json_data.get("SubscriberEmailAddresses"),
            SubscriberSnsTopicArns=json_data.get("SubscriberSnsTopicArns"),
            Threshold=json_data.get("Threshold"),
            ThresholdType=json_data.get("ThresholdType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationDefinition = NotificationDefinition


