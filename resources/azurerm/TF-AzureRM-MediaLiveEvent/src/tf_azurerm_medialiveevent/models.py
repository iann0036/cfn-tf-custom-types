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
    AutoStartEnabled: Optional[bool]
    Description: Optional[str]
    HostnamePrefix: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MediaServicesAccountName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TranscriptionLanguages: Optional[Sequence[str]]
    UseStaticHostname: Optional[bool]
    CrossSiteAccessPolicy: Optional[Sequence["_CrossSiteAccessPolicyDefinition"]]
    Encoding: Optional[Sequence["_EncodingDefinition"]]
    Input: Optional[Sequence["_InputDefinition"]]
    Preview: Optional[Sequence["_PreviewDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AutoStartEnabled=json_data.get("AutoStartEnabled"),
            Description=json_data.get("Description"),
            HostnamePrefix=json_data.get("HostnamePrefix"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MediaServicesAccountName=json_data.get("MediaServicesAccountName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TranscriptionLanguages=json_data.get("TranscriptionLanguages"),
            UseStaticHostname=json_data.get("UseStaticHostname"),
            CrossSiteAccessPolicy=deserialize_list(json_data.get("CrossSiteAccessPolicy"), CrossSiteAccessPolicyDefinition),
            Encoding=deserialize_list(json_data.get("Encoding"), EncodingDefinition),
            Input=deserialize_list(json_data.get("Input"), InputDefinition),
            Preview=deserialize_list(json_data.get("Preview"), PreviewDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class CrossSiteAccessPolicyDefinition(BaseModel):
    ClientAccessPolicy: Optional[str]
    CrossDomainPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrossSiteAccessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossSiteAccessPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientAccessPolicy=json_data.get("ClientAccessPolicy"),
            CrossDomainPolicy=json_data.get("CrossDomainPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossSiteAccessPolicyDefinition = CrossSiteAccessPolicyDefinition


@dataclass
class EncodingDefinition(BaseModel):
    KeyFrameInterval: Optional[str]
    PresetName: Optional[str]
    StretchMode: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncodingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncodingDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyFrameInterval=json_data.get("KeyFrameInterval"),
            PresetName=json_data.get("PresetName"),
            StretchMode=json_data.get("StretchMode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncodingDefinition = EncodingDefinition


@dataclass
class InputDefinition(BaseModel):
    AccessToken: Optional[str]
    KeyFrameIntervalDuration: Optional[str]
    StreamingProtocol: Optional[str]
    IpAccessControlAllow: Optional[Sequence["_IpAccessControlAllowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            KeyFrameIntervalDuration=json_data.get("KeyFrameIntervalDuration"),
            StreamingProtocol=json_data.get("StreamingProtocol"),
            IpAccessControlAllow=deserialize_list(json_data.get("IpAccessControlAllow"), IpAccessControlAllowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinition = InputDefinition


@dataclass
class IpAccessControlAllowDefinition(BaseModel):
    Address: Optional[str]
    Name: Optional[str]
    SubnetPrefixLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpAccessControlAllowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAccessControlAllowDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Name=json_data.get("Name"),
            SubnetPrefixLength=json_data.get("SubnetPrefixLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAccessControlAllowDefinition = IpAccessControlAllowDefinition


@dataclass
class PreviewDefinition(BaseModel):
    AlternativeMediaId: Optional[str]
    PreviewLocator: Optional[str]
    StreamingPolicyName: Optional[str]
    IpAccessControlAllow: Optional[Sequence["_IpAccessControlAllowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreviewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreviewDefinition"]:
        if not json_data:
            return None
        return cls(
            AlternativeMediaId=json_data.get("AlternativeMediaId"),
            PreviewLocator=json_data.get("PreviewLocator"),
            StreamingPolicyName=json_data.get("StreamingPolicyName"),
            IpAccessControlAllow=deserialize_list(json_data.get("IpAccessControlAllow"), IpAccessControlAllowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreviewDefinition = PreviewDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


