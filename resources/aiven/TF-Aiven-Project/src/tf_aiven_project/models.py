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
    AvailableCredits: Optional[str]
    BillingAddress: Optional[str]
    BillingCurrency: Optional[str]
    BillingEmails: Optional[Sequence[str]]
    BillingExtraText: Optional[str]
    BillingGroup: Optional[str]
    CaCert: Optional[str]
    CardId: Optional[str]
    CopyFromProject: Optional[str]
    Country: Optional[str]
    CountryCode: Optional[str]
    DefaultCloud: Optional[str]
    EstimatedBalance: Optional[str]
    Id: Optional[str]
    PaymentMethod: Optional[str]
    Project: Optional[str]
    TechnicalEmails: Optional[Sequence[str]]
    VatId: Optional[str]

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
            AvailableCredits=json_data.get("AvailableCredits"),
            BillingAddress=json_data.get("BillingAddress"),
            BillingCurrency=json_data.get("BillingCurrency"),
            BillingEmails=json_data.get("BillingEmails"),
            BillingExtraText=json_data.get("BillingExtraText"),
            BillingGroup=json_data.get("BillingGroup"),
            CaCert=json_data.get("CaCert"),
            CardId=json_data.get("CardId"),
            CopyFromProject=json_data.get("CopyFromProject"),
            Country=json_data.get("Country"),
            CountryCode=json_data.get("CountryCode"),
            DefaultCloud=json_data.get("DefaultCloud"),
            EstimatedBalance=json_data.get("EstimatedBalance"),
            Id=json_data.get("Id"),
            PaymentMethod=json_data.get("PaymentMethod"),
            Project=json_data.get("Project"),
            TechnicalEmails=json_data.get("TechnicalEmails"),
            VatId=json_data.get("VatId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


