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
    ActivationModes: Optional[Sequence[str]]
    ConcurrentStreamsPerConnection: Optional[float]
    ConnectionIdleTimeout: Optional[float]
    DefaultsFrom: Optional[str]
    EnforceTlsRequirements: Optional[str]
    FrameSize: Optional[float]
    HeaderTableSize: Optional[float]
    Id: Optional[str]
    IncludeContentLength: Optional[str]
    InsertHeader: Optional[str]
    InsertHeaderName: Optional[str]
    Name: Optional[str]
    ReceiveWindow: Optional[float]
    WriteSize: Optional[float]

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
            ActivationModes=json_data.get("ActivationModes"),
            ConcurrentStreamsPerConnection=json_data.get("ConcurrentStreamsPerConnection"),
            ConnectionIdleTimeout=json_data.get("ConnectionIdleTimeout"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            EnforceTlsRequirements=json_data.get("EnforceTlsRequirements"),
            FrameSize=json_data.get("FrameSize"),
            HeaderTableSize=json_data.get("HeaderTableSize"),
            Id=json_data.get("Id"),
            IncludeContentLength=json_data.get("IncludeContentLength"),
            InsertHeader=json_data.get("InsertHeader"),
            InsertHeaderName=json_data.get("InsertHeaderName"),
            Name=json_data.get("Name"),
            ReceiveWindow=json_data.get("ReceiveWindow"),
            WriteSize=json_data.get("WriteSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


