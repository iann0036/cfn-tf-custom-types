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
    Accessible: Optional[bool]
    AccountId: Optional[float]
    AccountName: Optional[str]
    AccountToken: Optional[str]
    DocSizeSetting: Optional[bool]
    Email: Optional[str]
    Id: Optional[str]
    MaxDailyGb: Optional[float]
    RetentionDays: Optional[float]
    Searchable: Optional[bool]
    SharingObjectsAccounts: Optional[Sequence[float]]
    UtilizationSettings: Optional[Sequence["_UtilizationSettingsDefinition"]]

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
            Accessible=json_data.get("Accessible"),
            AccountId=json_data.get("AccountId"),
            AccountName=json_data.get("AccountName"),
            AccountToken=json_data.get("AccountToken"),
            DocSizeSetting=json_data.get("DocSizeSetting"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            MaxDailyGb=json_data.get("MaxDailyGb"),
            RetentionDays=json_data.get("RetentionDays"),
            Searchable=json_data.get("Searchable"),
            SharingObjectsAccounts=json_data.get("SharingObjectsAccounts"),
            UtilizationSettings=deserialize_list(json_data.get("UtilizationSettings"), UtilizationSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UtilizationSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UtilizationSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UtilizationSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UtilizationSettingsDefinition = UtilizationSettingsDefinition


