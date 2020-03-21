# Terraform::AzureRM::VpnServerConfiguration

Manages a VPN Server Configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VpnServerConfiguration",
    "Properties" : {
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpnauthenticationtypes" title="VpnAuthenticationTypes">VpnAuthenticationTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpnprotocols" title="VpnProtocols">VpnProtocols</a>" : <i>[ String, ... ]</i>,
        "<a href="#azureactivedirectoryauthentication" title="AzureActiveDirectoryAuthentication">AzureActiveDirectoryAuthentication</a>" : <i>[ <a href="azureactivedirectoryauthentication.md">AzureActiveDirectoryAuthentication</a>, ... ]</i>,
        "<a href="#clientrevokedcertificate" title="ClientRevokedCertificate">ClientRevokedCertificate</a>" : <i>[ <a href="clientrevokedcertificate.md">ClientRevokedCertificate</a>, ... ]</i>,
        "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ <a href="clientrootcertificate.md">ClientRootCertificate</a>, ... ]</i>,
        "<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>" : <i>[ <a href="ipsecpolicy.md">IpsecPolicy</a>, ... ]</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>[ <a href="radiusserver.md">RadiusServer</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ <a href="serverrootcertificate.md">ServerRootCertificate</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VpnServerConfiguration
Properties:
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpnauthenticationtypes" title="VpnAuthenticationTypes">VpnAuthenticationTypes</a>: <i>
      - String</i>
    <a href="#vpnprotocols" title="VpnProtocols">VpnProtocols</a>: <i>
      - String</i>
    <a href="#azureactivedirectoryauthentication" title="AzureActiveDirectoryAuthentication">AzureActiveDirectoryAuthentication</a>: <i>
      - <a href="azureactivedirectoryauthentication.md">AzureActiveDirectoryAuthentication</a></i>
    <a href="#clientrevokedcertificate" title="ClientRevokedCertificate">ClientRevokedCertificate</a>: <i>
      - <a href="clientrevokedcertificate.md">ClientRevokedCertificate</a></i>
    <a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - <a href="clientrootcertificate.md">ClientRootCertificate</a></i>
    <a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>: <i>
      - <a href="ipsecpolicy.md">IpsecPolicy</a></i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>
      - <a href="radiusserver.md">RadiusServer</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - <a href="serverrootcertificate.md">ServerRootCertificate</a></i>
</pre>

## Properties

#### Location

The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnAuthenticationTypes

A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnProtocols

A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectoryAuthentication

_Required_: No

_Type_: List of <a href="azureactivedirectoryauthentication.md">AzureActiveDirectoryAuthentication</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRevokedCertificate

_Required_: No

_Type_: List of <a href="clientrevokedcertificate.md">ClientRevokedCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRootCertificate

_Required_: No

_Type_: List of <a href="clientrootcertificate.md">ClientRootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPolicy

_Required_: No

_Type_: List of <a href="ipsecpolicy.md">IpsecPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

_Required_: No

_Type_: List of <a href="radiusserver.md">RadiusServer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No

_Type_: List of <a href="serverrootcertificate.md">ServerRootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

