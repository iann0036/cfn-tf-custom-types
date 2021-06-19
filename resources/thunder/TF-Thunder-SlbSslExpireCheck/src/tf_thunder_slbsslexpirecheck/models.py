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
    Before: Optional[float]
    ExpireAddress1: Optional[str]
    Id: Optional[str]
    IntervalDays: Optional[float]
    SslExpireEmailAddress: Optional[str]
    Uuid: Optional[str]
    Exception: Optional[Sequence["_ExceptionDefinition"]]

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
            Before=json_data.get("Before"),
            ExpireAddress1=json_data.get("ExpireAddress1"),
            Id=json_data.get("Id"),
            IntervalDays=json_data.get("IntervalDays"),
            SslExpireEmailAddress=json_data.get("SslExpireEmailAddress"),
            Uuid=json_data.get("Uuid"),
            Exception=deserialize_list(json_data.get("Exception"), ExceptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExceptionDefinition(BaseModel):
    Action: Optional[str]
    CertificateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExceptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExceptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CertificateName=json_data.get("CertificateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExceptionDefinition = ExceptionDefinition


