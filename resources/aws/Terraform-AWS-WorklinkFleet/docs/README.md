# Terraform::AWS::WorklinkFleet

CloudFormation equivalent of aws_worklink_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::WorklinkFleet",
    "Properties" : {
        "<a href="#auditstreamarn" title="AuditStreamArn">AuditStreamArn</a>" : <i>String</i>,
        "<a href="#devicecacertificate" title="DeviceCaCertificate">DeviceCaCertificate</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optimizeforenduserlocation" title="OptimizeForEndUserLocation">OptimizeForEndUserLocation</a>" : <i>Boolean</i>,
        "<a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>" : <i>[ &lt;a href=&#34;identityprovider.md&#34;&gt;IdentityProvider&lt;/a&gt;, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::WorklinkFleet
Properties:
    <a href="#auditstreamarn" title="AuditStreamArn">AuditStreamArn</a>: <i>String</i>
    <a href="#devicecacertificate" title="DeviceCaCertificate">DeviceCaCertificate</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optimizeforenduserlocation" title="OptimizeForEndUserLocation">OptimizeForEndUserLocation</a>: <i>Boolean</i>
    <a href="#identityprovider" title="IdentityProvider">IdentityProvider</a>: <i>
      - &lt;a href=&#34;identityprovider.md&#34;&gt;IdentityProvider&lt;/a&gt;</i>
    <a href="#network" title="Network">Network</a>: <i>
      - &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;</i>
</pre>

## Properties

#### AuditStreamArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceCaCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizeForEndUserLocation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityProvider

_Required_: No

_Type_: List of &lt;a href=&#34;identityprovider.md&#34;&gt;IdentityProvider&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of &lt;a href=&#34;network.md&#34;&gt;Network&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CompanyCode

Returns the &lt;code&gt;CompanyCode&lt;/code&gt; value.

#### CreatedTime

Returns the &lt;code&gt;CreatedTime&lt;/code&gt; value.

#### LastUpdatedTime

Returns the &lt;code&gt;LastUpdatedTime&lt;/code&gt; value.

