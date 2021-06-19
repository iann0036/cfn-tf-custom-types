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
    Account: Optional[str]
    Attributes: Optional[str]
    Description: Optional[str]
    ErrorReason: Optional[str]
    File: Optional[str]
    Hypervisor: Optional[Sequence["_HypervisorDefinition"]]
    Id: Optional[str]
    ImageFormat: Optional[str]
    Name: Optional[str]
    NoUpload: Optional[bool]
    Platform: Optional[str]
    State: Optional[str]
    Uri: Optional[str]

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
            Account=json_data.get("Account"),
            Attributes=json_data.get("Attributes"),
            Description=json_data.get("Description"),
            ErrorReason=json_data.get("ErrorReason"),
            File=json_data.get("File"),
            Hypervisor=deserialize_list(json_data.get("Hypervisor"), HypervisorDefinition),
            Id=json_data.get("Id"),
            ImageFormat=json_data.get("ImageFormat"),
            Name=json_data.get("Name"),
            NoUpload=json_data.get("NoUpload"),
            Platform=json_data.get("Platform"),
            State=json_data.get("State"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HypervisorDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HypervisorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HypervisorDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HypervisorDefinition = HypervisorDefinition


