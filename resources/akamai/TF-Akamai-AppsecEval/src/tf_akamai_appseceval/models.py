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
    ConfigId: Optional[float]
    CurrentRuleset: Optional[str]
    EvalOperation: Optional[str]
    EvalStatus: Optional[str]
    EvaluatingRuleset: Optional[str]
    ExpirationDate: Optional[str]
    Id: Optional[str]
    OutputText: Optional[str]
    SecurityPolicyId: Optional[str]
    Version: Optional[float]

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
            ConfigId=json_data.get("ConfigId"),
            CurrentRuleset=json_data.get("CurrentRuleset"),
            EvalOperation=json_data.get("EvalOperation"),
            EvalStatus=json_data.get("EvalStatus"),
            EvaluatingRuleset=json_data.get("EvaluatingRuleset"),
            ExpirationDate=json_data.get("ExpirationDate"),
            Id=json_data.get("Id"),
            OutputText=json_data.get("OutputText"),
            SecurityPolicyId=json_data.get("SecurityPolicyId"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


