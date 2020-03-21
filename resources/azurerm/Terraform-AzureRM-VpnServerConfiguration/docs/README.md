# Terraform::AzureRM::VpnServerConfiguration

CloudFormation equivalent of azurerm_vpn_server_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VpnServerConfiguration",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#vpnauthenticationtypes" title="VpnAuthenticationTypes">VpnAuthenticationTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpnprotocols" title="VpnProtocols">VpnProtocols</a>" : <i>[ String, ... ]</i>,
        "<a href="#azureactivedirectoryauthentication" title="AzureActiveDirectoryAuthentication">AzureActiveDirectoryAuthentication</a>" : <i>[ &lt;a href=&#34;azureactivedirectoryauthentication.md&#34;&gt;AzureActiveDirectoryAuthentication&lt;/a&gt;, ... ]</i>,
        "<a href="#clientrevokedcertificate" title="ClientRevokedCertificate">ClientRevokedCertificate</a>" : <i>[ &lt;a href=&#34;clientrevokedcertificate.md&#34;&gt;ClientRevokedCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ &lt;a href=&#34;clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>" : <i>[ &lt;a href=&#34;ipsecpolicy.md&#34;&gt;IpsecPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#radiusserver" title="RadiusServer">RadiusServer</a>" : <i>[ &lt;a href=&#34;radiusserver.md&#34;&gt;RadiusServer&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ &lt;a href=&#34;serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VpnServerConfiguration
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#vpnauthenticationtypes" title="VpnAuthenticationTypes">VpnAuthenticationTypes</a>: <i>
      - String</i>
    <a href="#vpnprotocols" title="VpnProtocols">VpnProtocols</a>: <i>
      - String</i>
    <a href="#azureactivedirectoryauthentication" title="AzureActiveDirectoryAuthentication">AzureActiveDirectoryAuthentication</a>: <i>
      - &lt;a href=&#34;azureactivedirectoryauthentication.md&#34;&gt;AzureActiveDirectoryAuthentication&lt;/a&gt;</i>
    <a href="#clientrevokedcertificate" title="ClientRevokedCertificate">ClientRevokedCertificate</a>: <i>
      - &lt;a href=&#34;clientrevokedcertificate.md&#34;&gt;ClientRevokedCertificate&lt;/a&gt;</i>
    <a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - &lt;a href=&#34;clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;</i>
    <a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>: <i>
      - &lt;a href=&#34;ipsecpolicy.md&#34;&gt;IpsecPolicy&lt;/a&gt;</i>
    <a href="#radiusserver" title="RadiusServer">RadiusServer</a>: <i>
      - &lt;a href=&#34;radiusserver.md&#34;&gt;RadiusServer&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - &lt;a href=&#34;serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnAuthenticationTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnProtocols

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectoryAuthentication

_Required_: No

_Type_: List of &lt;a href=&#34;azureactivedirectoryauthentication.md&#34;&gt;AzureActiveDirectoryAuthentication&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRevokedCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;clientrevokedcertificate.md&#34;&gt;ClientRevokedCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRootCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;clientrootcertificate.md&#34;&gt;ClientRootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;ipsecpolicy.md&#34;&gt;IpsecPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServer

_Required_: No

_Type_: List of &lt;a href=&#34;radiusserver.md&#34;&gt;RadiusServer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;serverrootcertificate.md&#34;&gt;ServerRootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

