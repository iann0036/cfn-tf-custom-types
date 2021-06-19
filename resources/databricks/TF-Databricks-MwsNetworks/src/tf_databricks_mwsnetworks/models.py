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
    CreationTime: Optional[float]
    Id: Optional[str]
    NetworkId: Optional[str]
    NetworkName: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]
    VpcStatus: Optional[str]
    WorkspaceId: Optional[float]
    ErrorMessages: Optional[Sequence["_ErrorMessagesDefinition"]]
    VpcEndpoints: Optional[Sequence["_VpcEndpointsDefinition"]]

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
            CreationTime=json_data.get("CreationTime"),
            Id=json_data.get("Id"),
            NetworkId=json_data.get("NetworkId"),
            NetworkName=json_data.get("NetworkName"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
            VpcStatus=json_data.get("VpcStatus"),
            WorkspaceId=json_data.get("WorkspaceId"),
            ErrorMessages=deserialize_list(json_data.get("ErrorMessages"), ErrorMessagesDefinition),
            VpcEndpoints=deserialize_list(json_data.get("VpcEndpoints"), VpcEndpointsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ErrorMessagesDefinition(BaseModel):
    ErrorMessage: Optional[str]
    ErrorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorMessagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorMessagesDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorMessage=json_data.get("ErrorMessage"),
            ErrorType=json_data.get("ErrorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ErrorMessagesDefinition = ErrorMessagesDefinition


@dataclass
class VpcEndpointsDefinition(BaseModel):
    DataplaneRelay: Optional[Sequence[str]]
    RestApi: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcEndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcEndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            DataplaneRelay=json_data.get("DataplaneRelay"),
            RestApi=json_data.get("RestApi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcEndpointsDefinition = VpcEndpointsDefinition


