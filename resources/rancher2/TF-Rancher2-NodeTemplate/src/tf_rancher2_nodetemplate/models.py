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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    AuthCertificateAuthority: Optional[str]
    AuthKey: Optional[str]
    CloudCredentialId: Optional[str]
    Description: Optional[str]
    Driver: Optional[str]
    DriverId: Optional[str]
    EngineEnv: Optional[Sequence["_EngineEnvDefinition"]]
    EngineInsecureRegistry: Optional[Sequence[str]]
    EngineInstallUrl: Optional[str]
    EngineLabel: Optional[Sequence["_EngineLabelDefinition"]]
    EngineOpt: Optional[Sequence["_EngineOptDefinition"]]
    EngineRegistryMirror: Optional[Sequence[str]]
    EngineStorageDriver: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    UseInternalIpAddress: Optional[bool]
    Amazonec2Config: Optional[Sequence["_Amazonec2ConfigDefinition"]]
    AzureConfig: Optional[Sequence["_AzureConfigDefinition"]]
    DigitaloceanConfig: Optional[Sequence["_DigitaloceanConfigDefinition"]]
    HetznerConfig: Optional[Sequence["_HetznerConfigDefinition"]]
    LinodeConfig: Optional[Sequence["_LinodeConfigDefinition"]]
    NodeTaints: Optional[Sequence["_NodeTaintsDefinition"]]
    OpennebulaConfig: Optional[Sequence["_OpennebulaConfigDefinition"]]
    OpenstackConfig: Optional[Sequence["_OpenstackConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VsphereConfig: Optional[Sequence["_VsphereConfigDefinition"]]

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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            AuthCertificateAuthority=json_data.get("AuthCertificateAuthority"),
            AuthKey=json_data.get("AuthKey"),
            CloudCredentialId=json_data.get("CloudCredentialId"),
            Description=json_data.get("Description"),
            Driver=json_data.get("Driver"),
            DriverId=json_data.get("DriverId"),
            EngineEnv=deserialize_list(json_data.get("EngineEnv"), EngineEnvDefinition),
            EngineInsecureRegistry=json_data.get("EngineInsecureRegistry"),
            EngineInstallUrl=json_data.get("EngineInstallUrl"),
            EngineLabel=deserialize_list(json_data.get("EngineLabel"), EngineLabelDefinition),
            EngineOpt=deserialize_list(json_data.get("EngineOpt"), EngineOptDefinition),
            EngineRegistryMirror=json_data.get("EngineRegistryMirror"),
            EngineStorageDriver=json_data.get("EngineStorageDriver"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            UseInternalIpAddress=json_data.get("UseInternalIpAddress"),
            Amazonec2Config=deserialize_list(json_data.get("Amazonec2Config"), Amazonec2ConfigDefinition),
            AzureConfig=deserialize_list(json_data.get("AzureConfig"), AzureConfigDefinition),
            DigitaloceanConfig=deserialize_list(json_data.get("DigitaloceanConfig"), DigitaloceanConfigDefinition),
            HetznerConfig=deserialize_list(json_data.get("HetznerConfig"), HetznerConfigDefinition),
            LinodeConfig=deserialize_list(json_data.get("LinodeConfig"), LinodeConfigDefinition),
            NodeTaints=deserialize_list(json_data.get("NodeTaints"), NodeTaintsDefinition),
            OpennebulaConfig=deserialize_list(json_data.get("OpennebulaConfig"), OpennebulaConfigDefinition),
            OpenstackConfig=deserialize_list(json_data.get("OpenstackConfig"), OpenstackConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VsphereConfig=deserialize_list(json_data.get("VsphereConfig"), VsphereConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class EngineEnvDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EngineEnvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EngineEnvDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EngineEnvDefinition = EngineEnvDefinition


@dataclass
class EngineLabelDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EngineLabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EngineLabelDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EngineLabelDefinition = EngineLabelDefinition


@dataclass
class EngineOptDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EngineOptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EngineOptDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EngineOptDefinition = EngineOptDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class Amazonec2ConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    Ami: Optional[str]
    BlockDurationMinutes: Optional[str]
    DeviceName: Optional[str]
    EncryptEbsVolume: Optional[bool]
    Endpoint: Optional[str]
    IamInstanceProfile: Optional[str]
    InsecureTransport: Optional[bool]
    InstanceType: Optional[str]
    KeypairName: Optional[str]
    KmsKey: Optional[str]
    Monitoring: Optional[bool]
    OpenPort: Optional[Sequence[str]]
    PrivateAddressOnly: Optional[bool]
    Region: Optional[str]
    RequestSpotInstance: Optional[bool]
    Retries: Optional[str]
    RootSize: Optional[str]
    SecretKey: Optional[str]
    SecurityGroup: Optional[Sequence[str]]
    SecurityGroupReadonly: Optional[bool]
    SessionToken: Optional[str]
    SpotPrice: Optional[str]
    SshKeypath: Optional[str]
    SshUser: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[str]
    UseEbsOptimizedInstance: Optional[bool]
    UsePrivateAddress: Optional[bool]
    Userdata: Optional[str]
    VolumeType: Optional[str]
    VpcId: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Amazonec2ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Amazonec2ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            Ami=json_data.get("Ami"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
            DeviceName=json_data.get("DeviceName"),
            EncryptEbsVolume=json_data.get("EncryptEbsVolume"),
            Endpoint=json_data.get("Endpoint"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            InsecureTransport=json_data.get("InsecureTransport"),
            InstanceType=json_data.get("InstanceType"),
            KeypairName=json_data.get("KeypairName"),
            KmsKey=json_data.get("KmsKey"),
            Monitoring=json_data.get("Monitoring"),
            OpenPort=json_data.get("OpenPort"),
            PrivateAddressOnly=json_data.get("PrivateAddressOnly"),
            Region=json_data.get("Region"),
            RequestSpotInstance=json_data.get("RequestSpotInstance"),
            Retries=json_data.get("Retries"),
            RootSize=json_data.get("RootSize"),
            SecretKey=json_data.get("SecretKey"),
            SecurityGroup=json_data.get("SecurityGroup"),
            SecurityGroupReadonly=json_data.get("SecurityGroupReadonly"),
            SessionToken=json_data.get("SessionToken"),
            SpotPrice=json_data.get("SpotPrice"),
            SshKeypath=json_data.get("SshKeypath"),
            SshUser=json_data.get("SshUser"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            UseEbsOptimizedInstance=json_data.get("UseEbsOptimizedInstance"),
            UsePrivateAddress=json_data.get("UsePrivateAddress"),
            Userdata=json_data.get("Userdata"),
            VolumeType=json_data.get("VolumeType"),
            VpcId=json_data.get("VpcId"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Amazonec2ConfigDefinition = Amazonec2ConfigDefinition


@dataclass
class AzureConfigDefinition(BaseModel):
    AvailabilitySet: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    CustomData: Optional[str]
    DiskSize: Optional[str]
    Dns: Optional[str]
    DockerPort: Optional[str]
    Environment: Optional[str]
    FaultDomainCount: Optional[str]
    Image: Optional[str]
    Location: Optional[str]
    ManagedDisks: Optional[bool]
    NoPublicIp: Optional[bool]
    Nsg: Optional[str]
    OpenPort: Optional[Sequence[str]]
    PrivateIpAddress: Optional[str]
    ResourceGroup: Optional[str]
    Size: Optional[str]
    SshUser: Optional[str]
    StaticPublicIp: Optional[bool]
    StorageType: Optional[str]
    Subnet: Optional[str]
    SubnetPrefix: Optional[str]
    SubscriptionId: Optional[str]
    UpdateDomainCount: Optional[str]
    UsePrivateIp: Optional[bool]
    Vnet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilitySet=json_data.get("AvailabilitySet"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            CustomData=json_data.get("CustomData"),
            DiskSize=json_data.get("DiskSize"),
            Dns=json_data.get("Dns"),
            DockerPort=json_data.get("DockerPort"),
            Environment=json_data.get("Environment"),
            FaultDomainCount=json_data.get("FaultDomainCount"),
            Image=json_data.get("Image"),
            Location=json_data.get("Location"),
            ManagedDisks=json_data.get("ManagedDisks"),
            NoPublicIp=json_data.get("NoPublicIp"),
            Nsg=json_data.get("Nsg"),
            OpenPort=json_data.get("OpenPort"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            ResourceGroup=json_data.get("ResourceGroup"),
            Size=json_data.get("Size"),
            SshUser=json_data.get("SshUser"),
            StaticPublicIp=json_data.get("StaticPublicIp"),
            StorageType=json_data.get("StorageType"),
            Subnet=json_data.get("Subnet"),
            SubnetPrefix=json_data.get("SubnetPrefix"),
            SubscriptionId=json_data.get("SubscriptionId"),
            UpdateDomainCount=json_data.get("UpdateDomainCount"),
            UsePrivateIp=json_data.get("UsePrivateIp"),
            Vnet=json_data.get("Vnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureConfigDefinition = AzureConfigDefinition


@dataclass
class DigitaloceanConfigDefinition(BaseModel):
    AccessToken: Optional[str]
    Backups: Optional[bool]
    Image: Optional[str]
    Ipv6: Optional[bool]
    Monitoring: Optional[bool]
    PrivateNetworking: Optional[bool]
    Region: Optional[str]
    Size: Optional[str]
    SshKeyFingerprint: Optional[str]
    SshKeyPath: Optional[str]
    SshPort: Optional[str]
    SshUser: Optional[str]
    Tags: Optional[str]
    Userdata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DigitaloceanConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DigitaloceanConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            Backups=json_data.get("Backups"),
            Image=json_data.get("Image"),
            Ipv6=json_data.get("Ipv6"),
            Monitoring=json_data.get("Monitoring"),
            PrivateNetworking=json_data.get("PrivateNetworking"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            SshKeyFingerprint=json_data.get("SshKeyFingerprint"),
            SshKeyPath=json_data.get("SshKeyPath"),
            SshPort=json_data.get("SshPort"),
            SshUser=json_data.get("SshUser"),
            Tags=json_data.get("Tags"),
            Userdata=json_data.get("Userdata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DigitaloceanConfigDefinition = DigitaloceanConfigDefinition


@dataclass
class HetznerConfigDefinition(BaseModel):
    ApiToken: Optional[str]
    Image: Optional[str]
    Networks: Optional[str]
    ServerLocation: Optional[str]
    ServerType: Optional[str]
    UsePrivateNetwork: Optional[bool]
    Userdata: Optional[str]
    Volumes: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HetznerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HetznerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiToken=json_data.get("ApiToken"),
            Image=json_data.get("Image"),
            Networks=json_data.get("Networks"),
            ServerLocation=json_data.get("ServerLocation"),
            ServerType=json_data.get("ServerType"),
            UsePrivateNetwork=json_data.get("UsePrivateNetwork"),
            Userdata=json_data.get("Userdata"),
            Volumes=json_data.get("Volumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HetznerConfigDefinition = HetznerConfigDefinition


@dataclass
class LinodeConfigDefinition(BaseModel):
    AuthorizedUsers: Optional[str]
    CreatePrivateIp: Optional[bool]
    DockerPort: Optional[str]
    Image: Optional[str]
    InstanceType: Optional[str]
    Label: Optional[str]
    Region: Optional[str]
    RootPass: Optional[str]
    SshPort: Optional[str]
    SshUser: Optional[str]
    Stackscript: Optional[str]
    StackscriptData: Optional[str]
    SwapSize: Optional[str]
    Tags: Optional[str]
    Token: Optional[str]
    UaPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthorizedUsers=json_data.get("AuthorizedUsers"),
            CreatePrivateIp=json_data.get("CreatePrivateIp"),
            DockerPort=json_data.get("DockerPort"),
            Image=json_data.get("Image"),
            InstanceType=json_data.get("InstanceType"),
            Label=json_data.get("Label"),
            Region=json_data.get("Region"),
            RootPass=json_data.get("RootPass"),
            SshPort=json_data.get("SshPort"),
            SshUser=json_data.get("SshUser"),
            Stackscript=json_data.get("Stackscript"),
            StackscriptData=json_data.get("StackscriptData"),
            SwapSize=json_data.get("SwapSize"),
            Tags=json_data.get("Tags"),
            Token=json_data.get("Token"),
            UaPrefix=json_data.get("UaPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinodeConfigDefinition = LinodeConfigDefinition


@dataclass
class NodeTaintsDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    TimeAdded: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeTaintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeTaintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            TimeAdded=json_data.get("TimeAdded"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeTaintsDefinition = NodeTaintsDefinition


@dataclass
class OpennebulaConfigDefinition(BaseModel):
    B2dSize: Optional[str]
    Cpu: Optional[str]
    DevPrefix: Optional[str]
    DisableVnc: Optional[bool]
    DiskResize: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    ImageOwner: Optional[str]
    Memory: Optional[str]
    NetworkId: Optional[str]
    NetworkName: Optional[str]
    NetworkOwner: Optional[str]
    Password: Optional[str]
    SshUser: Optional[str]
    TemplateId: Optional[str]
    TemplateName: Optional[str]
    User: Optional[str]
    Vcpu: Optional[str]
    XmlRpcUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpennebulaConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpennebulaConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            B2dSize=json_data.get("B2dSize"),
            Cpu=json_data.get("Cpu"),
            DevPrefix=json_data.get("DevPrefix"),
            DisableVnc=json_data.get("DisableVnc"),
            DiskResize=json_data.get("DiskResize"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            ImageOwner=json_data.get("ImageOwner"),
            Memory=json_data.get("Memory"),
            NetworkId=json_data.get("NetworkId"),
            NetworkName=json_data.get("NetworkName"),
            NetworkOwner=json_data.get("NetworkOwner"),
            Password=json_data.get("Password"),
            SshUser=json_data.get("SshUser"),
            TemplateId=json_data.get("TemplateId"),
            TemplateName=json_data.get("TemplateName"),
            User=json_data.get("User"),
            Vcpu=json_data.get("Vcpu"),
            XmlRpcUrl=json_data.get("XmlRpcUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpennebulaConfigDefinition = OpennebulaConfigDefinition


@dataclass
class OpenstackConfigDefinition(BaseModel):
    ActiveTimeout: Optional[str]
    ApplicationCredentialId: Optional[str]
    ApplicationCredentialName: Optional[str]
    ApplicationCredentialSecret: Optional[str]
    AuthUrl: Optional[str]
    AvailabilityZone: Optional[str]
    BootFromVolume: Optional[bool]
    Cacert: Optional[str]
    ConfigDrive: Optional[bool]
    DomainId: Optional[str]
    DomainName: Optional[str]
    EndpointType: Optional[str]
    FlavorId: Optional[str]
    FlavorName: Optional[str]
    FloatingIpPool: Optional[str]
    ImageId: Optional[str]
    ImageName: Optional[str]
    Insecure: Optional[bool]
    IpVersion: Optional[str]
    KeypairName: Optional[str]
    NetId: Optional[str]
    NetName: Optional[str]
    NovaNetwork: Optional[bool]
    Password: Optional[str]
    PrivateKeyFile: Optional[str]
    Region: Optional[str]
    SecGroups: Optional[str]
    SshPort: Optional[str]
    SshUser: Optional[str]
    TenantId: Optional[str]
    TenantName: Optional[str]
    UserDataFile: Optional[str]
    Username: Optional[str]
    VolumeDevicePath: Optional[str]
    VolumeId: Optional[str]
    VolumeName: Optional[str]
    VolumeSize: Optional[str]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveTimeout=json_data.get("ActiveTimeout"),
            ApplicationCredentialId=json_data.get("ApplicationCredentialId"),
            ApplicationCredentialName=json_data.get("ApplicationCredentialName"),
            ApplicationCredentialSecret=json_data.get("ApplicationCredentialSecret"),
            AuthUrl=json_data.get("AuthUrl"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BootFromVolume=json_data.get("BootFromVolume"),
            Cacert=json_data.get("Cacert"),
            ConfigDrive=json_data.get("ConfigDrive"),
            DomainId=json_data.get("DomainId"),
            DomainName=json_data.get("DomainName"),
            EndpointType=json_data.get("EndpointType"),
            FlavorId=json_data.get("FlavorId"),
            FlavorName=json_data.get("FlavorName"),
            FloatingIpPool=json_data.get("FloatingIpPool"),
            ImageId=json_data.get("ImageId"),
            ImageName=json_data.get("ImageName"),
            Insecure=json_data.get("Insecure"),
            IpVersion=json_data.get("IpVersion"),
            KeypairName=json_data.get("KeypairName"),
            NetId=json_data.get("NetId"),
            NetName=json_data.get("NetName"),
            NovaNetwork=json_data.get("NovaNetwork"),
            Password=json_data.get("Password"),
            PrivateKeyFile=json_data.get("PrivateKeyFile"),
            Region=json_data.get("Region"),
            SecGroups=json_data.get("SecGroups"),
            SshPort=json_data.get("SshPort"),
            SshUser=json_data.get("SshUser"),
            TenantId=json_data.get("TenantId"),
            TenantName=json_data.get("TenantName"),
            UserDataFile=json_data.get("UserDataFile"),
            Username=json_data.get("Username"),
            VolumeDevicePath=json_data.get("VolumeDevicePath"),
            VolumeId=json_data.get("VolumeId"),
            VolumeName=json_data.get("VolumeName"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackConfigDefinition = OpenstackConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class VsphereConfigDefinition(BaseModel):
    Boot2dockerUrl: Optional[str]
    Cfgparam: Optional[Sequence[str]]
    CloneFrom: Optional[str]
    CloudConfig: Optional[str]
    Cloudinit: Optional[str]
    ContentLibrary: Optional[str]
    CpuCount: Optional[str]
    CreationType: Optional[str]
    CustomAttributes: Optional[Sequence[str]]
    Datacenter: Optional[str]
    Datastore: Optional[str]
    DatastoreCluster: Optional[str]
    DiskSize: Optional[str]
    Folder: Optional[str]
    Hostsystem: Optional[str]
    MemorySize: Optional[str]
    Network: Optional[Sequence[str]]
    Password: Optional[str]
    Pool: Optional[str]
    SshPassword: Optional[str]
    SshPort: Optional[str]
    SshUser: Optional[str]
    SshUserGroup: Optional[str]
    Tags: Optional[Sequence[str]]
    Username: Optional[str]
    VappIpAllocationPolicy: Optional[str]
    VappIpProtocol: Optional[str]
    VappProperty: Optional[Sequence[str]]
    VappTransport: Optional[str]
    Vcenter: Optional[str]
    VcenterPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Boot2dockerUrl=json_data.get("Boot2dockerUrl"),
            Cfgparam=json_data.get("Cfgparam"),
            CloneFrom=json_data.get("CloneFrom"),
            CloudConfig=json_data.get("CloudConfig"),
            Cloudinit=json_data.get("Cloudinit"),
            ContentLibrary=json_data.get("ContentLibrary"),
            CpuCount=json_data.get("CpuCount"),
            CreationType=json_data.get("CreationType"),
            CustomAttributes=json_data.get("CustomAttributes"),
            Datacenter=json_data.get("Datacenter"),
            Datastore=json_data.get("Datastore"),
            DatastoreCluster=json_data.get("DatastoreCluster"),
            DiskSize=json_data.get("DiskSize"),
            Folder=json_data.get("Folder"),
            Hostsystem=json_data.get("Hostsystem"),
            MemorySize=json_data.get("MemorySize"),
            Network=json_data.get("Network"),
            Password=json_data.get("Password"),
            Pool=json_data.get("Pool"),
            SshPassword=json_data.get("SshPassword"),
            SshPort=json_data.get("SshPort"),
            SshUser=json_data.get("SshUser"),
            SshUserGroup=json_data.get("SshUserGroup"),
            Tags=json_data.get("Tags"),
            Username=json_data.get("Username"),
            VappIpAllocationPolicy=json_data.get("VappIpAllocationPolicy"),
            VappIpProtocol=json_data.get("VappIpProtocol"),
            VappProperty=json_data.get("VappProperty"),
            VappTransport=json_data.get("VappTransport"),
            Vcenter=json_data.get("Vcenter"),
            VcenterPort=json_data.get("VcenterPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereConfigDefinition = VsphereConfigDefinition


