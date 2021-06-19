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
    AwsAccountId: Optional[str]
    AwsEndpointServiceId: Optional[str]
    AwsVpcEndpointId: Optional[str]
    Id: Optional[str]
    Region: Optional[str]
    State: Optional[str]
    UseCase: Optional[str]
    VpcEndpointId: Optional[str]
    VpcEndpointName: Optional[str]

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
            AwsAccountId=json_data.get("AwsAccountId"),
            AwsEndpointServiceId=json_data.get("AwsEndpointServiceId"),
            AwsVpcEndpointId=json_data.get("AwsVpcEndpointId"),
            Id=json_data.get("Id"),
            Region=json_data.get("Region"),
            State=json_data.get("State"),
            UseCase=json_data.get("UseCase"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcEndpointName=json_data.get("VpcEndpointName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


