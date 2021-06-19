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
    CheckSites: Optional[Sequence[float]]
    ExpectedResponse: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    Interval: Optional[str]
    IntervalPolicy: Optional[str]
    Name: Optional[str]
    Resolver: Optional[str]
    VerificationPolicy: Optional[str]

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
            CheckSites=json_data.get("CheckSites"),
            ExpectedResponse=json_data.get("ExpectedResponse"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            IntervalPolicy=json_data.get("IntervalPolicy"),
            Name=json_data.get("Name"),
            Resolver=json_data.get("Resolver"),
            VerificationPolicy=json_data.get("VerificationPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


