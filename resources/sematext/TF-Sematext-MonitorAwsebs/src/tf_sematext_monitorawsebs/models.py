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
    AwsAccessKey: Optional[str]
    AwsFetchFrequency: Optional[str]
    AwsRegion: Optional[str]
    AwsSecretKey: Optional[str]
    BillingPlanId: Optional[float]
    DiscountCode: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ScApptokenEntries: Optional[Sequence["_ScApptokenEntriesDefinition"]]
    Apptoken: Optional[Sequence["_ApptokenDefinition"]]

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
            AwsAccessKey=json_data.get("AwsAccessKey"),
            AwsFetchFrequency=json_data.get("AwsFetchFrequency"),
            AwsRegion=json_data.get("AwsRegion"),
            AwsSecretKey=json_data.get("AwsSecretKey"),
            BillingPlanId=json_data.get("BillingPlanId"),
            DiscountCode=json_data.get("DiscountCode"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ScApptokenEntries=deserialize_list(json_data.get("ScApptokenEntries"), ScApptokenEntriesDefinition),
            Apptoken=deserialize_list(json_data.get("Apptoken"), ApptokenDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScApptokenEntriesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScApptokenEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScApptokenEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScApptokenEntriesDefinition = ScApptokenEntriesDefinition


@dataclass
class ApptokenDefinition(BaseModel):
    Names: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ApptokenDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApptokenDefinition"]:
        if not json_data:
            return None
        return cls(
            Names=json_data.get("Names"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApptokenDefinition = ApptokenDefinition


