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
    AggregatorName: Optional[str]
    AggregatorType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Status: Optional[str]
    AggregatorAccounts: Optional[Sequence["_AggregatorAccountsDefinition"]]
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
            AggregatorName=json_data.get("AggregatorName"),
            AggregatorType=json_data.get("AggregatorType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
            AggregatorAccounts=deserialize_list(json_data.get("AggregatorAccounts"), AggregatorAccountsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AggregatorAccountsDefinition(BaseModel):
    AccountId: Optional[str]
    AccountName: Optional[str]
    AccountType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregatorAccountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregatorAccountsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AccountName=json_data.get("AccountName"),
            AccountType=json_data.get("AccountType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregatorAccountsDefinition = AggregatorAccountsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


