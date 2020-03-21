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
    Adjustable: Optional[bool]
    Arn: Optional[str]
    DefaultValue: Optional[float]
    QuotaCode: Optional[str]
    QuotaName: Optional[str]
    RequestId: Optional[str]
    RequestStatus: Optional[str]
    ServiceCode: Optional[str]
    ServiceName: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Adjustable=json_data.get("Adjustable"),
            Arn=json_data.get("Arn"),
            DefaultValue=json_data.get("DefaultValue"),
            QuotaCode=json_data.get("QuotaCode"),
            QuotaName=json_data.get("QuotaName"),
            RequestId=json_data.get("RequestId"),
            RequestStatus=json_data.get("RequestStatus"),
            ServiceCode=json_data.get("ServiceCode"),
            ServiceName=json_data.get("ServiceName"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


