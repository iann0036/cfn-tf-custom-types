# Terraform::AzureRM::VirtualNetworkGateway

CloudFormation equivalent of azurerm_virtual_network_gateway

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualNetworkGateway",
    "Properties" : {
        "<a href="#activeactive" title="ActiveActive">ActiveActive</a>" : <i>Boolean</i>,
        "<a href="#defaultlocalnetworkgatewayid" title="DefaultLocalNetworkGatewayId">DefaultLocalNetworkGatewayId</a>" : <i>String</i>,
        "<a href="#enablebgp" title="EnableBgp">EnableBgp</a>" : <i>Boolean</i>,
        "<a href="#generation" title="Generation">Generation</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpntype" title="VpnType">VpnType</a>" : <i>String</i>,
        "<a href="#bgpsettings" title="BgpSettings">BgpSettings</a>" : <i>[ &lt;a href=&#34;bgpsettings.md&#34;&gt;BgpSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#vpnclientconfiguration" title="VpnClientConfiguration">VpnClientConfiguration</a>" : <i>[ &lt;a href=&#34;vpnclientconfiguration.md&#34;&gt;VpnClientConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>" : <i>[ &lt;a href=&#34;revokedcertificate.md&#34;&gt;RevokedCertificate&lt;/a&gt;, ... ]</i>,
        "<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>" : <i>[ &lt;a href=&#34;rootcertificate.md&#34;&gt;RootCertificate&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualNetworkGateway
Properties:
    <a href="#activeactive" title="ActiveActive">ActiveActive</a>: <i>Boolean</i>
    <a href="#defaultlocalnetworkgatewayid" title="DefaultLocalNetworkGatewayId">DefaultLocalNetworkGatewayId</a>: <i>String</i>
    <a href="#enablebgp" title="EnableBgp">EnableBgp</a>: <i>Boolean</i>
    <a href="#generation" title="Generation">Generation</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpntype" title="VpnType">VpnType</a>: <i>String</i>
    <a href="#bgpsettings" title="BgpSettings">BgpSettings</a>: <i>
      - &lt;a href=&#34;bgpsettings.md&#34;&gt;BgpSettings&lt;/a&gt;</i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#vpnclientconfiguration" title="VpnClientConfiguration">VpnClientConfiguration</a>: <i>
      - &lt;a href=&#34;vpnclientconfiguration.md&#34;&gt;VpnClientConfiguration&lt;/a&gt;</i>
    <a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>: <i>
      - &lt;a href=&#34;revokedcertificate.md&#34;&gt;RevokedCertificate&lt;/a&gt;</i>
    <a href="#rootcertificate" title="RootCertificate">RootCertificate</a>: <i>
      - &lt;a href=&#34;rootcertificate.md&#34;&gt;RootCertificate&lt;/a&gt;</i>
</pre>

## Properties

#### ActiveActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLocalNetworkGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBgp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Generation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Sku

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpSettings

_Required_: No

_Type_: List of &lt;a href=&#34;bgpsettings.md&#34;&gt;BgpSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;vpnclientconfiguration.md&#34;&gt;VpnClientConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokedCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;revokedcertificate.md&#34;&gt;RevokedCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootCertificate

_Required_: No

_Type_: List of &lt;a href=&#34;rootcertificate.md&#34;&gt;RootCertificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

