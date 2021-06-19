# TF::AVI::Cloud OpenstackConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#admintenant" title="AdminTenant">AdminTenant</a>" : <i>String</i>,
    "<a href="#admintenantuuid" title="AdminTenantUuid">AdminTenantUuid</a>" : <i>String</i>,
    "<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>" : <i>Boolean</i>,
    "<a href="#antiaffinity" title="AntiAffinity">AntiAffinity</a>" : <i>Boolean</i>,
    "<a href="#authurl" title="AuthUrl">AuthUrl</a>" : <i>String</i>,
    "<a href="#configdrive" title="ConfigDrive">ConfigDrive</a>" : <i>Boolean</i>,
    "<a href="#contraildisablepolicy" title="ContrailDisablePolicy">ContrailDisablePolicy</a>" : <i>Boolean</i>,
    "<a href="#contrailendpoint" title="ContrailEndpoint">ContrailEndpoint</a>" : <i>String</i>,
    "<a href="#contrailplugin" title="ContrailPlugin">ContrailPlugin</a>" : <i>Boolean</i>,
    "<a href="#externalnetworks" title="ExternalNetworks">ExternalNetworks</a>" : <i>Boolean</i>,
    "<a href="#freefloatingips" title="FreeFloatingips">FreeFloatingips</a>" : <i>Boolean</i>,
    "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
    "<a href="#imgformat" title="ImgFormat">ImgFormat</a>" : <i>String</i>,
    "<a href="#importkeystonetenants" title="ImportKeystoneTenants">ImportKeystoneTenants</a>" : <i>Boolean</i>,
    "<a href="#insecure" title="Insecure">Insecure</a>" : <i>Boolean</i>,
    "<a href="#keystonehost" title="KeystoneHost">KeystoneHost</a>" : <i>String</i>,
    "<a href="#mapadmintocloudadmin" title="MapAdminToCloudadmin">MapAdminToCloudadmin</a>" : <i>Boolean</i>,
    "<a href="#mgmtnetworkname" title="MgmtNetworkName">MgmtNetworkName</a>" : <i>String</i>,
    "<a href="#mgmtnetworkuuid" title="MgmtNetworkUuid">MgmtNetworkUuid</a>" : <i>String</i>,
    "<a href="#nameowner" title="NameOwner">NameOwner</a>" : <i>Boolean</i>,
    "<a href="#neutronrbac" title="NeutronRbac">NeutronRbac</a>" : <i>Boolean</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#privilege" title="Privilege">Privilege</a>" : <i>String</i>,
    "<a href="#provname" title="ProvName">ProvName</a>" : <i>[ String, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>Boolean</i>,
    "<a href="#tenantse" title="TenantSe">TenantSe</a>" : <i>Boolean</i>,
    "<a href="#useadminurl" title="UseAdminUrl">UseAdminUrl</a>" : <i>Boolean</i>,
    "<a href="#useinternalendpoints" title="UseInternalEndpoints">UseInternalEndpoints</a>" : <i>Boolean</i>,
    "<a href="#usekeystoneauth" title="UseKeystoneAuth">UseKeystoneAuth</a>" : <i>Boolean</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#customseimageproperties" title="CustomSeImageProperties">CustomSeImageProperties</a>" : <i>[ <a href="customseimagepropertiesdefinition.md">CustomSeImagePropertiesDefinition</a>, ... ]</i>,
    "<a href="#hypervisorproperties" title="HypervisorProperties">HypervisorProperties</a>" : <i>[ <a href="hypervisorpropertiesdefinition.md">HypervisorPropertiesDefinition</a>, ... ]</i>,
    "<a href="#providervipnetworks" title="ProviderVipNetworks">ProviderVipNetworks</a>" : <i>[ <a href="providervipnetworksdefinition.md">ProviderVipNetworksDefinition</a>, ... ]</i>,
    "<a href="#rolemapping" title="RoleMapping">RoleMapping</a>" : <i>[ <a href="rolemappingdefinition.md">RoleMappingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#admintenant" title="AdminTenant">AdminTenant</a>: <i>String</i>
