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
    AddressLines: Optional[Sequence[str]]
    BillingCurrency: Optional[str]
    BillingEmails: Optional[Sequence[str]]
    BillingExtraText: Optional[str]
    CardId: Optional[str]
    City: Optional[str]
    Company: Optional[str]
    CountryCode: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    VatId: Optional[str]
    ZipCode: Optional[str]

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
            AddressLines=json_data.get("AddressLines"),
            BillingCurrency=json_data.get("BillingCurrency"),
            BillingEmails=json_data.get("BillingEmails"),
            BillingExtraText=json_data.get("BillingExtraText"),
            CardId=json_data.get("CardId"),
            City=json_data.get("City"),
            Company=json_data.get("Company"),
            CountryCode=json_data.get("CountryCode"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            VatId=json_data.get("VatId"),
            ZipCode=json_data.get("ZipCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


