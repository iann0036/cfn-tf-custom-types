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
    Email: Optional[str]
    Id: Optional[str]
    Restricted: Optional[bool]
    SshKeys: Optional[Sequence[str]]
    TfaEnabled: Optional[bool]
    Username: Optional[str]
    DomainGrant: Optional[Sequence["_DomainGrantDefinition"]]
    GlobalGrants: Optional[Sequence["_GlobalGrantsDefinition"]]
    ImageGrant: Optional[Sequence["_ImageGrantDefinition"]]
    LinodeGrant: Optional[Sequence["_LinodeGrantDefinition"]]
    LongviewGrant: Optional[Sequence["_LongviewGrantDefinition"]]
    NodebalancerGrant: Optional[Sequence["_NodebalancerGrantDefinition"]]
    StackscriptGrant: Optional[Sequence["_StackscriptGrantDefinition"]]
    VolumeGrant: Optional[Sequence["_VolumeGrantDefinition"]]

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
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Restricted=json_data.get("Restricted"),
            SshKeys=json_data.get("SshKeys"),
            TfaEnabled=json_data.get("TfaEnabled"),
            Username=json_data.get("Username"),
            DomainGrant=deserialize_list(json_data.get("DomainGrant"), DomainGrantDefinition),
            GlobalGrants=deserialize_list(json_data.get("GlobalGrants"), GlobalGrantsDefinition),
            ImageGrant=deserialize_list(json_data.get("ImageGrant"), ImageGrantDefinition),
            LinodeGrant=deserialize_list(json_data.get("LinodeGrant"), LinodeGrantDefinition),
            LongviewGrant=deserialize_list(json_data.get("LongviewGrant"), LongviewGrantDefinition),
            NodebalancerGrant=deserialize_list(json_data.get("NodebalancerGrant"), NodebalancerGrantDefinition),
            StackscriptGrant=deserialize_list(json_data.get("StackscriptGrant"), StackscriptGrantDefinition),
            VolumeGrant=deserialize_list(json_data.get("VolumeGrant"), VolumeGrantDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DomainGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainGrantDefinition = DomainGrantDefinition


@dataclass
class GlobalGrantsDefinition(BaseModel):
    AccountAccess: Optional[str]
    AddDomains: Optional[bool]
    AddImages: Optional[bool]
    AddLinodes: Optional[bool]
    AddLongview: Optional[bool]
    AddNodebalancers: Optional[bool]
    AddStackscripts: Optional[bool]
    AddVolumes: Optional[bool]
    CancelAccount: Optional[bool]
    LongviewSubscription: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalGrantsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalGrantsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountAccess=json_data.get("AccountAccess"),
            AddDomains=json_data.get("AddDomains"),
            AddImages=json_data.get("AddImages"),
            AddLinodes=json_data.get("AddLinodes"),
            AddLongview=json_data.get("AddLongview"),
            AddNodebalancers=json_data.get("AddNodebalancers"),
            AddStackscripts=json_data.get("AddStackscripts"),
            AddVolumes=json_data.get("AddVolumes"),
            CancelAccount=json_data.get("CancelAccount"),
            LongviewSubscription=json_data.get("LongviewSubscription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalGrantsDefinition = GlobalGrantsDefinition


@dataclass
class ImageGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageGrantDefinition = ImageGrantDefinition


@dataclass
class LinodeGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinodeGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinodeGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinodeGrantDefinition = LinodeGrantDefinition


@dataclass
class LongviewGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LongviewGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LongviewGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LongviewGrantDefinition = LongviewGrantDefinition


@dataclass
class NodebalancerGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodebalancerGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodebalancerGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodebalancerGrantDefinition = NodebalancerGrantDefinition


@dataclass
class StackscriptGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackscriptGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackscriptGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackscriptGrantDefinition = StackscriptGrantDefinition


@dataclass
class VolumeGrantDefinition(BaseModel):
    Id: Optional[float]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeGrantDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeGrantDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeGrantDefinition = VolumeGrantDefinition


