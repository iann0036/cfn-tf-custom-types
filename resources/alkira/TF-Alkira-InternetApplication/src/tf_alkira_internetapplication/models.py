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
    BillingTags: Optional[Sequence[float]]
    ConnectorId: Optional[str]
    ConnectorType: Optional[str]
    FqdnPrefix: Optional[str]
    GroupId: Optional[float]
    Id: Optional[str]
    InternetApplicationId: Optional[float]
    Name: Optional[str]
    PrivateIp: Optional[str]
    PrivatePort: Optional[str]
    Segment: Optional[str]
    Size: Optional[str]

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
            BillingTags=json_data.get("BillingTags"),
            ConnectorId=json_data.get("ConnectorId"),
            ConnectorType=json_data.get("ConnectorType"),
            FqdnPrefix=json_data.get("FqdnPrefix"),
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            InternetApplicationId=json_data.get("InternetApplicationId"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            PrivatePort=json_data.get("PrivatePort"),
            Segment=json_data.get("Segment"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


