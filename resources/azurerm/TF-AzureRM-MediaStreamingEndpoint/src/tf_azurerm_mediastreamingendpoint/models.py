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
    CdnEnabled: Optional[bool]
    CdnProfile: Optional[str]
    CdnProvider: Optional[str]
    CustomHostNames: Optional[Sequence[str]]
    Description: Optional[str]
    HostName: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MaxCacheAgeSeconds: Optional[float]
    MediaServicesAccountName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ScaleUnits: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AccessControl: Optional[Sequence["_AccessControlDefinition"]]
    CrossSiteAccessPolicy: Optional[Sequence["_CrossSiteAccessPolicyDefinition"]]
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
            CdnEnabled=json_data.get("CdnEnabled"),
            CdnProfile=json_data.get("CdnProfile"),
            CdnProvider=json_data.get("CdnProvider"),
            CustomHostNames=json_data.get("CustomHostNames"),
            Description=json_data.get("Description"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaxCacheAgeSeconds=json_data.get("MaxCacheAgeSeconds"),
            MediaServicesAccountName=json_data.get("MediaServicesAccountName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScaleUnits=json_data.get("ScaleUnits"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AccessControl=deserialize_list(json_data.get("AccessControl"), AccessControlDefinition),
            CrossSiteAccessPolicy=deserialize_list(json_data.get("CrossSiteAccessPolicy"), CrossSiteAccessPolicyDefinition),
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
class AccessControlDefinition(BaseModel):
    AkamaiSignatureHeaderAuthenticationKey: Optional[Sequence["_AkamaiSignatureHeaderAuthenticationKeyDefinition"]]
    IpAllow: Optional[Sequence["_IpAllowDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlDefinition"]:
        if not json_data:
            return None
        return cls(
            AkamaiSignatureHeaderAuthenticationKey=deserialize_list(json_data.get("AkamaiSignatureHeaderAuthenticationKey"), AkamaiSignatureHeaderAuthenticationKeyDefinition),
            IpAllow=deserialize_list(json_data.get("IpAllow"), IpAllowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlDefinition = AccessControlDefinition


@dataclass
class AkamaiSignatureHeaderAuthenticationKeyDefinition(BaseModel):
    Base64Key: Optional[str]
    Expiration: Optional[str]
    Identifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AkamaiSignatureHeaderAuthenticationKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AkamaiSignatureHeaderAuthenticationKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Base64Key=json_data.get("Base64Key"),
            Expiration=json_data.get("Expiration"),
            Identifier=json_data.get("Identifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AkamaiSignatureHeaderAuthenticationKeyDefinition = AkamaiSignatureHeaderAuthenticationKeyDefinition


@dataclass
class IpAllowDefinition(BaseModel):
    Address: Optional[str]
    Name: Optional[str]
    SubnetPrefixLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpAllowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAllowDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Name=json_data.get("Name"),
            SubnetPrefixLength=json_data.get("SubnetPrefixLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAllowDefinition = IpAllowDefinition


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


