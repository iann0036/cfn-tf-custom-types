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
    Arguments: Optional[Sequence["_ArgumentsDefinition"]]
    Arn: Optional[str]
    AvailabilityZone: Optional[str]
    ExtraJarsS3Path: Optional[str]
    ExtraPythonLibsS3Path: Optional[str]
    FailureReason: Optional[str]
    GlueVersion: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NumberOfNodes: Optional[float]
    NumberOfWorkers: Optional[float]
    PrivateAddress: Optional[str]
    PublicAddress: Optional[str]
    PublicKey: Optional[str]
    PublicKeys: Optional[Sequence[str]]
    RoleArn: Optional[str]
    SecurityConfiguration: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Status: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
    WorkerType: Optional[str]
    YarnEndpointAddress: Optional[str]
    ZeppelinRemoteSparkInterpreterPort: Optional[float]

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
            Arguments=deserialize_list(json_data.get("Arguments"), ArgumentsDefinition),
            Arn=json_data.get("Arn"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ExtraJarsS3Path=json_data.get("ExtraJarsS3Path"),
            ExtraPythonLibsS3Path=json_data.get("ExtraPythonLibsS3Path"),
            FailureReason=json_data.get("FailureReason"),
            GlueVersion=json_data.get("GlueVersion"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            PrivateAddress=json_data.get("PrivateAddress"),
            PublicAddress=json_data.get("PublicAddress"),
            PublicKey=json_data.get("PublicKey"),
            PublicKeys=json_data.get("PublicKeys"),
            RoleArn=json_data.get("RoleArn"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            WorkerType=json_data.get("WorkerType"),
            YarnEndpointAddress=json_data.get("YarnEndpointAddress"),
            ZeppelinRemoteSparkInterpreterPort=json_data.get("ZeppelinRemoteSparkInterpreterPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ArgumentsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArgumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgumentsDefinition = ArgumentsDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


