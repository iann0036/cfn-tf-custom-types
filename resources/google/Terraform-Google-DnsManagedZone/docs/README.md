# Terraform::Google::DnsManagedZone

CloudFormation equivalent of google_dns_managed_zone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DnsManagedZone",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>" : <i>[ &lt;a href=&#34;dnssecconfig.md&#34;&gt;DnssecConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>" : <i>[ &lt;a href=&#34;privatevisibilityconfig.md&#34;&gt;PrivateVisibilityConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#defaultkeyspecs" title="DefaultKeySpecs">DefaultKeySpecs</a>" : <i>[ &lt;a href=&#34;defaultkeyspecs.md&#34;&gt;DefaultKeySpecs&lt;/a&gt;, ... ]</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ &lt;a href=&#34;networks.md&#34;&gt;Networks&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DnsManagedZone
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>: <i>
      - &lt;a href=&#34;dnssecconfig.md&#34;&gt;DnssecConfig&lt;/a&gt;</i>
    <a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>: <i>
      - &lt;a href=&#34;privatevisibilityconfig.md&#34;&gt;PrivateVisibilityConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#defaultkeyspecs" title="DefaultKeySpecs">DefaultKeySpecs</a>: <i>
      - &lt;a href=&#34;defaultkeyspecs.md&#34;&gt;DefaultKeySpecs&lt;/a&gt;</i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - &lt;a href=&#34;networks.md&#34;&gt;Networks&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dnssecconfig.md&#34;&gt;DnssecConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateVisibilityConfig

_Required_: No

_Type_: List of &lt;a href=&#34;privatevisibilityconfig.md&#34;&gt;PrivateVisibilityConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultKeySpecs

_Required_: No

_Type_: List of &lt;a href=&#34;defaultkeyspecs.md&#34;&gt;DefaultKeySpecs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of &lt;a href=&#34;networks.md&#34;&gt;Networks&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### NameServers

Returns the &lt;code&gt;NameServers&lt;/code&gt; value.

