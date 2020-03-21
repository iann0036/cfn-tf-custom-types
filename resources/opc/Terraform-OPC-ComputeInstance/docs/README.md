# Terraform::OPC::ComputeInstance

CloudFormation equivalent of opc_compute_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeInstance",
    "Properties" : {
        "<a href="#bootorder" title="BootOrder">BootOrder</a>" : <i>[ Double, ... ]</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#imagelist" title="ImageList">ImageList</a>" : <i>String</i>,
        "<a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reversedns" title="ReverseDns">ReverseDns</a>" : <i>Boolean</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>" : <i>[ &lt;a href=&#34;networkinginfo.md&#34;&gt;NetworkingInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>[ &lt;a href=&#34;storage.md&#34;&gt;Storage&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeInstance
Properties:
    <a href="#bootorder" title="BootOrder">BootOrder</a>: <i>
      - Double</i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#imagelist" title="ImageList">ImageList</a>: <i>String</i>
    <a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reversedns" title="ReverseDns">ReverseDns</a>: <i>Boolean</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>: <i>
      - &lt;a href=&#34;networkinginfo.md&#34;&gt;NetworkingInfo&lt;/a&gt;</i>
    <a href="#storage" title="Storage">Storage</a>: <i>
      - &lt;a href=&#34;storage.md&#34;&gt;Storage&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### BootOrder

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceAttributes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseDns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingInfo

_Required_: No

_Type_: List of &lt;a href=&#34;networkinginfo.md&#34;&gt;NetworkingInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of &lt;a href=&#34;storage.md&#34;&gt;Storage&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Attributes

Returns the &lt;code&gt;Attributes&lt;/code&gt; value.

#### AvailabilityDomain

Returns the &lt;code&gt;AvailabilityDomain&lt;/code&gt; value.

#### Domain

Returns the &lt;code&gt;Domain&lt;/code&gt; value.

#### Entry

Returns the &lt;code&gt;Entry&lt;/code&gt; value.

#### Fingerprint

Returns the &lt;code&gt;Fingerprint&lt;/code&gt; value.

#### Fqdn

Returns the &lt;code&gt;Fqdn&lt;/code&gt; value.

#### ImageFormat

Returns the &lt;code&gt;ImageFormat&lt;/code&gt; value.

#### IpAddress

Returns the &lt;code&gt;IpAddress&lt;/code&gt; value.

#### PlacementRequirements

Returns the &lt;code&gt;PlacementRequirements&lt;/code&gt; value.

#### Platform

Returns the &lt;code&gt;Platform&lt;/code&gt; value.

#### Priority

Returns the &lt;code&gt;Priority&lt;/code&gt; value.

#### QuotaReservation

Returns the &lt;code&gt;QuotaReservation&lt;/code&gt; value.

#### Relationships

Returns the &lt;code&gt;Relationships&lt;/code&gt; value.

#### Resolvers

Returns the &lt;code&gt;Resolvers&lt;/code&gt; value.

#### Site

Returns the &lt;code&gt;Site&lt;/code&gt; value.

#### StartTime

Returns the &lt;code&gt;StartTime&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### Vcable

Returns the &lt;code&gt;Vcable&lt;/code&gt; value.

#### Virtio

Returns the &lt;code&gt;Virtio&lt;/code&gt; value.

#### VncAddress

Returns the &lt;code&gt;VncAddress&lt;/code&gt; value.

