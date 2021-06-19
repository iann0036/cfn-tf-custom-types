# TF::AVI::Cloud

The Cloud resource allows the creation and management of Avi Cloud

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Cloud",
    "Properties" : {
        "<a href="#apicmode" title="ApicMode">ApicMode</a>" : <i>Boolean</i>,
        "<a href="#autoscalepollinginterval" title="AutoscalePollingInterval">AutoscalePollingInterval</a>" : <i>Double</i>,
        "<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>" : <i>Boolean</i>,
        "<a href="#dnsproviderref" title="DnsProviderRef">DnsProviderRef</a>" : <i>String</i>,
        "<a href="#dnsresolutiononse" title="DnsResolutionOnSe">DnsResolutionOnSe</a>" : <i>Boolean</i>,
        "<a href="#eastwestdnsproviderref" title="EastWestDnsProviderRef">EastWestDnsProviderRef</a>" : <i>String</i>,
        "<a href="#eastwestipamproviderref" title="EastWestIpamProviderRef">EastWestIpamProviderRef</a>" : <i>String</i>,
        "<a href="#enableviponallinterfaces" title="EnableVipOnAllInterfaces">EnableVipOnAllInterfaces</a>" : <i>Boolean</i>,
        "<a href="#enablevipstaticroutes" title="EnableVipStaticRoutes">EnableVipStaticRoutes</a>" : <i>Boolean</i>,
        "<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>" : <i>Boolean</i>,
        "<a href="#ipamproviderref" title="IpamProviderRef">IpamProviderRef</a>" : <i>String</i>,
        "<a href="#licensetier" title="LicenseTier">LicenseTier</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objnameprefix" title="ObjNamePrefix">ObjNamePrefix</a>" : <i>String</i>,
        "<a href="#preferstaticroutes" title="PreferStaticRoutes">PreferStaticRoutes</a>" : <i>Boolean</i>,
        "<a href="#segrouptemplateref" title="SeGroupTemplateRef">SeGroupTemplateRef</a>" : <i>String</i>,
        "<a href="#statebaseddnsregistration" title="StateBasedDnsRegistration">StateBasedDnsRegistration</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vmcdeployment" title="VmcDeployment">VmcDeployment</a>" : <i>Boolean</i>,
        "<a href="#vtype" title="Vtype">Vtype</a>" : <i>String</i>,
        "<a href="#apicconfiguration" title="ApicConfiguration">ApicConfiguration</a>" : <i>[ <a href="apicconfigurationdefinition.md">ApicConfigurationDefinition</a>, ... ]</i>,
        "<a href="#awsconfiguration" title="AwsConfiguration">AwsConfiguration</a>" : <i>[ <a href="awsconfigurationdefinition.md">AwsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#azureconfiguration" title="AzureConfiguration">AzureConfiguration</a>" : <i>[ <a href="azureconfigurationdefinition.md">AzureConfigurationDefinition</a>, ... ]</i>,
        "<a href="#cloudstackconfiguration" title="CloudstackConfiguration">CloudstackConfiguration</a>" : <i>[ <a href="cloudstackconfigurationdefinition.md">CloudstackConfigurationDefinition</a>, ... ]</i>,
        "<a href="#customtags" title="CustomTags">CustomTags</a>" : <i>[ <a href="customtagsdefinition.md">CustomTagsDefinition</a>, ... ]</i>,
        "<a href="#dnsresolvers" title="DnsResolvers">DnsResolvers</a>" : <i>[ <a href="dnsresolversdefinition.md">DnsResolversDefinition</a>, ... ]</i>,
        "<a href="#dockerconfiguration" title="DockerConfiguration">DockerConfiguration</a>" : <i>[ <a href="dockerconfigurationdefinition.md">DockerConfigurationDefinition</a>, ... ]</i>,
        "<a href="#gcpconfiguration" title="GcpConfiguration">GcpConfiguration</a>" : <i>[ <a href="gcpconfigurationdefinition.md">GcpConfigurationDefinition</a>, ... ]</i>,
        "<a href="#linuxserverconfiguration" title="LinuxserverConfiguration">LinuxserverConfiguration</a>" : <i>[ <a href="linuxserverconfigurationdefinition.md">LinuxserverConfigurationDefinition</a>, ... ]</i>,
        "<a href="#nsxconfiguration" title="NsxConfiguration">NsxConfiguration</a>" : <i>[ <a href="nsxconfigurationdefinition.md">NsxConfigurationDefinition</a>, ... ]</i>,
        "<a href="#nsxtconfiguration" title="NsxtConfiguration">NsxtConfiguration</a>" : <i>[ <a href="nsxtconfigurationdefinition.md">NsxtConfigurationDefinition</a>, ... ]</i>,
        "<a href="#openstackconfiguration" title="OpenstackConfiguration">OpenstackConfiguration</a>" : <i>[ <a href="openstackconfigurationdefinition.md">OpenstackConfigurationDefinition</a>, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>, ... ]</i>,
        "<a href="#rancherconfiguration" title="RancherConfiguration">RancherConfiguration</a>" : <i>[ <a href="rancherconfigurationdefinition.md">RancherConfigurationDefinition</a>, ... ]</i>,
        "<a href="#vcaconfiguration" title="VcaConfiguration">VcaConfiguration</a>" : <i>[ <a href="vcaconfigurationdefinition.md">VcaConfigurationDefinition</a>, ... ]</i>,
        "<a href="#vcenterconfiguration" title="VcenterConfiguration">VcenterConfiguration</a>" : <i>[ <a href="vcenterconfigurationdefinition.md">VcenterConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Cloud
Properties:
    <a href="#apicmode" title="ApicMode">ApicMode</a>: <i>Boolean</i>
    <a href="#autoscalepollinginterval" title="AutoscalePollingInterval">AutoscalePollingInterval</a>: <i>Double</i>
    <a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>: <i>Boolean</i>
    <a href="#dnsproviderref" title="DnsProviderRef">DnsProviderRef</a>: <i>String</i>
    <a href="#dnsresolutiononse" title="DnsResolutionOnSe">DnsResolutionOnSe</a>: <i>Boolean</i>
    <a href="#eastwestdnsproviderref" title="EastWestDnsProviderRef">EastWestDnsProviderRef</a>: <i>String</i>
    <a href="#eastwestipamproviderref" title="EastWestIpamProviderRef">EastWestIpamProviderRef</a>: <i>String</i>
    <a href="#enableviponallinterfaces" title="EnableVipOnAllInterfaces">EnableVipOnAllInterfaces</a>: <i>Boolean</i>
    <a href="#enablevipstaticroutes" title="EnableVipStaticRoutes">EnableVipStaticRoutes</a>: <i>Boolean</i>
    <a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>: <i>Boolean</i>
    <a href="#ipamproviderref" title="IpamProviderRef">IpamProviderRef</a>: <i>String</i>
    <a href="#licensetier" title="LicenseTier">LicenseTier</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objnameprefix" title="ObjNamePrefix">ObjNamePrefix</a>: <i>String</i>
    <a href="#preferstaticroutes" title="PreferStaticRoutes">PreferStaticRoutes</a>: <i>Boolean</i>
    <a href="#segrouptemplateref" title="SeGroupTemplateRef">SeGroupTemplateRef</a>: <i>String</i>
    <a href="#statebaseddnsregistration" title="StateBasedDnsRegistration">StateBasedDnsRegistration</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vmcdeployment" title="VmcDeployment">VmcDeployment</a>: <i>Boolean</i>
    <a href="#vtype" title="Vtype">Vtype</a>: <i>String</i>
    <a href="#apicconfiguration" title="ApicConfiguration">ApicConfiguration</a>: <i>
      - <a href="apicconfigurationdefinition.md">ApicConfigurationDefinition</a></i>
    <a href="#awsconfiguration" title="AwsConfiguration">AwsConfiguration</a>: <i>
      - <a href="awsconfigurationdefinition.md">AwsConfigurationDefinition</a></i>
    <a href="#azureconfiguration" title="AzureConfiguration">AzureConfiguration</a>: <i>
      - <a href="azureconfigurationdefinition.md">AzureConfigurationDefinition</a></i>
    <a href="#cloudstackconfiguration" title="CloudstackConfiguration">CloudstackConfiguration</a>: <i>
      - <a href="cloudstackconfigurationdefinition.md">CloudstackConfigurationDefinition</a></i>
    <a href="#customtags" title="CustomTags">CustomTags</a>: <i>
      - <a href="customtagsdefinition.md">CustomTagsDefinition</a></i>
    <a href="#dnsresolvers" title="DnsResolvers">DnsResolvers</a>: <i>
      - <a href="dnsresolversdefinition.md">DnsResolversDefinition</a></i>
    <a href="#dockerconfiguration" title="DockerConfiguration">DockerConfiguration</a>: <i>
      - <a href="dockerconfigurationdefinition.md">DockerConfigurationDefinition</a></i>
    <a href="#gcpconfiguration" title="GcpConfiguration">GcpConfiguration</a>: <i>
      - <a href="gcpconfigurationdefinition.md">GcpConfigurationDefinition</a></i>
    <a href="#linuxserverconfiguration" title="LinuxserverConfiguration">LinuxserverConfiguration</a>: <i>
      - <a href="linuxserverconfigurationdefinition.md">LinuxserverConfigurationDefinition</a></i>
    <a href="#nsxconfiguration" title="NsxConfiguration">NsxConfiguration</a>: <i>
      - <a href="nsxconfigurationdefinition.md">NsxConfigurationDefinition</a></i>
    <a href="#nsxtconfiguration" title="NsxtConfiguration">NsxtConfiguration</a>: <i>
      - <a href="nsxtconfigurationdefinition.md">NsxtConfigurationDefinition</a></i>
    <a href="#openstackconfiguration" title="OpenstackConfiguration">OpenstackConfiguration</a>: <i>
      - <a href="openstackconfigurationdefinition.md">OpenstackConfigurationDefinition</a></i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a></i>
    <a href="#rancherconfiguration" title="RancherConfiguration">RancherConfiguration</a>: <i>
      - <a href="rancherconfigurationdefinition.md">RancherConfigurationDefinition</a></i>
    <a href="#vcaconfiguration" title="VcaConfiguration">VcaConfiguration</a>: <i>
      - <a href="vcaconfigurationdefinition.md">VcaConfigurationDefinition</a></i>
    <a href="#vcenterconfiguration" title="VcenterConfiguration">VcenterConfiguration</a>: <i>
      - <a href="vcenterconfigurationdefinition.md">VcenterConfigurationDefinition</a></i>
</pre>

## Properties

#### ApicMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalePollingInterval

Cloudconnector polling interval in seconds for external autoscale groups, minimum 60 seconds. Allowed values are 60-3600. Field introduced in 18.2.2. Unit is seconds. Allowed in basic(allowed values- 60) edition, essentials(allowed values- 60) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpEnabled

Select the ip address management scheme.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsProviderRef

Dns profile for the cloud. It is a reference to an object of type ipamdnsproviderprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsResolutionOnSe

By default, pool member fqdns are resolved on the controller. When this is set, pool member fqdns are instead resolved on service engines in this cloud. This is useful in scenarios where pool member fqdns can only be resolved from service engines and not from the controller. Field introduced in 18.2.6. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWestDnsProviderRef

Dns profile for east-west services. It is a reference to an object of type ipamdnsproviderprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWestIpamProviderRef

Ipam profile for east-west services. Warning - please use virtual subnets in this ipam profile that do not conflict with the underlay networks or any overlay networks in the cluster. For example in aws and gcp, 169.254.0.0/16 is used for storing instance metadata. Hence, it should not be used in this profile. It is a reference to an object of type ipamdnsproviderprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVipOnAllInterfaces

Enable vip on all data interfaces for the cloud. Field introduced in 18.2.9, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVipStaticRoutes

Use static routes for vip side network resolution during virtualservice placement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6AutocfgEnabled

Enable ipv6 auto configuration. Field introduced in 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamProviderRef

Ipam profile for the cloud. It is a reference to an object of type ipamdnsproviderprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseTier

Specifies the default license tier which would be used by new se groups. This field by default inherits the value from system configuration. Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS. Field introduced in 17.2.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

If no license type is specified then default license enforcement for the cloud type is chosen. The default mappings are container cloud is max ses, openstack and vmware is cores and linux it is sockets. Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

Mtu setting for the cloud. Unit is bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjNamePrefix

Default prefix for all automatically created objects in this cloud. This prefix can be overridden by the se-group template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferStaticRoutes

Prefer static routes over interface routes during virtualservice placement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupTemplateRef

The service engine group to use as template. It is a reference to an object of type serviceenginegroup. Field introduced in 18.2.5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateBasedDnsRegistration

Dns records for vips are added/deleted based on the operational state of the vips. Field introduced in 17.1.12. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmcDeployment

This deployment is vmware on aws cloud. Field introduced in 20.1.5, 21.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vtype

Cloud type. Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP, CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT. Allowed in basic(allowed values- cloud_none,cloud_nsxt) edition, essentials(allowed values- cloud_none,cloud_vcenter) edition, enterprise edition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApicConfiguration

_Required_: No

_Type_: List of <a href="apicconfigurationdefinition.md">ApicConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsConfiguration

_Required_: No

_Type_: List of <a href="awsconfigurationdefinition.md">AwsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureConfiguration

_Required_: No

_Type_: List of <a href="azureconfigurationdefinition.md">AzureConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudstackConfiguration

_Required_: No

_Type_: List of <a href="cloudstackconfigurationdefinition.md">CloudstackConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTags

_Required_: No

_Type_: List of <a href="customtagsdefinition.md">CustomTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsResolvers

_Required_: No

_Type_: List of <a href="dnsresolversdefinition.md">DnsResolversDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerConfiguration

_Required_: No

_Type_: List of <a href="dockerconfigurationdefinition.md">DockerConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpConfiguration

_Required_: No

_Type_: List of <a href="gcpconfigurationdefinition.md">GcpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxserverConfiguration

_Required_: No

_Type_: List of <a href="linuxserverconfigurationdefinition.md">LinuxserverConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxConfiguration

_Required_: No

_Type_: List of <a href="nsxconfigurationdefinition.md">NsxConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtConfiguration

_Required_: No

_Type_: List of <a href="nsxtconfigurationdefinition.md">NsxtConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackConfiguration

_Required_: No

_Type_: List of <a href="openstackconfigurationdefinition.md">OpenstackConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RancherConfiguration

_Required_: No

_Type_: List of <a href="rancherconfigurationdefinition.md">RancherConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcaConfiguration

_Required_: No

_Type_: List of <a href="vcaconfigurationdefinition.md">VcaConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterConfiguration

_Required_: No

_Type_: List of <a href="vcenterconfigurationdefinition.md">VcenterConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

