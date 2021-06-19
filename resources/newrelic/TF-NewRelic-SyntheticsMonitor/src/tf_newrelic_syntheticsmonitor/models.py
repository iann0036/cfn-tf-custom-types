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
    BypassHeadRequest: Optional[bool]
    Frequency: Optional[float]
    Id: Optional[str]
    Locations: Optional[Sequence[str]]
    Name: Optional[str]
    SlaThreshold: Optional[float]
    Status: Optional[str]
    TreatRedirectAsFailure: Optional[bool]
    Type: Optional[str]
    Uri: Optional[str]
    ValidationString: Optional[str]
    VerifySsl: Optional[bool]

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
            BypassHeadRequest=json_data.get("BypassHeadRequest"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Locations=json_data.get("Locations"),
            Name=json_data.get("Name"),
            SlaThreshold=json_data.get("SlaThreshold"),
            Status=json_data.get("Status"),
            TreatRedirectAsFailure=json_data.get("TreatRedirectAsFailure"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
            ValidationString=json_data.get("ValidationString"),
            VerifySsl=json_data.get("VerifySsl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


