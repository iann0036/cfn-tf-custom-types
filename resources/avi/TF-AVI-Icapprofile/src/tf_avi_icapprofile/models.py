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
    Allow204: Optional[bool]
    BufferSize: Optional[float]
    BufferSizeExceedAction: Optional[str]
    CloudRef: Optional[str]
    Description: Optional[str]
    EnablePreview: Optional[bool]
    FailAction: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PoolGroupRef: Optional[str]
    PreviewSize: Optional[float]
    ResponseTimeout: Optional[float]
    ServiceUri: Optional[str]
    SlowResponseWarningThreshold: Optional[float]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Vendor: Optional[str]

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
            Allow204=json_data.get("Allow204"),
            BufferSize=json_data.get("BufferSize"),
            BufferSizeExceedAction=json_data.get("BufferSizeExceedAction"),
            CloudRef=json_data.get("CloudRef"),
            Description=json_data.get("Description"),
            EnablePreview=json_data.get("EnablePreview"),
            FailAction=json_data.get("FailAction"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PoolGroupRef=json_data.get("PoolGroupRef"),
            PreviewSize=json_data.get("PreviewSize"),
            ResponseTimeout=json_data.get("ResponseTimeout"),
            ServiceUri=json_data.get("ServiceUri"),
            SlowResponseWarningThreshold=json_data.get("SlowResponseWarningThreshold"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