<a href="#admintenantuuid" title="AdminTenantUuid">AdminTenantUuid</a>: <i>String</i>
<a href="#allowedaddresspairs" title="AllowedAddressPairs">AllowedAddressPairs</a>: <i>Boolean</i>
<a href="#antiaffinity" title="AntiAffinity">AntiAffinity</a>: <i>Boolean</i>
<a href="#authurl" title="AuthUrl">AuthUrl</a>: <i>String</i>
<a href="#configdrive" title="ConfigDrive">ConfigDrive</a>: <i>Boolean</i>
<a href="#contraildisablepolicy" title="ContrailDisablePolicy">ContrailDisablePolicy</a>: <i>Boolean</i>
<a href="#contrailendpoint" title="ContrailEndpoint">ContrailEndpoint</a>: <i>String</i>
<a href="#contrailplugin" title="ContrailPlugin">ContrailPlugin</a>: <i>Boolean</i>
<a href="#externalnetworks" title="ExternalNetworks">ExternalNetworks</a>: <i>Boolean</i>
<a href="#freefloatingips" title="FreeFloatingips">FreeFloatingips</a>: <i>Boolean</i>
<a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
<a href="#imgformat" title="ImgFormat">ImgFormat</a>: <i>String</i>
<a href="#importkeystonetenants" title="ImportKeystoneTenants">ImportKeystoneTenants</a>: <i>Boolean</i>
<a href="#insecure" title="Insecure">Insecure</a>: <i>Boolean</i>
<a href="#keystonehost" title="KeystoneHost">KeystoneHost</a>: <i>String</i>
<a href="#mapadmintocloudadmin" title="MapAdminToCloudadmin">MapAdminToCloudadmin</a>: <i>Boolean</i>
<a href="#mgmtnetworkname" title="MgmtNetworkName">MgmtNetworkName</a>: <i>String</i>
<a href="#mgmtnetworkuuid" title="MgmtNetworkUuid">MgmtNetworkUuid</a>: <i>String</i>
<a href="#nameowner" title="NameOwner">NameOwner</a>: <i>Boolean</i>
<a href="#neutronrbac" title="NeutronRbac">NeutronRbac</a>: <i>Boolean</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#privilege" title="Privilege">Privilege</a>: <i>String</i>
<a href="#provname" title="ProvName">ProvName</a>: <i>
      - String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>Boolean</i>
<a href="#tenantse" title="TenantSe">TenantSe</a>: <i>Boolean</i>
<a href="#useadminurl" title="UseAdminUrl">UseAdminUrl</a>: <i>Boolean</i>
<a href="#useinternalendpoints" title="UseInternalEndpoints">UseInternalEndpoints</a>: <i>Boolean</i>
<a href="#usekeystoneauth" title="UseKeystoneAuth">UseKeystoneAuth</a>: <i>Boolean</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#customseimageproperties" title="CustomSeImageProperties">CustomSeImageProperties</a>: <i>
      - <a href="customseimagepropertiesdefinition.md">CustomSeImagePropertiesDefinition</a></i>
<a href="#hypervisorproperties" title="HypervisorProperties">HypervisorProperties</a>: <i>
      - <a href="hypervisorpropertiesdefinition.md">HypervisorPropertiesDefinition</a></i>
<a href="#providervipnetworks" title="ProviderVipNetworks">ProviderVipNetworks</a>: <i>
      - <a href="providervipnetworksdefinition.md">ProviderVipNetworksDefinition</a></i>
<a href="#rolemapping" title="RoleMapping">RoleMapping</a>: <i>
      - <a href="rolemappingdefinition.md">RoleMappingDefinition</a></i>
</pre>

## Properties

#### AdminTenant

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminTenantUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedAddressPairs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiAffinity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigDrive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContrailDisablePolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContrailEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContrailPlugin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeFloatingips

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImgFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportKeystoneTenants

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Insecure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeystoneHost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapAdminToCloudadmin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtNetworkName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtNetworkUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameOwner

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeutronRbac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privilege

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvName

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantSe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAdminUrl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseInternalEndpoints

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseKeystoneAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSeImageProperties

_Required_: No

_Type_: List of <a href="customseimagepropertiesdefinition.md">CustomSeImagePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HypervisorProperties

_Required_: No

_Type_: List of <a href="hypervisorpropertiesdefinition.md">HypervisorPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVipNetworks

_Required_: No

_Type_: List of <a href="providervipnetworksdefinition.md">ProviderVipNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleMapping

_Required_: No

_Type_: List of <a href="rolemappingdefinition.md">RoleMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

