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
    ApproveValue: Optional[str]
    AuditMode: Optional[str]
    AuditReason: Optional[str]
    DesireValue: Optional[float]
    EffectiveTime: Optional[str]
    ExpireTime: Optional[str]
    Id: Optional[str]
    NoticeType: Optional[float]
    ProductCode: Optional[str]
    QuotaActionCode: Optional[str]
    QuotaCategory: Optional[str]
    QuotaDescription: Optional[str]
    QuotaName: Optional[str]
    QuotaUnit: Optional[str]
    Reason: Optional[str]
    Status: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]

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
            ApproveValue=json_data.get("ApproveValue"),
            AuditMode=json_data.get("AuditMode"),
            AuditReason=json_data.get("AuditReason"),
            DesireValue=json_data.get("DesireValue"),
            EffectiveTime=json_data.get("EffectiveTime"),
            ExpireTime=json_data.get("ExpireTime"),
            Id=json_data.get("Id"),
            NoticeType=json_data.get("NoticeType"),
            ProductCode=json_data.get("ProductCode"),
            QuotaActionCode=json_data.get("QuotaActionCode"),
            QuotaCategory=json_data.get("QuotaCategory"),
            QuotaDescription=json_data.get("QuotaDescription"),
            QuotaName=json_data.get("QuotaName"),
            QuotaUnit=json_data.get("QuotaUnit"),
            Reason=json_data.get("Reason"),
            Status=json_data.get("Status"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DimensionsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


