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
    GroupId: Optional[float]
    Id: Optional[str]
    Receivers: Optional[Sequence["_ReceiversDefinition"]]

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
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            Receivers=deserialize_list(json_data.get("Receivers"), ReceiversDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReceiversDefinition(BaseModel):
    EndTime: Optional[float]
    NotifyWay: Optional[Sequence[str]]
    ReceiveLanguage: Optional[str]
    ReceiverGroupList: Optional[Sequence[float]]
    ReceiverType: Optional[str]
    ReceiverUserList: Optional[Sequence[float]]
    StartTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReceiversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReceiversDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            NotifyWay=json_data.get("NotifyWay"),
            ReceiveLanguage=json_data.get("ReceiveLanguage"),
            ReceiverGroupList=json_data.get("ReceiverGroupList"),
            ReceiverType=json_data.get("ReceiverType"),
            ReceiverUserList=json_data.get("ReceiverUserList"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReceiversDefinition = ReceiversDefinition


