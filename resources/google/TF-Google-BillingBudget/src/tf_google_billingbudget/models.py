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
    BillingAccount: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    AllUpdatesRule: Optional[Sequence["_AllUpdatesRuleDefinition"]]
    Amount: Optional[Sequence["_AmountDefinition"]]
    BudgetFilter: Optional[Sequence["_BudgetFilterDefinition"]]
    ThresholdRules: Optional[Sequence["_ThresholdRulesDefinition"]]
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
            BillingAccount=json_data.get("BillingAccount"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            AllUpdatesRule=deserialize_list(json_data.get("AllUpdatesRule"), AllUpdatesRuleDefinition),
            Amount=deserialize_list(json_data.get("Amount"), AmountDefinition),
            BudgetFilter=deserialize_list(json_data.get("BudgetFilter"), BudgetFilterDefinition),
            ThresholdRules=deserialize_list(json_data.get("ThresholdRules"), ThresholdRulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllUpdatesRuleDefinition(BaseModel):
    DisableDefaultIamRecipients: Optional[bool]
    MonitoringNotificationChannels: Optional[Sequence[str]]
    PubsubTopic: Optional[str]
    SchemaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllUpdatesRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllUpdatesRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableDefaultIamRecipients=json_data.get("DisableDefaultIamRecipients"),
            MonitoringNotificationChannels=json_data.get("MonitoringNotificationChannels"),
            PubsubTopic=json_data.get("PubsubTopic"),
            SchemaVersion=json_data.get("SchemaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllUpdatesRuleDefinition = AllUpdatesRuleDefinition


@dataclass
class AmountDefinition(BaseModel):
    LastPeriodAmount: Optional[bool]
    SpecifiedAmount: Optional[Sequence["_SpecifiedAmountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AmountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmountDefinition"]:
        if not json_data:
            return None
        return cls(
            LastPeriodAmount=json_data.get("LastPeriodAmount"),
            SpecifiedAmount=deserialize_list(json_data.get("SpecifiedAmount"), SpecifiedAmountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmountDefinition = AmountDefinition


@dataclass
class SpecifiedAmountDefinition(BaseModel):
    CurrencyCode: Optional[str]
    Nanos: Optional[float]
    Units: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpecifiedAmountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecifiedAmountDefinition"]:
        if not json_data:
            return None
        return cls(
            CurrencyCode=json_data.get("CurrencyCode"),
            Nanos=json_data.get("Nanos"),
            Units=json_data.get("Units"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecifiedAmountDefinition = SpecifiedAmountDefinition


@dataclass
class BudgetFilterDefinition(BaseModel):
    CreditTypes: Optional[Sequence[str]]
    CreditTypesTreatment: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Projects: Optional[Sequence[str]]
    Services: Optional[Sequence[str]]
    Subaccounts: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BudgetFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BudgetFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            CreditTypes=json_data.get("CreditTypes"),
            CreditTypesTreatment=json_data.get("CreditTypesTreatment"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Projects=json_data.get("Projects"),
            Services=json_data.get("Services"),
            Subaccounts=json_data.get("Subaccounts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BudgetFilterDefinition = BudgetFilterDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ThresholdRulesDefinition(BaseModel):
    SpendBasis: Optional[str]
    ThresholdPercent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            SpendBasis=json_data.get("SpendBasis"),
            ThresholdPercent=json_data.get("ThresholdPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdRulesDefinition = ThresholdRulesDefinition


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


