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
    Id: Optional[str]
    IsisAdjacencyChange: Optional[float]
    IsisAreaMismatch: Optional[float]
    IsisAttemptToExceedMaxSequence: Optional[float]
    IsisAuthenticationFailure: Optional[float]
    IsisAuthenticationTypeFailure: Optional[float]
    IsisCorruptedLspDetected: Optional[float]
    IsisDatabaseOverload: Optional[float]
    IsisIdLenMismatch: Optional[float]
    IsisLspTooLargeToPropagate: Optional[float]
    IsisManualAddressDrops: Optional[float]
    IsisMaxAreaAddressesMismatch: Optional[float]
    IsisOriginatingLspBufferSizeMismatch: Optional[float]
    IsisOwnLspPurge: Optional[float]
    IsisProtocolsSupportedMismatch: Optional[float]
    IsisRejectedAdjacency: Optional[float]
    IsisSequenceNumberSkip: Optional[float]
    IsisVersionSkew: Optional[float]
    Uuid: Optional[str]

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
            Id=json_data.get("Id"),
            IsisAdjacencyChange=json_data.get("IsisAdjacencyChange"),
            IsisAreaMismatch=json_data.get("IsisAreaMismatch"),
            IsisAttemptToExceedMaxSequence=json_data.get("IsisAttemptToExceedMaxSequence"),
            IsisAuthenticationFailure=json_data.get("IsisAuthenticationFailure"),
            IsisAuthenticationTypeFailure=json_data.get("IsisAuthenticationTypeFailure"),
            IsisCorruptedLspDetected=json_data.get("IsisCorruptedLspDetected"),
            IsisDatabaseOverload=json_data.get("IsisDatabaseOverload"),
            IsisIdLenMismatch=json_data.get("IsisIdLenMismatch"),
            IsisLspTooLargeToPropagate=json_data.get("IsisLspTooLargeToPropagate"),
            IsisManualAddressDrops=json_data.get("IsisManualAddressDrops"),
            IsisMaxAreaAddressesMismatch=json_data.get("IsisMaxAreaAddressesMismatch"),
            IsisOriginatingLspBufferSizeMismatch=json_data.get("IsisOriginatingLspBufferSizeMismatch"),
            IsisOwnLspPurge=json_data.get("IsisOwnLspPurge"),
            IsisProtocolsSupportedMismatch=json_data.get("IsisProtocolsSupportedMismatch"),
            IsisRejectedAdjacency=json_data.get("IsisRejectedAdjacency"),
            IsisSequenceNumberSkip=json_data.get("IsisSequenceNumberSkip"),
            IsisVersionSkew=json_data.get("IsisVersionSkew"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


